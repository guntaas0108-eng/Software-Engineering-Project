import re

with open('code/frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make sure body is pristine
body_css = '''
body {
    background-color: #F8FAFC !important;
    background-image: none !important;
    animation: none !important;
    color: #1E293B !important;
}
'''

css += "\n" + body_css

with open('code/frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
