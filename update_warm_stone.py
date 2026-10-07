import re

with open('code/frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the stark white root variables with a Warm Stone & Terracotta palette
new_root = '''
:root {
    --primary: #2C3E50; /* Deep Slate Blue */
    --primary-light: #34495E;
    --primary-dark: #1A252F;
    --accent: #C27A59; /* Muted Terracotta */
    --accent-dark: #A66548;
    --bg-main: #E9E6E1; /* Warm Stone / Greige - NOT white */
    --card-bg: #FDFDFD; /* Very soft off-white for cards */
    --border: #D1CCC4;
    --text-primary: #2C3E50;
    --text-secondary: #596775;
    --text-muted: #8E98A3;
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --shadow-sm: 0 4px 10px rgba(44, 62, 80, 0.05);
    --shadow-md: 0 10px 25px rgba(44, 62, 80, 0.08);
    --shadow-lg: 0 20px 40px rgba(44, 62, 80, 0.12);
}
'''
css = re.sub(r':root\s*\{[^}]+\}', new_root.strip(), css, count=1)

# Ensure body uses this new non-white background
body_replacement = '''
body {
    font-family: 'Outfit', sans-serif;
    background-color: var(--bg-main) !important;
    background-image: none !important;
    animation: none !important;
    color: var(--text-primary) !important;
    line-height: 1.6;
    min-height: 100vh;
}
'''
css = re.sub(r'body\s*\{[^}]+\}', body_replacement.strip(), css)

# Make sure the navbar has a distinct, rich color so it doesn't blend into the white
nav_replacement = '''
.navbar {
    background: #2C3E50 !important;
    border-bottom: 4px solid #C27A59 !important;
    padding: 0.8rem 1.5rem;
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}
.brand-title {
    color: #FFFFFF !important;
    font-family: 'Playfair Display', serif !important;
    font-size: 1.6rem;
    font-weight: 800;
}
.nav-btn {
    color: #D1CCC4 !important;
    border: none !important;
    border-radius: 6px !important;
    font-weight: 600;
    font-size: 0.9rem;
    transition: all 0.2s ease;
    background: transparent !important;
}
.nav-btn:hover { background: rgba(255,255,255,0.1) !important; color: #FFFFFF !important; }
.nav-btn.active {
    background: #C27A59 !important;
    color: #FFFFFF !important;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.status-label { color: #FFFFFF !important; }
'''
css = re.sub(r'\.navbar\s*\{[^}]+\}(?:\s*\.brand-title\s*\{[^}]+\})?(?:\s*\.nav-btn\s*\{[^}]+\})?(?:\s*\.nav-btn:hover\s*\{[^}]+\})?(?:\s*\.nav-btn\.active\s*\{[^}]+\})?', nav_replacement.strip(), css)

# Update buttons to use the rich terracotta
css = re.sub(r'\.btn-primary\s*\{[^}]+\}', '''
.btn-primary {
    background: #C27A59 !important;
    color: #FFFFFF !important;
    border: none !important;
    box-shadow: 0 4px 12px rgba(194, 122, 89, 0.3) !important;
}
''', css)

# Ensure the hero section overlay is sophisticated and NOT neon
css = re.sub(r'\.hero-gradient-overlay\s*\{[^}]+\}', '''
.hero-gradient-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(to bottom, rgba(44, 62, 80, 0.6) 0%, rgba(26, 37, 47, 0.9) 100%);
    z-index: 2;
}
''', css)

# Make sure cards are solid and visible
css = re.sub(r'\.card, \.bento-card, \.filter-card, \.valuation-card, \.chat-wrapper, \.modal-box, \.auth-box, \.form-container, \.property-card\s*\{[^}]+\}', '''
.card, .bento-card, .filter-card, .valuation-card, .chat-wrapper, .modal-box, .auth-box, .form-container, .property-card {
    background: var(--card-bg) !important;
    border: 1px solid #FFFFFF !important; /* Creates a slight bevel effect against the stone background */
    border-radius: var(--radius-md) !important;
    box-shadow: var(--shadow-sm) !important;
    color: var(--text-primary) !important;
}
''', css)

with open('code/frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied Warm Stone & Terracotta Theme.")
