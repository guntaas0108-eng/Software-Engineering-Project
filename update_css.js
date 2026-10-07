const fs = require('fs');
let css = fs.readFileSync('code/frontend/style.css', 'utf8');

// Replace root variables
const newRoot = :root {
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
};

css = css.replace(/:root\s*\{[^}]+\}/, newRoot);

// Specific targeted replacements
css = css.replace(/\.navbar\s*\{([^}]+)\}/, (match, p1) => {
    return '.navbar {' + p1.replace(/background:\s*#ffffff;/, 'background: rgba(15, 23, 42, 0.75); backdrop-filter: blur(12px);') + '}';
});

// Any background: #ffffff; -> background: var(--card-bg);  except when it's color: #ffffff
css = css.replace(/background(?:-color)?:\s*#ffffff;/g, 'background: var(--card-bg);');
css = css.replace(/background:\s*linear-gradient\(180deg, #f8fafc 0%, #ffffff 100%\);/g, 'background: linear-gradient(180deg, rgba(15,23,42,0.8) 0%, rgba(11,17,32,0.9) 100%);');

// Update inputs
css = css.replace(/border:\s*1px solid #cbd5e1;/g, 'border: 1px solid var(--border);');
css = css.replace(/color:\s*#0f172a;/g, 'color: var(--text-primary);');

// Table header
css = css.replace(/background:\s*#f1f5f9;/g, 'background: rgba(255,255,255,0.05);');

// Generic borders (if hardcoded)
css = css.replace(/border:\s*1px solid #e2e8f0/g, 'border: 1px solid var(--border)');
css = css.replace(/border-bottom:\s*1px solid #e2e8f0/g, 'border-bottom: 1px solid var(--border)');
css = css.replace(/border-top:\s*1px solid #e2e8f0/g, 'border-top: 1px solid var(--border)');

// Adding general glassmorphism styles to cards
css += 
.card, .bento-card, .filter-card, .valuation-card, .chat-wrapper, .modal-box, .auth-box {
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.05);
    box-shadow: var(--shadow-md);
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

/* Gradients for text and emphasis */
.hero-text h1 {
    background: linear-gradient(135deg, #a5b4fc, #818cf8, #6366f1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
;

fs.writeFileSync('code/frontend/style.css', css);
console.log("CSS Updated successfully.");
