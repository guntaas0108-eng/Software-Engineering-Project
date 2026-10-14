import re

with open('code/frontend/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the section header to include the correct ID
old_header = r'<h2>Curated Listings</h2>'
new_header = '<h2 id="listings-count-label">Curated Listings</h2>'

html = re.sub(old_header, new_header, html)

with open('code/frontend/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
