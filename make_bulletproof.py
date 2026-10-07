import re

with open('code/frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Make loadProperties bulletproof against any missing HTML elements
bulletproof_loadProperties = '''
async function loadProperties() {
    try {
        const cityEl = document.getElementById("city-filter");
        const ptypeEl = document.getElementById("category-filter");
        const barometerEl = document.getElementById("barometer-filter");
        const searchEl = document.getElementById("search-input");

        const city = cityEl ? cityEl.value : "All";
        const ptype = ptypeEl ? ptypeEl.value : "All";
        const barometer = barometerEl ? barometerEl.value : "All";
        const search = searchEl ? searchEl.value.trim() : "";

        const params = new URLSearchParams();
        if (city !== "All") params.append("city", city);
        if (ptype !== "All") params.append("property_type", ptype);
        if (barometer !== "All") params.append("barometer", barometer);
        if (search) params.append("search", search);

        const res = await fetch(API_BASE + '/api/properties?' + params.toString());
        const data = await res.json();

        if (data.success) {
            currentProperties = data.data;
            renderProperties(data.data);
            populateChatChannels(data.data);
        }
    } catch (err) {
        console.error("Error loading properties:", err);
        showToast("Error loading properties: " + err.message);
    }
}
'''
js = re.sub(r'async function loadProperties\(\)\s*\{.*?catch\s*\(err\)\s*\{\s*console\.error\("Error loading properties:",\s*err\);\s*showToast\("Error connecting to server\. Is backend running\?"\);\s*\}\s*\}', bulletproof_loadProperties.strip(), js, flags=re.DOTALL)

with open('code/frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)
