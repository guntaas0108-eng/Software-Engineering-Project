import re

with open('code/frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update text colors to be white/light for the glass theme
css = re.sub(r'--text-primary:\s*[^;]+;', r'--text-primary: #ffffff;', css)
css = re.sub(r'--text-secondary:\s*[^;]+;', r'--text-secondary: rgba(255, 255, 255, 0.85);', css)
css = re.sub(r'--text-muted:\s*[^;]+;', r'--text-muted: rgba(255, 255, 255, 0.6);', css)

# Fix specific hardcoded text colors
css = re.sub(r'color:\s*#1e293b\s*!important;', r'color: #ffffff !important;', css)
css = re.sub(r'color:\s*#0F172A;', r'color: #ffffff;', css)
css = re.sub(r'color:\s*#475569;', r'color: rgba(255,255,255,0.85);', css)

# 2. Make cards highly transparent (True Glassmorphism)
glass_css = '''
.navbar {
    background: rgba(255, 255, 255, 0.05) !important;
    backdrop-filter: blur(24px) !important;
    -webkit-backdrop-filter: blur(24px) !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.15) !important;
}

.card, .bento-card, .filter-card, .valuation-card, .chat-wrapper, .modal-box, .auth-box, .glass-panel, .prop-card {
    background: rgba(255, 255, 255, 0.1) !important;
    backdrop-filter: blur(24px) !important;
    -webkit-backdrop-filter: blur(24px) !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2) !important;
    color: #ffffff !important;
}

.prop-card h3, .prop-card h4, .prop-card p, .prop-card span {
    color: #ffffff !important;
}

/* Fix specific price/valuation blocks inside prop cards */
.prop-price-row {
    background: rgba(0, 0, 0, 0.2) !important;
    border-radius: var(--radius-md);
    padding: 10px;
    border: 1px solid rgba(255,255,255,0.1);
}

.val-amount {
    color: #ffffff !important;
    text-shadow: 0 2px 10px rgba(255,255,255,0.3);
}

/* Inputs and Selects: Dark Glass */
.modern-input, select, textarea {
    background: rgba(0, 0, 0, 0.25) !important;
    color: #ffffff !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
    backdrop-filter: blur(10px);
}
.modern-input:focus, select:focus, textarea:focus {
    background: rgba(0, 0, 0, 0.4) !important;
    border-color: rgba(255,255,255,0.5) !important;
    box-shadow: 0 0 0 4px rgba(255,255,255,0.1) !important;
}
.modern-input::placeholder, textarea::placeholder {
    color: rgba(255,255,255,0.5) !important;
}

/* Dropdown options text in dark glass needs to be dark so it's readable on OS default dropdowns */
select option {
    background: #1e293b;
    color: #ffffff;
}

/* Buttons */
.btn-outline {
    border: 1px solid rgba(255,255,255,0.4) !important;
    color: #ffffff !important;
    background: rgba(255,255,255,0.05) !important;
}
.btn-outline:hover {
    background: rgba(255,255,255,0.15) !important;
}

/* Badges / Chips */
.prop-badge, .legend-chip {
    background: rgba(0,0,0,0.3) !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
    color: #ffffff !important;
    backdrop-filter: blur(10px);
}

/* Remove old opaque backgrounds */
'''

# We need to wipe out the old card/input regex overrides I added previously at the bottom of the file
css = re.sub(r'\.card, \.bento-card, \.filter-card, \.valuation-card, \.chat-wrapper, \.modal-box, \.auth-box, \.glass-panel \{[^\}]+\}', '', css)
css = re.sub(r'\.prop-card \{[^\}]+\}', '', css)
css = re.sub(r'\.modern-input, select, textarea \{[^\}]+\}', '', css)

# Append the new pure glass CSS
css += glass_css

# Ensure body text is white
css = re.sub(r'color:\s*var\(--text-primary\);', r'color: #ffffff;', css)
css = re.sub(r'color:\s*#1e293b;', r'color: #ffffff;', css)

with open('code/frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Dynamic Glass Theme applied.")
