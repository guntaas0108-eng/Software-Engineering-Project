import sqlite3
import os
from datetime import datetime, timezone

DB_PATH = os.path.join(os.path.dirname(__file__), "real_estate.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(ml_predictor=None):
    """Initializes tables and seeds initial realistic sample properties."""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT UNIQUE NOT NULL,
        role TEXT NOT NULL,
        created_at TEXT
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS otp_codes (
        phone TEXT PRIMARY KEY,
        otp TEXT NOT NULL,
        expires_at TEXT NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS properties (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        property_type TEXT NOT NULL,
        city TEXT NOT NULL,
        locality TEXT NOT NULL,
        area_sqft REAL NOT NULL,
        bedrooms INTEGER DEFAULT 2,
        bathrooms INTEGER DEFAULT 2,
        property_age INTEGER DEFAULT 0,
        has_parking INTEGER DEFAULT 1,
        furnishing TEXT DEFAULT 'Semi-Furnished',
        price REAL NOT NULL,
        predicted_price REAL,
        barometer_score INTEGER,
        barometer_verdict TEXT,
        image_url TEXT,
        seller_name TEXT,
        seller_phone TEXT,
        created_at TEXT
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        property_id INTEGER NOT NULL,
        sender_type TEXT NOT NULL,
        sender_name TEXT NOT NULL,
        message_text TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        FOREIGN KEY (property_id) REFERENCES properties(id)
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        property_id INTEGER NOT NULL,
        buyer_name TEXT NOT NULL,
        buyer_phone TEXT NOT NULL,
        visit_date TEXT NOT NULL,
        visit_time TEXT NOT NULL,
        notes TEXT,
        status TEXT DEFAULT 'pending',
        first_inquiry_timestamp TEXT,
        confirmed_timestamp TEXT,
        time_to_appointment_seconds REAL,
        created_at TEXT NOT NULL,
        FOREIGN KEY (property_id) REFERENCES properties(id)
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS payments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        property_id INTEGER NOT NULL,
        appointment_id INTEGER,
        buyer_name TEXT NOT NULL,
        amount REAL NOT NULL,
        payment_method TEXT NOT NULL,
        transaction_id TEXT NOT NULL,
        payment_status TEXT DEFAULT 'success',
        timestamp TEXT NOT NULL,
        FOREIGN KEY (property_id) REFERENCES properties(id)
    );
    """)

    conn.commit()

    # Seed properties if empty
    cur.execute("SELECT COUNT(*) FROM properties")
    count = cur.fetchone()[0]
    if count == 0 and ml_predictor:
        seed_properties(conn, ml_predictor)

    conn.close()

def seed_properties(conn, ml_predictor):
    """Seed initial representative properties across cities and categories."""
    initial_properties = [
        {
            "title": "Luxury 3 BHK High-Rise Apartment",
            "description": "Modern apartment near Thapar University with clubhouse, 24/7 power backup, and modular kitchen.",
            "property_type": "Apartment",
            "city": "Patiala",
            "locality": "Bhadson Road",
            "area_sqft": 1650,
            "bedrooms": 3,
            "bathrooms": 3,
            "property_age": 2,
            "has_parking": 1,
            "furnishing": "Semi-Furnished",
            "price": 8200000,
            "image_url": "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=800&q=80",
            "seller_name": "Guntaas Singh",
            "seller_phone": "+91 98765 43210"
        },
        {
            "title": "Grand 4 BHK Independent Villa",
            "description": "Spacious independent villa with landscaped garden, Italian marble flooring, and double car garage.",
            "property_type": "Villa",
            "city": "Chandigarh",
            "locality": "Sector 8",
            "area_sqft": 3200,
            "bedrooms": 4,
            "bathrooms": 4,
            "property_age": 4,
            "has_parking": 1,
            "furnishing": "Fully-Furnished",
            "price": 24500000,
            "image_url": "https://images.unsplash.com/photo-1613977257363-707ba9348227?auto=format&fit=crop&w=800&q=80",
            "seller_name": "Atiksh Gupta",
            "seller_phone": "+91 98111 22334"
        },
        {
            "title": "Prime Retail Commercial Showroom",
            "description": "High footfall commercial space suitable for bank, franchise store, or restaurant hub.",
            "property_type": "Commercial",
            "city": "Mohali",
            "locality": "Phase 7 Market",
            "area_sqft": 2100,
            "bedrooms": 0,
            "bathrooms": 2,
            "property_age": 3,
            "has_parking": 1,
            "furnishing": "Unfurnished",
            "price": 17800000,
            "image_url": "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=800&q=80",
            "seller_name": "Haneesh",
            "seller_phone": "+91 99222 33445"
        },
        {
            "title": "Cozy 2 BHK Garden Facing Flat",
            "description": "Peaceful gated society with swimming pool, gym, and park view balcony.",
            "property_type": "Residential",
            "city": "Patiala",
            "locality": "Urban Estate Phase II",
            "area_sqft": 1200,
            "bedrooms": 2,
            "bathrooms": 2,
            "property_age": 6,
            "has_parking": 1,
            "furnishing": "Semi-Furnished",
            "price": 5100000,
            "image_url": "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?auto=format&fit=crop&w=800&q=80",
            "seller_name": "Dhruv Rajput",
            "seller_phone": "+91 97333 44556"
        },
        {
            "title": "Gaming & Bowling Entertainment Arena Space",
            "description": "Pre-configured entertainment hub suitable for VR arcade, gaming zone, and cafe lounge.",
            "property_type": "Entertainment",
            "city": "Chandigarh",
            "locality": "Industrial Area Phase 1",
            "area_sqft": 4500,
            "bedrooms": 0,
            "bathrooms": 4,
            "property_age": 1,
            "has_parking": 1,
            "furnishing": "Fully-Furnished",
            "price": 31000000,
            "image_url": "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=800&q=80",
            "seller_name": "Guntaas Singh",
            "seller_phone": "+91 98765 43210"
        },
        {
            "title": "Smart Tech 3 BHK Penthouse",
            "description": "Panoramic city view with private terrace, automated smart switches, and EV charging spot.",
            "property_type": "Apartment",
            "city": "Bangalore",
            "locality": "Whitefield",
            "area_sqft": 2200,
            "bedrooms": 3,
            "bathrooms": 3,
            "property_age": 1,
            "has_parking": 1,
            "furnishing": "Fully-Furnished",
            "price": 26500000,
            "image_url": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=80",
            "seller_name": "Atiksh Gupta",
            "seller_phone": "+91 98111 22334"
        }
    ]

    cur = conn.cursor()
    now_str = datetime.now(timezone.utc).isoformat()

    for p in initial_properties:
        pred_res = ml_predictor.predict(p)
        cur.execute("""
        INSERT INTO properties (
            title, description, property_type, city, locality,
            area_sqft, bedrooms, bathrooms, property_age, has_parking,
            furnishing, price, predicted_price, barometer_score, barometer_verdict,
            image_url, seller_name, seller_phone, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            p["title"], p["description"], p["property_type"], p["city"], p["locality"],
            p["area_sqft"], p["bedrooms"], p["bathrooms"], p["property_age"], p["has_parking"],
            p["furnishing"], p["price"], pred_res["predicted_price"], pred_res["barometer_score"],
            pred_res["barometer_verdict"], p["image_url"], p["seller_name"], p["seller_phone"], now_str
        ))
        prop_id = cur.lastrowid

        # Add initial sample negotiation message to show the feature
        cur.execute("""
        INSERT INTO messages (property_id, sender_type, sender_name, message_text, timestamp)
        VALUES (?, 'seller', ?, ?, ?)
        """, (
            prop_id,
            p["seller_name"],
            f"Hello! Thank you for viewing {p['title']}. Feel free to ask questions or propose a site visit.",
            now_str
        ))

    conn.commit()

def check_duplicate(title, property_type, locality, city):
    """Detects possible duplicate listings based on title similarity and location."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    SELECT id, title, locality, city FROM properties 
    WHERE property_type = ? AND city = ?
    """, (property_type, city))
    rows = cur.fetchall()
    conn.close()

    duplicates = []
    clean_title = set(title.lower().split())
    for r in rows:
        existing_tokens = set(r["title"].lower().split())
        overlap = clean_title.intersection(existing_tokens)
        locality_match = (locality.lower() in r["locality"].lower()) or (r["locality"].lower() in locality.lower())
        
        if len(overlap) >= 2 or locality_match:
            duplicates.append({
                "id": r["id"],
                "title": r["title"],
                "locality": r["locality"],
                "similarity_reason": "Matching locality or significant title overlap"
            })
    return duplicates

def add_property(data, ml_predictor):
    """Add a new property, evaluate prediction and barometer, and insert."""
    pred_res = ml_predictor.predict(data)
    now_str = datetime.now(timezone.utc).isoformat()

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO properties (
        title, description, property_type, city, locality,
        area_sqft, bedrooms, bathrooms, property_age, has_parking,
        furnishing, price, predicted_price, barometer_score, barometer_verdict,
        image_url, seller_name, seller_phone, created_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data.get("title", "Untitled Property"),
        data.get("description", ""),
        data.get("property_type", "Residential"),
        data.get("city", "Patiala"),
        data.get("locality", "Central"),
        float(data.get("area_sqft", 1000)),
        int(data.get("bedrooms", 2)),
        int(data.get("bathrooms", 2)),
        int(data.get("property_age", 0)),
        1 if data.get("has_parking") in [1, True, "1", "true"] else 0,
        data.get("furnishing", "Semi-Furnished"),
        float(data.get("price", pred_res["predicted_price"])),
        pred_res["predicted_price"],
        pred_res["barometer_score"],
        pred_res["barometer_verdict"],
        data.get("image_url") or "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&w=800&q=80",
        data.get("seller_name", "Anonymous Seller"),
        data.get("seller_phone", "+91 99999 00000"),
        now_str
    ))
    prop_id = cur.lastrowid
    conn.commit()
    conn.close()

    return {
        "id": prop_id,
        "prediction": pred_res
    }

import random
from datetime import timedelta

def generate_otp(phone):
    conn = get_connection()
    cur = conn.cursor()
    otp = str(random.randint(1000, 9999))
    expires = (datetime.now(timezone.utc) + timedelta(minutes=10)).isoformat()
    cur.execute("INSERT OR REPLACE INTO otp_codes (phone, otp, expires_at) VALUES (?, ?, ?)", (phone, otp, expires))
    conn.commit()
    conn.close()
    return otp

def verify_otp(phone, otp, name=None, role=None):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT otp, expires_at FROM otp_codes WHERE phone = ?", (phone,))
    row = cur.fetchone()
    
    if not row or row["otp"] != otp:
        conn.close()
        return False, "Invalid or missing OTP."
    
    if datetime.fromisoformat(row["expires_at"]) < datetime.now(timezone.utc):
        conn.close()
        return False, "OTP expired."
        
    cur.execute("DELETE FROM otp_codes WHERE phone = ?", (phone,))
    
    cur.execute("SELECT * FROM users WHERE phone = ?", (phone,))
    user = cur.fetchone()
    
    if not user:
        if not name or not role:
            conn.close()
            return False, "New user requires name and role."
        now_str = datetime.now(timezone.utc).isoformat()
        cur.execute("INSERT INTO users (name, phone, role, created_at) VALUES (?, ?, ?, ?)", (name, phone, role, now_str))
        cur.execute("SELECT * FROM users WHERE phone = ?", (phone,))
        user = cur.fetchone()
        
    conn.commit()
    conn.close()
    return True, dict(user)


def login_user(phone, name=None, role=None):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE phone = ?", (phone,))
    user = cur.fetchone()
    
    if not user:
        if not name or not role:
            conn.close()
            return False, "New user requires name and role."
        now_str = datetime.now(timezone.utc).isoformat()
        cur.execute("INSERT INTO users (name, phone, role, created_at) VALUES (?, ?, ?, ?)", (name, phone, role, now_str))
        cur.execute("SELECT * FROM users WHERE phone = ?", (phone,))
        user = cur.fetchone()
        
    conn.commit()
    conn.close()
    return True, dict(user)
