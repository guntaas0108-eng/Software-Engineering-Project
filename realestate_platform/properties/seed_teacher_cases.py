import os
import sys
from pathlib import Path
from decimal import Decimal

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()

from django.contrib.auth import get_user_model
from properties.models import Property
from accounts.models import UserProfile

User = get_user_model()

# Ensure seller accounts exist
seller1 = User.objects.filter(username="seller1").first()
if not seller1:
    seller1 = User.objects.create_user(username="seller1", password="seller123")
    seller1.profile.role = UserProfile.Role.SELLER
    seller1.profile.save()

seller2 = User.objects.filter(username="seller2").first()
if not seller2:
    seller2 = User.objects.create_user(username="seller2", password="seller2123")
    seller2.profile.role = UserProfile.Role.SELLER
    seller2.profile.save()

properties_to_create = [
    # =========================================================================
    # CASE 1: BEST TIME: BUY NOW 🚀 (Under-valued deals, ratio <= 0.95, diff_pct <= -5%)
    # =========================================================================
    {
        "seller": seller1,
        "title": "The Palm Court Luxury Penthouse — High Equity Deal",
        "description": "Panoramic duplex penthouse overlooking the city greenbelt. Features Italian marble flooring, 12-ft ceiling heights, wraparound private sky deck, and direct private elevator access. Priced significantly below algorithmic comp valuation for quick family liquidation.",
        "category": Property.Category.RESIDENTIAL,
        "locality": "Sector 17",
        "city": "Chandigarh",
        "area_sqft": Decimal("3400"),
        "bedrooms": 4,
        "bathrooms": 4,
        "age_years": 2,
        "listed_price": Decimal("18000000"),
        "predicted_price": Decimal("22000000"),  # ratio = 0.818 -> BEST TIME: BUY NOW 🚀
        "status": Property.Status.ACTIVE,
    },
    {
        "seller": seller2,
        "title": "Grand Heritage Villa — Foreclosure Valuation Deal",
        "description": "Distinguished colonial courtyard villa featuring expansive manicured lawns, private solar heated swimming pool, 3-car air-conditioned garage, and bespoke teak woodwork throughout. Urgent off-market transaction at heavy equity discount.",
        "category": Property.Category.RESIDENTIAL,
        "locality": "Sarabha Nagar",
        "city": "Ludhiana",
        "area_sqft": Decimal("4800"),
        "bedrooms": 5,
        "bathrooms": 5,
        "age_years": 3,
        "listed_price": Decimal("25500000"),
        "predicted_price": Decimal("31000000"),  # ratio = 0.822 -> BEST TIME: BUY NOW 🚀
        "status": Property.Status.ACTIVE,
    },
    {
        "seller": seller1,
        "title": "The Crest Panoramic Sky Duplex — High Yield",
        "description": "Ultra-luxury sky duplex on Golf Course Road with double-height living room, floor-to-ceiling soundproof acoustic glazing, automated smart home lighting, and private concierge lobby. Strong capital appreciation potential.",
        "category": Property.Category.RESIDENTIAL,
        "locality": "Golf Course Extension",
        "city": "Gurgaon",
        "area_sqft": Decimal("5200"),
        "bedrooms": 5,
        "bathrooms": 6,
        "age_years": 1,
        "listed_price": Decimal("37000000"),
        "predicted_price": Decimal("44000000"),  # ratio = 0.841 -> BEST TIME: BUY NOW 🚀
        "status": Property.Status.ACTIVE,
    },
    {
        "seller": seller2,
        "title": "Aura Commercial IT Suites — Grade-A Office Hub",
        "description": "Grade-A LEED certified commercial office suites with institutional corporate tenant lease underway. High dual-income yield asset with 10.5% projected annual micro-market appreciation. Significant discount to replacement cost.",
        "category": Property.Category.COMMERCIAL,
        "locality": "Cyber City Phase III",
        "city": "Gurgaon",
        "area_sqft": Decimal("6500"),
        "bedrooms": None,
        "bathrooms": 4,
        "age_years": 2,
        "listed_price": Decimal("51000000"),
        "predicted_price": Decimal("62000000"),  # ratio = 0.822 -> BEST TIME: BUY NOW 🚀
        "status": Property.Status.ACTIVE,
    },

    # =========================================================================
    # CASE 2: FAVORABLE TIME: BUY NOW 🟢 (Fair Market, ratio 0.96 - 1.04, diff_pct -4% to +4%)
    # =========================================================================
    {
        "seller": seller1,
        "title": "Kensington Royal Manor — Fair Market Benchmark",
        "description": "Exquisite Mediterranean-styled sanctuary featuring Portuguese tile accents, private saltwater pool, lush frangipani courtyards, and sunlit chef kitchen. Perfectly priced at fair market valuation with steady compounding upside.",
        "category": Property.Category.RESIDENTIAL,
        "locality": "Assagao",
        "city": "Goa",
        "area_sqft": Decimal("3800"),
        "bedrooms": 4,
        "bathrooms": 4,
        "age_years": 1,
        "listed_price": Decimal("25800000"),
        "predicted_price": Decimal("26000000"),  # ratio = 0.992 -> FAVORABLE TIME: BUY NOW 🟢
        "status": Property.Status.ACTIVE,
    },
    {
        "seller": seller2,
        "title": "The Solarium Garden Penthouse — Prime Corridor",
        "description": "Contemporary glass penthouse with panoramic views of the tech corridor. Smart climate zones, motorized louvers, private plunge pool on the upper deck, and EV charging station. Accurately benchmarked to neighborhood comps.",
        "category": Property.Category.RESIDENTIAL,
        "locality": "Whitefield",
        "city": "Bangalore",
        "area_sqft": Decimal("2900"),
        "bedrooms": 3,
        "bathrooms": 3,
        "age_years": 2,
        "listed_price": Decimal("19800000"),
        "predicted_price": Decimal("19500000"),  # ratio = 1.015 -> FAVORABLE TIME: BUY NOW 🟢
        "status": Property.Status.ACTIVE,
    },
    {
        "seller": seller1,
        "title": "Pinecrest Lakeview Bungalow — Heritage Avenue",
        "description": "Classic brick bungalow situated on prestigious Mall Road. Features manicured front lawns, high vaulted timber ceilings, library den with fireplace, and separate guest annex. Fair market asking valuation.",
        "category": Property.Category.RESIDENTIAL,
        "locality": "Mall Road Enclave",
        "city": "Amritsar",
        "area_sqft": Decimal("4200"),
        "bedrooms": 4,
        "bathrooms": 4,
        "age_years": 4,
        "listed_price": Decimal("21200000"),
        "predicted_price": Decimal("21000000"),  # ratio = 1.009 -> FAVORABLE TIME: BUY NOW 🟢
        "status": Property.Status.ACTIVE,
    },
    {
        "seller": seller2,
        "title": "Banjara Heights Architectural Residence — Premium Comps",
        "description": "Modernist concrete and glass residence perched on the rocky ridge of Banjara Hills. Designed by acclaimed architectural firm with infinity lap pool, climate-controlled wine cellar, and subterranean screening room.",
        "category": Property.Category.RESIDENTIAL,
        "locality": "Road No. 10, Banjara Hills",
        "city": "Hyderabad",
        "area_sqft": Decimal("5600"),
        "bedrooms": 5,
        "bathrooms": 5,
        "age_years": 2,
        "listed_price": Decimal("42500000"),
        "predicted_price": Decimal("42000000"),  # ratio = 1.012 -> FAVORABLE TIME: BUY NOW 🟢
        "status": Property.Status.ACTIVE,
    },

    # =========================================================================
    # CASE 3: MONITOR & NEGOTIATE ⏳ (Mild premium, ratio 1.05 - 1.12, diff_pct +5% to +12%)
    # =========================================================================
    {
        "seller": seller1,
        "title": "The Renaissance Duplex — Negotiate Entry",
        "description": "Spacious park-facing duplex with handcrafted wood molding and marble fireplace. The proprietor is seeking an elevated asking premium. Prospective buyers are advised by ML models to negotiate towards fair comp valuation.",
        "category": Property.Category.RESIDENTIAL,
        "locality": "Model Town",
        "city": "Ludhiana",
        "area_sqft": Decimal("3100"),
        "bedrooms": 4,
        "bathrooms": 3,
        "age_years": 3,
        "listed_price": Decimal("20200000"),
        "predicted_price": Decimal("18500000"),  # ratio = 1.092 -> MONITOR & NEGOTIATE ⏳
        "status": Property.Status.ACTIVE,
    },
    {
        "seller": seller2,
        "title": "Sovereign Marina Sky Suite — Price Spread Advisory",
        "description": "Frontline sea-facing residence with sunset views over the Arabian Sea. While rare, the current asking price reflects speculative seller sentiment. Negotiating down before contract closing is highly recommended.",
        "category": Property.Category.RESIDENTIAL,
        "locality": "Marine Lines",
        "city": "Mumbai",
        "area_sqft": Decimal("2200"),
        "bedrooms": 3,
        "bathrooms": 3,
        "age_years": 5,
        "listed_price": Decimal("38000000"),
        "predicted_price": Decimal("35000000"),  # ratio = 1.085 -> MONITOR & NEGOTIATE ⏳
        "status": Property.Status.ACTIVE,
    },
    {
        "seller": seller1,
        "title": "Cedar Valley Estate Villa — Premium Locality Spread",
        "description": "Stately villa situated along tree-lined Sector 8 boulevard. Features private tennis court, solar water heating, imported travertine marble, and private domestic quarters. Seller asking price carries an 8.8% negotiable margin.",
        "category": Property.Category.RESIDENTIAL,
        "locality": "Sector 8",
        "city": "Chandigarh",
        "area_sqft": Decimal("4500"),
        "bedrooms": 5,
        "bathrooms": 4,
        "age_years": 4,
        "listed_price": Decimal("37000000"),
        "predicted_price": Decimal("34000000"),  # ratio = 1.088 -> MONITOR & NEGOTIATE ⏳
        "status": Property.Status.ACTIVE,
    },
    {
        "seller": seller2,
        "title": "Prestige Techpark Office Floor — Moderate Asking Spread",
        "description": "Full-floor commercial office space with modern modular partitions, server room infrastructure, dedicated elevators, and 12 reserved basement parking slots. Advise counter-offering at fair valuation.",
        "category": Property.Category.COMMERCIAL,
        "locality": "Hitec City",
        "city": "Hyderabad",
        "area_sqft": Decimal("4000"),
        "bedrooms": None,
        "bathrooms": 3,
        "age_years": 2,
        "listed_price": Decimal("41500000"),
        "predicted_price": Decimal("38000000"),  # ratio = 1.092 -> MONITOR & NEGOTIATE ⏳
        "status": Property.Status.ACTIVE,
    },

    # =========================================================================
    # CASE 4: WAIT FOR CORRECTION 📉 (High premium, ratio > 1.15, diff_pct +20% to +40%)
    # =========================================================================
    {
        "seller": seller1,
        "title": "The Apex Super-Penthouse — Speculative Overpricing",
        "description": "High-altitude penthouse with glass-bottom infinity cantilever. Currently listed with a massive +30% speculative bubble premium above ML regression comps. Algorithmic engines strongly advise buyers to WAIT for market correction.",
        "category": Property.Category.RESIDENTIAL,
        "locality": "Worli",
        "city": "Mumbai",
        "area_sqft": Decimal("4800"),
        "bedrooms": 4,
        "bathrooms": 5,
        "age_years": 2,
        "listed_price": Decimal("58500000"),
        "predicted_price": Decimal("45000000"),  # ratio = 1.300 -> WAIT FOR CORRECTION 📉
        "status": Property.Status.ACTIVE,
    },
    {
        "seller": seller2,
        "title": "The Venetian Classical Manor — Severe Premium Markup",
        "description": "Neo-classical estate featuring Roman columns and imported bronze chandeliers. Listed at an extreme +35% valuation gap over neighborhood comp algorithms. Delaying purchase saves significant capital.",
        "category": Property.Category.RESIDENTIAL,
        "locality": "Golf Links",
        "city": "New Delhi",
        "area_sqft": Decimal("6000"),
        "bedrooms": 6,
        "bathrooms": 6,
        "age_years": 6,
        "listed_price": Decimal("81000000"),
        "predicted_price": Decimal("60000000"),  # ratio = 1.350 -> WAIT FOR CORRECTION 📉
        "status": Property.Status.ACTIVE,
    },
    {
        "seller": seller1,
        "title": "Hilltop Castle & Orchard Retreat — Overpriced Valuation",
        "description": "Sprawling colonial hill station estate with apple orchards and misty valley panoramas. Overpriced by nearly 30% against micro-market regression models. Waiting for pricing adjustment strongly recommended.",
        "category": Property.Category.RESIDENTIAL,
        "locality": "Kodaikanal Enclave",
        "city": "Kodaikanal",
        "area_sqft": Decimal("5500"),
        "bedrooms": 5,
        "bathrooms": 4,
        "age_years": 7,
        "listed_price": Decimal("28500000"),
        "predicted_price": Decimal("22000000"),  # ratio = 1.295 -> WAIT FOR CORRECTION 📉
        "status": Property.Status.ACTIVE,
    },
    {
        "seller": seller2,
        "title": "Opal Skyline Commercial Tower — Speculative Asking Floor",
        "description": "Multi-tier glass commercial complex. Asking price has inflated beyond tenant yield capitalization rates. ML timing models predict market price adjustment within 6–12 months.",
        "category": Property.Category.COMMERCIAL,
        "locality": "DLF Cyber City",
        "city": "Gurgaon",
        "area_sqft": Decimal("7500"),
        "bedrooms": None,
        "bathrooms": 5,
        "age_years": 3,
        "listed_price": Decimal("92000000"),
        "predicted_price": Decimal("70000000"),  # ratio = 1.314 -> WAIT FOR CORRECTION 📉
        "status": Property.Status.ACTIVE,
    },

    # =========================================================================
    # CASE 5: SOLD OUT / ACQUIRED 🏷️ (Transacted via Escrow, grayscale & disabled)
    # =========================================================================
    {
        "seller": seller1,
        "title": "The Royal Pavilion Penthouse — Transacted & Acquired",
        "description": "Historic top-tier penthouse recently acquired through PropertyPulse sovereign escrow token settlement. Legal title transferred, custody sealed, and public reservation channels closed.",
        "category": Property.Category.RESIDENTIAL,
        "locality": "Civil Lines",
        "city": "Jaipur",
        "area_sqft": Decimal("3600"),
        "bedrooms": 4,
        "bathrooms": 4,
        "age_years": 3,
        "listed_price": Decimal("16500000"),
        "predicted_price": Decimal("17000000"),
        "status": Property.Status.SOLD,
    },
    {
        "seller": seller2,
        "title": "Casa Bianca Waterfront Villa — Escrow Closed & Sold",
        "description": "Ultra-private sea-facing villa in North Goa featuring private beach trail. Fully funded and successfully transacted via escrow. Displayed in public archives for historical comp valuation.",
        "category": Property.Category.RESIDENTIAL,
        "locality": "Anjuna Coastal Highway",
        "city": "Goa",
        "area_sqft": Decimal("4400"),
        "bedrooms": 4,
        "bathrooms": 5,
        "age_years": 2,
        "listed_price": Decimal("28000000"),
        "predicted_price": Decimal("29500000"),
        "status": Property.Status.SOLD,
    },

    # =========================================================================
    # CASE 6: SPECIALIZED LAND PLOT & GOLF ENCLAVE (Asset diversity)
    # =========================================================================
    {
        "seller": seller1,
        "title": "The Sovereign Highland Plot — 1-Acre Prime Land",
        "description": "Rare freehold corner plot in a gated luxury enclave with mountain views. All municipal utility connections, security post, and boundary walls completed. High appreciation potential with +1.5% compounding tilt.",
        "category": Property.Category.LAND,
        "locality": "Panchkula Extension",
        "city": "Panchkula",
        "area_sqft": Decimal("10800"),
        "bedrooms": None,
        "bathrooms": None,
        "age_years": 0,
        "listed_price": Decimal("22000000"),
        "predicted_price": Decimal("26000000"),  # ratio = 0.846 -> BEST TIME: BUY NOW 🚀
        "status": Property.Status.ACTIVE,
    },
    {
        "seller": seller2,
        "title": "Silver Oak Championship Golf Villa — Fair Valuation",
        "description": "Signature villa directly facing the 14th fairway. Double-height foyer, heated swimming pool, rooftop putting green, and private golf cart garage. Fairly priced benchmark entry.",
        "category": Property.Category.RESIDENTIAL,
        "locality": "Sector 38 Golf Links",
        "city": "Chandigarh",
        "area_sqft": Decimal("4100"),
        "bedrooms": 4,
        "bathrooms": 4,
        "age_years": 2,
        "listed_price": Decimal("27500000"),
        "predicted_price": Decimal("28000000"),  # ratio = 0.982 -> FAVORABLE TIME: BUY NOW 🟢
        "status": Property.Status.ACTIVE,
    },
]

created_count = 0
for data in properties_to_create:
    title = data["title"]
    # Check if already exists to prevent duplicate execution
    prop = Property.objects.filter(title=title).first()
    if not prop:
        Property.objects.create(**data)
        created_count += 1
        print(f"Created estate: {title}")
    else:
        # Update fields
        for k, v in data.items():
            setattr(prop, k, v)
        prop.save()
        print(f"Updated estate: {title}")

print(f"\nSUCCESS: Seeded/Updated {len(properties_to_create)} demonstration estates!")
print(f"Total estates now in database: {Property.objects.count()}")
