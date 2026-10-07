import re

with open('code/frontend/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the option values
html = html.replace('<option value="">All Cities</option>', '<option value="All">All Cities</option>')
html = html.replace('<option value="">All Types</option>', '<option value="All">All Types</option>')
html = html.replace('<option value="">AI Rating: Any</option>', '<option value="All">AI Rating: Any</option>')

with open('code/frontend/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
