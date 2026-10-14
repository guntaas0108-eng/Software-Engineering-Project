import re

with open('code/frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix hero-model-r2
js = js.replace('document.getElementById("hero-model-r2").textContent = ml.r2_score;', '// hero-model-r2 removed')

with open('code/frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)
