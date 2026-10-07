import re

with open('code/frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix the getElementById references in loadProperties
js = js.replace('document.getElementById("filter-city")', 'document.getElementById("city-filter")')
js = js.replace('document.getElementById("filter-type")', 'document.getElementById("category-filter")')
js = js.replace('document.getElementById("filter-barometer")', 'document.getElementById("barometer-filter")')
js = js.replace('document.getElementById("filter-search")', 'document.getElementById("search-input")')

with open('code/frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Fixed filter IDs in app.js.")
