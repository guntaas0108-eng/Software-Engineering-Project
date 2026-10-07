import re

with open('code/frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_root = '''
:root {
    --primary: #6366f1;
    --primary-dark: #4f46e5;
    --primary-light: rgba(99, 102, 241, 0.15);
    --accent: #10b981;
    --accent-dark: #059669;
    --warning: #f59e0b;
    --danger: #ef4444;
    --bg-main: #0b1120;
    --card-bg: rgba(30, 41, 59, 0.7);
    --border: rgba(255, 255, 255, 0.1);
    --text-primary: #f8fafc;
    --text-secondary: #94a3b8;
    --text-muted: #64748b;
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 20px;
    --shadow-sm: 0 4px 6px -1px rgba(0,0,0,0.5);
    --shadow-md: 0 10px 15px -3px rgba(0,0,0,0.5);
    --shadow-lg: 0 20px 25px -5px rgba(0,0,0,0.5);
}
'''

css = re.sub(r':root\s*\{[^}]+\}', new_root.strip(), css, count=1)

# Specific targeted replacements
css = re.sub(r'(\.navbar\s*\{[^}]+)background:\s*#ffffff;', r'\1background: rgba(15, 23, 42, 0.75); backdrop-filter: blur(12px);', css)

# Background color generic replacements
css = re.sub(r'background(?:-color)?:\s*#ffffff;', r'background: var(--card-bg);', css)
css = re.sub(r'background:\s*#fffbeb;', r'background: rgba(245, 158, 11, 0.1);', css)
css = re.sub(r'background:\s*linear-gradient\(180deg, #f8fafc 0%, #ffffff 100%\);', r'background: linear-gradient(180deg, rgba(15,23,42,0.8) 0%, rgba(11,17,32,0.9) 100%);', css)

# Inputs
css = re.sub(r'border:\s*1px solid #cbd5e1;', r'border: 1px solid var(--border);', css)
css = re.sub(r'color:\s*#0f172a;', r'color: var(--text-primary);', css)

# Tables
css = re.sub(r'background:\s*#f1f5f9;', r'background: rgba(255,255,255,0.05);', css)
css = re.sub(r'background:\s*#f8fafc;', r'background: rgba(255,255,255,0.02);', css)

# Borders
css = re.sub(r'border(-[a-z]+)?:\s*1px solid #e2e8f0', r'border\1: 1px solid var(--border)', css)

# Badges and UI blocks
css = re.sub(r'color:\s*#334155;', r'color: var(--text-secondary);', css)

additional_css = '''
.card, .bento-card, .filter-card, .valuation-card, .chat-wrapper, .modal-box, .auth-box, .glass-panel {
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(255,255,255,0.05) !important;
    box-shadow: var(--shadow-md) !important;
    background: var(--card-bg) !important;
}

.modern-input, select, textarea {
    background: rgba(15, 23, 42, 0.6) !important;
    color: var(--text-primary) !important;
    border: 1px solid var(--border) !important;
}

.modern-input:focus, select:focus, textarea:focus {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px var(--primary-light) !important;
}

.modern-input::placeholder, textarea::placeholder {
    color: var(--text-muted);
}

.hero-text h1 {
    background: linear-gradient(135deg, #a5b4fc, #818cf8, #6366f1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
}

.btn-primary {
    background: linear-gradient(135deg, #4f46e5, #3b82f6) !important;
    border: none !important;
    box-shadow: 0 4px 15px rgba(79, 70, 229, 0.4) !important;
}

.btn-primary:hover {
    box-shadow: 0 6px 20px rgba(79, 70, 229, 0.6) !important;
    transform: translateY(-2px);
}

.btn-success {
    background: linear-gradient(135deg, #059669, #10b981) !important;
    border: none !important;
    box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4) !important;
}

.btn-success:hover {
    box-shadow: 0 6px 20px rgba(16, 185, 129, 0.6) !important;
    transform: translateY(-2px);
}

.prop-card {
    transition: all 0.3s ease;
    background: var(--card-bg) !important;
    border: 1px solid rgba(255,255,255,0.05) !important;
    backdrop-filter: blur(12px);
}
.prop-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px -10px rgba(99, 102, 241, 0.3) !important;
    border-color: rgba(99, 102, 241, 0.3) !important;
}
.prop-img-container img {
    opacity: 0.9;
}
.prop-card:hover .prop-img-container img {
    opacity: 1;
    transform: scale(1.05);
    transition: all 0.5s ease;
}

/* Fix chat messages */
.chat-msg.buyer .msg-bubble { background: linear-gradient(135deg, #4f46e5, #3b82f6); color: white; }
.chat-msg.seller .msg-bubble { background: rgba(255,255,255,0.1); color: var(--text-primary); border: 1px solid var(--border); }

/* Make the brand pop */
.brand-icon { filter: drop-shadow(0 0 8px rgba(99, 102, 241, 0.8)); }
.brand-title { color: #f8fafc; font-weight: 800; letter-spacing: -0.5px; }

/* Filter Card enhancements */
.filter-card {
    background: linear-gradient(180deg, rgba(30,41,59,0.7) 0%, rgba(15,23,42,0.8) 100%) !important;
}

/* Custom scrollbar for dark theme */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: var(--bg-main); }
::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: rgba(255,255,255,0.2); }
'''

css += additional_css

with open('code/frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS updated with Python successfully.")
