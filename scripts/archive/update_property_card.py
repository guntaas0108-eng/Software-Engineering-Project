import re

with open('code/frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix property-card background to be pure glass
css = re.sub(r'\.property-card\s*\{[^}]+\}', '''
.property-card {
    background: rgba(255, 255, 255, 0.1) !important;
    backdrop-filter: blur(24px) !important;
    -webkit-backdrop-filter: blur(24px) !important;
    border-radius: var(--radius-lg);
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    overflow: hidden;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2) !important;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    display: flex;
    flex-direction: column;
    color: #ffffff !important;
}
''', css)

# Make sure all h3, h4, p inside property card are white
css += '''
.property-card h3, .property-card h4, .property-card p, .property-card span, .property-card div {
    color: #ffffff !important;
}
.property-card .price-row {
    background: rgba(0,0,0,0.2) !important;
    border-radius: var(--radius-md);
    padding: 12px;
    border: 1px solid rgba(255,255,255,0.1);
}
.property-card .val-amount {
    color: #ffffff !important;
    text-shadow: 0 2px 10px rgba(255,255,255,0.3);
}
.property-card .card-type-tag, .property-card .card-location-tag {
    background: rgba(0,0,0,0.5) !important;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.2);
}
'''

with open('code/frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed property-card glass styles.")
