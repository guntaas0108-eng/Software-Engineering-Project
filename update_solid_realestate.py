import re

with open('code/frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. New Solid Real Estate Root Variables
new_root = '''
:root {
    --primary: #0F2A4A; /* Architectural Navy */
    --primary-light: #1D4370;
    --primary-dark: #0A1B31;
    --accent: #B47A46; /* Terracotta / Brick / Copper */
    --accent-dark: #9A6538;
    --warning: #F59E0B;
    --danger: #DC2626;
    --bg-main: #F8FAFC; /* Gallery Off-White */
    --card-bg: #FFFFFF; /* Solid White */
    --border: #E2E8F0;
    --text-primary: #1E293B;
    --text-secondary: #475569;
    --text-muted: #94A3B8;
    --radius-sm: 4px; /* Sharper, structural edges */
    --radius-md: 8px;
    --radius-lg: 12px;
    --shadow-sm: 0 2px 4px rgba(15, 42, 74, 0.05);
    --shadow-md: 0 10px 30px rgba(15, 42, 74, 0.08);
    --shadow-lg: 0 20px 40px rgba(15, 42, 74, 0.12);
}
'''
css = re.sub(r':root\s*\{[^}]+\}', new_root.strip(), css, count=1)

# 2. Fix the Body and animated gradient
body_pattern = r'body\s*\{[^}]+\}'
body_replacement = '''
body {
    font-family: 'Outfit', sans-serif;
    background-color: var(--bg-main);
    background-image: none;
    animation: none;
    color: var(--text-primary);
    line-height: 1.6;
    min-height: 100vh;
}
'''
css = re.sub(body_pattern, body_replacement.strip(), css, count=1)

# 3. Nuke ALL glassmorphism and transparent overrides
# (I will match the entire block that sets backgrounds to rgba(...) and backdrop-filter)
css = re.sub(r'backdrop-filter:\s*blur[^;]+;', '', css)
css = re.sub(r'-webkit-backdrop-filter:\s*blur[^;]+;', '', css)
css = re.sub(r'background:\s*rgba\(255,\s*255,\s*255,\s*0\.\d+\)[^;]*;', 'background: #ffffff;', css)
css = re.sub(r'background:\s*rgba\(0,\s*0,\s*0,\s*0\.\d+\)[^;]*;', 'background: #ffffff;', css)

# 4. Restore standard text colors
css = re.sub(r'color:\s*#ffffff\s*!important;', 'color: var(--text-primary) !important;', css)
css = re.sub(r'color:\s*rgba\(255,\s*255,\s*255,\s*0\.\d+\)[^;]*;', 'color: var(--text-secondary);', css)

# 5. Fix inputs
input_pattern = r'\.modern-input,\s*select,\s*textarea\s*\{[^}]+\}'
input_replacement = '''
.modern-input, select, textarea {
    background: #F1F5F9 !important;
    color: var(--text-primary) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-sm);
    padding: 0.75rem 1rem;
    font-family: inherit;
    font-size: 16px !important;
    transition: all 0.2s ease;
}
.modern-input:focus, select:focus, textarea:focus {
    background: #FFFFFF !important;
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px rgba(15, 42, 74, 0.1) !important;
}
.modern-input::placeholder, textarea::placeholder {
    color: var(--text-muted) !important;
    font-weight: 400;
}
'''
css = re.sub(input_pattern, input_replacement.strip(), css)

# Fix hover borders
css = re.sub(r'border-color:\s*#ffffff\s*!important;', 'border-color: var(--primary) !important;', css)

# 6. Add specific Real Estate Theme styling
real_estate_css = '''
/* ?? SOLID REAL ESTATE THEME */

/* Header / Navbar - Solid Navy */
.navbar {
    background: var(--primary) !important;
    border-bottom: 4px solid var(--accent) !important; /* Terracotta structural line */
    padding: 0.75rem 1.5rem;
}
.brand-title {
    color: #FFFFFF !important;
    font-family: 'Playfair Display', serif !important;
    font-size: 1.8rem;
}
.nav-btn {
    color: #F8FAFC !important;
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 4px !important; /* Sharp architectural */
}
.nav-btn.active {
    background: var(--accent) !important;
    color: #FFFFFF !important;
    border-color: var(--accent) !important;
}
.status-label { color: #FFFFFF !important; }

/* Buttons */
.btn {
    border-radius: 4px !important;
    font-weight: 600;
    letter-spacing: 0.5px;
}
.btn-primary {
    background: var(--primary) !important;
    color: #FFFFFF !important;
    border: none !important;
    box-shadow: none !important;
}
.btn-primary:hover {
    background: var(--primary-light) !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(15,42,74,0.2) !important;
}
.btn-success {
    background: var(--accent) !important;
    color: #FFFFFF !important;
}
.btn-success:hover {
    background: var(--accent-dark) !important;
}

/* Cards & Containers - Solid White */
.card, .bento-card, .filter-card, .valuation-card, .chat-wrapper, .modal-box, .auth-box, .form-container, .property-card {
    background: #FFFFFF !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-sm) !important; /* Architectural sharp */
    box-shadow: var(--shadow-sm) !important;
    color: var(--text-primary) !important;
}

/* Typography Overrides */
h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: var(--primary) !important;
}
.hero-text h1 {
    color: var(--primary) !important;
    text-shadow: none !important;
    -webkit-text-fill-color: var(--primary) !important;
}
.hero-text p {
    color: var(--text-secondary) !important;
    text-shadow: none !important;
}

/* Property Cards */
.prop-price-row {
    background: #F8FAFC !important;
    border: 1px solid #E2E8F0 !important;
}
.val-amount {
    color: var(--primary) !important;
    text-shadow: none !important;
}

/* Labels */
label {
    color: var(--primary) !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 600 !important;
    text-transform: uppercase;
    font-size: 0.8rem;
    letter-spacing: 0.5px;
}
'''
css += "\n" + real_estate_css

# Fix some remaining inline color overrides I might have left
css = re.sub(r'color:\s*#ffffff\s*!important;', '', css) # Strip stray white text

with open('code/frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Solid Real Estate Theme applied.")
