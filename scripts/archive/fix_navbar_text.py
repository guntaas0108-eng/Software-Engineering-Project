with open('code/frontend/style.css', 'a', encoding='utf-8') as f:
    f.write('''

/* ========================================================= */
/* ?? ABSOLUTE FINAL MASTER OVERRIDES FOR NAVBAR VISIBILITY  */
/* ========================================================= */
.navbar {
    background: #FFFFFF !important;
    border-bottom: 2px solid #CBD5E1 !important;
}

.brand-title {
    color: #0F172A !important; /* Pure Dark Slate */
    text-shadow: none !important;
}

.nav-btn {
    color: #0F172A !important; /* Pure Dark Slate */
    background: #F1F5F9 !important;
    border: 1px solid #CBD5E1 !important;
    box-shadow: none !important;
}

.nav-btn:hover {
    background: #E2E8F0 !important;
    color: #000000 !important;
}

.nav-btn.active {
    background: #1D4ED8 !important; /* Royal Blue */
    color: #FFFFFF !important;
    border-color: #1D4ED8 !important;
}

.status-label {
    color: #0F172A !important;
    font-weight: 800 !important;
}

/* Fix ML Regression badge in screenshot */
.status-badge {
    color: #0F172A !important; /* Dark text instead of white */
    font-weight: 700 !important;
    border: 1px solid #10B981 !important;
}
''')

print("Master overrides for dark navbar text applied.")
