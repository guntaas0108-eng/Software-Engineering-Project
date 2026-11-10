# PropertyPulse — Comprehensive Platform Guide & Change Log
### *Curated Luxury Real Estate, AI Intelligence & Sovereign Escrow Platform*

This document provides a complete, structured summary of all features, architectural changes, role permissions, and test accounts implemented in **PropertyPulse**. Share this guide with your teammates, friends, or project evaluators to demonstrate the full capabilities of the platform.

---

## 🏛️ 1. Project Overview & Aesthetic System

PropertyPulse has been transformed into a **high-end luxury estate marketplace** (*"old-money" country estates, waterfront villas, and gated enclaves*):

* **Design Palette (Emerald & Gold):**
  * **Primary Dark Background:** `#07130F`
  * **Surface Cards & Headers:** `#0F2019`
  * **Primary Royal Accent:** Gold (`#D4AF37`) & Light Gold (`#F0D98A`)
  * **Secondary Elements:** Sage Green (`#9DB5A5`)
  * **Text Elements:** Warm Ivory (`#F5F1E8`)
* **Typography:**
  * **Headings:** *Cormorant Garamond* (Classic luxury serif)
  * **Body & UI:** *Jost* (Clean geometric sans-serif)
* **Cinematic Reveal Intro:**
  * Animated dual-curtain gold reveal with an SVG architectural skyline pulse.
  * Remembers session state (`sessionStorage`) so return navigation is instant; includes a **"Replay Intro"** button in the footer for demonstrations.

---

## 👥 2. Strict Role-Based Separation

Every user role has a **strictly tailored interface, permissions, and AI agent**. Users cannot see or access features outside their assigned role:

| Feature / Permission | Accredited Buyer | Estate Proprietor / Seller | Platform Administrator |
| :--- | :---: | :---: | :---: |
| **Navbar Role Indicator** | Standard Dropdown | Standard Dropdown | Glowing `🛡️ Admin Command` Button |
| **List Estate (`+ List Estate`)** | ❌ **Hidden & Blocked** | ✅ **Active** | ❌ **Hidden & Blocked** |
| **Dedicated AI Chatbot** | **Estate Concierge AI** | **Portfolio Strategist AI** | **Executive Platform AI** |
| **Role Switcher in Chatbot** | ❌ **Completely Removed** | ❌ **Completely Removed** | ❌ **Completely Removed** |
| **Saved Residences Dashboard** | ✅ **Active** | ❌ Hidden | ❌ Hidden |
| **Escrow Ledger & Receipts** | ✅ **Active** | ❌ Hidden | ❌ Hidden |
| **Proprietor Listings & Analytics** | ❌ **Blocked (302 Redirect)** | ✅ **Active** | ❌ **Blocked (302 Redirect)** |
| **Command Center (`/accounts/command-center/`)** | ❌ **Blocked (Redirect + Alert)** | ❌ **Blocked (Redirect + Alert)** | ✅ **Exclusive Access** |
| **Escrow Dispute & Refund Powers** | ❌ None | ❌ None | ✅ **Sovereign Override** |
| **Listing Moderation & Duplicate Deletion** | ❌ None | ❌ None | ✅ **Sovereign Override** |
| **KYC Gold Accreditation Toggles** | ❌ None | ❌ None | ✅ **Sovereign Override** |

---

## 🤖 3. Dual Role-Segregated AI Advisory & Machine Learning Engine

The platform integrates dual role-segregated AI assistants alongside an enterprise **Machine Learning Price Predictor & Buy-Now vs Future Decision Engine**:

### A. Machine Learning Valuation & Horizon Decision Engine
* **Hugging Face Hub & Local Hybrid Model**: Powered by `Haneesh112/propertypulse-price-predictor` (`model.joblib`) with seamless local offline fallback. Evaluates property size (sq ft), bedrooms, bathrooms, and category against market regression benchmarks.
* **Buy Now vs. In Future Decision Matrix**:
  * **🟢 BUY NOW (Optimal Investment Window)**: When Asking Price $\le$ Model Valuation. Indicates favorable pricing before future appreciation kicks in.
  * **🟡 FAIR VALUE (Market Benchmark)**: When Asking Price is within $\pm 5\%$ of fair market valuation.
  * **🟠 MONITOR & NEGOTIATE**: When Asking Price is $5\%$ to $20\%$ above benchmark.
  * **🔴 WAIT / FUTURE (Overpriced Premium)**: When Asking Price exceeds benchmark by $>20\%$. Suggests monitoring or awaiting price correction.
* **3-Year Appreciation & Delay Cost Horizon**:
  * Calculates projected 3-year asset valuation under compound market growth ($8.2\%$ CAGR).
  * Computes the **Opportunity Cost of Delaying** if purchased now vs. waiting 12 to 36 months.
* **Dynamic Emoji Investment Barometer**:
  * Visual badge with situational emojis (⚡ *Great Deal - Buy Now!*, ⚖️ *Fair Market Benchmark*, 🔍 *Negotiate*, ⏳ *Wait for Correction*, 🏛️ *Sold Out / Archive*).
  * Available **strictly to Accredited Buyers** on property detail and comparison pages.

### B. Estate Concierge AI (Exclusively for Buyers)
* **Target Audience:** Accredited buyers, investors, and prospective clients.
* **Capabilities:**
  * Curates luxury residences by lifestyle amenities (e.g. *"Show me villas with an infinity pool"*).
  * Computes mathematical mortgage amortizations and monthly EMIs (e.g. *"Calculate EMI for a ₹15 Cr estate loan"* at 8.5% luxury lending rate).
  * Explains ML algorithmic valuations and investment timing signals.
  * Informs the buyer about unread seller dispatches and confirmed viewing tours.
* **UI Controls:** Mode switchers are completely disabled. Prompts chips only display buyer discovery queries.

### C. Portfolio Strategist AI (Exclusively for Sellers)
* **Target Audience:** Estate proprietors, luxury homeowners, and developers.
* **Capabilities:**
  * Analyzes asking prices against the Machine Learning AI Barometer.
  * Recommends luxury staging protocols (twilight photography, title clearance, VIP viewing briefs).
  * Monitors buyer inquiries and private appointment requests.
  * Advises on token escrow security deposits.
* **UI Controls:** Mode switchers are completely disabled. Prompt chips only display seller optimization queries.

### D. Executive Platform AI (Exclusively for Administrators)
* **Target Audience:** Platform administrators.
* **Capabilities:**
  * Summarizes platform GMV, active escrow deposits, and pending disputes.
  * Diagnoses duplicate listing risks and unverified high-value accounts.

---

## 🛡️ 4. Sovereign Administrator Command Center

Accessible strictly at [`/accounts/command-center/`](file:///c:/Users/gunta/Desktop/Software-Engineering-Project-main/realestate_platform/accounts/templates/accounts/admin_dashboard.html) for users with staff/admin credentials (`admin`):

1. **Executive Real Estate KPIs:**
   * **Platform Gross Estate Value:** Total value of cataloged estates.
   * **Escrow Custodial Holds:** Total token deposits currently held in fiduciary trust.
   * **Active Inquiries & Scheduled Tours:** Live negotiation and inspection counts.
   * **Accredited Network:** Breakdown of verified Buyers vs. Sellers.
2. **Dispute Station (Duplicate Listing Moderation):**
   * Uses duplicate detection algorithms to surface potential clone/scraped listings.
   * **Approve Unique:** Clears flag and confirms listing authenticity.
   * **De-list:** Suspends the duplicate listing from public searches.
   * **Permanently Expunge:** One-click permanent deletion of fraudulent duplicates.
3. **Escrow Custody Supervision & Bilateral Dispute Intervention:**
   * Real-time ledger of all escrow deposits.
   * **Force Refund to Buyer:** Returns token funds to buyer if seller defaults or inspection reveals unresolvable defects.
   * **Disburse Escrow to Seller:** Clears and releases held funds directly to the seller.
   * Direct link to printable official Escrow Deeds.
4. **User Management & Gold KYC Accreditation Station:**
   * One-click toggle for **Gold Verified Accreditation Seal** (`is_verified`).
   * One-click account sanction toggle (`is_active` — Suspend fraudulent accounts or Restore access).
5. **Listing Quality & Sanction Control:**
   * Immediate toggle to suspend or reinstate any marketplace estate.
6. **1-Click Algorithmic Platform Health Scan:**
   * Automated diagnostic scanner checking for pricing outliers vs the AI Barometer, duplicate risks, missing listing media, unverified sellers, and pending escrows.

---

## 💬 5. Real-Time Negotiation Chat & Tour Scheduling

* **Dynamic In-App Messaging:**
  * Powered by Django Channels ASGI WebSocket connection with automated polling fallback.
  * Instant real-time communication between buyer and seller regarding specific estates.
* **VIP Site Visit Appointments:**
  * Buyers can propose inspection appointments with custom dates and times.
  * Sellers receive instant notifications to **Confirm** or **Decline**.
  * Confirmed appointments update the system metric: **Time-to-Appointment** ($T_{\text{appt}}$ target $\le 2$ hours).

---

## 💳 6. Fiduciary Escrow Payment Gateway

* **Multi-Mode Luxury Checkout:**
  * **Credit / Debit Cards:** VISA, MasterCard, RuPay, Amex.
  * **Instant UPI & Dynamic QR:** Scan & Pay via any UPI app.
  * **Private Wealth Net Banking:** Direct settlement via HDFC Private, ICICI Wealth, HSBC Premier, SBI.
  * **1-Click Sandbox Test Mode:** Instant simulation for demonstration and review.
* **Printable Invoice Deed Receipts:**
  * Printable legal token agreement receipt with official transaction hash, timestamp, RERA stamp placeholder, and property specs.

---

## 🔒 7. Enterprise Order-App Security Architecture

To ensure institutional financial standards for escrow deposits and transaction security, the platform incorporates enterprise security controls:
* **Cryptographic HMAC-SHA256 Audit Seal**: Every transaction receipt and state transition is cryptographically signed using platform secret hashes (`X-Audit-Signature: hmac-sha256:...`).
* **Idempotency Protection**: Checkout forms issue unique UUID idempotency keys stored in session cache (`idempotency_key`), preventing duplicate charge submissions from double-clicking or network retries.
* **Transaction Rate Limiting**: `OrderRateLimitMiddleware` restricts payment checkouts to at most 1 request per 2 seconds per user session (`HTTP 429 Too Many Requests`).
* **Anti-Self-Dealing Guard**: Sellers are strictly prohibited from depositing escrow on their own properties.
* **Strict Admin Purchasing Prohibition**: Platform administrators are strictly limited to supervisory oversight; checkout attempts by staff accounts are blocked with administrative policy warnings.
* **Security Headers**: Standardized injection of `X-Frame-Options: SAMEORIGIN`, `X-Content-Type-Options: nosniff`, and `Strict-Transport-Security`.

---

## 🏛️ 8. Teacher Demonstration Suite & 35 Test Estates

The platform includes **35 cataloged estates** showcasing all 6 valuation and lifecycle scenarios designed specifically for demonstration:
1. **Case 1: Exceptional Value / "BUY NOW" Deal** — *The Palm Manor*, *Silver Oak Woodland Estate* (Asking price significantly below ML valuation).
2. **Case 2: Fair Market Benchmark** — *The Grand Imperial Haveli*, *Emerald Crest Fair Benchmark* (Asking price aligns with ML prediction).
3. **Case 3: Monitor & Negotiate** — *The Whispering Pines Alpine Villa*, *Fairview Lakefront Benchmark* (Asking price 5-15% above benchmark).
4. **Case 4: Overpriced / "WAIT IN FUTURE"** — *Skyline Sovereign Penthouse*, *The Grand Sovereign Palace* (Premium markup >25%; ML warns buyer to wait or negotiate).
5. **Case 5: Sold Out Property Grayscale Archive** — *Highland Crest SOLD Manor*, *The Sunset Ridge SOLD Villa* (Grayscale styling, `SOLD OUT` banner, disabled escrow actions).
6. **Case 6: Agricultural Land & Commercial Assets** — *Golden Ridge Commercial Office Park*, *Valley Green Agricultural Plantation*.

---

## 🔑 9. Login Credentials Cheatsheet

Use these pre-configured credentials to demonstrate all perspectives of the platform:

| Role | Username | Password | What to Observe / Test |
| :--- | :--- | :--- | :--- |
| **Platform Administrator** | `admin` | `admin123` | • Glowing `🛡️ Admin Command` button in navbar.<br>• Full access to `/accounts/command-center/`.<br>• Cannot see `+ List Estate`.<br>• Executive Platform AI assistant. |
| **Estate Proprietor (Seller)** | `seller1` | `seller123` | • `+ List Estate` button visible.<br>• Access to `My Listings` and `Proprietor Analytics`.<br>• **Portfolio Strategist AI** assistant.<br>• Receives buyer tour requests & escrow deposits. |
| **Estate Proprietor (Seller 2)** | `seller2` | `seller2123` | • Secondary seller account with active listings. |
| **Accredited Buyer** | `guntaas2006` | `guntaas123` | • No `+ List Estate` button.<br>• **Estate Concierge AI** assistant with pool & mortgage chips.<br>• Can save estates, book inspections, and make escrow deposits. |
| **Accredited Buyer (Buyer 1)** | `buyer1` | `buyer123` | • Secondary buyer account for multi-party chat testing. |

---

## 🚀 9. How to Run the Platform

1. **Activate Virtual Environment:**
   ```powershell
   .\realestate_platform\.venv\Scripts\activate
   ```
2. **Start the Development Server (Daphne ASGI Server):**
   ```powershell
   python realestate_platform\manage.py runserver 127.0.0.1:8000
   ```
3. **Open Browser:**
   * Visit: `http://127.0.0.1:8000/`
   * Admin Command Center: `http://127.0.0.1:8000/accounts/command-center/`
   * AI Advisor: `http://127.0.0.1:8000/chat/advisor/`
   * All Residences: `http://127.0.0.1:8000/properties/`
