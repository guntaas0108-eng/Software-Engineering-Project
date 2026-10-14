import re

with open('code/frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace any vibrant button gradients with solid real estate colors
css = re.sub(r'background:\s*linear-gradient\(135deg,\s*#4F46E5,\s*#7C3AED\)\s*!important;', r'background: var(--primary) !important;', css)
css = re.sub(r'background:\s*linear-gradient\(135deg,\s*#FF5A5F,\s*#F43F5E\)\s*!important;', r'background: var(--accent) !important;', css)
css = re.sub(r'background:\s*linear-gradient\(135deg,\s*#4F46E5,\s*#7C3AED\);', r'background: var(--primary);', css)

# Replace neon text clipping
css = re.sub(r'background:\s*linear-gradient\(135deg,\s*#FF5A5F,\s*#7C3AED,\s*#4F46E5\);', r'color: var(--primary);', css)

with open('code/frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Remaining vibrant button/text colors neutralized.")
