import re

with open('code/frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add placeholder styling to CSS
placeholder_css = '''
/* FIX INPUT PLACEHOLDER CONTRAST */
.modern-input::placeholder, textarea::placeholder {
    color: rgba(255, 255, 255, 0.85) !important;
    font-weight: 500;
}

.modern-input, select, textarea {
    background: rgba(0, 0, 0, 0.35) !important;
    color: #ffffff !important;
    font-weight: 600 !important;
    border: 1px solid rgba(255, 255, 255, 0.4) !important;
}

.modern-input:focus, select:focus, textarea:focus {
    background: rgba(0, 0, 0, 0.5) !important;
    border-color: #ffffff !important;
    box-shadow: 0 0 0 4px rgba(255, 255, 255, 0.2) !important;
}
'''

css += "\n" + placeholder_css + "\n"

with open('code/frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Placeholder CSS fixed.")
