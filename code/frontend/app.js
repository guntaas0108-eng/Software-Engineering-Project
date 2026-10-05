// EstatePulse Frontend Application Controller
const API_BASE = "";

let currentProperties = [];
let activePropertyForChat = null;
let chatPollingInterval = null;
let currentLivePrediction = null;
let debounceTimeout = null;

// Initialize on page load
document.addEventListener("DOMContentLoaded", () => {
    loadProperties();
    triggerLivePrediction();
    loadAnalytics();

    // Set minimum appointment date to tomorrow
    const tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    const dateInput = document.getElementById("modal-appt-date");
    if (dateInput) {
        dateInput.min = tomorrow.toISOString().split("T")[0];
        dateInput.value = tomorrow.toISOString().split("T")[0];
    }
});

// -------------------------------------------------------------
// Navigation & Tab Switching
// -------------------------------------------------------------
function switchTab(tabName) {
    document.querySelectorAll(".tab-pane").forEach(el => el.classList.remove("active"));
    document.querySelectorAll(".nav-btn").forEach(el => el.classList.remove("active"));

    const targetTab = document.getElementById(`tab-${tabName}`);
    const targetBtn = document.getElementById(`tab-btn-${tabName}`);

    if (targetTab) targetTab.classList.add("active");
    if (targetBtn) targetBtn.classList.add("active");

    if (tabName === "chat") {
        startChatPolling();
        if (currentProperties.length > 0 && !activePropertyForChat) {
            selectChatProperty(currentProperties[0].id);
        }
    } else {
        stopChatPolling();
    }

    if (tabName === "analytics") {
        loadAnalytics();
    }
}

// -------------------------------------------------------------
// Marketplace Listings & Buyer Barometer
// -------------------------------------------------------------
async function loadProperties() {
    try {
        const city = document.getElementById("filter-city").value;
        const ptype = document.getElementById("filter-type").value;
        const barometer = document.getElementById("filter-barometer").value;
        const search = document.getElementById("filter-search").value.trim();

        const params = new URLSearchParams();
        if (city !== "All") params.append("city", city);
        if (ptype !== "All") params.append("property_type", ptype);
        if (barometer !== "All") params.append("barometer", barometer);
        if (search) params.append("search", search);

        const res = await fetch(`${API_BASE}/api/properties?${params.toString()}`);
        const data = await res.json();

        if (data.success) {
            currentProperties = data.data;
            renderProperties(data.data);
            populateChatChannels(data.data);
            updateHeroStats(data.data);
        }
    } catch (err) {
        console.error("Error loading properties:", err);
        showToast("Error connecting to server. Is backend running?");
    }
}

function debounceFilter() {
    clearTimeout(debounceTimeout);
    debounceTimeout = setTimeout(() => {
        loadProperties();
    }, 300);
}

function resetFilters() {
    document.getElementById("filter-search").value = "";
    document.getElementById("filter-city").value = "All";
    document.getElementById("filter-type").value = "All";
    document.getElementById("filter-barometer").value = "All";
    loadProperties();
}

function formatINR(val) {
    if (!val) return "₹0";
    if (val >= 10000000) {
        return `₹ ${(val / 10000000).toFixed(2)} Cr`;
    }
    if (val >= 100000) {
        return `₹ ${(val / 100000).toFixed(2)} Lakh`;
    }
    return `₹ ${Number(val).toLocaleString("en-IN")}`;
}

function renderProperties(props) {
    const grid = document.getElementById("properties-grid");
    const countLbl = document.getElementById("listings-count-label");
    countLbl.textContent = `Available Listings (${props.length})`;

    if (props.length === 0) {
        grid.innerHTML = `
            <div style="grid-column: 1 / -1; text-align: center; padding: 3rem; background: #fff; border-radius: 12px;">
                <h3>No properties found matching criteria</h3>
                <p style="color: #64748b; margin-top: 0.5rem;">Try adjusting filters or clear your search terms.</p>
                <button class="btn btn-secondary" style="margin-top: 1rem;" onclick="resetFilters()">Reset Filters</button>
            </div>
        `;
        return;
    }

    grid.innerHTML = props.map(p => {
        const diffPct = p.predicted_price ? (((p.price - p.predicted_price) / p.predicted_price) * 100).toFixed(1) : 0;
        
        let barometerClass = "barometer-fair";
        let barometerIcon = "⚖️";
        let barometerText = p.barometer_verdict || "Fair Market Price";
        let barometerDiff = "";

        if (diffPct <= -10) {
            barometerClass = "barometer-good";
            barometerIcon = "🌟";
            barometerDiff = `${Math.abs(diffPct)}% Below Market Value`;
        } else if (diffPct >= 10) {
            barometerClass = "barometer-high";
            barometerIcon = "💎";
            barometerDiff = `+${diffPct}% Premium Over Model`;
        } else {
            barometerDiff = `Within standard market range`;
        }

        const thumb = p.image_url || "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&w=800&q=80";

        return `
            <article class="property-card">
                <div class="card-img-wrapper">
                    <img src="${thumb}" alt="${p.title}" loading="lazy" onerror="this.src='https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&w=800&q=80'">
                    <span class="card-type-tag">${p.property_type}</span>
                    <span class="card-city-tag">📍 ${p.city}</span>
                </div>
                <div class="card-content">
                    <h3 class="card-title" title="${p.title}">${p.title}</h3>
                    <div class="card-locality">📍 ${p.locality}, ${p.city}</div>

                    <div class="card-price-row">
                        <div>
                            <div class="price-main-val">${formatINR(p.price)}</div>
                            <span class="price-sub">₹ ${Math.round(p.price / p.area_sqft).toLocaleString("en-IN")}/sq.ft</span>
                        </div>
                        <div class="price-ml-val">
                            <span class="ml-tag">ML Fair Valuation</span>
                            <div class="ml-amount">${formatINR(p.predicted_price)}</div>
                        </div>
                    </div>

                    <!-- Buyer Barometer -->
                    <div class="card-barometer ${barometerClass}">
                        <div class="barometer-lbl">
                            <span>${barometerIcon}</span>
                            <span>${barometerText}</span>
                        </div>
                        <span class="barometer-score-tag">${barometerDiff}</span>
                    </div>

                    <div class="card-specs">
                        <span class="spec-pill">📐 ${p.area_sqft} sq.ft</span>
                        ${p.bedrooms > 0 ? `<span class="spec-pill">🛏️ ${p.bedrooms} BHK</span>` : ""}
                        <span class="spec-pill">🚿 ${p.bathrooms} Bath</span>
                        <span class="spec-pill">🛋️ ${p.furnishing}</span>
                        <span class="spec-pill">${p.has_parking ? "🚗 Parking" : "No Parking"}</span>
                    </div>

                    <div class="card-actions">
                        <button class="btn btn-outline btn-sm" onclick="viewPropertyDetail(${p.id})">🔍 Details</button>
                        <button class="btn btn-primary btn-sm" onclick="openChatForProperty(${p.id})">💬 Negotiate Chat</button>
                        <button class="btn btn-success btn-sm" onclick="promptScheduleVisit(${p.id})">📅 Visit</button>
                    </div>
                </div>
            </article>
        `;
    }).join("");
}

function updateHeroStats(props) {
    document.getElementById("hero-total-props").textContent = props.length;
}

// -------------------------------------------------------------
// Property Detail View
// -------------------------------------------------------------
async function viewPropertyDetail(propId) {
    try {
        const res = await fetch(`${API_BASE}/api/properties/${propId}`);
        const data = await res.json();
        if (!data.success) return;

        const p = data.data;
        const v = p.valuation || {};

        document.getElementById("det-title").textContent = p.title;

        document.getElementById("det-body").innerHTML = `
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 1.5rem;">
                <img src="${p.image_url}" style="width: 100%; height: 260px; object-fit: cover; border-radius: 8px;">
                <div>
                    <h4 style="margin-bottom: 0.5rem;">Overview</h4>
                    <p style="color: #475569; font-size: 0.9rem; margin-bottom: 1rem;">${p.description || "Well maintained property in prime location."}</p>
                    
                    <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; border: 1px solid #e2e8f0;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                            <strong>Asking Price:</strong>
                            <span style="font-size: 1.1rem; color: #2563eb; font-weight: 800;">${formatINR(p.price)}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                            <strong>ML Fair Valuation:</strong>
                            <span style="font-weight: 700;">${formatINR(p.predicted_price)}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                            <strong>Rate per Sq.Ft:</strong>
                            <span>₹ ${Math.round(p.price / p.area_sqft).toLocaleString("en-IN")}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <strong>Seller:</strong>
                            <span>${p.seller_name} (${p.seller_phone})</span>
                        </div>
                    </div>
                </div>
            </div>

            <div style="background: #f1f5f9; padding: 1rem; border-radius: 8px; margin-bottom: 1.5rem;">
                <h4 style="margin-bottom: 0.5rem;">Buyer Barometer Analysis</h4>
                <p style="font-size: 0.88rem; color: #334155;"><strong>Status:</strong> ${v.barometer_verdict || p.barometer_verdict} (${v.difference_percentage || 0}% variance)</p>
                <p style="font-size: 0.85rem; color: #64748b; margin-top: 4px;">${v.advice || "Fair market listing."}</p>
            </div>

            <div style="display: flex; gap: 0.75rem; justify-content: flex-end;">
                <button class="btn btn-secondary" onclick="closeModals()">Close</button>
                <button class="btn btn-primary" onclick="closeModals(); openChatForProperty(${p.id});">Open WhatsApp Chat</button>
                <button class="btn btn-success" onclick="closeModals(); promptScheduleVisit(${p.id});">Schedule Site Visit</button>
            </div>
        `;

        document.getElementById("property-detail-modal").classList.remove("hidden");
    } catch (err) {
        console.error(err);
    }
}

// -------------------------------------------------------------
// Seller Portal: Live ML Prediction & Duplicate Detection
// -------------------------------------------------------------
async function triggerLivePrediction() {
    const area = document.getElementById("prop-area").value;
    const ptype = document.getElementById("prop-type").value;
    const city = document.getElementById("prop-city").value;
    const beds = document.getElementById("prop-beds").value;
    const baths = document.getElementById("prop-baths").value;
    const age = document.getElementById("prop-age").value;
    const furnish = document.getElementById("prop-furnish").value;
    const parking = document.getElementById("prop-parking").value;

    if (!area || area <= 0) return;

    try {
        const payload = {
            area_sqft: parseFloat(area),
            property_type: ptype,
            city: city,
            bedrooms: parseInt(beds) || 2,
            bathrooms: parseInt(baths) || 2,
            property_age: parseInt(age) || 0,
            furnishing: furnish,
            has_parking: parking === "1" ? 1 : 0
        };

        const res = await fetch(`${API_BASE}/api/predict`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
        const data = await res.json();

        if (data.success) {
            currentLivePrediction = data.data;
            const predPrice = data.data.predicted_price;
            document.getElementById("live-predicted-val").textContent = formatINR(predPrice);
            document.getElementById("live-psf").textContent = `Rate: ₹ ${Math.round(predPrice / area).toLocaleString("en-IN")} / sq.ft`;
            
            // Auto fill price suggestion if empty
            const priceInput = document.getElementById("prop-price");
            if (!priceInput.value) {
                priceInput.placeholder = `Suggested: ${Math.round(predPrice)}`;
            }

            evaluateSellerBarometer();
        }
    } catch (err) {
        console.error("Live prediction error:", err);
    }
}

function evaluateSellerBarometer() {
    const askingPrice = parseFloat(document.getElementById("prop-price").value);
    if (!currentLivePrediction || !askingPrice) return;

    const predPrice = currentLivePrediction.predicted_price;
    const diffPct = (((askingPrice - predPrice) / predPrice) * 100).toFixed(1);

    const badge = document.getElementById("live-barometer-badge");
    const bar = document.getElementById("live-barometer-bar");
    const text = document.getElementById("live-barometer-text");

    let fillWidth = Math.max(10, Math.min(95, 50 - (diffPct * 1.5)));
    bar.style.width = `${fillWidth}%`;

    if (diffPct <= -10) {
        badge.textContent = `🌟 Great Deal for Buyers (${Math.abs(diffPct)}% Under Market)`;
        badge.style.color = "#047857";
        text.textContent = "Your listing is priced attractively. You will likely receive fast buyer visits and inquiries!";
    } else if (diffPct <= 10) {
        badge.textContent = `⚖️ Fair Market Price (${diffPct >= 0 ? "+" : ""}${diffPct}% Aligned)`;
        badge.style.color = "#1d4ed8";
        text.textContent = "Your asking price matches our Multiple Linear Regression market baseline.";
    } else {
        badge.textContent = `💎 Premium Price (+${diffPct}% Over Market Model)`;
        badge.style.color = "#b45309";
        text.textContent = "Buyers may negotiate strongly or request justifications for this premium pricing.";
    }
}

async function checkDuplicates() {
    const title = document.getElementById("prop-title").value.trim();
    const ptype = document.getElementById("prop-type").value;
    const city = document.getElementById("prop-city").value;
    const locality = document.getElementById("prop-locality").value.trim();

    if (!title || !locality) return;

    try {
        const res = await fetch(`${API_BASE}/api/check-duplicates`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ title, property_type: ptype, city, locality })
        });
        const data = await res.json();

        const warnBox = document.getElementById("duplicate-warning-box");
        const warnText = document.getElementById("dup-details-text");

        if (data.success && data.duplicates.length > 0) {
            const matches = data.duplicates.map(d => `"${d.title}" in ${d.locality}`).join(", ");
            warnText.textContent = `Similar existing listings found: ${matches}. Please verify you are not submitting a duplicate.`;
            warnBox.classList.remove("hidden");
        } else {
            warnBox.classList.add("hidden");
        }
    } catch (err) {
        console.error("Duplicate check error:", err);
    }
}

async function handlePropertySubmit(e) {
    e.preventDefault();

    const title = document.getElementById("prop-title").value.trim();
    const desc = document.getElementById("prop-desc").value.trim();
    const ptype = document.getElementById("prop-type").value;
    const city = document.getElementById("prop-city").value;
    const locality = document.getElementById("prop-locality").value.trim();
    const area = parseFloat(document.getElementById("prop-area").value);
    const beds = parseInt(document.getElementById("prop-beds").value) || 0;
    const baths = parseInt(document.getElementById("prop-baths").value) || 1;
    const age = parseInt(document.getElementById("prop-age").value) || 0;
    const furnish = document.getElementById("prop-furnish").value;
    const parking = document.getElementById("prop-parking").value === "1" ? 1 : 0;
    const price = parseFloat(document.getElementById("prop-price").value);
    const seller = document.getElementById("prop-seller").value.trim();
    const phone = document.getElementById("prop-phone").value.trim();
    const img = document.getElementById("prop-image").value.trim();

    const payload = {
        title, description: desc, property_type: ptype, city, locality,
        area_sqft: area, bedrooms: beds, bathrooms: baths, property_age: age,
        furnishing: furnish, has_parking: parking, price: price,
        seller_name: seller, seller_phone: phone, image_url: img
    };

    try {
        const res = await fetch(`${API_BASE}/api/properties`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
        const data = await res.json();

        if (data.success) {
            showToast("🎉 Property listed successfully with instant ML valuation!");
            document.getElementById("new-property-form").reset();
            document.getElementById("duplicate-warning-box").classList.add("hidden");
            await loadProperties();
            switchTab("marketplace");
        } else {
            showToast("Failed to list property: " + data.error);
        }
    } catch (err) {
        console.error("Error creating property:", err);
        showToast("Network error submitting property.");
    }
}

// -------------------------------------------------------------
// WhatsApp-like Integrated Communication
// -------------------------------------------------------------
function populateChatChannels(props) {
    const list = document.getElementById("chat-channels-list");
    if (!list) return;

    list.innerHTML = props.map(p => {
        const thumb = p.image_url || "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&w=800&q=80";
        const isActive = activePropertyForChat && activePropertyForChat.id === p.id ? "active" : "";
        return `
            <div class="chat-channel-item ${isActive}" onclick="selectChatProperty(${p.id})">
                <img src="${thumb}" class="channel-thumb" alt="prop">
                <div class="channel-info">
                    <div class="channel-title">${p.title}</div>
                    <div class="channel-sub">${p.locality}, ${p.city} • ${formatINR(p.price)}</div>
                </div>
            </div>
        `;
    }).join("");
}

function openChatForProperty(propId) {
    switchTab("chat");
    selectChatProperty(propId);
}

function selectChatProperty(propId) {
    const prop = currentProperties.find(p => p.id === propId);
    if (!prop) return;

    activePropertyForChat = prop;
    populateChatChannels(currentProperties);

    // Update active nav
    document.getElementById("chat-prop-img").src = prop.image_url || "";
    document.getElementById("chat-prop-title").textContent = prop.title;
    document.getElementById("chat-prop-seller").textContent = `Seller: ${prop.seller_name} (${prop.seller_phone}) • Price: ${formatINR(prop.price)}`;

    fetchMessages(propId);
}

async function fetchMessages(propId) {
    if (!propId) return;
    try {
        const res = await fetch(`${API_BASE}/api/properties/${propId}/messages`);
        const data = await res.json();
        if (data.success) {
            renderChatMessages(data.data);
        }
    } catch (err) {
        console.error("Error fetching messages:", err);
    }
}

function renderChatMessages(msgs) {
    const container = document.getElementById("chat-messages-container");
    if (msgs.length === 0) {
        container.innerHTML = `<div class="chat-empty"><p>No messages yet. Send a query below to start negotiation!</p></div>`;
        return;
    }

    container.innerHTML = msgs.map(m => {
        const timeStr = m.timestamp ? new Date(m.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) : "";
        return `
            <div class="message-bubble ${m.sender_type}">
                <div class="msg-sender">${m.sender_name}</div>
                <div class="msg-text">${escapeHtml(m.message_text)}</div>
                <div class="msg-time">${timeStr}</div>
            </div>
        `;
    }).join("");

    container.scrollTop = container.scrollHeight;
}

async function handleSendMessage(e) {
    e.preventDefault();
    if (!activePropertyForChat) {
        showToast("Please select a property discussion first");
        return;
    }

    const input = document.getElementById("chat-input-text");
    const text = input.value.trim();
    if (!text) return;

    const role = document.getElementById("chat-sender-role").value;
    const senderName = role === "buyer" ? "Guntaas Singh (Buyer)" : activePropertyForChat.seller_name;

    try {
        const res = await fetch(`${API_BASE}/api/properties/${activePropertyForChat.id}/messages`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                sender_type: role,
                sender_name: senderName,
                message_text: text
            })
        });
        const data = await res.json();
        if (data.success) {
            input.value = "";
            fetchMessages(activePropertyForChat.id);
        }
    } catch (err) {
        console.error("Error sending message:", err);
    }
}

function startChatPolling() {
    stopChatPolling();
    chatPollingInterval = setInterval(() => {
        if (activePropertyForChat) {
            fetchMessages(activePropertyForChat.id);
        }
    }, 3000);
}

function stopChatPolling() {
    if (chatPollingInterval) {
        clearInterval(chatPollingInterval);
        chatPollingInterval = null;
    }
}

// -------------------------------------------------------------
// Site Visit Appointments & Metric Measurement
// -------------------------------------------------------------
function promptScheduleVisit(propId) {
    const prop = currentProperties.find(p => p.id === propId);
    if (!prop) return;
    activePropertyForChat = prop;
    openAppointmentModal();
}

function openAppointmentModal() {
    if (!activePropertyForChat) {
        showToast("Please choose a property first");
        return;
    }
    document.getElementById("modal-appt-prop-title").value = activePropertyForChat.title;
    document.getElementById("modal-appt-prop-id").value = activePropertyForChat.id;
    document.getElementById("appointment-modal").classList.remove("hidden");
}

async function handleAppointmentSubmit(e) {
    e.preventDefault();
    const propId = document.getElementById("modal-appt-prop-id").value;
    const name = document.getElementById("modal-appt-name").value;
    const phone = document.getElementById("modal-appt-phone").value;
    const date = document.getElementById("modal-appt-date").value;
    const time = document.getElementById("modal-appt-time").value;
    const notes = document.getElementById("modal-appt-notes").value;

    try {
        const res = await fetch(`${API_BASE}/api/appointments`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                property_id: parseInt(propId),
                buyer_name: name,
                buyer_phone: phone,
                visit_date: date,
                visit_time: time,
                notes: notes
            })
        });
        const data = await res.json();

        if (data.success) {
            closeModals();
            showToast("📅 Site visit requested! Notification sent in chat.");
            openChatForProperty(parseInt(propId));
            loadAnalytics();
        }
    } catch (err) {
        console.error("Error scheduling appointment:", err);
    }
}

async function confirmAppointment(apptId) {
    try {
        const res = await fetch(`${API_BASE}/api/appointments/${apptId}/confirm`, {
            method: "POST"
        });
        const data = await res.json();
        if (data.success) {
            showToast(`✅ Visit confirmed! Measured Time-to-Appointment: ${data.time_to_appointment_human}`);
            loadAnalytics();
            if (activePropertyForChat) fetchMessages(activePropertyForChat.id);
        }
    } catch (err) {
        console.error("Error confirming visit:", err);
    }
}

// -------------------------------------------------------------
// Payment Integration (Booking Token)
// -------------------------------------------------------------
function openPaymentModal() {
    if (!activePropertyForChat) {
        showToast("Please select a property first");
        return;
    }
    document.getElementById("modal-pay-prop-title").value = activePropertyForChat.title;
    document.getElementById("modal-pay-prop-id").value = activePropertyForChat.id;
    document.getElementById("payment-modal").classList.remove("hidden");
}

async function handlePaymentSubmit(e) {
    e.preventDefault();
    const propId = document.getElementById("modal-pay-prop-id").value;
    const buyerName = document.getElementById("modal-pay-buyer-name").value;
    const method = document.getElementById("modal-pay-method").value;

    try {
        const res = await fetch(`${API_BASE}/api/payments`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                property_id: parseInt(propId),
                buyer_name: buyerName,
                amount: 500.0,
                payment_method: method
            })
        });
        const data = await res.json();
        if (data.success) {
            closeModals();
            showToast(`💳 Payment Successful! Txn ID: ${data.transaction_id}`);
            if (activePropertyForChat) fetchMessages(activePropertyForChat.id);
            loadAnalytics();
        }
    } catch (err) {
        console.error("Payment error:", err);
    }
}

// -------------------------------------------------------------
// Evaluation & System Analytics
// -------------------------------------------------------------
async function loadAnalytics() {
    try {
        const res = await fetch(`${API_BASE}/api/metrics`);
        const data = await res.json();
        if (!data.success) return;

        // Primary Metric
        const apptMetrics = data.appointments;
        document.getElementById("metric-median-time").textContent = apptMetrics.median_time_to_appointment_human || "0.0 min";
        document.getElementById("hero-median-time").textContent = apptMetrics.median_time_to_appointment_human || "< 2 hrs";

        // ML Metrics
        const ml = data.ml_model;
        document.getElementById("metric-r2").textContent = ml.r2_score;
        document.getElementById("hero-model-r2").textContent = ml.r2_score;
        document.getElementById("metric-rmse").textContent = `RMSE: ₹ ${Math.round(ml.rmse).toLocaleString("en-IN")}`;

        document.getElementById("diag-mse").textContent = ml.mse.toLocaleString("en-IN");
        document.getElementById("diag-rmse").textContent = `₹ ${Math.round(ml.rmse).toLocaleString("en-IN")}`;
        document.getElementById("diag-mae").textContent = `₹ ${Math.round(ml.mae).toLocaleString("en-IN")}`;
        document.getElementById("diag-r2").textContent = ml.r2_score;
        document.getElementById("diag-intercept").textContent = `₹ ${Math.round(ml.intercept).toLocaleString("en-IN")}`;
        document.getElementById("diag-samples").textContent = `${ml.training_samples} historical entries`;

        // Communication
        const mp = data.marketplace;
        document.getElementById("metric-engagement").textContent = `${mp.engagement_rate_percent}%`;
        document.getElementById("metric-total-msgs").textContent = `${mp.total_messages} Messages Exchanged`;

        // Payments
        const pay = data.payments;
        document.getElementById("metric-payments").textContent = pay.total_transactions;
        document.getElementById("metric-revenue").textContent = `Total: ₹ ${pay.total_amount_collected.toLocaleString("en-IN")}`;

        // Barometer Distribution
        const dist = mp.barometer_distribution;
        const goodCount = dist["Great Deal"] || 0;
        const fairCount = dist["Fair Market Price"] || 0;
        const highCount = dist["Premium / High"] || 0;
        const totalDist = (goodCount + fairCount + highCount) || 1;

        document.getElementById("chart-val-good").textContent = `${goodCount} (${Math.round(goodCount/totalDist*100)}%)`;
        document.getElementById("chart-val-fair").textContent = `${fairCount} (${Math.round(fairCount/totalDist*100)}%)`;
        document.getElementById("chart-val-high").textContent = `${highCount} (${Math.round(highCount/totalDist*100)}%)`;

        document.getElementById("chart-bar-good").style.width = `${Math.round(goodCount/totalDist*100)}%`;
        document.getElementById("chart-bar-fair").style.width = `${Math.round(fairCount/totalDist*100)}%`;
        document.getElementById("chart-bar-high").style.width = `${Math.round(highCount/totalDist*100)}%`;

        // Load appointments table
        loadAppointmentsTable();
    } catch (err) {
        console.error("Analytics fetch error:", err);
    }
}

async function loadAppointmentsTable() {
    try {
        const res = await fetch(`${API_BASE}/api/appointments`);
        const data = await res.json();
        if (!data.success) return;

        const tbody = document.getElementById("appointments-tbody");
        if (data.data.length === 0) {
            tbody.innerHTML = `<tr><td colspan="7" style="text-align: center; color: #94a3b8;">No site visits scheduled yet. Use the marketplace or chat to schedule one.</td></tr>`;
            return;
        }

        tbody.innerHTML = data.data.map(a => {
            const isConfirmed = a.status === "confirmed";
            const timeDur = a.time_to_appointment_seconds !== null ? `${Math.round(a.time_to_appointment_seconds / 60)} min` : "Pending seller confirmation";
            const statusBadge = isConfirmed ? 
                `<span style="background: #d1fae5; color: #047857; padding: 3px 8px; border-radius: 4px; font-weight: 700;">Confirmed</span>` :
                `<span style="background: #fef3c7; color: #b45309; padding: 3px 8px; border-radius: 4px; font-weight: 700;">Pending</span>`;

            return `
                <tr>
                    <td>#${a.id}</td>
                    <td><strong>${a.property_title}</strong></td>
                    <td>${a.buyer_name} (${a.buyer_phone})</td>
                    <td>${a.visit_date} at ${a.visit_time}</td>
                    <td>${statusBadge}</td>
                    <td><code>${timeDur}</code></td>
                    <td>
                        ${!isConfirmed ? 
                            `<button class="btn btn-sm btn-success" onclick="confirmAppointment(${a.id})">Confirm Visit</button>` : 
                            `<span style="color: #10b981; font-weight: 700;">✓ Confirmed</span>`
                        }
                    </td>
                </tr>
            `;
        }).join("");
    } catch (err) {
        console.error("Appointments table load error:", err);
    }
}

// -------------------------------------------------------------
// Utilities & Modals
// -------------------------------------------------------------
function closeModals() {
    document.querySelectorAll(".modal-overlay").forEach(el => el.classList.add("hidden"));
}

function showToast(msg) {
    const toast = document.getElementById("toast");
    toast.textContent = msg;
    toast.classList.remove("hidden");
    setTimeout(() => {
        toast.classList.add("hidden");
    }, 3500);
}

function escapeHtml(str) {
    if (!str) return "";
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}
