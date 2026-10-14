import re

with open('code/frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. High Contrast Root Variables for Maximum Clarity
new_root = '''
:root {
    --primary: #1D4ED8; /* Royal Blue */
    --primary-light: #EFF6FF;
    --primary-dark: #1E3A8A;
    --accent: #059669; /* Emerald Green */
    --bg-main: #E2E8F0; /* Slate 200 - Very distinct from white cards */
    --card-bg: #FFFFFF; /* Pure White */
    --border: #CBD5E1; /* Slate 300 - Clear borders */
    --text-primary: #0F172A; /* Slate 900 - Almost Black */
    --text-secondary: #334155; /* Slate 700 - Dark Gray */
    --text-muted: #64748B; /* Slate 500 */
    --radius-sm: 6px;
    --radius-md: 10px;
    --radius-lg: 16px;
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.1);
    --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
    --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -2px rgba(0,0,0,0.05);
}
'''
css = re.sub(r':root\s*\{[^}]+\}', new_root.strip(), css, count=1)

# 2. Fix the Body for Clarity
body_replacement = '''
body {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important; /* Extremely readable font */
    background-color: var(--bg-main) !important;
    color: var(--text-primary) !important;
    line-height: 1.6;
    min-height: 100vh;
}
'''
css = re.sub(r'body\s*\{[^}]+\}', body_replacement.strip(), css)

# 3. Clear Navbar
nav_replacement = '''
.navbar {
    background: #FFFFFF !important;
    border-bottom: 2px solid #E2E8F0 !important;
    padding: 0.8rem 1.5rem;
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}
.brand-title {
    color: #1D4ED8 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 1.6rem;
    font-weight: 800;
}
.nav-btn {
    color: #334155 !important;
    background: #F1F5F9 !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 6px !important;
    font-weight: 600;
    font-size: 0.95rem;
    padding: 0.5rem 1rem !important;
}
.nav-btn:hover { background: #E2E8F0 !important; color: #0F172A !important; }
.nav-btn.active {
    background: #1D4ED8 !important;
    color: #FFFFFF !important;
    border-color: #1D4ED8 !important;
}
.status-label { color: #334155 !important; font-weight: 700; }
'''
css = re.sub(r'\.navbar\s*\{[^}]+\}(?:\s*\.brand-title\s*\{[^}]+\})?(?:\s*\.nav-btn\s*\{[^}]+\})?(?:\s*\.nav-btn:hover\s*\{[^}]+\})?(?:\s*\.nav-btn\.active\s*\{[^}]+\})?(?:\s*\.status-label\s*\{[^}]+\})?', nav_replacement.strip(), css)

# 4. Clear Cards
css = re.sub(r'\.card, \.bento-card, \.filter-card, \.valuation-card, \.chat-wrapper, \.modal-box, \.auth-box, \.form-container, \.property-card\s*\{[^}]+\}', '''
.card, .bento-card, .filter-card, .valuation-card, .chat-wrapper, .modal-box, .auth-box, .form-container, .property-card {
    background: #FFFFFF !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: var(--radius-md) !important;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
    color: #0F172A !important;
    padding: 1.5rem;
}
.property-card { padding: 0; }
''', css)

# 5. Clear Inputs
css = re.sub(r'\.modern-input,\s*select,\s*textarea\s*\{[^}]+\}', '''
.modern-input, select, textarea {
    background: #FFFFFF !important;
    color: #0F172A !important;
    border: 2px solid #CBD5E1 !important;
    border-radius: 6px !important;
    padding: 0.8rem 1rem;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    transition: all 0.2s ease;
}
''', css)
css = re.sub(r'\.modern-input:focus,\s*select:focus,\s*textarea:focus\s*\{[^}]+\}', '''
.modern-input:focus, select:focus, textarea:focus {
    background: #F8FAFC !important;
    border-color: #1D4ED8 !important;
    outline: none;
    box-shadow: 0 0 0 3px rgba(29, 78, 216, 0.2) !important;
}
''', css)
css = re.sub(r'\.modern-input::placeholder,\s*textarea::placeholder\s*\{[^}]+\}', '''
.modern-input::placeholder, textarea::placeholder {
    color: #94A3B8 !important;
    font-weight: 400 !important;
}
''', css)

# 6. Buttons
css = re.sub(r'\.btn-primary\s*\{[^}]+\}', '''
.btn-primary {
    background: #1D4ED8 !important;
    color: #FFFFFF !important;
    border: none !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 6px rgba(29, 78, 216, 0.2) !important;
}
''', css)

# 7. Labels
css = re.sub(r'label\s*\{\s*color:\s*var\(--primary\)\s*!important;\s*font-family:\s*\'Outfit\'[^\}]+\}', '''
label {
    color: #334155 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.85rem;
    margin-bottom: 0.5rem;
    display: block;
}
''', css)

# 8. Floating search bar specific
css = re.sub(r'\.floating-search-bar\s*\{[^}]+\}', '''
.floating-search-bar {
    background: #FFFFFF !important;
    width: 100%;
    border-radius: 12px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.3) !important;
    overflow: hidden;
    display: flex;
    flex-direction: column;
}
''', css)

# Restore default Plus Jakarta Sans in html
with open('code/frontend/index.html', 'r', encoding='utf-8') as h:
    html = h.read()
html = re.sub(r'<link href="https://fonts.googleapis.com/css2\?family=Outfit[^"]+" rel="stylesheet">', '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">', html)
with open('code/frontend/index.html', 'w', encoding='utf-8') as h:
    h.write(html)

with open('code/frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("High Contrast Clear Theme applied.")
