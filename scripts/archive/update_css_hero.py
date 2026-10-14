import re

with open('code/frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

hero_css = '''
/* ========================================================= */
/* ?? STUNNING REAL ESTATE HERO SECTION                      */
/* ========================================================= */

.marketplace-body {
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 1.5rem 3rem 1.5rem;
}

.real-estate-hero {
    position: relative;
    width: 100%;
    height: 75vh;
    min-height: 600px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: -1px; /* seamless with navbar */
}

.hero-bg-image {
    position: absolute;
    inset: 0;
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    z-index: 1;
}

.hero-gradient-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(to bottom, rgba(15, 42, 74, 0.4) 0%, rgba(10, 27, 49, 0.8) 100%);
    z-index: 2;
}

.hero-content-wrapper {
    position: relative;
    z-index: 3;
    width: 100%;
    max-width: 1000px;
    padding: 0 1.5rem;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.hero-badge {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    color: #ffffff;
    padding: 6px 16px;
    border-radius: 30px;
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 1.5rem;
}

.hero-title {
    font-size: 4.5rem !important;
    font-family: 'Playfair Display', serif !important;
    color: #ffffff !important;
    line-height: 1.1 !important;
    margin-bottom: 1rem;
    text-shadow: 0 4px 20px rgba(0,0,0,0.3);
}

.hero-subtitle {
    font-size: 1.2rem;
    color: rgba(255, 255, 255, 0.9) !important;
    max-width: 600px;
    margin: 0 auto 3rem auto;
    font-weight: 300;
    text-shadow: 0 2px 10px rgba(0,0,0,0.2);
}

/* Floating Search Bar (Zillow Style) */
.floating-search-bar {
    background: #ffffff;
    width: 100%;
    border-radius: 16px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    overflow: hidden;
    display: flex;
    flex-direction: column;
    padding: 0;
}

.search-inputs-row {
    display: flex;
    width: 100%;
    border-bottom: 1px solid #e2e8f0;
}

.search-input-group {
    flex: 1;
    padding: 1.2rem 1.5rem;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    text-align: left;
}
.search-input-group.flex-2 { flex: 2; }

.search-divider {
    width: 1px;
    background: #e2e8f0;
    margin: 1rem 0;
}

.search-input-group label {
    font-size: 0.75rem !important;
    color: #64748b !important;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 0.3rem;
}

.minimal-input {
    width: 100%;
    border: none !important;
    background: transparent !important;
    padding: 0 !important;
    font-size: 1.1rem !important;
    color: #0f172a !important;
    font-weight: 600 !important;
    box-shadow: none !important;
    border-radius: 0 !important;
}
.minimal-input:focus {
    outline: none !important;
    box-shadow: none !important;
}

.search-action-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 1.5rem;
    background: #f8fafc;
}

.barometer-select {
    width: auto !important;
    font-size: 0.95rem !important;
    color: #475569 !important;
    background: transparent !important;
    cursor: pointer;
}

.search-submit-btn {
    padding: 0.75rem 2.5rem !important;
    font-size: 1.05rem !important;
    border-radius: 8px !important;
    background: #0F2A4A !important; /* Navy */
}
.search-submit-btn:hover {
    background: #1D4370 !important;
    transform: none !important;
}

/* Mobile Hero Adjustments */
@media (max-width: 768px) {
    .hero-title { font-size: 2.8rem !important; }
    .search-inputs-row { flex-direction: column; border-bottom: none; }
    .search-divider { width: 100%; height: 1px; margin: 0; }
    .search-action-row { flex-direction: column; gap: 1rem; padding: 1.5rem; }
    .search-submit-btn { width: 100%; }
    .real-estate-hero { height: auto; min-height: 80vh; padding: 4rem 0; }
}
'''

css += "\n" + hero_css

# Also fix the navbar color so it's transparent on top of the hero! Wait, navbar is sticky and outside the tab. 
# I will make the navbar solid white for extreme cleanliness (like Airbnb/Zillow)
css = re.sub(r'\.navbar\s*\{[^}]+\}', '''
.navbar {
    background: #ffffff !important;
    border-bottom: 1px solid #e2e8f0 !important;
    padding: 0.8rem 1.5rem;
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: 0 4px 20px rgba(0,0,0,0.03);
}
.brand-title {
    color: #0F2A4A !important;
    font-family: 'Playfair Display', serif !important;
    font-size: 1.6rem;
    font-weight: 800;
}
.nav-btn {
    color: #475569 !important;
    border: none !important;
    border-radius: 6px !important;
    font-weight: 600;
    font-size: 0.9rem;
    transition: all 0.2s ease;
}
.nav-btn:hover { background: #f1f5f9 !important; color: #0F172A !important; }
.nav-btn.active {
    background: #F8FAFC !important;
    color: #0F2A4A !important;
    border: 1px solid #e2e8f0 !important;
    box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}
''', css)

with open('code/frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Hero CSS added and Navbar fixed.")
