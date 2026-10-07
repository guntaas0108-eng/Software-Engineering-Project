import re

with open('code/frontend/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Redesign the Marketplace Tab
old_marketplace = r'<section id="tab-marketplace" class="tab-pane active">.*?</section>'

new_marketplace = '''
        <section id="tab-marketplace" class="tab-pane active">
            
            <!-- GORGEOUS FULL-BLEED REAL ESTATE HERO -->
            <div class="real-estate-hero">
                <div class="hero-bg-image" style="background-image: url('https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=2000&q=80');"></div>
                <div class="hero-gradient-overlay"></div>
                
                <div class="hero-content-wrapper">
                    <span class="hero-badge">EstatePulse AI</span>
                    <h1 class="hero-title">Find your perfect place.</h1>
                    <p class="hero-subtitle">Experience AI-powered valuations, transparent pricing, and instant seller negotiations.</p>
                    
                    <!-- Floating Search Box (Zillow Style) -->
                    <div class="floating-search-bar">
                        <div class="search-inputs-row">
                            <div class="search-input-group flex-2">
                                <label>Location or Keyword</label>
                                <input type="text" id="search-input" placeholder="Search by locality, title..." class="minimal-input" oninput="triggerLiveSearch()">
                            </div>
                            <div class="search-divider"></div>
                            <div class="search-input-group">
                                <label>City</label>
                                <select id="city-filter" class="minimal-input" onchange="loadProperties()">
                                    <option value="">All Cities</option>
                                    <option value="Bangalore">Bangalore</option>
                                    <option value="Chandigarh">Chandigarh</option>
                                    <option value="Patiala">Patiala</option>
                                </select>
                            </div>
                            <div class="search-divider"></div>
                            <div class="search-input-group">
                                <label>Category</label>
                                <select id="category-filter" class="minimal-input" onchange="loadProperties()">
                                    <option value="">All Types</option>
                                    <option value="Apartment">Apartment</option>
                                    <option value="House">House</option>
                                    <option value="Commercial">Commercial</option>
                                </select>
                            </div>
                        </div>
                        <div class="search-action-row">
                            <select id="barometer-filter" class="minimal-input barometer-select" onchange="loadProperties()">
                                <option value="">AI Rating: Any</option>
                                <option value="good">Great Deals (< Market)</option>
                                <option value="fair">Fair Market Value</option>
                            </select>
                            <button class="btn btn-primary search-submit-btn" onclick="loadProperties()">Search Properties</button>
                            <button class="btn btn-outline" style="border:none;" onclick="resetFilters()">Reset</button>
                        </div>
                    </div>
                </div>
            </div>

            <div class="marketplace-body">
                <div class="section-header" style="margin-top: 2rem;">
                    <h2>Curated Listings</h2>
                    <div class="legend" style="gap: 15px;">
                        <span class="legend-chip" style="background: rgba(16,185,129,0.1); color: #059669; border: 1px solid #10b981;"><span class="dot" style="background:#10b981;"></span> Great Deal</span>
                        <span class="legend-chip" style="background: rgba(59,130,246,0.1); color: #2563eb; border: 1px solid #3b82f6;"><span class="dot" style="background:#3b82f6;"></span> Fair Value</span>
                    </div>
                </div>
                
                <div class="property-grid" id="properties-grid">
                    <!-- Loaded dynamically -->
                </div>
            </div>
        </section>
'''

# Replace it using regex
html = re.sub(old_marketplace, new_marketplace.strip(), html, flags=re.DOTALL)

with open('code/frontend/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML Structure updated with Hero Image.")
