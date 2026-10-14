import re

with open('code/frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Remove the call to updateHeroStats
js = js.replace('updateHeroStats(data.data);', '// updateHeroStats(data.data); removed since hero redesign')

# Remove the function definition to be clean
js = re.sub(r'function updateHeroStats\(props\)\s*\{\s*document\.getElementById\("hero-total-props"\)\.textContent[^}]+\}', '', js)

with open('code/frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)
