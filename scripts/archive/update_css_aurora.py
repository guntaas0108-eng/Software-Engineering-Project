import re

with open('code/frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update variables
new_root = '''
:root {
    --primary: #4F46E5;
    --primary-dark: #3730A3;
    --primary-light: #E0E7FF;
    --accent: #FF5A5F;
    --accent-dark: #E11D48;
    --warning: #F59E0B;
    --danger: #EF4444;
    --bg-main: #f8fafc;
    --card-bg: rgba(255, 255, 255, 0.65);
    --border: rgba(255, 255, 255, 0.8);
    --text-primary: #0F172A;
    --text-secondary: #475569;
    --text-muted: #94A3B8;
    --radius-sm: 12px;
    --radius-md: 16px;
    --radius-lg: 24px;
    --shadow-sm: 0 4px 6px -1px rgba(0,0,0,0.02);
    --shadow-md: 0 8px 32px 0 rgba(31, 38, 135, 0.07);
    --shadow-lg: 0 20px 25px -5px rgba(0,0,0,0.05);
}
'''
css = re.sub(r':root\s*\{[^}]+\}', new_root.strip(), css, count=1)

# 2. Add Aurora Mesh Background to body
# Find the body tag and replace its background
body_replacement = '''
body {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: #f4f7f6;
    background-image: 
        radial-gradient(at 0% 0%, hsla(253,16%,7%,0) 0, transparent 50%), 
        radial-gradient(at 50% 0%, hsla(225,39%,30%,0) 0, transparent 50%), 
        radial-gradient(at 100% 0%, hsla(339,49%,30%,0) 0, transparent 50%),
        radial-gradient(at 0% 100%, hsla(22,100%,77%,0.4) 0px, transparent 50%),
        radial-gradient(at 80% 100%, hsla(242,100%,70%,0.3) 0px, transparent 50%),
        radial-gradient(at 0% 50%, hsla(355,100%,93%,0.6) 0px, transparent 50%),
        radial-gradient(at 80% 50%, hsla(340,100%,76%,0.3) 0px, transparent 50%);
    background-attachment: fixed;
    color: var(--text-primary);
    line-height: 1.5;
    min-height: 100vh;
}
'''
css = re.sub(r'body\s*\{[^}]+\}', body_replacement.strip(), css, count=1)

# 3. Add Premium Overrides at the end
additional_css = '''

/* === PREMIUM AURORA GLASS UI === */

.navbar {
    background: rgba(255, 255, 255, 0.5) !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.8) !important;
}

.card, .bento-card, .filter-card, .valuation-card, .chat-wrapper, .modal-box, .auth-box, .glass-panel {
    background: rgba(255, 255, 255, 0.6) !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    border: 1px solid rgba(255,255,255,0.9) !important;
    box-shadow: 0 10px 40px -10px rgba(31, 38, 135, 0.1) !important;
    border-radius: var(--radius-lg);
}

.modern-input, select, textarea {
    background: rgba(255, 255, 255, 0.8) !important;
    border: 1px solid rgba(0,0,0,0.06) !important;
    border-radius: var(--radius-sm);
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);
    transition: all 0.3s ease;
}

.modern-input:focus, select:focus, textarea:focus {
    background: #ffffff !important;
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 4px var(--primary-light) !important;
}

.btn {
    border-radius: 50px !important;
    text-transform: none;
    font-weight: 600;
    letter-spacing: 0.3px;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.btn-primary {
    background: linear-gradient(135deg, #4F46E5, #7C3AED) !important;
    color: white !important;
    border: none !important;
    box-shadow: 0 4px 15px rgba(124, 58, 237, 0.3) !important;
}

.btn-primary:hover {
    box-shadow: 0 8px 25px rgba(124, 58, 237, 0.4) !important;
    transform: translateY(-2px);
}

.btn-success {
    background: linear-gradient(135deg, #FF5A5F, #F43F5E) !important;
    color: white !important;
    border: none !important;
    box-shadow: 0 4px 15px rgba(255, 90, 95, 0.3) !important;
}

.btn-success:hover {
    box-shadow: 0 8px 25px rgba(255, 90, 95, 0.4) !important;
    transform: translateY(-2px);
}

.hero-text h1 {
    background: linear-gradient(135deg, #FF5A5F, #7C3AED, #4F46E5);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
}

.prop-card {
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    background: rgba(255,255,255,0.7) !important;
    border: 1px solid rgba(255,255,255,0.9) !important;
    backdrop-filter: blur(10px);
}

.prop-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 20px 40px -10px rgba(79, 70, 229, 0.15) !important;
}

.prop-img-container {
    border-radius: var(--radius-lg) var(--radius-lg) 0 0;
    overflow: hidden;
}

.prop-img-container img {
    transition: transform 0.6s ease;
}

.prop-card:hover .prop-img-container img {
    transform: scale(1.08);
}

.h-stat-box {
    background: rgba(255,255,255,0.6);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,1);
    box-shadow: 0 8px 32px rgba(31,38,135,0.05);
}

/* Chat Bubbles */
.chat-msg.buyer .msg-bubble { 
    background: linear-gradient(135deg, #4F46E5, #7C3AED); 
    color: white; 
    border: none;
}
.chat-msg.seller .msg-bubble { 
    background: rgba(255,255,255,0.9); 
    border: 1px solid rgba(0,0,0,0.05); 
    box-shadow: 0 2px 10px rgba(0,0,0,0.02);
}

/* Scrollbar */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(0,0,0,0.15); border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: rgba(0,0,0,0.25); }

/* Make the loader colors pop more */
.dynamic-loader {
    background-color: #0b1120;
}
'''
css += additional_css

with open('code/frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Aurora Glass theme applied successfully.")
