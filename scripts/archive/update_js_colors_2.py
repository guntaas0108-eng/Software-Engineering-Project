import re

with open('code/frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace hardcoded dark colors in JS templates to white/glass friendly
js = re.sub(r'color:\s*#64748b;', r'color: rgba(255,255,255,0.7);', js)
js = re.sub(r'color:\s*#475569;', r'color: rgba(255,255,255,0.7);', js)
js = re.sub(r'color:\s*#94a3b8;', r'color: rgba(255,255,255,0.7);', js)
js = re.sub(r'color:\s*#0f172a;', r'color: #ffffff;', js)
js = re.sub(r'background:\s*#f8fafc;', r'background: rgba(0,0,0,0.2);', js)
js = re.sub(r'border:\s*1px solid #e2e8f0;', r'border: 1px solid rgba(255,255,255,0.2);', js)
js = re.sub(r'color:\s*#2563eb;', r'color: #ffffff;', js)

# Fix appointment badges
js = re.sub(r'background:\s*#d1fae5;\s*color:\s*#047857;', r'background: rgba(16, 185, 129, 0.2); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.4);', js)
js = re.sub(r'background:\s*#fef3c7;\s*color:\s*#b45309;', r'background: rgba(245, 158, 11, 0.2); color: #f59e0b; border: 1px solid rgba(245, 158, 11, 0.4);', js)

with open('code/frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("JS inline styles updated.")
