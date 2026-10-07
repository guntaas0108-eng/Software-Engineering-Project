import re

with open('code/frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace body background with animated vibrant gradient
body_pattern = r'body\s*\{[^}]+\}'
body_replacement = '''
body {
    font-family: 'Outfit', sans-serif;
    background: linear-gradient(-45deg, #FF512F, #DD2476, #4F46E5, #0ea5e9);
    background-size: 400% 400%;
    animation: gradientVibe 15s ease infinite;
    color: var(--text-primary);
    line-height: 1.6;
    min-height: 100vh;
}

@keyframes gradientVibe {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

h1, h2, h3, .brand-title {
    font-family: 'Playfair Display', serif !important;
    letter-spacing: -0.5px;
}

h1 {
    font-size: 3.5rem !important;
    font-weight: 800 !important;
}

h2 {
    font-size: 2.2rem !important;
}
'''
css = re.sub(body_pattern, body_replacement.strip(), css, count=1)

# Ensure cards are bright glass to contrast the background
css = re.sub(r'background:\s*rgba\(255,\s*255,\s*255,\s*0.6\)\s*!important;', r'background: rgba(255, 255, 255, 0.9) !important;', css)
css = re.sub(r'backdrop-filter:\s*blur\(20px\)\s*!important;', r'backdrop-filter: blur(25px) !important;', css)

# Make text inside the hero banner pop
css += '''
.hero-text h1 {
    background: none !important;
    -webkit-text-fill-color: #ffffff !important;
    color: #ffffff !important;
    text-shadow: 0 4px 20px rgba(0,0,0,0.3);
}
.hero-text p {
    color: rgba(255,255,255,0.95) !important;
    font-size: 1.2rem;
    font-weight: 400;
    text-shadow: 0 2px 10px rgba(0,0,0,0.2);
}
.h-stat-box {
    background: rgba(255,255,255,0.9) !important;
    border: none !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2) !important;
}
.h-stat-val {
    color: #DD2476 !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 700 !important;
}
.brand-title {
    color: #1e293b !important;
}
.nav-btn {
    font-family: 'Outfit', sans-serif;
    font-weight: 600;
}
.btn {
    font-family: 'Outfit', sans-serif;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.val-amount {
    font-family: 'Playfair Display', serif !important;
    color: #4F46E5 !important;
    font-size: 2.5rem !important;
}
'''

with open('code/frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Vibrant Animated Theme applied.")
