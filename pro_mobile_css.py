import re

with open('code/frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Prevent Horizontal Scrolling globally (crucial for native app feel)
if 'overflow-x: hidden' not in css[:200]:
    css = re.sub(r'body\s*\{', r'html, body {\n    overflow-x: hidden;\n    width: 100%;\n    -webkit-text-size-adjust: 100%;\n}\n\nbody {', css, count=1)

# 2. Fix iOS Zooming Issue (inputs must be at least 16px)
css = re.sub(r'(\.modern-input,\s*select,\s*textarea\s*\{[^}]+)font-size:\s*0\.95rem;', r'\1font-size: 16px;', css)

# 3. Ensure the dynamic loader hides overflow when zooming
css = re.sub(r'\.dynamic-loader\s*\{', r'.dynamic-loader {\n    overflow: hidden;', css)

# 4. Improve the Mobile Responsiveness Block
better_mobile_css = '''
/* --------------------------------------------------- */
/* ?? PRO-GRADE MOBILE OPTIMIZATION                    */
/* --------------------------------------------------- */
@media (max-width: 768px) {
    /* Base fixes */
    html, body {
        overflow-x: hidden !important;
        position: relative;
        width: 100%;
    }
    
    /* Avoid iOS Input Zoom */
    .modern-input, select, textarea {
        font-size: 16px !important; 
    }

    /* Navbar: Native App Feel */
    .navbar {
        padding: 0.5rem !important;
    }
    .nav-container {
        padding: 0 !important;
        gap: 8px !important;
    }
    .brand-title {
        font-size: 1.4rem !important;
    }
    
    /* Make tabs scroll horizontally smoothly without scrollbar */
    .nav-tabs {
        flex-wrap: nowrap !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch !important;
        scrollbar-width: none; /* Firefox */
        -ms-overflow-style: none;  /* IE and Edge */
        padding-bottom: 5px;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }
    .nav-tabs::-webkit-scrollbar {
        display: none; /* Chrome/Safari */
    }
    .nav-btn {
        padding: 8px 16px !important;
        font-size: 0.9rem !important;
        white-space: nowrap !important;
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 20px;
    }
    .nav-btn.active {
        background: rgba(255,255,255,0.2) !important;
    }

    /* Chat Layout Fixes */
    .chat-wrapper {
        display: flex !important;
        flex-direction: column !important;
        height: calc(100vh - 140px) !important; /* Proper height for mobile */
        border-radius: 12px;
    }
    .chat-sidebar {
        display: flex !important;
        flex-direction: row !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch;
        min-height: 90px !important;
        max-height: 90px !important;
        padding: 8px !important;
        scrollbar-width: none;
    }
    .chat-sidebar::-webkit-scrollbar { display: none; }
    .chat-channel-item {
        min-width: 80px !important;
        max-width: 80px !important;
        padding: 5px !important;
        margin-right: 8px;
        border-radius: 10px;
    }
    .channel-thumb {
        width: 35px !important;
        height: 35px !important;
    }
    .channel-title {
        font-size: 0.75rem !important;
    }
    .channel-sub { display: none; /* Too much info for mobile top bar */ }

    .chat-main {
        flex: 1;
        display: flex;
        flex-direction: column;
    }
    .chat-messages {
        flex: 1;
        overflow-y: auto;
        padding: 10px !important;
    }
    .chat-input-area {
        padding: 10px !important;
    }

    /* Property Cards Native Look */
    .property-card {
        margin-bottom: 1rem !important;
        border-radius: 16px !important;
    }
    .card-img-wrapper {
        height: 200px !important;
    }

    /* Form Inputs */
    .form-container {
        padding: 1.2rem !important;
    }
    .auth-box {
        padding: 1.2rem !important;
        margin-top: 10vh !important;
    }

    /* Adjust loader for mobile */
    .loader-word {
        font-size: 1.8rem !important;
        gap: 4px !important;
    }
}
'''

# Append or replace the mobile section. To be safe, just append at the end (CSS cascading will prioritize this).
css += "\n" + better_mobile_css

with open('code/frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Pro-Grade Mobile Optimizations Applied.")
