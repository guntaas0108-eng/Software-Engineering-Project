import re

with open('code/frontend/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the oninput handler
html = html.replace('oninput="triggerLiveSearch()"', 'oninput="debounceFilter()"')

with open('code/frontend/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
