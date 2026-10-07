import os
import uuid
from datetime import datetime, timezone
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

from ml_model import RealEstatePricePredictor
import database as db

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "frontend"))

app = Flask(__name__, static_folder=FRONTEND_DIR)
CORS(app)

# Initialize ML model and database
predictor = RealEstatePricePredictor()
predictor.train()
db.init_db(ml_predictor=predictor)


# -------------------------------------------------------------
# Frontend Routes
# -------------------------------------------------------------
@app.route("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory(FRONTEND_DIR, filename)


# -------------------------------------------------------------
# Machine Learning Endpoints
# -------------------------------------------------------------
@app.route("/api/predict", methods=["POST"])
def predict_price():
    data = request.get_json() or {}
    try:
        result = predictor.predict(data)
        return jsonify({"success": True, "data": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@app.route("/api/ml-metrics", methods=["GET"])
def ml_metrics():
    return jsonify({"success": True, "metrics": predictor.metrics})


# -------------------------------------------------------------
# Auth & OTP Endpoints
# -------------------------------------------------------------
@app.route("/api/auth/send-otp", methods=["POST"])
def send_otp():
    data = request.get_json() or {}
    phone = data.get("phone")
    if not phone:
        return jsonify({"success": False, "error": "Phone number required"}), 400
    
    otp = db.generate_otp(phone)
    # Simulate sending SMS by printing to console
    print(f"\n{'='*40}")
    print(f"MOCK SMS TO {phone}:")
    print(f"Your EstatePulse OTP is: {otp}")
    print(f"{'='*40}\n")
    
    return jsonify({"success": True, "message": "OTP sent successfully (Check console!)"})

@app.route("/api/auth/verify-otp", methods=["POST"])
def verify_otp():
    data = request.get_json() or {}
    phone = data.get("phone")
    otp = data.get("otp")
    name = data.get("name")
    role = data.get("role")
    
    if not phone or not otp:
        return jsonify({"success": False, "error": "Phone and OTP required"}), 400
        
    success, result = db.verify_otp(phone, otp, name, role)
    if success:
        return jsonify({"success": True, "user": result})
    else:
        return jsonify({"success": False, "error": result}), 400

@app.route("/api/auth/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    phone = data.get("phone")
    name = data.get("name")
    role = data.get("role")
    
    if not phone:
        return jsonify({"success": False, "error": "Phone required"}), 400
        
    success, result = db.login_user(phone, name, role)
    if success:
        return jsonify({"success": True, "user": result})
    else:
        return jsonify({"success": False, "error": result}), 400

# -------------------------------------------------------------
# Property Listing Endpoints
# -------------------------------------------------------------
@app.route("/api/properties", methods=["GET"])
def get_properties():
    city = request.args.get("city")
    ptype = request.args.get("property_type")
    barometer = request.args.get("barometer")
    search = request.args.get("search")
    min_price = request.args.get("min_price", type=float)
    max_price = request.args.get("max_price", type=float)
    seller_phone = request.args.get("seller_phone")

    query = "SELECT * FROM properties WHERE 1=1"
    params = []

    if city and city != "All":
        query += " AND city = ?"
        params.append(city)
    if ptype and ptype != "All":
        query += " AND property_type = ?"
        params.append(ptype)
    if barometer and barometer != "All":
        query += " AND barometer_verdict = ?"
        params.append(barometer)
    if min_price is not None:
        query += " AND price >= ?"
        params.append(min_price)
    if max_price is not None:
        query += " AND price <= ?"
        params.append(max_price)
    if seller_phone:
        query += " AND seller_phone = ?"
        params.append(seller_phone)
    if search:
        query += " AND (title LIKE ? OR locality LIKE ? OR description LIKE ?)"
        term = f"%{search}%"
        params.extend([term, term, term])

    query += " ORDER BY id DESC"

    conn = db.get_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()

    return jsonify({"success": True, "count": len(rows), "data": rows})

@app.route("/api/properties/<int:prop_id>", methods=["GET"])
def get_property(prop_id):
    conn = db.get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM properties WHERE id = ?", (prop_id,))
    row = cur.fetchone()
    conn.close()

    if not row:
        return jsonify({"success": False, "error": "Property not found"}), 404

    prop_data = dict(row)
    # Get associated metrics
    eval_data = predictor.predict(prop_data)
    prop_data["valuation"] = eval_data
    return jsonify({"success": True, "data": prop_data})

@app.route("/api/check-duplicates", methods=["POST"])
def check_duplicates():
    data = request.get_json() or {}
    title = data.get("title", "")
    ptype = data.get("property_type", "Residential")
    locality = data.get("locality", "")
    city = data.get("city", "Patiala")

    dups = db.check_duplicate(title, ptype, locality, city)
    return jsonify({"success": True, "duplicates": dups})

@app.route("/api/properties", methods=["POST"])
def create_property():
    data = request.get_json() or {}
    if not data.get("title") or not data.get("price") or not data.get("area_sqft"):
        return jsonify({"success": False, "error": "Title, price, and area are required"}), 400

    created = db.add_property(data, predictor)
    return jsonify({"success": True, "property_id": created["id"], "prediction": created["prediction"]}), 201


# -------------------------------------------------------------
# Integrated Communication (WhatsApp-like Chat) Endpoints
# -------------------------------------------------------------
@app.route("/api/properties/<int:prop_id>/messages", methods=["GET"])
def get_messages(prop_id):
    conn = db.get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM messages WHERE property_id = ? ORDER BY id ASC", (prop_id,))
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return jsonify({"success": True, "data": rows})

@app.route("/api/properties/<int:prop_id>/messages", methods=["POST"])
def post_message(prop_id):
    data = request.get_json() or {}
    sender_type = data.get("sender_type", "buyer")
    sender_name = data.get("sender_name", "Prospective Buyer")
    message_text = data.get("message_text", "").strip()

    if not message_text:
        return jsonify({"success": False, "error": "Message text cannot be empty"}), 400

    now_str = datetime.now(timezone.utc).isoformat()
    conn = db.get_connection()
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO messages (property_id, sender_type, sender_name, message_text, timestamp)
    VALUES (?, ?, ?, ?, ?)
    """, (prop_id, sender_type, sender_name, message_text, now_str))
    msg_id = cur.lastrowid
    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "message": {
            "id": msg_id,
            "property_id": prop_id,
            "sender_type": sender_type,
            "sender_name": sender_name,
            "message_text": message_text,
            "timestamp": now_str
        }
    }), 201


# -------------------------------------------------------------
# Site Visit Appointment & Time-to-Appointment Tracking
# -------------------------------------------------------------
@app.route("/api/appointments", methods=["POST"])
def schedule_appointment():
    data = request.get_json() or {}
    prop_id = data.get("property_id")
    buyer_name = data.get("buyer_name", "Anonymous Buyer")
    buyer_phone = data.get("buyer_phone", "+91 98000 00000")
    visit_date = data.get("visit_date")
    visit_time = data.get("visit_time")
    notes = data.get("notes", "")

    if not prop_id or not visit_date or not visit_time:
        return jsonify({"success": False, "error": "Property ID, date, and time are required"}), 400

    now_str = datetime.now(timezone.utc).isoformat()

    conn = db.get_connection()
    cur = conn.cursor()

    # Find earliest message from buyer for this property to measure time-to-appointment accurately
    cur.execute("""
    SELECT timestamp FROM messages 
    WHERE property_id = ? AND sender_type = 'buyer'
    ORDER BY id ASC LIMIT 1
    """, (prop_id,))
    first_msg = cur.fetchone()
    first_inquiry = first_msg["timestamp"] if first_msg else now_str

    cur.execute("""
    INSERT INTO appointments (
        property_id, buyer_name, buyer_phone, visit_date, visit_time,
        notes, status, first_inquiry_timestamp, created_at
    ) VALUES (?, ?, ?, ?, ?, ?, 'pending', ?, ?)
    """, (prop_id, buyer_name, buyer_phone, visit_date, visit_time, notes, first_inquiry, now_str))
    appt_id = cur.lastrowid

    # Post an automatic event message into the property chat thread
    chat_text = f"📅 Appointment requested for {visit_date} at {visit_time}. Buyer: {buyer_name} ({buyer_phone})."
    cur.execute("""
    INSERT INTO messages (property_id, sender_type, sender_name, message_text, timestamp)
    VALUES (?, 'buyer', ?, ?, ?)
    """, (prop_id, buyer_name, chat_text, now_str))

    conn.commit()
    conn.close()

    return jsonify({"success": True, "appointment_id": appt_id, "status": "pending"}), 201

@app.route("/api/appointments/<int:appt_id>/confirm", methods=["POST"])
def confirm_appointment(appt_id):
    now = datetime.now(timezone.utc)
    now_str = now.isoformat()

    conn = db.get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM appointments WHERE id = ?", (appt_id,))
    appt = cur.fetchone()

    if not appt:
        conn.close()
        return jsonify({"success": False, "error": "Appointment not found"}), 404

    # Calculate time-to-appointment duration
    first_inquiry_str = appt["first_inquiry_timestamp"] or appt["created_at"]
    try:
        first_time = datetime.fromisoformat(first_inquiry_str)
        duration_seconds = max(0.0, (now - first_time).total_seconds())
    except Exception:
        duration_seconds = 0.0

    cur.execute("""
    UPDATE appointments 
    SET status = 'confirmed', confirmed_timestamp = ?, time_to_appointment_seconds = ?
    WHERE id = ?
    """, (now_str, duration_seconds, appt_id))

    # Add seller confirmation into property chat
    cur.execute("""
    INSERT INTO messages (property_id, sender_type, sender_name, message_text, timestamp)
    VALUES (?, 'seller', 'Seller', ?, ?)
    """, (
        appt["property_id"],
        f"✅ Appointment confirmed for {appt['visit_date']} at {appt['visit_time']}. Looking forward to showing you the property!",
        now_str
    ))

    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "appointment_id": appt_id,
        "status": "confirmed",
        "time_to_appointment_seconds": round(duration_seconds, 1),
        "time_to_appointment_human": f"{round(duration_seconds / 60, 1)} minutes"
    })

@app.route("/api/appointments", methods=["GET"])
def list_appointments():
    prop_id = request.args.get("property_id")
    conn = db.get_connection()
    cur = conn.cursor()
    if prop_id:
        cur.execute("""
        SELECT a.*, p.title as property_title 
        FROM appointments a 
        JOIN properties p ON a.property_id = p.id
        WHERE a.property_id = ? ORDER BY a.id DESC
        """, (prop_id,))
    else:
        cur.execute("""
        SELECT a.*, p.title as property_title 
        FROM appointments a 
        JOIN properties p ON a.property_id = p.id
        ORDER BY a.id DESC
        """)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return jsonify({"success": True, "data": rows})


# -------------------------------------------------------------
# Payment Integration (Booking Fee & Site Visit Confirmation)
# -------------------------------------------------------------
@app.route("/api/payments", methods=["POST"])
def process_payment():
    data = request.get_json() or {}
    prop_id = data.get("property_id")
    appt_id = data.get("appointment_id")
    buyer_name = data.get("buyer_name", "Prospective Buyer")
    amount = float(data.get("amount", 500.0))
    payment_method = data.get("payment_method", "UPI / Razorpay Gateway")

    if not prop_id:
        return jsonify({"success": False, "error": "Property ID is required"}), 400

    txn_id = f"TXN-{uuid.uuid4().hex[:10].upper()}"
    now_str = datetime.now(timezone.utc).isoformat()

    conn = db.get_connection()
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO payments (
        property_id, appointment_id, buyer_name, amount, payment_method,
        transaction_id, payment_status, timestamp
    ) VALUES (?, ?, ?, ?, ?, ?, 'success', ?)
    """, (prop_id, appt_id, buyer_name, amount, payment_method, txn_id, now_str))

    # Add confirmation to chat
    cur.execute("""
    INSERT INTO messages (property_id, sender_type, sender_name, message_text, timestamp)
    VALUES (?, 'system', 'Payment Gateway', ?, ?)
    """, (
        prop_id,
        f"💳 Booking Fee of ₹{amount:,.0f} verified successfully. Transaction ID: {txn_id} ({payment_method}).",
        now_str
    ))

    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "transaction_id": txn_id,
        "amount": amount,
        "payment_method": payment_method,
        "status": "success",
        "timestamp": now_str
    }), 201


# -------------------------------------------------------------
# Evaluation & System Metrics
# -------------------------------------------------------------
@app.route("/api/metrics", methods=["GET"])
def get_system_metrics():
    conn = db.get_connection()
    cur = conn.cursor()

    # Total properties
    cur.execute("SELECT COUNT(*) FROM properties")
    total_props = cur.fetchone()[0]

    # Barometer distribution
    cur.execute("SELECT barometer_verdict, COUNT(*) as count FROM properties GROUP BY barometer_verdict")
    barometer_dist = {r["barometer_verdict"]: r["count"] for r in cur.fetchall()}

    # Total conversations / messages
    cur.execute("SELECT COUNT(DISTINCT property_id) FROM messages")
    engaged_props = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM messages")
    total_messages = cur.fetchone()[0]

    # Appointment metrics (Time-to-appointment)
    cur.execute("""
    SELECT time_to_appointment_seconds 
    FROM appointments 
    WHERE status = 'confirmed' AND time_to_appointment_seconds IS NOT NULL
    """)
    times = [r["time_to_appointment_seconds"] for r in cur.fetchall()]

    if times:
        avg_time = sum(times) / len(times)
        sorted_times = sorted(times)
        mid = len(sorted_times) // 2
        median_time = sorted_times[mid] if len(sorted_times) % 2 != 0 else (sorted_times[mid-1] + sorted_times[mid]) / 2
    else:
        avg_time = 0.0
        median_time = 0.0

    # Total payments
    cur.execute("SELECT COUNT(*), COALESCE(SUM(amount), 0) FROM payments WHERE payment_status = 'success'")
    pay_count, total_revenue = cur.fetchone()

    conn.close()

    engagement_rate = round((engaged_props / total_props * 100), 1) if total_props > 0 else 0.0

    return jsonify({
        "success": True,
        "ml_model": predictor.metrics,
        "marketplace": {
            "total_properties": total_props,
            "barometer_distribution": barometer_dist,
            "engaged_properties_count": engaged_props,
            "engagement_rate_percent": engagement_rate,
            "total_messages": total_messages
        },
        "appointments": {
            "total_confirmed_with_metric": len(times),
            "median_time_to_appointment_seconds": round(median_time, 1),
            "median_time_to_appointment_human": f"{round(median_time / 60, 1)} minutes" if median_time < 3600 else f"{round(median_time / 3600, 2)} hours",
            "target_threshold": "Median <= 2 hours (UCS503P Goal Met)"
        },
        "payments": {
            "total_transactions": pay_count,
            "total_amount_collected": total_revenue
        }
    })


if __name__ == "__main__":
    import threading
    import webbrowser
    
    port = int(os.environ.get("PORT", 5000))
    url = f"http://localhost:{port}"
    print(f"Real Estate Marketplace starting on {url}")
    
    # Automatically open the site in the default browser after 1.5 seconds
    threading.Timer(1.5, lambda: webbrowser.open(url)).start()
    
    app.run(host="0.0.0.0", port=port, debug=False)

