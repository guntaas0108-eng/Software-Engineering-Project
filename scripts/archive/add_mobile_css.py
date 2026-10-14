import re

with open('code/frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add a comprehensive mobile media query block
mobile_css = '''
/* ========================================================= */
/* ?? MOBILE RESPONSIVENESS OVERRIDES                        */
/* ========================================================= */
@media (max-width: 768px) {
    /* Base */
    body { font-size: 15px; }
    .main-content { padding: 1rem 0.5rem; }
    
    /* Typography */
    h1 { font-size: 2.2rem !important; line-height: 1.2; margin-bottom: 1rem; }
    h2 { font-size: 1.6rem !important; }
    
    /* Navbar Optimization for Touch */
    .nav-container {
        flex-direction: column;
        padding: 0.8rem;
        gap: 12px;
        align-items: stretch;
    }
    .brand { justify-content: center; margin-bottom: 5px; }
    .nav-tabs {
        width: 100%;
        overflow-x: auto;
        white-space: nowrap;
        justify-content: flex-start;
        padding-bottom: 10px;
        -webkit-overflow-scrolling: touch;
        gap: 8px;
    }
    .nav-btn {
        flex: 0 0 auto;
        font-size: 0.85rem;
        padding: 8px 12px;
    }
    .nav-status {
        width: 100%;
        justify-content: center;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 5px;
    }
    .nav-status button {
        flex: 1 1 45%;
        margin-left: 0 !important;
    }

    /* Filters (Marketplace) */
    .filter-card {
        display: flex !important;
        flex-direction: column !important;
        gap: 1rem !important;
        padding: 1.5rem !important;
    }
    .filter-group {
        width: 100%;
    }

    /* Grids & Cards */
    .property-grid, .bento-grid, .metrics-grid {
        grid-template-columns: 1fr !important;
        gap: 1.5rem;
    }
    .property-card {
        margin-bottom: 10px;
    }
    .card-img-wrapper {
        height: 220px;
    }

    /* Hero Banner */
    .hero-banner {
        padding: 2rem 1rem !important;
        text-align: center;
    }
    .hero-stats {
        display: flex;
        flex-direction: column;
        gap: 15px;
        margin-top: 2rem;
    }
    .h-stat-box {
        width: 100%;
    }

    /* Chat Layout */
    .chat-wrapper {
        display: flex !important;
        flex-direction: column !important;
        height: calc(100vh - 120px) !important;
    }
    .chat-sidebar {
        display: flex !important;
        flex-direction: row !important;
        overflow-x: auto;
        overflow-y: hidden;
        border-right: none !important;
        border-bottom: 1px solid rgba(255,255,255,0.1) !important;
        min-height: 110px;
        max-height: 110px !important;
        padding: 10px !important;
        gap: 10px;
    }
    .chat-channel-item {
        flex-direction: column;
        align-items: center;
        min-width: 120px;
        max-width: 120px;
        padding: 5px !important;
        text-align: center;
    }
    .channel-thumb {
        width: 40px;
        height: 40px;
        margin-bottom: 5px;
    }
    .channel-info { margin-left: 0 !important; }
    .channel-title { font-size: 0.8rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; width: 100%; }
    .channel-sub { font-size: 0.7rem; }
    
    .chat-main {
        flex: 1;
        display: flex;
        flex-direction: column;
        overflow: hidden;
    }

    /* Modals & Overlays */
    .auth-box, .modal-box {
        width: 95% !important;
        padding: 1.5rem !important;
        margin: 10px auto;
    }
    
    /* Table / Dashboard */
    .appointments-table, .metrics-table {
        display: block;
        overflow-x: auto;
        white-space: nowrap;
    }
}

/* Extra small devices */
@media (max-width: 400px) {
    h1 { font-size: 1.8rem !important; }
    .nav-status button {
        flex: 1 1 100%;
    }
}
'''

css += "\n" + mobile_css + "\n"

with open('code/frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Mobile CSS added.")
