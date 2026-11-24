import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs('docs/images', exist_ok=True)

def save_fig(fig, filename):
    path = os.path.join('docs/images', filename)
    fig.savefig(path, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f"Saved: {path}")

# ==================== 1. THAPAR LOGO ====================
def gen_thapar_logo():
    fig, ax = plt.subplots(figsize=(6, 3), dpi=200)
    ax.axis('off')
    
    # Red background box / icon
    # Drawing stylized 'ti'
    ax.text(0.5, 0.70, "ti", fontsize=58, fontweight='bold', color='#B81D24', ha='center', va='center', fontfamily='serif')
    ax.plot([0.25, 0.75], [0.50, 0.50], color='#B81D24', lw=2)
    ax.text(0.5, 0.38, "THAPAR INSTITUTE", fontsize=15, fontweight='bold', color='#1A1A1A', ha='center', va='center', fontfamily='serif')
    ax.text(0.5, 0.25, "OF ENGINEERING & TECHNOLOGY", fontsize=12, fontweight='bold', color='#1A1A1A', ha='center', va='center', fontfamily='serif')
    ax.text(0.5, 0.14, "(Deemed to be University)", fontsize=10, fontstyle='italic', color='#555555', ha='center', va='center', fontfamily='serif')
    
    save_fig(fig, 'thapar_logo.png')

# ==================== 2. SWIMLANE DIAGRAM ====================
def gen_swimlane():
    fig, ax = plt.subplots(figsize=(12, 7), dpi=200)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis('off')

    lanes = ["Accredited Buyer", "PropertyPulse Controller", "ML Valuation Engine", "Estate Proprietor (Seller)"]
    colors = ["#E8F4F8", "#FBF7EA", "#EAF5EA", "#F5EBEB"]
    
    for i, (lane, col) in enumerate(zip(lanes, colors)):
        y = 6 - i * 1.5
        rect = patches.Rectangle((0.2, y - 0.2), 11.6, 1.4, facecolor=col, edgecolor='#777777', lw=1.2)
        ax.add_patch(rect)
        ax.text(0.3, y + 0.5, lane, fontsize=10, fontweight='bold', color='#222222', rotation=0)

    # Actions in Seller Lane (y = 1.5)
    ax.add_patch(patches.FancyBboxPatch((2.0, 1.6), 2.2, 0.8, boxstyle="round,pad=0.1", fc='#FFFFFF', ec='#882222', lw=1.5))
    ax.text(3.1, 2.0, "Input Property Dimensions\n& Location Attributes", ha='center', va='center', fontsize=7.5)

    # Action in Controller Lane (y = 4.5)
    ax.add_patch(patches.FancyBboxPatch((4.6, 4.6), 2.0, 0.8, boxstyle="round,pad=0.1", fc='#FFFFFF', ec='#AA8822', lw=1.5))
    ax.text(5.6, 5.0, "Feature Extraction\n& Validation", ha='center', va='center', fontsize=7.5)

    # Action in ML Engine Lane (y = 3.0)
    ax.add_patch(patches.FancyBboxPatch((4.6, 3.1), 2.0, 0.8, boxstyle="round,pad=0.1", fc='#FFFFFF', ec='#228822', lw=1.5))
    ax.text(5.6, 3.5, "Regression Model Inference\n& Duplicate Scan", ha='center', va='center', fontsize=7.5)

    # Action back to Seller Lane
    ax.add_patch(patches.FancyBboxPatch((7.0, 1.6), 2.0, 0.8, boxstyle="round,pad=0.1", fc='#FFFFFF', ec='#882222', lw=1.5))
    ax.text(8.0, 2.0, "Review AI Barometer\n& Set Asking Price", ha='center', va='center', fontsize=7.5)

    # Action in Buyer Lane (y = 6.0)
    ax.add_patch(patches.FancyBboxPatch((7.0, 6.1), 2.0, 0.8, boxstyle="round,pad=0.1", fc='#FFFFFF', ec='#225588', lw=1.5))
    ax.text(8.0, 6.5, "Search, Filter by Pool/View\n& Verify Valuation Badge", ha='center', va='center', fontsize=7.5)

    # Final Buyer Action
    ax.add_patch(patches.FancyBboxPatch((9.5, 6.1), 2.0, 0.8, boxstyle="round,pad=0.1", fc='#FFFFFF', ec='#225588', lw=1.5))
    ax.text(10.5, 6.5, "Book VIP Inspection\n& Commit Escrow Deposit", ha='center', va='center', fontsize=7.5)

    # Arrows
    arrow_props = dict(arrowstyle="->", lw=1.5, color='#333333')
    ax.annotate("", xy=(4.6, 5.0), xytext=(4.2, 2.0), arrowprops=arrow_props)
    ax.annotate("", xy=(5.6, 3.9), xytext=(5.6, 4.6), arrowprops=arrow_props)
    ax.annotate("", xy=(7.0, 2.0), xytext=(6.6, 3.5), arrowprops=arrow_props)
    ax.annotate("", xy=(8.0, 6.1), xytext=(8.0, 2.4), arrowprops=arrow_props)
    ax.annotate("", xy=(9.5, 6.5), xytext=(9.0, 6.5), arrowprops=arrow_props)

    ax.set_title("Figure 2.3.1: Multi-Role Swimlane Activity Workflow", fontsize=12, fontweight='bold', pad=15)
    save_fig(fig, 'fig_swimlane.png')

# ==================== 3. DFD LEVEL 0 (CONTEXT) ====================
def gen_dfd_lvl0():
    fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Central System Process
    circle = patches.Circle((5, 3), 1.3, facecolor='#F5EBE0', edgecolor='#8A6E24', lw=2.5)
    ax.add_patch(circle)
    ax.text(5, 3.2, "0.0", fontsize=12, fontweight='bold', ha='center', color='#8A6E24')
    ax.text(5, 2.8, "PropertyPulse\nPlatform", fontsize=10, fontweight='bold', ha='center', color='#111111')

    # External Entities
    entities = [
        ("Accredited Buyer", (1.2, 4.8), "#D0E8F2"),
        ("Estate Proprietor\n(Seller)", (1.2, 1.2), "#FCE8E6"),
        ("Platform\nAdministrator", (8.8, 4.8), "#E2F0D9"),
        ("Banking & Escrow\nPayment Rails", (8.8, 1.2), "#FFF2CC")
    ]

    for name, (x, y), col in entities:
        rect = patches.Rectangle((x-1.1, y-0.6), 2.2, 1.2, facecolor=col, edgecolor='#333333', lw=1.8)
        ax.add_patch(rect)
        ax.text(x, y, name, ha='center', va='center', fontsize=8.5, fontweight='bold')

    # Flows
    kw = dict(arrowstyle="->", lw=1.3, color='#444444')
    # Buyer flows
    ax.annotate("Search & EMI Inquiries", xy=(3.8, 3.6), xytext=(2.3, 4.8), arrowprops=kw, fontsize=7.5)
    ax.annotate("Estates & Barometer Badges", xy=(2.3, 4.4), xytext=(3.8, 3.2), arrowprops=kw, fontsize=7.5)
    
    # Seller flows
    ax.annotate("Listing Specs & Photos", xy=(3.8, 2.6), xytext=(2.3, 1.4), arrowprops=kw, fontsize=7.5)
    ax.annotate("Predicted Valuation & Visits", xy=(2.3, 1.0), xytext=(3.8, 2.2), arrowprops=kw, fontsize=7.5)

    # Admin flows
    ax.annotate("Duplicate Flags & Escrow Ledgers", xy=(7.7, 4.6), xytext=(6.2, 3.6), arrowprops=kw, fontsize=7.5)
    ax.annotate("Sanctions & Dispute Overrides", xy=(6.2, 3.2), xytext=(7.7, 4.2), arrowprops=kw, fontsize=7.5)

    # Bank flows
    ax.annotate("Payment Commitments", xy=(7.7, 1.4), xytext=(6.2, 2.4), arrowprops=kw, fontsize=7.5)
    ax.annotate("Settlement Clearances", xy=(6.2, 2.0), xytext=(7.7, 1.0), arrowprops=kw, fontsize=7.5)

    ax.set_title("Figure 2.4.2: Data Flow Diagram (DFD Level 0 — Context Model)", fontsize=11, fontweight='bold', pad=12)
    save_fig(fig, 'fig_dfd_lvl0.png')

# ==================== 4. DFD LEVEL 1 ====================
def gen_dfd_lvl1():
    fig, ax = plt.subplots(figsize=(11, 7), dpi=200)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7)
    ax.axis('off')

    # 5 Major processes
    procs = [
        ("1.0\nAuth & KYC\nAccreditation", (2.0, 5.5)),
        ("2.0\nListing Intake\n& ML Valuation", (5.5, 5.5)),
        ("3.0\nLive Chat &\nSite Tour Engine", (9.0, 5.5)),
        ("4.0\nFiduciary Escrow\n& Token Holding", (3.5, 2.0)),
        ("5.0\nAdministrator\nDispute Station", (7.5, 2.0))
    ]

    for label, (x, y) in procs:
        circle = patches.Circle((x, y), 0.85, facecolor='#FAF3E0', edgecolor='#A08020', lw=1.8)
        ax.add_patch(circle)
        ax.text(x, y, label, ha='center', va='center', fontsize=7.5, fontweight='bold')

    # Data Stores
    stores = [
        ("D1: User Profiles & Roles", (2.0, 3.8)),
        ("D2: Property Catalog & Media", (5.5, 3.8)),
        ("D3: Messages & Tour Visits", (9.0, 3.8)),
        ("D4: Escrow Ledger & Deeds", (5.5, 0.6))
    ]

    for label, (x, y) in stores:
        # Open-ended rect (data store standard)
        rect = patches.Rectangle((x-1.3, y-0.25), 2.6, 0.5, facecolor='#EBF4F6', edgecolor='#2B6777', lw=1.4)
        ax.add_patch(rect)
        ax.text(x, y, label, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#1B4757')

    # Connections
    kw = dict(arrowstyle="->", lw=1.2, color='#333333')
    ax.annotate("", xy=(2.0, 4.05), xytext=(2.0, 4.65), arrowprops=kw)
    ax.annotate("", xy=(5.5, 4.05), xytext=(5.5, 4.65), arrowprops=kw)
    ax.annotate("", xy=(9.0, 4.05), xytext=(9.0, 4.65), arrowprops=kw)
    ax.annotate("", xy=(4.2, 0.85), xytext=(3.5, 1.15), arrowprops=kw)
    ax.annotate("", xy=(6.8, 0.85), xytext=(7.5, 1.15), arrowprops=kw)
    ax.annotate("", xy=(7.5, 2.85), xytext=(5.5, 3.55), arrowprops=kw)
    ax.annotate("", xy=(4.65, 5.5), xytext=(2.85, 5.5), arrowprops=kw)

    ax.set_title("Figure 2.4.3: Data Flow Diagram (DFD Level 1 — Functional Decompositions)", fontsize=11, fontweight='bold', pad=12)
    save_fig(fig, 'fig_dfd_lvl1.png')

# ==================== 5. DFD LEVEL 2 (VALUATION & ESCROW) ====================
def gen_dfd_lvl2():
    fig, ax = plt.subplots(figsize=(11, 7), dpi=200)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7)
    ax.axis('off')

    subprocs = [
        ("2.1\nFeature Vector\nNormalization", (2.0, 5.2)),
        ("2.2\nMultivariate Linear\nRegression (y_hat)", (5.5, 5.2)),
        ("2.3\nBarometer Classify\n& Duplicate Scan", (9.0, 5.2)),
        ("4.1\nIntent Creation\n& Multi-Rail Dispatch", (2.0, 2.0)),
        ("4.2\nFiduciary Trust\nLock & Receipt Deed", (5.5, 2.0)),
        ("4.3\nBilateral Dispute\nRefund / Release", (9.0, 2.0))
    ]

    for label, (x, y) in subprocs:
        circle = patches.Circle((x, y), 0.85, facecolor='#FFF8E7', edgecolor='#B8860B', lw=1.6)
        ax.add_patch(circle)
        ax.text(x, y, label, ha='center', va='center', fontsize=7.2, fontweight='bold')

    # D2 Store
    rect1 = patches.Rectangle((4.3, 3.4), 2.4, 0.5, facecolor='#EBF4F6', edgecolor='#2B6777', lw=1.2)
    ax.add_patch(rect1)
    ax.text(5.5, 3.65, "D2: Property Catalog", ha='center', va='center', fontsize=8, fontweight='bold')

    kw = dict(arrowstyle="->", lw=1.3, color='#333333')
    ax.annotate("Raw Inputs", xy=(1.15, 5.2), xytext=(0.2, 5.2), arrowprops=kw, fontsize=7)
    ax.annotate("Normalized X", xy=(4.65, 5.2), xytext=(2.85, 5.2), arrowprops=kw, fontsize=7)
    ax.annotate("Estimated y_hat", xy=(8.15, 5.2), xytext=(6.35, 5.2), arrowprops=kw, fontsize=7)
    ax.annotate("Comps & Verified", xy=(6.5, 3.9), xytext=(8.5, 4.4), arrowprops=kw, fontsize=7)

    ax.annotate("Buyer Checkout", xy=(1.15, 2.0), xytext=(0.2, 2.0), arrowprops=kw, fontsize=7)
    ax.annotate("Webhook Sig OK", xy=(4.65, 2.0), xytext=(2.85, 2.0), arrowprops=kw, fontsize=7)
    ax.annotate("Dispute Escalation", xy=(8.15, 2.0), xytext=(6.35, 2.0), arrowprops=kw, fontsize=7)

    ax.set_title("Figure 2.4.4: Data Flow Diagram (DFD Level 2 — Valuation & Escrow Sub-Processes)", fontsize=11, fontweight='bold', pad=12)
    save_fig(fig, 'fig_dfd_lvl2.png')

# ==================== 6. CLASS DIAGRAM 2 (SERVICE & INTELLIGENCE) ====================
def gen_class_service():
    fig, ax = plt.subplots(figsize=(11, 7), dpi=200)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7)
    ax.axis('off')

    classes = [
        ("PricePredictor\n---------------------------\n+ model: LinearRegression\n+ scaler: StandardScaler\n---------------------------\n+ predict(features): Decimal\n+ train(dataset): Metrics\n+ evaluate_residuals(): float", (1.0, 3.8), 2.8, 2.6, "#E8F0FE"),
        ("ChatbotEngine\n---------------------------\n+ buyer_persona: str\n+ seller_persona: str\n+ admin_persona: str\n---------------------------\n+ generate_buyer_bot(q): str\n+ generate_seller_bot(q): str\n+ generate_admin_bot(q): str", (4.2, 3.8), 2.8, 2.6, "#FEF7E0"),
        ("EscrowFiduciaryService\n---------------------------\n+ lock_period: int = 48h\n+ commission_rate: Decimal\n---------------------------\n+ hold_deposit(payment_id)\n+ authorize_refund(admin, id)\n+ disburse_to_seller(id)", (7.4, 3.8), 2.8, 2.6, "#E6F4EA"),
        ("DuplicateDetector\n---------------------------\n+ sim_threshold: float = 0.85\n---------------------------\n+ find_duplicates(prop): list\n+ calculate_similarity(): float", (1.0, 0.5), 2.8, 2.2, "#FCE8E6"),
        ("NotificationBroker\n---------------------------\n+ channel_layer: InMemory/Redis\n---------------------------\n+ dispatch_message(conv_id)\n+ broadcast_alert(user_id)", (4.2, 0.5), 2.8, 2.2, "#F3E8FD"),
        ("PlatformHealthScanner\n---------------------------\n+ metrics_cache: dict\n---------------------------\n+ run_audit(): dict\n+ flag_price_outliers(): list", (7.4, 0.5), 2.8, 2.2, "#FFF0F5")
    ]

    for text, (x, y), w, h, col in classes:
        rect = patches.Rectangle((x, y), w, h, facecolor=col, edgecolor='#333333', lw=1.4)
        ax.add_patch(rect)
        ax.text(x + 0.1, y + h - 0.2, text, va='top', fontsize=7, fontfamily='monospace')

    ax.set_title("Figure 3.2.2: Class Diagram (Service & Algorithmic Intelligence Architecture)", fontsize=11, fontweight='bold', pad=12)
    save_fig(fig, 'fig_class_service.png')

# ==================== 7. COLLABORATION DIAGRAMS ====================
def gen_collab_appointment():
    fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    nodes = [
        ("Buyer Client", (1.5, 4.5), "#D2E3FC"),
        ("ChatController", (5.0, 4.5), "#FEEFC3"),
        ("Appointment\nScheduler", (8.5, 4.5), "#CEEAD6"),
        ("Seller Client", (8.5, 1.5), "#FAD2CF"),
        ("Notification\nBroker", (5.0, 1.5), "#E8D5F5")
    ]

    for label, (x, y), col in nodes:
        rect = patches.FancyBboxPatch((x-1.0, y-0.5), 2.0, 1.0, boxstyle="round,pad=0.1", fc=col, ec='#333333', lw=1.5)
        ax.add_patch(rect)
        ax.text(x, y, label, ha='center', va='center', fontsize=8, fontweight='bold')

    kw = dict(arrowstyle="->", lw=1.3, color='#333333')
    ax.plot([2.5, 4.0], [4.5, 4.5], color='#444444', lw=1.5)
    ax.text(3.25, 4.7, "1: request_appt(time)\n-->", ha='center', fontsize=7)

    ax.plot([6.0, 7.5], [4.5, 4.5], color='#444444', lw=1.5)
    ax.text(6.75, 4.7, "2: create_record(PENDING)\n-->", ha='center', fontsize=7)

    ax.plot([8.5, 8.5], [4.0, 2.0], color='#444444', lw=1.5)
    ax.text(8.9, 3.0, "3: alert_seller()\n|v", ha='left', fontsize=7)

    ax.plot([7.5, 6.0], [1.5, 1.5], color='#444444', lw=1.5)
    ax.text(6.75, 1.7, "<-- 4: confirm_appt()\n", ha='center', fontsize=7)

    ax.plot([4.0, 2.5], [1.5, 4.0], color='#444444', lw=1.5)
    ax.text(2.6, 2.4, "5: websocket_push(CONFIRMED)\n^", ha='left', fontsize=7)

    ax.set_title("Figure 3.4.1: Collaboration Diagram — Real-Time Site Tour Scheduling", fontsize=11, fontweight='bold', pad=12)
    save_fig(fig, 'fig_collab_appointment.png')

def gen_collab_escrow():
    fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    nodes = [
        ("Buyer", (1.5, 4.5), "#D2E3FC"),
        ("EscrowService", (5.0, 4.5), "#FEEFC3"),
        ("PaymentGateway\n(Card/UPI/Net)", (8.5, 4.5), "#FFF0F5"),
        ("FiduciaryLedger", (5.0, 1.5), "#CEEAD6"),
        ("Administrator", (1.5, 1.5), "#FAD2CF"),
        ("Seller", (8.5, 1.5), "#E8D5F5")
    ]

    for label, (x, y), col in nodes:
        rect = patches.FancyBboxPatch((x-1.0, y-0.5), 2.0, 1.0, boxstyle="round,pad=0.1", fc=col, ec='#333333', lw=1.5)
        ax.add_patch(rect)
        ax.text(x, y, label, ha='center', va='center', fontsize=8, fontweight='bold')

    ax.plot([2.5, 4.0], [4.5, 4.5], color='#444444', lw=1.5)
    ax.text(3.25, 4.7, "1: commit_token()\n-->", ha='center', fontsize=7)

    ax.plot([6.0, 7.5], [4.5, 4.5], color='#444444', lw=1.5)
    ax.text(6.75, 4.7, "2: create_payment_intent()\n-->", ha='center', fontsize=7)

    ax.plot([8.5, 6.0], [4.0, 1.8], color='#444444', lw=1.5)
    ax.text(7.6, 2.9, "3: webhook_verify()\n<--", ha='center', fontsize=7)

    ax.plot([5.0, 5.0], [4.0, 2.0], color='#444444', lw=1.5)
    ax.text(5.3, 3.0, "4: lock_custody(PAID)\n|v", ha='left', fontsize=7)

    ax.plot([2.5, 4.0], [1.5, 1.5], color='#444444', lw=1.5)
    ax.text(3.25, 1.7, "<-- 5: dispute_escalate()\n6: force_refund() -->", ha='center', fontsize=7)

    ax.plot([6.0, 7.5], [1.5, 1.5], color='#444444', lw=1.5)
    ax.text(6.75, 1.7, "7: disburse_if_cleared() -->\n", ha='center', fontsize=7)

    ax.set_title("Figure 3.4.2: Collaboration Diagram — Fiduciary Escrow Settlement & Dispute", fontsize=11, fontweight='bold', pad=12)
    save_fig(fig, 'fig_collab_escrow.png')

# ==================== 8. STATE CHART DIAGRAMS ====================
def gen_state_property():
    fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')

    # Initial state
    circle_init = patches.Circle((0.8, 3.5), 0.2, facecolor='#111111')
    ax.add_patch(circle_init)

    states = [
        ("DRAFT\n(Proprietor Input)", (2.2, 3.5), "#E8F0FE"),
        ("PENDING_VALUATION\n(ML Features Validated)", (5.2, 3.5), "#FFF2CC"),
        ("ACTIVE_CATALOG\n(Public Marketplace)", (8.2, 3.5), "#D4EDDA"),
        ("FLAGGED_DUPLICATE\n(Dispute Station Hold)", (5.2, 1.2), "#F8D7DA"),
        ("INACTIVE_SUSPENDED\n(Admin Sanction)", (8.2, 1.2), "#E2E3E5")
    ]

    for label, (x, y), col in states:
        rect = patches.FancyBboxPatch((x-1.0, y-0.45), 2.0, 0.9, boxstyle="round,pad=0.1", fc=col, ec='#333333', lw=1.4)
        ax.add_patch(rect)
        ax.text(x, y, label, ha='center', va='center', fontsize=7, fontweight='bold')

    kw = dict(arrowstyle="->", lw=1.3, color='#333333')
    ax.annotate("", xy=(1.2, 3.5), xytext=(1.0, 3.5), arrowprops=kw)
    ax.annotate("save()", xy=(4.2, 3.5), xytext=(3.2, 3.5), arrowprops=kw, fontsize=7)
    ax.annotate("no duplicate", xy=(7.2, 3.5), xytext=(6.2, 3.5), arrowprops=kw, fontsize=7)
    ax.annotate("duplicate >= 0.85", xy=(5.2, 1.65), xytext=(5.2, 3.05), arrowprops=kw, fontsize=7)
    ax.annotate("approve unique", xy=(7.4, 3.2), xytext=(6.0, 1.65), arrowprops=kw, fontsize=7)
    ax.annotate("admin suspend", xy=(8.2, 1.65), xytext=(8.2, 3.05), arrowprops=kw, fontsize=7)

    ax.set_title("Figure 3.5.1: State Chart Diagram — Property Listing Lifecycle", fontsize=11, fontweight='bold', pad=12)
    save_fig(fig, 'fig_state_property.png')

def gen_state_escrow():
    fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')

    circle_init = patches.Circle((0.8, 3.5), 0.2, facecolor='#111111')
    ax.add_patch(circle_init)

    states = [
        ("CREATED\n(Checkout Token Initialized)", (2.2, 3.5), "#E8F0FE"),
        ("PAID_IN_ESCROW\n(Secured in Fiduciary Trust)", (5.5, 3.5), "#D4EDDA"),
        ("FAILED\n(Gateway Auth Reject)", (2.2, 1.2), "#F8D7DA"),
        ("DISPUTED\n(Admin Dispute Station)", (5.5, 1.2), "#FFF3CD"),
        ("REFUNDED\n(Bilateral Return to Buyer)", (8.5, 1.2), "#E2E3E5"),
        ("DISBURSED\n(Settled to Proprietor)", (8.5, 3.5), "#C3E6CB")
    ]

    for label, (x, y), col in states:
        rect = patches.FancyBboxPatch((x-1.0, y-0.45), 2.0, 0.9, boxstyle="round,pad=0.1", fc=col, ec='#333333', lw=1.4)
        ax.add_patch(rect)
        ax.text(x, y, label, ha='center', va='center', fontsize=7, fontweight='bold')

    kw = dict(arrowstyle="->", lw=1.3, color='#333333')
    ax.annotate("", xy=(1.2, 3.5), xytext=(1.0, 3.5), arrowprops=kw)
    ax.annotate("webhook signature OK", xy=(4.5, 3.5), xytext=(3.2, 3.5), arrowprops=kw, fontsize=7)
    ax.annotate("card decline", xy=(2.2, 1.65), xytext=(2.2, 3.05), arrowprops=kw, fontsize=7)
    ax.annotate("inspection pass", xy=(7.5, 3.5), xytext=(6.5, 3.5), arrowprops=kw, fontsize=7)
    ax.annotate("defect report", xy=(5.5, 1.65), xytext=(5.5, 3.05), arrowprops=kw, fontsize=7)
    ax.annotate("admin refund", xy=(7.5, 1.2), xytext=(6.5, 1.2), arrowprops=kw, fontsize=7)

    ax.set_title("Figure 3.5.2: State Chart Diagram — Escrow Fiduciary Lifecycle", fontsize=11, fontweight='bold', pad=12)
    save_fig(fig, 'fig_state_escrow.png')

# ==================== 9. COMPONENT DIAGRAM ====================
def gen_component():
    fig, ax = plt.subplots(figsize=(11, 7), dpi=200)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7)
    ax.axis('off')

    components = [
        ("<<component>>\nUI Presentation Layer\n- Bootstrap 5 / Emerald & Gold\n- Cinematic Intro SVG\n- Floating Capsule Dock\n- Responsive Viewports", (0.8, 4.0), 3.0, 2.4, "#E8F0FE"),
        ("<<component>>\nDjango 5.x Web Application\n- accounts (Auth & Role Logic)\n- properties (Catalog & Search)\n- chat (Channels ASGI & AI Bots)\n- payments (Escrow Multi-Rail)", (4.3, 4.0), 3.2, 2.4, "#FEF7E0"),
        ("<<component>>\nML Valuation Engine\n- LinearRegression Core\n- PricePredictor API\n- Hugging Face Hub Bridge\n- Feature Normalization", (8.0, 4.0), 2.6, 2.4, "#E6F4EA"),
        ("<<component>>\nWebSocket Async Router\n- Daphne ASGI Gateway\n- ChatConsumer Socket\n- In-Memory/Redis Channel Layer", (4.3, 1.0), 3.2, 2.2, "#F3E8FD"),
        ("<<component>>\nSQLite Relational Database\n- Users & UserProfile\n- Properties & Images\n- Conversations & Appointments\n- Payment Escrow Ledger", (0.8, 1.0), 3.0, 2.2, "#FFF0F5"),
        ("<<component>>\nExternal Payment Gateway\n- Mock Fiduciary Rail\n- Card / UPI QR / Net Banking\n- Webhook Signature Verify", (8.0, 1.0), 2.6, 2.2, "#EBF4F6")
    ]

    for label, (x, y), w, h, col in components:
        rect = patches.Rectangle((x, y), w, h, facecolor=col, edgecolor='#222222', lw=1.5)
        ax.add_patch(rect)
        # Tab boxes indicating UML component
        tab1 = patches.Rectangle((x-0.2, y+h-0.6), 0.4, 0.25, facecolor=col, edgecolor='#222222', lw=1.2)
        tab2 = patches.Rectangle((x-0.2, y+h-1.1), 0.4, 0.25, facecolor=col, edgecolor='#222222', lw=1.2)
        ax.add_patch(tab1)
        ax.add_patch(tab2)
        ax.text(x + 0.1, y + h - 0.2, label, va='top', fontsize=7.2, fontfamily='sans-serif')

    kw = dict(arrowstyle="<->", lw=1.5, color='#444444')
    ax.annotate("", xy=(3.8, 5.2), xytext=(4.3, 5.2), arrowprops=kw)
    ax.annotate("", xy=(7.5, 5.2), xytext=(8.0, 5.2), arrowprops=kw)
    ax.annotate("", xy=(5.9, 4.0), xytext=(5.9, 3.2), arrowprops=kw)
    ax.annotate("", xy=(2.3, 4.0), xytext=(2.3, 3.2), arrowprops=kw)
    ax.annotate("", xy=(7.5, 2.1), xytext=(8.0, 2.1), arrowprops=kw)

    ax.set_title("Figure 4.1: UML Component Architecture Diagram", fontsize=11, fontweight='bold', pad=12)
    save_fig(fig, 'fig_component.png')

# ==================== 10. DEPLOYMENT DIAGRAM ====================
def gen_deployment():
    fig, ax = plt.subplots(figsize=(11, 7), dpi=200)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7)
    ax.axis('off')

    nodes = [
        ("<<node>>\nClient Device (Workstation / Mobile)\n----------------------------------------\n[Web Browser (Chrome, Firefox, Safari)]\n- DOM Execution & WebSocket Client\n- Bootstrap 5 & Gold Theme Styles\n- Session Storage State Engine", (0.8, 2.2), 3.0, 3.4, "#E8F4F8"),
        ("<<node>>\nHost Server (Localhost / Production)\n----------------------------------------\n[Daphne ASGI Server Process]\n- Port 8000 (HTTP + WSS Protocols)\n- Django Application Framework 5.x\n- Channels Event Loop & StatReloader\n- AI Chatbot Engines (Buyer/Seller/Admin)", (4.3, 2.2), 3.4, 3.4, "#FFF8E7"),
        ("<<node>>\nStorage Subsystem\n----------------------------------------\n[SQLite3 Relational DB]\n- db.sqlite3 (WAL Mode)\n[Static & Media Filesystem]\n- /static/css (emerald-gold-v4)\n- /media/property_images/ (15 Estates)", (8.2, 2.2), 2.6, 3.4, "#EAEAEA")
    ]

    for label, (x, y), w, h, col in nodes:
        # Draw 3D cube effect for UML node
        rect = patches.Rectangle((x, y), w, h, facecolor=col, edgecolor='#222222', lw=1.5)
        ax.add_patch(rect)
        ax.text(x + 0.1, y + h - 0.2, label, va='top', fontsize=7.2, fontfamily='sans-serif')

    kw = dict(arrowstyle="<->", lw=1.6, color='#222222')
    ax.annotate("HTTP / WebSocket (WSS)\nTCP Port 8000", xy=(3.8, 3.9), xytext=(4.3, 3.9), arrowprops=kw, fontsize=7.5, ha='center')
    ax.annotate("Direct File I/O &\nSQL Query Engine", xy=(7.7, 3.9), xytext=(8.2, 3.9), arrowprops=kw, fontsize=7.5, ha='center')

    ax.set_title("Figure 4.2: UML Deployment Architecture Diagram", fontsize=11, fontweight='bold', pad=12)
    save_fig(fig, 'fig_deployment.png')

# ==================== 11. ER DIAGRAM ====================
def gen_er_model():
    fig, ax = plt.subplots(figsize=(12, 8), dpi=200)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')

    entities = [
        ("USER (auth_user)\n---------------------\nPK: id (int)\n- username (varchar)\n- email (varchar)\n- is_staff (bool)\n- is_active (bool)", (0.5, 4.8), 2.4, 2.6, "#E8F0FE"),
        ("USER_PROFILE\n---------------------\nPK: id (int)\nFK: user_id (1:1)\n- role (BUYER/SELLER/ADMIN)\n- phone (varchar)\n- is_verified (bool)", (3.4, 4.8), 2.4, 2.6, "#E8F0FE"),
        ("PROPERTY\n---------------------\nPK: id (int)\nFK: seller_id (User)\nFK: duplicate_of_id\n- title, city, locality\n- listed_price (Decimal)\n- predicted_price (Decimal)\n- status (ACTIVE/INACTIVE)", (6.3, 4.8), 2.5, 2.6, "#FFF2CC"),
        ("PROPERTY_IMAGE\n---------------------\nPK: id (int)\nFK: property_id (Property)\n- image (ImageField)\n- uploaded_at (datetime)", (9.3, 4.8), 2.3, 2.6, "#FFF2CC"),
        ("CONVERSATION\n---------------------\nPK: id (int)\nFK: property_id\nFK: buyer_id (User)\nFK: seller_id (User)\n- created_at (datetime)", (0.5, 1.0), 2.4, 2.6, "#E6F4EA"),
        ("MESSAGE\n---------------------\nPK: id (int)\nFK: conversation_id\nFK: sender_id (User)\n- body (text)\n- read_at (datetime)", (3.4, 1.0), 2.4, 2.6, "#E6F4EA"),
        ("APPOINTMENT\n---------------------\nPK: id (int)\nFK: conversation_id\nFK: requested_by (User)\n- status (REQ/CONF/DECL)\n- scheduled_for (datetime)", (6.3, 1.0), 2.5, 2.6, "#FCE8E6"),
        ("PAYMENT (ESCROW)\n---------------------\nPK: id (int)\nFK: estate_id (Property)\nFK: buyer_id (User)\n- amount_paise (int)\n- status (PAID/REF/HELD)\n- public_id (UUID)", (9.3, 1.0), 2.3, 2.6, "#F3E8FD")
    ]

    for label, (x, y), w, h, col in entities:
        rect = patches.Rectangle((x, y), w, h, facecolor=col, edgecolor='#222222', lw=1.3)
        ax.add_patch(rect)
        ax.text(x + 0.1, y + h - 0.2, label, va='top', fontsize=6.8, fontfamily='monospace')

    kw = dict(arrowstyle="->", lw=1.2, color='#555555')
    ax.annotate("1:1", xy=(3.4, 6.0), xytext=(2.9, 6.0), arrowprops=kw, fontsize=7)
    ax.annotate("1:N", xy=(6.3, 6.0), xytext=(5.8, 6.0), arrowprops=kw, fontsize=7)
    ax.annotate("1:N", xy=(9.3, 6.0), xytext=(8.8, 6.0), arrowprops=kw, fontsize=7)
    ax.annotate("1:N", xy=(3.4, 2.2), xytext=(2.9, 2.2), arrowprops=kw, fontsize=7)
    ax.annotate("1:N", xy=(6.3, 2.2), xytext=(5.8, 2.2), arrowprops=kw, fontsize=7)
    ax.annotate("1:N", xy=(9.3, 2.2), xytext=(8.8, 2.2), arrowprops=kw, fontsize=7)

    ax.set_title("Figure 4.4: Relational Database Entity-Relationship (ER) Architecture", fontsize=11, fontweight='bold', pad=12)
    save_fig(fig, 'fig_er_model.png')

if __name__ == '__main__':
    print("Generating comprehensive visual engineering diagrams...")
    gen_thapar_logo()
    gen_swimlane()
    gen_dfd_lvl0()
    gen_dfd_lvl1()
    gen_dfd_lvl2()
    gen_class_service()
    gen_collab_appointment()
    gen_collab_escrow()
    gen_state_property()
    gen_state_escrow()
    gen_component()
    gen_deployment()
    gen_er_model()
    print("All diagrams generated successfully!")
