import re

with open('code/frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Aggressively remove the neon body block
css = re.sub(r'body\s*\{\s*font-family[^}]+background:\s*linear-gradient\(-45deg[^}]+\}', '', css)
css = re.sub(r'@keyframes gradientVibe\s*\{[^}]+\}', '', css)
css = re.sub(r'animation:\s*gradientVibe[^;]+;', '', css)

with open('code/frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Neon gradient aggressively destroyed.")
