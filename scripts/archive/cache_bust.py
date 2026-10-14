import re

with open('code/frontend/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add cache busting
html = re.sub(r'href="style\.css(\?v=\d+)?"', 'href="style.css?v=3"', html)
html = re.sub(r'src="app\.js(\?v=\d+)?"', 'src="app.js?v=3"', html)

with open('code/frontend/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
