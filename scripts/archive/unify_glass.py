import re

with open('code/frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update root variables for text and borders to support glass
css = re.sub(r'--text-primary:\s*[^;]+;', r'--text-primary: #ffffff;', css)
css = re.sub(r'--text-secondary:\s*[^;]+;', r'--text-secondary: rgba(255, 255, 255, 0.85);', css)
css = re.sub(r'--text-muted:\s*[^;]+;', r'--text-muted: rgba(255, 255, 255, 0.6);', css)
css = re.sub(r'--border:\s*[^;]+;', r'--border: rgba(255, 255, 255, 0.15);', css)
css = re.sub(r'--card-bg:\s*[^;]+;', r'--card-bg: rgba(255, 255, 255, 0.1);', css)

# 2. Replace hardcoded opaque white backgrounds with transparent glass
css = re.sub(r'background:\s*#ffffff;', r'background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);', css)

# 3. Fix input fields so they aren't solid white or gray, but dark glass
input_pattern = r'\.modern-input,\s*select,\s*textarea\s*\{[^}]+\}'
input_replacement = '''
.modern-input, select, textarea {
    background: rgba(0, 0, 0, 0.2) !important;
    color: #ffffff !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
    backdrop-filter: blur(10px);
    border-radius: var(--radius-sm);
    padding: 0.75rem 1rem;
    font-family: inherit;
    font-size: 0.95rem;
    transition: all 0.2s ease;
}
'''
css = re.sub(input_pattern, input_replacement.strip(), css)

# 4. Fix dropdown options text (they can't be transparent dark glass, because OS dropdowns don't support backdrop filter well, so we make them solid dark)
if 'select option' not in css:
    css += '\nselect option { background: #1e293b; color: #ffffff; }\n'

# 5. Make sure the body color applies properly, and remove any forced dark text
css = re.sub(r'color:\s*#1e293b\s*!important;', r'color: #ffffff !important;', css)
css = re.sub(r'color:\s*#0F172A;', r'color: #ffffff;', css)
css = re.sub(r'color:\s*#475569;', r'color: rgba(255,255,255,0.85);', css)
css = re.sub(r'background:\s*#f8fafc;', r'background: rgba(0,0,0,0.15);', css) # for old stat boxes
css = re.sub(r'background:\s*#f1f5f9;', r'background: rgba(255,255,255,0.05);', css) # tables
css = re.sub(r'background:\s*#e2e8f0;', r'background: rgba(255,255,255,0.1);', css)

# Fix specific text colors in CSS rules
css = re.sub(r'color:\s*var\(--text-primary\);', r'color: #ffffff;', css)

# Remove the old card-bg opacity override that forced solid white
css = re.sub(r'background:\s*rgba\(255,\s*255,\s*255,\s*0.9\)\s*!important;', r'background: rgba(255, 255, 255, 0.1) !important;', css)

# Fix Brand Title specifically
css = re.sub(r'\.brand-title\s*\{[^}]+\}', '''
.brand-title {
    color: #ffffff !important;
    font-family: 'Playfair Display', serif !important;
    letter-spacing: -0.5px;
}
''', css)

# Fix mathematical formula block so it looks premium inside glass
css = re.sub(r'\.ml-formula\s*\{[^}]+\}', '''
.ml-formula {
    background: rgba(0, 0, 0, 0.25);
    border: 1px solid rgba(255, 255, 255, 0.15);
    padding: 1.5rem;
    border-radius: var(--radius-md);
    margin-bottom: 1.5rem;
    color: #ffffff;
}
''', css)

# Fix nav container background (if it has one)
css = re.sub(r'\.navbar\s*\{[^}]+\}', '''
.navbar {
    background: rgba(255, 255, 255, 0.05) !important;
    backdrop-filter: blur(24px) !important;
    -webkit-backdrop-filter: blur(24px) !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.15);
    position: sticky;
    top: 0;
    z-index: 100;
}
''', css)

# Let's write the CSS
with open('code/frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Unified glass theme applied.")
