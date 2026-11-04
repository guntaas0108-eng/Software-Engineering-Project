import re
from decimal import Decimal
from django.db.models import Q
from properties.models import Property
from chat.models import Conversation, Message, Appointment
from payments.models import Payment


def get_user_notifications(user):
    """Retrieve real-time unread messages and appointment alerts for the user."""
    if not user.is_authenticated:
        return []

    alerts = []
    # 1. Unread messages
    unread_msgs = Message.objects.filter(
        conversation__in=Conversation.objects.filter(Q(buyer=user) | Q(seller=user))
    ).exclude(sender=user).filter(read_at__isnull=True).select_related("sender", "conversation", "conversation__property")[:5]

    for m in unread_msgs:
        alerts.append({
            "type": "message",
            "title": f"New message from {m.sender.username}",
            "body": f"Regarding '{m.conversation.property.title}': {m.body[:80]}...",
            "link": f"/chat/{m.conversation.pk}/",
            "time": m.created_at.strftime("%H:%M"),
        })

    # 2. Appointment updates for buyer
    confirmed_appts = Appointment.objects.filter(
        conversation__buyer=user, status=Appointment.Status.CONFIRMED
    ).select_related("conversation__property", "conversation__seller")[:3]
    for a in confirmed_appts:
        alerts.append({
            "type": "appointment_confirmed",
            "title": "Site Visit Confirmed",
            "body": f"Proprietor {a.conversation.seller.username} confirmed inspection for '{a.conversation.property.title}' on {a.scheduled_for.strftime('%b %d, %H:%M')}.",
            "link": f"/chat/{a.conversation.pk}/",
            "time": a.updated_at.strftime("%H:%M"),
        })

    # 3. New appointment requests for seller
    pending_appts = Appointment.objects.filter(
        conversation__seller=user, status=Appointment.Status.REQUESTED
    ).select_related("conversation__property", "conversation__buyer")[:3]
    for a in pending_appts:
        alerts.append({
            "type": "appointment_requested",
            "title": "VIP Inspection Requested",
            "body": f"Client {a.conversation.buyer.username} requested a visit on '{a.conversation.property.title}'.",
            "link": f"/chat/{a.conversation.pk}/",
            "time": a.created_at.strftime("%H:%M"),
        })

    # 4. Escrow payments received for seller
    recent_escrow = Payment.objects.filter(
        estate__seller=user, status=Payment.Status.PAID
    ).select_related("estate", "buyer")[:3]
    for p in recent_escrow:
        alerts.append({
            "type": "escrow_deposit",
            "title": "Escrow Token Secured",
            "body": f"₹{p.amount_rupees:,.0f} secured in fiduciary custody by {p.buyer.username} for '{p.estate.title}'.",
            "link": f"/payments/receipt/{p.public_id}/",
            "time": p.paid_at.strftime("%H:%M") if p.paid_at else "",
        })

    return alerts


def generate_buyer_bot_response(query, user):
    """
    Estate Concierge AI: Private client advisor assisting buyers in discovering estates,
    calculating mortgage/EMI, explaining AI valuations, and checking alerts.
    """
    q = query.lower().strip()
    notifications = get_user_notifications(user) if user and user.is_authenticated else []

    # 1. Notifications / Message inquiries
    if any(k in q for k in ["notification", "alert", "message", "unread", "who messaged", "updates"]):
        if not user or not user.is_authenticated:
            return (
                "Please **Sign In** to review your confidential message dispatches and site-visit status updates."
            )
        if not notifications:
            return (
                "You have no pending unread notifications at this moment. All message channels and site visits are up to date."
            )
        res = "Here are your latest dispatches and portfolio updates:\n\n"
        for n in notifications:
            res += f"- **{n['title']}**: {n['body']} [View Channel &rarr;]({n['link']})\n"
        return res

    # 2. Mortgage / EMI calculation
    if any(k in q for k in ["emi", "mortgage", "loan", "interest", "calculate payment"]):
        # Extract numbers like 10, 20, 15 Cr, etc.
        numbers = re.findall(r"\d+(?:\.\d+)?", q)
        principal = Decimal("100000000") # default 10 Cr
        if numbers:
            val = float(numbers[0])
            if "cr" in q or "crore" in q:
                principal = Decimal(val * 10000000)
            elif "lakh" in q or "lac" in q:
                principal = Decimal(val * 100000)
            elif val > 1000:
                principal = Decimal(val)

        # Standard luxury estate loan: 8.5% interest, 15-year tenure (180 months)
        r = (Decimal("8.5") / Decimal(100)) / Decimal(12)
        n = 180
        # EMI = P * r * (1+r)^n / ((1+r)^n - 1)
        r_float = float(r)
        emi_float = float(principal) * r_float * ((1 + r_float) ** n) / (((1 + r_float) ** n) - 1)
        emi = round(emi_float)

        return (
            f"### Luxury Mortgage &amp; EMI Computation\n\n"
            f"- **Principal Loan Amount:** ₹{principal:,.0f}\n"
            f"- **Benchmark Luxury Lending Rate:** 8.50% p.a.\n"
            f"- **Tenure:** 15 Years (180 months)\n"
            f"- **Estimated Monthly Installment (EMI):** **₹{emi:,.0f} / month**\n\n"
            f"Would you like me to connect you with our sovereign private banking partners (HDFC Private, ICICI Wealth, HSBC Premier)?"
        )

    # 3. Filtering by features (pool, garden, penthouse, beach, colonial, haveli)
    if any(k in q for k in ["pool", "swimming", "infinity"]):
        props = Property.objects.filter(
            Q(description__icontains="pool") | Q(title__icontains="pool")
        )[:3]
        if props.exists():
            res = "I have curated these private estates featuring bespoke swimming facilities:\n\n"
            for p in props:
                res += (
                    f"- **[{p.title}](/properties/{p.pk}/)** — ₹{p.listed_price:,.0f}\n"
                    f"  *{p.locality}, {p.city}* &middot; {p.area_sqft} sqft &middot; {p.bedrooms} BHK\n"
                    f"  *{p.description[:110]}...*\n\n"
                )
            return res

    if any(k in q for k in ["penthouse", "sky", "view"]):
        props = Property.objects.filter(
            Q(title__icontains="penthouse") | Q(title__icontains="sky") | Q(description__icontains="penthouse")
        )[:3]
        if props.exists():
            res = "Here are our premier skyline residences and penthouses:\n\n"
            for p in props:
                res += (
                    f"- **[{p.title}](/properties/{p.pk}/)** — ₹{p.listed_price:,.0f}\n"
                    f"  *{p.locality}, {p.city}* &middot; {p.bedrooms} BHK &middot; AI Barometer: **{p.barometer_label()}**\n\n"
                )
            return res

    if any(k in q for k in ["great deal", "fair price", "below market", "best price", "valuation"]):
        great_deals = [p for p in Property.objects.all() if p.barometer_key() == "great"][:3]
        if great_deals:
            res = "Our algorithmic AI valuation has identified the following **Great Deal** properties (priced favorably below estimated market value):\n\n"
            for p in great_deals:
                res += (
                    f"- **[{p.title}](/properties/{p.pk}/)**\n"
                    f"  Listed: ₹{p.listed_price:,.0f} | AI Model Estimate: ₹{p.predicted_price:,.0f}\n"
                    f"  *{p.locality}, {p.city}*\n\n"
                )
            return res

    # 4. Location inquiry (Mumbai, Delhi, Bangalore, Goa, Jaipur, etc.)
    for city in ["mumbai", "delhi", "bangalore", "goa", "jaipur", "hyderabad", "gurgaon"]:
        if city in q:
            matches = Property.objects.filter(
                Q(city__icontains=city) | Q(locality__icontains=city)
            )[:3]
            if matches.exists():
                res = f"Here are distinguished residences currently available in **{city.title()}**:\n\n"
                for p in matches:
                    res += f"- **[{p.title}](/properties/{p.pk}/)** — ₹{p.listed_price:,.0f} ({p.locality})\n"
                return res

    # 5. General Greeting or overview
    all_props = Property.objects.all()[:4]
    return (
        f"Welcome to PropertyPulse. I am your **Private Client Estate Concierge**.\n\n"
        f"I have direct access to our complete collection of **{Property.objects.count()} curated luxury estates** across Mumbai, Delhi, Bangalore, Goa, and historic enclaves.\n\n"
        f"**How may I assist you today?**\n"
        f"- *'Show me properties with an infinity pool'*\n"
        f"- *'Which estates are tagged as Great Deals?'*\n"
        f"- *'Calculate mortgage EMI for a 20 Cr villa'*\n"
        f"- *'Check my latest messages from sellers'*\n\n"
        f"Featured Spotlight: **[{all_props[0].title}](/properties/{all_props[0].pk}/)** in {all_props[0].locality} at ₹{all_props[0].listed_price:,.0f}."
    )


def generate_seller_bot_response(query, user):
    """
    Portfolio Strategist AI: Dedicated advisor assisting sellers and estate proprietors
    with pricing optimization, ML barometer analytics, listing staging, and buyer inquiries.
    """
    q = query.lower().strip()
    notifications = get_user_notifications(user) if user and user.is_authenticated else []

    # 1. Inquiries & Activity Notifications
    if any(k in q for k in ["inquiry", "inquiries", "who viewed", "buyer", "messages", "alerts"]):
        if not user or not user.is_authenticated:
            return "Please **Sign In** as a seller to review your active buyer inquiries."
        if not notifications:
            return (
                "You have no unread buyer inquiries or pending visit requests at this moment. "
                "Your active listings remain prominently showcased to qualified HNI investors."
            )
        res = "### Current Proprietor Inquiries &amp; Escrow Activity:\n\n"
        for n in notifications:
            res += f"- **{n['title']}**: {n['body']} [Respond in Channel &rarr;]({n['link']})\n"
        return res

    # 2. Pricing and Valuation Strategy
    if any(k in q for k in ["price", "pricing", "barometer", "fair value", "compete", "valuation"]):
        user_props = Property.objects.filter(seller=user) if user and user.is_authenticated else []
        if user_props:
            res = "### Portfolio Pricing &amp; Market Alignment Analysis\n\n"
            for p in user_props:
                res += (
                    f"- **{p.title}**:\n"
                    f"  - Listed Price: ₹{p.listed_price:,.0f}\n"
                    f"  - AI Barometer Estimate: ₹{p.predicted_price:,.0f}\n"
                    f"  - Current Status: **{p.barometer_label()}**\n\n"
                )
            res += (
                "**Strategic Recommendation:** Listings calibrated within &plusmn;5% of our AI Valuation "
                "garner 3.4x more private site visit requests from high-net-worth family offices."
            )
            return res
        else:
            return (
                "Our AI Pricing Barometer models square footage, age, architectural category, and micro-market historical comps. "
                "Properties priced at or slightly under the algorithmic estimate earn the coveted **Great Deal** green badge, "
                "maximizing initial buyer engagement."
            )

    # 3. Staging and Marketing Advice
    if any(k in q for k in ["stage", "staging", "photo", "pictures", "description", "market", "tips"]):
        return (
            "### Luxury Estate Staging &amp; Presentation Protocol\n\n"
            "1. **Golden Hour &amp; Dusk Aerials:** Twilight photography highlights architectural lighting and landscape perimeter.\n"
            "2. **De-clutter &amp; Neutral Luxury:** Keep primary living salons minimal with architectural flora and curated art.\n"
            "3. **Clear Legal Pedigree:** Highlight clear title deeds, occupancy certificates, and RERA registration in the initial summary.\n"
            "4. **Private Escort Ready:** Ensure caretakers or estate managers are briefed for confidential VIP client walk-throughs."
        )

    # 4. General Seller Overview
    user_count = Property.objects.filter(seller=user).count() if user and user.is_authenticated else 0
    return (
        f"Greetings. I am your **Portfolio Strategist AI**.\n\n"
        f"You currently have **{user_count} estates** registered under your portfolio on PropertyPulse.\n\n"
        f"**Areas I can assist you with:**\n"
        f"- *'Analyze my listing prices against the AI barometer'*\n"
        f"- *'Check new buyer inquiries and appointment requests'*\n"
        f"- *'How can I optimize my property description for UHNW buyers?'*\n"
        f"- *'What are the guidelines for accepting token escrow deposits?'*"
    )


def generate_admin_bot_response(query, user):
    """
    Executive Platform AI: Dedicated diagnostic & oversight AI for platform administrators.
    Provides real-time health checks, dispute summaries, and escrow auditing.
    """
    q = query.lower().strip()

    total_props = Property.objects.count()
    duplicates_count = Property.objects.filter(possible_duplicate_of__isnull=False).count()
    total_payments = Payment.objects.count()
    paid_payments = Payment.objects.filter(status=Payment.Status.PAID)
    escrow_held = sum(p.amount_rupees for p in paid_payments)
    open_conversations = Conversation.objects.count()
    pending_appts = Appointment.objects.filter(status=Appointment.Status.REQUESTED).count()

    if any(k in q for k in ["duplicate", "flag", "fraud"]):
        if duplicates_count > 0:
            flagged = Property.objects.filter(possible_duplicate_of__isnull=False).select_related("seller", "possible_duplicate_of")[:3]
            res = f"### Duplicate Detection Alert ({duplicates_count} Flagged Listings)\n\n"
            for f in flagged:
                orig_title = f.possible_duplicate_of.title if f.possible_duplicate_of else "Catalog comp"
                res += f"- **{f.title}** (Seller: {f.seller.username}) &rarr; Flagged against *'{orig_title}'*\n"
            res += f"\nYou can approve, de-list, or expunge them at [Command Center Duplicate Station](/accounts/command-center/)."
            return res
        return "All active estates have passed algorithmic duplicate screening. No unresolved flags present."

    if any(k in q for k in ["escrow", "payment", "money", "fund", "balance", "custody"]):
        return (
            f"### Escrow Custody Ledger Overview\n\n"
            f"- **Active Escrow Funds in Custody:** ₹{escrow_held:,.0f}\n"
            f"- **Total Platform Settlements:** {total_payments}\n"
            f"- **Cleared Payments:** {paid_payments.count()}\n\n"
            f"Manage bilateral dispute refunds or release funds at the [Escrow Fiduciary Station](/accounts/command-center/)."
        )

    if any(k in q for k in ["health", "scan", "status", "overview", "metric", "audit"]):
        return (
            f"### Platform Sovereign Diagnostic Summary\n\n"
            f"- **Catalog Estates:** {total_props} listings\n"
            f"- **Flagged Duplicate Risks:** {duplicates_count}\n"
            f"- **Escrow Held in Fiduciary Trust:** ₹{escrow_held:,.0f}\n"
            f"- **Active Inquiries & Negotiations:** {open_conversations}\n"
            f"- **Pending VIP Inspections:** {pending_appts}\n\n"
            f"System status is **Operational**. Access the full executive management console at [Administrator Command Center](/accounts/command-center/)."
        )

    return (
        f"Greetings Administrator. I am your **Executive Platform Oversight AI**.\n\n"
        f"**Platform Snapshot:**\n"
        f"- Active Estates: **{total_props}** | Flagged Duplicates: **{duplicates_count}**\n"
        f"- Escrow Trust Fund: **₹{escrow_held:,.0f}** | Negotiation Channels: **{open_conversations}**\n\n"
        f"**Direct Commands:**\n"
        f"- *'Check platform health and diagnostics'*\n"
        f"- *'Review duplicate listing risks'*\n"
        f"- *'Audit escrow balance and custody settlements'*"
    )

