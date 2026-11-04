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

## 🤖 3. Dual Role-Segregated AI Advisory Engine

The AI assistants are strictly segregated on both the frontend UI and the backend API:

### A. Estate Concierge AI (Exclusively for Buyers)
* **Target Audience:** Accredited buyers, investors, and prospective clients.
* **Capabilities:**
  * Curates luxury residences by lifestyle amenities (e.g. *"Show me villas with an infinity pool"*).
  * Computes mathematical mortgage amortizations and monthly EMIs (e.g. *"Calculate EMI for a ₹15 Cr estate loan"* at 8.5% luxury lending rate).
  * Explains ML algorithmic valuations (*Great Deal*, *Fair Price*, *Premium*).
  * Informs the buyer about unread seller dispatches and confirmed viewing tours.
* **UI Controls:** Mode switchers are completely disabled. Prompts chips only display buyer discovery queries.

### B. Portfolio Strategist AI (Exclusively for Sellers)
* **Target Audience:** Estate proprietors, luxury homeowners, and developers.
* **Capabilities:**
  * Analyzes asking prices against the Machine Learning AI Barometer.
  * Recommends luxury staging protocols (twilight photography, title clearance, VIP viewing briefs).
  * Monitors buyer inquiries and private appointment requests.
  * Advises on token escrow security deposits.
* **UI Controls:** Mode switchers are completely disabled. Prompt chips only display seller optimization queries.

### C. Executive Platform AI (Exclusively for Administrators)
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

## 🏛️ 7. Curated Catalog of 15 Luxury Test Estates

The database comes pre-seeded with **15 luxury estates** featuring high-resolution photography, AI Barometer valuations, and distinct architectural categories:
* *The Palm Manor — Waterfront Colonial Estate* (Alibaug)
* *The Grand Imperial Haveli* (Civil Lines, Jaipur)
* *Skyline Sovereign Penthouse* (Worli Sea Face, Mumbai)
* *The Whispering Pines Alpine Villa* (Kasauli Hills)
* *Monsoon Palms Portuguese Heritage Villa* (Assagao, Goa)
* *The Glass Pavilion Modernist Estate* (Golf Links, New Delhi)
* *The Royal Orchard Country Estate* (Sadahalli, Bangalore)
* *The Crestview Lakefront Villa* (Udaipur Lakefront)
* *Elysium Heights Duplex Sky-Mansion* (Jubilee Hills, Hyderabad)
* *The Sterling Heritage Plantation Villa* (Coonoor, Nilgiris)
* *The Citadel Modernist Mansion* (DLF Phase 5, Gurgaon)
* *The Azure Bay Cliffside Residence* (Dona Paula, Goa)
* *The Windsor Court Georgian Villa* (Race Course, Dehradun)
* *The Emerald Courtyard Haveli* (Old City Enclave, Udaipur)
* *The Solarium Glass Villa* (Lonavala Hill Crest)

---

## 🔑 8. Login Credentials Cheatsheet

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
