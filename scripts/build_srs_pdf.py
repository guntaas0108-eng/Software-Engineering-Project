import os
import base64
import subprocess
import shutil

def load_image_b64(rel_path):
    ext = rel_path.split('.')[-1].lower()
    mime = 'image/png' if ext == 'png' else 'image/jpeg'
    with open(rel_path, 'rb') as f:
        data = base64.b64encode(f.read()).decode('utf-8')
    return f'data:{mime};base64,{data}'

fig_buyer_act = load_image_b64('docs/images/fig_page_6_1.png')
fig_seller_act = load_image_b64('docs/images/fig_page_7_1.jpeg')
fig_usecase = load_image_b64('docs/images/fig_page_8_1.jpeg')
fig_class = load_image_b64('docs/images/fig_page_9_1.png')
fig_seq_seller = load_image_b64('docs/images/fig_page_10_1.png')
fig_seq_buyer = load_image_b64('docs/images/fig_page_11_1.jpeg')

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Software Requirements Specification - PropertyPulse</title>
<style>
    @page {{
        size: A4;
        margin: 20mm 20mm 20mm 20mm;
    }}
    
    body {{
        font-family: "Times New Roman", Times, "Latin Modern Roman", Georgia, serif;
        font-size: 11pt;
        line-height: 1.5;
        color: #111;
        margin: 0;
        padding: 0;
    }}

    .page {{
        page-break-after: always;
        position: relative;
        min-height: 240mm;
        box-sizing: border-box;
    }}
    .page:last-of-type {{
        page-break-after: avoid;
    }}

    .page-header {{
        position: absolute;
        top: -12mm;
        left: 0;
        right: 0;
        display: flex;
        justify-content: space-between;
        font-size: 9.5pt;
        color: #444;
        border-bottom: 0.5pt solid #aaa;
        padding-bottom: 2mm;
    }}

    .page-footer {{
        position: absolute;
        bottom: 2mm;
        left: 0;
        right: 0;
        text-align: center;
        font-size: 10pt;
        color: #222;
    }}

    /* Title Page */
    .title-page {{
        text-align: center;
        padding-top: 5mm;
        height: 245mm;
        box-sizing: border-box;
    }}
    .title-header-left {{
        text-align: left;
        font-size: 11pt;
        font-weight: bold;
        margin-bottom: 18mm;
        color: #000;
    }}
    .course-title {{
        font-size: 14pt;
        font-weight: bold;
        letter-spacing: 0.5px;
        margin-bottom: 16mm;
    }}
    .project-name {{
        font-size: 24pt;
        font-weight: bold;
        letter-spacing: 1px;
        margin-bottom: 3mm;
    }}
    .project-tagline {{
        font-size: 12pt;
        font-style: italic;
        margin-bottom: 8mm;
    }}
    .doc-type {{
        font-size: 13pt;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        border-top: 1.5pt solid #000;
        border-bottom: 1.5pt solid #000;
        display: inline-block;
        padding: 2.5mm 8mm;
        margin-bottom: 16mm;
    }}
    .authors-block {{
        font-size: 11pt;
        line-height: 1.5;
        margin-bottom: 16mm;
    }}
    .authors-block strong {{
        display: block;
        font-size: 12pt;
        margin-bottom: 2mm;
    }}
    .submission-block {{
        font-size: 11pt;
        line-height: 1.4;
    }}
    .submission-block strong {{
        font-size: 12pt;
    }}

    /* Typography */
    h1 {{
        font-size: 18pt;
        font-weight: bold;
        margin-top: 0;
        margin-bottom: 6mm;
        border-bottom: 1pt solid #333;
        padding-bottom: 2mm;
    }}
    h2 {{
        font-size: 13pt;
        font-weight: bold;
        margin-top: 6mm;
        margin-bottom: 3mm;
    }}
    h3 {{
        font-size: 11.5pt;
        font-weight: bold;
        margin-top: 4mm;
        margin-bottom: 2mm;
    }}
    p {{
        text-align: justify;
        text-justify: inter-word;
        margin-top: 0;
        margin-bottom: 3.5mm;
    }}
    ul, ol {{
        margin-top: 0;
        margin-bottom: 3.5mm;
        padding-left: 6mm;
    }}
    li {{
        margin-bottom: 1.5mm;
        text-align: justify;
    }}
    .page-tight h2 {{
        margin-top: 4mm;
        margin-bottom: 2mm;
    }}
    .page-tight p {{
        margin-bottom: 2mm;
    }}
    .page-tight ul {{
        margin-bottom: 2.5mm;
    }}
    .page-tight li {{
        margin-bottom: 1mm;
    }}
    .page-tight .math-block {{
        margin: 2.5mm 0;
    }}

    /* Table of Contents */
    .toc-item {{
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        margin-bottom: 2mm;
        font-size: 10.5pt;
    }}
    .toc-title {{
        flex: 1;
        overflow: hidden;
        white-space: nowrap;
    }}
    .toc-title::after {{
        content: " ........................................................................................................................................................................................";
        color: #777;
    }}
    .toc-page {{
        padding-left: 2mm;
        font-weight: bold;
    }}
    .toc-h1 {{
        font-weight: bold;
        font-size: 11pt;
        margin-top: 3mm;
    }}
    .toc-h2 {{
        padding-left: 5mm;
    }}

    /* Diagrams */
    .figure-box {{
        text-align: center;
        margin: 6mm 0;
        page-break-inside: avoid;
    }}
    .figure-box img {{
        max-width: 90%;
        max-height: 180mm;
        border: 0.5pt solid #ddd;
        border-radius: 2px;
    }}
    .figure-caption {{
        font-size: 10pt;
        font-style: italic;
        margin-top: 2.5mm;
        color: #222;
    }}

    /* Tables */
    table {{
        width: 100%;
        border-collapse: collapse;
        margin: 4mm 0;
        font-size: 10pt;
        page-break-inside: avoid;
    }}
    th, td {{
        border: 0.5pt solid #333;
        padding: 2.5mm 3mm;
        text-align: left;
    }}
    th {{
        background-color: #f2f2f2;
        font-weight: bold;
    }}

    /* Math formulas */
    .math-block {{
        text-align: center;
        font-family: "Latin Modern Math", "Cambria Math", "Times New Roman", serif;
        font-style: italic;
        margin: 3.5mm 0;
        font-size: 11.5pt;
    }}

    .svg-diagram {{
        max-width: 95%;
        margin: 0 auto;
        display: block;
    }}
</style>
</head>
<body>

<!-- ========================================================= -->
<!-- COVER PAGE                                                -->
<!-- ========================================================= -->
<div class="page title-page">
    <div class="title-header-left">UCS503- Project Report</div>
    
    <div class="course-title">UCS 503 – SOFTWARE ENGINEERING</div>

    <div class="project-name">PROPERTY PULSE</div>
    <div class="project-tagline">Real Estate Platform with ML Price Predictor</div>
    <div class="doc-type">Software Requirements Specification (SRS)</div>

    <div class="authors-block">
        <strong>Submitted by:</strong>
        1024030108 &nbsp; Guntaas Singh<br>
        1024030112 &nbsp; Haneesh<br>
        1024030538 &nbsp; Dhruv Rajput<br>
        102303133 &nbsp; Atiksh Gupta<br><br>
        Group: 3C14, BE Third Year, COE
    </div>

    <div class="submission-block">
        <strong>Submitted to:</strong><br>
        Ms. Anushka<br><br>
        Computer Science and Engineering Department<br>
        Thapar Institute of Engineering and Technology<br><br>
        October 2026
    </div>
</div>

<!-- ========================================================= -->
<!-- TABLE OF CONTENTS                                         -->
<!-- ========================================================= -->
<div class="page">
    <div class="page-header">
        <span>UCS503- Project Report</span>
        <span>Software Requirements Specification</span>
    </div>

    <h1>Contents</h1>

    <div class="toc-item toc-h1">
        <span class="toc-title">1 &nbsp; Introduction</span>
        <span class="toc-page">3</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">1.1 &nbsp; Purpose</span>
        <span class="toc-page">3</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">1.2 &nbsp; Intended Audience and Reading Suggestions</span>
        <span class="toc-page">3</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">1.3 &nbsp; Project Scope</span>
        <span class="toc-page">3</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">Figure 1.1: Entire Work-flow</span>
        <span class="toc-page">4</span>
    </div>

    <div class="toc-item toc-h1">
        <span class="toc-title">2 &nbsp; Overall Description</span>
        <span class="toc-page">5</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">2.1 &nbsp; Product Perspective</span>
        <span class="toc-page">5</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">2.2 &nbsp; User Classes and Characteristics</span>
        <span class="toc-page">5</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">Figure 2.1: Type of Users</span>
        <span class="toc-page">5</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">2.3 &nbsp; Product Functions</span>
        <span class="toc-page">6</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">2.4 &nbsp; Operating Environment</span>
        <span class="toc-page">6</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">2.5 &nbsp; Design Activities and Architectural Models</span>
        <span class="toc-page">7</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">Figure 2.2: Activity Diagram &mdash; Buyer Lifecycle</span>
        <span class="toc-page">7</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">Figure 2.3: Activity Diagram &mdash; Seller Lifecycle</span>
        <span class="toc-page">8</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">Figure 2.4: System Use Case Diagram</span>
        <span class="toc-page">9</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">Figure 2.5: Class Diagram &amp; Relational Schema</span>
        <span class="toc-page">10</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">Figure 2.6: Sequence Diagram &mdash; Seller Submission</span>
        <span class="toc-page">11</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">Figure 2.7: Sequence Diagram &mdash; Buyer Browsing &amp; Save</span>
        <span class="toc-page">12</span>
    </div>

    <div class="toc-item toc-h1">
        <span class="toc-title">3 &nbsp; System Features</span>
        <span class="toc-page">13</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">3.1 &nbsp; Description and Priority</span>
        <span class="toc-page">13</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">3.2 &nbsp; Functional Requirements (Module Breakdown)</span>
        <span class="toc-page">13</span>
    </div>

    <div class="toc-item toc-h1">
        <span class="toc-title">4 &nbsp; Other Nonfunctional Requirements</span>
        <span class="toc-page">14</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">4.1 &nbsp; Performance Requirements</span>
        <span class="toc-page">14</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">4.2 &nbsp; Security Requirements</span>
        <span class="toc-page">14</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">4.3 &nbsp; Software Quality Attributes</span>
        <span class="toc-page">14</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">4.4 &nbsp; Business Rules &amp; Evaluation Metrics</span>
        <span class="toc-page">14</span>
    </div>

    <div class="toc-item toc-h1">
        <span class="toc-title">5 &nbsp; Other Requirements</span>
        <span class="toc-page">15</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">5.1 &nbsp; Operational Constraints</span>
        <span class="toc-page">15</span>
    </div>
    <div class="toc-item toc-h2">
        <span class="toc-title">5.2 &nbsp; Future System Evolution</span>
        <span class="toc-page">15</span>
    </div>

    <div class="page-footer">2</div>
</div>

<!-- ========================================================= -->
<!-- CHAPTER 1: INTRODUCTION                                   -->
<!-- ========================================================= -->
<div class="page">
    <div class="page-header">
        <span>UCS503- Project Report</span>
        <span>Chapter 1 &nbsp; Introduction</span>
    </div>

    <h1>1 &nbsp; Introduction</h1>

    <h2>1.1 &nbsp; Purpose</h2>
    <p>
        The real estate market currently struggles with fragmented, unverified property listings, opaque pricing mechanisms, and slow buyer-seller transaction coordination. Buyers cannot easily determine whether an asking price reflects authentic market valuation, while sellers suffer from duplicate listings and lack of transparent price guidance. 
    </p>
    <p>
        <strong>PROPERTY PULSE</strong> (also referred to as <em>EstatePulse</em>) is an integrated, web-based real estate platform developed to eliminate market asymmetry. By embedding a Machine Learning pricing model directly into the property listing lifecycle and introducing an automated <strong>Buyer Barometer</strong>, the software empowers both buyers and sellers with objective pricing benchmarks, spam prevention, and a streamlined negotiation workflow.
    </p>

    <h2>1.2 &nbsp; Intended Audience and Reading Suggestions</h2>
    <p>
        This Software Requirements Specification (SRS) is prepared for course evaluators (Ms. Anushka), software architects, developers, testers, and project managers.
    </p>
    <ul>
        <li><strong>Academic Evaluators:</strong> Review Chapter 1 (Objectives), Chapter 3 (Functional Specifications), and Chapter 4 (Empirical Evaluation Metrics).</li>
        <li><strong>Development Team:</strong> Refer to Chapter 2 (System Architecture, Activity &amp; Sequence Diagrams) and Chapter 3 (API Module specifications).</li>
        <li><strong>Quality Assurance Engineers:</strong> Validate against Section 4 (Performance, Security, and Non-functional Quality Attributes).</li>
    </ul>

    <h2>1.3 &nbsp; Project Scope</h2>
    <p>
        Property Pulse establishes a comprehensive, end-to-end digital transaction ecosystem for three core user groups: <strong>General Users</strong>, <strong>Buyers</strong>, and <strong>Sellers</strong>.
    </p>
    <p>
        When a seller submits a property listing with physical dimensions, age, city, and furnishing attributes, an automated ML Price Predictor computes an instant estimated fair market price ($\hat{{y}}$). Simultaneously, a dedicated Duplicate Checker queries the database to flag potential duplicate listings before insertion. 
    </p>
    <p>
        Buyers explore curated listings guided by the <strong>Buyer Barometer</strong>&mdash;a visual indicator classifying properties into <em>Great Deal</em>, <em>Fair Market Price</em>, or <em>Premium</em> based on mathematical variance between asking prices and model predictions. Interested buyers can negotiate terms via an in-app WhatsApp-style chat and schedule site visits by paying a nominal booking token fee through an integrated checkout modal.
    </p>
    <p>
        The platform instruments and measures empirical software engineering metrics, most notably <strong>Time-to-Appointment</strong> ($T_{{appt}} = t_{{confirmed}} - t_{{inquiry}}$), aiming for a median duration $\le 2$ hours during pilot operations.
    </p>

    <div class="page-footer">3</div>
</div>

<!-- ========================================================= -->
<!-- WORKFLOW DIAGRAM PAGE                                     -->
<!-- ========================================================= -->
<div class="page">
    <div class="page-header">
        <span>UCS503- Project Report</span>
        <span>Chapter 1 &nbsp; Introduction</span>
    </div>

    <h2>1.4 &nbsp; System Work-flow Overview</h2>
    <p>
        Figure 1.1 illustrates the high-level workflow of the PropertyPulse platform, showing the continuous interaction cycle between Buyers, Sellers, the Machine Learning service, and the System Evaluation Engine.
    </p>

    <div class="figure-box">
        <svg class="svg-diagram" viewBox="0 0 650 420" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 0 L 10 5 L 0 10 z" fill="#333" />
                </marker>
            </defs>
            <!-- Nodes -->
            <rect x="220" y="20" width="210" height="45" rx="8" fill="#e8f0fe" stroke="#1a73e8" stroke-width="1.5"/>
            <text x="325" y="47" font-family="Times New Roman" font-size="14" font-weight="bold" text-anchor="middle" fill="#1a73e8">Seller (Submits Listing)</text>

            <rect x="220" y="105" width="210" height="45" rx="8" fill="#fef7e0" stroke="#f9ab00" stroke-width="1.5"/>
            <text x="325" y="132" font-family="Times New Roman" font-size="14" font-weight="bold" text-anchor="middle" fill="#b06000">ML Predictor &amp; DupCheck</text>

            <rect x="220" y="190" width="210" height="45" rx="8" fill="#e6f4ea" stroke="#137333" stroke-width="1.5"/>
            <text x="325" y="217" font-family="Times New Roman" font-size="14" font-weight="bold" text-anchor="middle" fill="#137333">Marketplace &amp; Barometer</text>

            <rect x="220" y="275" width="210" height="45" rx="8" fill="#fce8e6" stroke="#c5221f" stroke-width="1.5"/>
            <text x="325" y="302" font-family="Times New Roman" font-size="14" font-weight="bold" text-anchor="middle" fill="#c5221f">Buyer (Inquiry &amp; Chat)</text>

            <rect x="220" y="360" width="210" height="45" rx="8" fill="#f3e8fd" stroke="#9334e6" stroke-width="1.5"/>
            <text x="325" y="387" font-family="Times New Roman" font-size="14" font-weight="bold" text-anchor="middle" fill="#7627bb">Site Visit &amp; Token Payment</text>

            <!-- Connectors -->
            <line x1="325" y1="65" x2="325" y2="105" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
            <text x="335" y="90" font-family="Times New Roman" font-size="11" fill="#555">Validates &amp; Predicts</text>

            <line x1="325" y1="150" x2="325" y2="190" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
            <text x="335" y="175" font-family="Times New Roman" font-size="11" fill="#555">Publishes Listing</text>

            <line x1="325" y1="235" x2="325" y2="275" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
            <text x="335" y="260" font-family="Times New Roman" font-size="11" fill="#555">Discovers &amp; Evaluates</text>

            <line x1="325" y1="320" x2="325" y2="360" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
            <text x="335" y="345" font-family="Times New Roman" font-size="11" fill="#555">Schedules Appointment</text>

            <!-- Feedback loop -->
            <path d="M 430 382 C 550 382, 550 42, 430 42" fill="none" stroke="#666" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#arrow)"/>
            <text x="560" y="215" font-family="Times New Roman" font-size="11" font-style="italic" fill="#666" transform="rotate(90 560 215)">Seller Confirms &amp; Logs T_appt</text>
        </svg>
        <div class="figure-caption">Figure 1.1: Entire System Work-flow</div>
    </div>

    <p>
        Every entity is interdependent. The seller's listing initiates the cycle; the machine learning service injects objective market context; the buyer makes data-driven negotiation decisions; and the evaluation engine tracks duration until confirmed physical inspection.
    </p>

    <div class="page-footer">4</div>
</div>

<!-- ========================================================= -->
<!-- CHAPTER 2: OVERALL DESCRIPTION                            -->
<!-- ========================================================= -->
<div class="page">
    <div class="page-header">
        <span>UCS503- Project Report</span>
        <span>Chapter 2 &nbsp; Overall Description</span>
    </div>

    <h1>2 &nbsp; Overall Description</h1>

    <h2>2.1 &nbsp; Product Perspective</h2>
    <p>
        PropertyPulse is an independent, 3-tier web platform engineered to replace manual and fragmented real estate ad postings. The data is centrally managed within an ACID-compliant relational schema, decoupling the client-side presentation layer from the predictive intelligence backend.
    </p>

    <h2>2.2 &nbsp; User Classes and Characteristics</h2>
    <p>
        The system identifies four primary user classes with defined permissions:
    </p>
    <ul>
        <li><strong>General User / Guest:</strong> Unauthenticated visitor browsing listings with full search and Buyer Barometer visibility.</li>
        <li><strong>Buyer:</strong> Authenticated buyer capable of sending messages, saving properties, and booking site visit appointments.</li>
        <li><strong>Seller:</strong> Authenticated owner/broker with permissions to list properties, receive instant ML valuations, review duplicate alerts, chat with leads, and confirm visits.</li>
        <li><strong>Evaluator / Admin:</strong> Course instructor or system administrator auditing regression diagnostics ($R^2$, MSE) and Time-to-Appointment metrics.</li>
    </ul>

    <div class="figure-box">
        <svg class="svg-diagram" viewBox="0 0 500 160" xmlns="http://www.w3.org/2000/svg">
            <rect x="180" y="10" width="140" height="35" rx="5" fill="#f1f3f4" stroke="#5f6368" stroke-width="1.5"/>
            <text x="250" y="32" font-family="Times New Roman" font-size="13" font-weight="bold" text-anchor="middle">Platform Users</text>

            <line x1="250" y1="45" x2="250" y2="70" stroke="#5f6368" stroke-width="1.5"/>
            <line x1="80" y1="70" x2="420" y2="70" stroke="#5f6368" stroke-width="1.5"/>

            <line x1="80" y1="70" x2="80" y2="95" stroke="#5f6368" stroke-width="1.5"/>
            <line x1="190" y1="70" x2="190" y2="95" stroke="#5f6368" stroke-width="1.5"/>
            <line x1="310" y1="70" x2="310" y2="95" stroke="#5f6368" stroke-width="1.5"/>
            <line x1="420" y1="70" x2="420" y2="95" stroke="#5f6368" stroke-width="1.5"/>

            <rect x="25" y="95" width="110" height="32" rx="4" fill="#e8f0fe" stroke="#1a73e8" stroke-width="1.2"/>
            <text x="80" y="115" font-family="Times New Roman" font-size="11.5" text-anchor="middle" fill="#1a73e8">General User</text>

            <rect x="145" y="95" width="90" height="32" rx="4" fill="#e6f4ea" stroke="#137333" stroke-width="1.2"/>
            <text x="190" y="115" font-family="Times New Roman" font-size="11.5" text-anchor="middle" fill="#137333">Buyer</text>

            <rect x="265" y="95" width="90" height="32" rx="4" fill="#fef7e0" stroke="#b06000" stroke-width="1.2"/>
            <text x="310" y="115" font-family="Times New Roman" font-size="11.5" text-anchor="middle" fill="#b06000">Seller</text>

            <rect x="370" y="95" width="100" height="32" rx="4" fill="#fce8e6" stroke="#c5221f" stroke-width="1.2"/>
            <text x="420" y="115" font-family="Times New Roman" font-size="11.5" text-anchor="middle" fill="#c5221f">Evaluator/Admin</text>
        </svg>
        <div class="figure-caption">Figure 2.1: Type of Users</div>
    </div>

    <h2>2.3 &nbsp; Product Functions</h2>
    <p>
        The core product functions encompass:
    </p>
    <ol>
        <li><strong>Automated Valuation Engine:</strong> Instant Multiple Linear Regression price estimation based on physical square footage, room counts, locality, age, and furnishing status.</li>
        <li><strong>Buyer Barometer Visualization:</strong> Real-time variance calculation labeling properties as <em>Great Deal</em>, <em>Fair Market Price</em>, or <em>Premium</em>.</li>
        <li><strong>Duplicate Listing Prevention:</strong> Lexical and structural candidate matching scanning existing database records.</li>
        <li><strong>Property-Isolated Negotiation Chat:</strong> Dedicated messaging threads eliminating fragmented communication.</li>
        <li><strong>Site Visit Scheduling &amp; Escrow Token:</strong> Booking slot reservations accompanied by digital token fee settlements.</li>
        <li><strong>Diagnostics Console:</strong> Empirical reporting of Time-to-Appointment metrics and regression errors ($R^2$, MSE, RMSE).</li>
    </ol>

    <h2>2.4 &nbsp; Operating Environment</h2>
    <p>
        The software operates in any standard computing environment:
    </p>
    <ul>
        <li><strong>Operating System:</strong> Windows 10/11, Ubuntu Linux 20.04+, macOS.</li>
        <li><strong>Runtime Stack:</strong> Python 3.10+ (Flask 3.x, Scikit-learn 1.4+, NumPy, SQLite3).</li>
        <li><strong>Client Web Browsers:</strong> Google Chrome, Mozilla Firefox, Apple Safari, Microsoft Edge, and modern mobile browsers.</li>
    </ul>

    <div class="page-footer">5</div>
</div>

<!-- ========================================================= -->
<!-- ACTIVITY DIAGRAM: BUYER                                   -->
<!-- ========================================================= -->
<div class="page">
    <div class="page-header">
        <span>UCS503- Project Report</span>
        <span>Chapter 2 &nbsp; Methodology and Design</span>
    </div>

    <h2>2.5 &nbsp; Design Activities and Architectural Models</h2>
    <h3>2.5.1 &nbsp; Buyer Lifecycle Activity Diagram</h3>
    <p>
        Figure 2.2 details the workflow from a prospective buyer's perspective. The buyer initiates search and filter operations, inspects property details and the visual Buyer Barometer, saves the property or initiates real-time negotiation chat, and schedules a site visit via payment token checkout.
    </p>

    <div class="figure-box">
        <img src="{fig_buyer_act}" alt="Buyer Activity Diagram">
        <div class="figure-caption">Figure 2.2: Activity Diagram &mdash; Buyer Lifecycle (Search, Save, Chat, and Site Visit Booking)</div>
    </div>

    <div class="page-footer">6</div>
</div>

<!-- ========================================================= -->
<!-- ACTIVITY DIAGRAM: SELLER                                  -->
<!-- ========================================================= -->
<div class="page">
    <div class="page-header">
        <span>UCS503- Project Report</span>
        <span>Chapter 2 &nbsp; Methodology and Design</span>
    </div>

    <h3>2.5.2 &nbsp; Seller Lifecycle Activity Diagram with ML Validation</h3>
    <p>
        Figure 2.3 depicts the seller's workflow. When a seller enters listing specifications, the system triggers the ML PricePredictor and DuplicateChecker before saving the listing. Upon receiving buyer inquiries, the seller negotiates and confirms the appointment slot, logging the confirmed timestamp.
    </p>

    <div class="figure-box">
        <img src="{fig_seller_act}" alt="Seller Activity Diagram">
        <div class="figure-caption">Figure 2.3: Activity Diagram &mdash; Seller Lifecycle with ML Price Prediction and Duplicate Check</div>
    </div>

    <div class="page-footer">7</div>
</div>

<!-- ========================================================= -->
<!-- USE CASE DIAGRAM                                          -->
<!-- ========================================================= -->
<div class="page">
    <div class="page-header">
        <span>UCS503- Project Report</span>
        <span>Chapter 2 &nbsp; Methodology and Design</span>
    </div>

    <h3>2.5.3 &nbsp; System UML Use Case Diagram</h3>
    <p>
        Figure 2.4 specifies the functional interactions across all system actors: General User, Buyer, Seller, and the External Payment Gateway. Core use cases incorporate &laquo;include&raquo; dependencies for price prediction, duplicate checking, and payment confirmation.
    </p>

    <div class="figure-box">
        <img src="{fig_usecase}" alt="System Use Case Diagram">
        <div class="figure-caption">Figure 2.4: System Use Case Diagram across General Users, Buyers, Sellers, and Payment Gateway</div>
    </div>

    <div class="page-footer">8</div>
</div>

<!-- ========================================================= -->
<!-- CLASS DIAGRAM                                             -->
<!-- ========================================================= -->
<div class="page">
    <div class="page-header">
        <span>UCS503- Project Report</span>
        <span>Chapter 2 &nbsp; Methodology and Design</span>
    </div>

    <h3>2.5.4 &nbsp; UML Class Diagram and Relational Schema</h3>
    <p>
        Figure 2.5 defines the domain model and database architecture. Primary entities include <code>User</code>, <code>Property</code>, <code>SavedProperty</code>, <code>PropertyImage</code>, <code>Message</code>, <code>Appointment</code>, and <code>Payment</code>, with service delegation to <code>PricePredictor</code>.
    </p>

    <div class="figure-box">
        <img src="{fig_class}" alt="UML Class Diagram">
        <div class="figure-caption">Figure 2.5: UML Class Diagram &amp; Entity Relationships</div>
    </div>

    <div class="page-footer">9</div>
</div>

<!-- ========================================================= -->
<!-- SEQUENCE DIAGRAM: SELLER                                  -->
<!-- ========================================================= -->
<div class="page">
    <div class="page-header">
        <span>UCS503- Project Report</span>
        <span>Chapter 2 &nbsp; Methodology and Design</span>
    </div>

    <h3>2.5.5 &nbsp; Sequence Diagram &mdash; Seller Listing &amp; ML Valuation</h3>
    <p>
        Figure 2.6 illustrates the chronological message exchange during property submission. The controller delegates feature vectors to the ML PricePredictor and verifies candidate duplicates prior to persistence.
    </p>

    <div class="figure-box">
        <img src="{fig_seq_seller}" alt="Seller Sequence Diagram">
        <div class="figure-caption">Figure 2.6: Sequence Diagram &mdash; Seller Listing Submission, ML Valuation, and Duplicate Check</div>
    </div>

    <div class="page-footer">10</div>
</div>

<!-- ========================================================= -->
<!-- SEQUENCE DIAGRAM: BUYER                                   -->
<!-- ========================================================= -->
<div class="page">
    <div class="page-header">
        <span>UCS503- Project Report</span>
        <span>Chapter 2 &nbsp; Methodology and Design</span>
    </div>

    <h3>2.5.6 &nbsp; Sequence Diagram &mdash; Buyer Browsing &amp; Save</h3>
    <p>
        Figure 2.7 shows the sequence of interactions when a buyer queries active listings, filters by Barometer rating, and saves a selected property to their authenticated dashboard.
    </p>

    <div class="figure-box">
        <img src="{fig_seq_buyer}" alt="Buyer Sequence Diagram">
        <div class="figure-caption">Figure 2.7: Sequence Diagram &mdash; Buyer Browsing, Filtering, and Property Save Operations</div>
    </div>

    <div class="page-footer">11</div>
</div>

<!-- ========================================================= -->
<!-- CHAPTER 3: SYSTEM FEATURES                                -->
<!-- ========================================================= -->
<div class="page">
    <div class="page-header">
        <span>UCS503- Project Report</span>
        <span>Chapter 3 &nbsp; System Features</span>
    </div>

    <h1>3 &nbsp; System Features</h1>

    <h2>3.1 &nbsp; Description and Priority</h2>
    <p>
        The functional features are prioritized into three operational tiers:
    </p>

    <table>
        <thead>
            <tr>
                <th>Priority</th>
                <th>Feature ID</th>
                <th>Feature Name</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>High (P1)</strong></td>
                <td>FEAT-01</td>
                <td>ML Price Predictor</td>
                <td>Computes fair market valuation using Multiple Linear Regression.</td>
            </tr>
            <tr>
                <td><strong>High (P1)</strong></td>
                <td>FEAT-02</td>
                <td>Duplicate Listing Checker</td>
                <td>Scans database on submission to flag matching listings in locality.</td>
            </tr>
            <tr>
                <td><strong>High (P1)</strong></td>
                <td>FEAT-03</td>
                <td>Buyer Barometer Visualizer</td>
                <td>Categorizes listings into Great Deal, Fair Value, or Premium.</td>
            </tr>
            <tr>
                <td><strong>High (P1)</strong></td>
                <td>FEAT-04</td>
                <td>Negotiation Chat Engine</td>
                <td>Property-isolated messaging threads between buyer and seller.</td>
            </tr>
            <tr>
                <td><strong>Medium (P2)</strong></td>
                <td>FEAT-05</td>
                <td>Appointment &amp; Token Payment</td>
                <td>Booking slot calendar and token payment transaction logging.</td>
            </tr>
            <tr>
                <td><strong>Medium (P2)</strong></td>
                <td>FEAT-06</td>
                <td>Role-Based Authentication</td>
                <td>Seamless phone login with isolated Buyer and Seller views.</td>
            </tr>
            <tr>
                <td><strong>Low (P3)</strong></td>
                <td>FEAT-07</td>
                <td>Diagnostics &amp; Attribution</td>
                <td>Live telemetry tracking Time-to-Appointment and model errors.</td>
            </tr>
        </tbody>
    </table>

    <h2>3.2 &nbsp; Functional Requirements (Module Breakdown)</h2>

    <h3>Module 1: Property Listing &amp; Duplicate Detection</h3>
    <ul>
        <li><strong>FR-1.1:</strong> The system shall accept property listings containing Title, Description, Category, City, Locality, Area (sq.ft), Bedrooms, Bathrooms, Age, Parking, Furnishing, and Asking Price.</li>
        <li><strong>FR-1.2:</strong> System shall validate positive numeric values for Area and Price.</li>
        <li><strong>FR-1.3:</strong> When title and locality are entered, the system shall invoke <code>POST /api/check-duplicates</code> to flag similar existing records.</li>
    </ul>

    <h3>Module 2: ML Price Prediction &amp; Buyer Barometer</h3>
    <ul>
        <li><strong>FR-2.1:</strong> The system shall invoke <code>POST /api/predict</code> upon specification entry and return estimated price ($\hat{{y}}$) within 100ms.</li>
        <li><strong>FR-2.2:</strong> Price deviation percentage shall be computed as $\Delta\% = ((P_{{ask}} - P_{{pred}}) / P_{{pred}}) \times 100$.</li>
        <li><strong>FR-2.3:</strong> Properties shall display color-coded badges: <em>Great Deal</em> ($\Delta\% \le -10\%$), <em>Fair Market Price</em> ($-10\% &lt; \Delta\% \le +10\%$), or <em>Premium</em> ($\Delta\% &gt; +10\%$).</li>
    </ul>

    <h3>Module 3: In-App Chat &amp; Site Visit Scheduling</h3>
    <ul>
        <li><strong>FR-3.1:</strong> Each property shall maintain a dedicated messaging thread identified by <code>property_id</code>.</li>
        <li><strong>FR-3.2:</strong> The receipt of the initial buyer message shall instantiate <code>first_inquiry_timestamp</code>.</li>
        <li><strong>FR-3.3:</strong> Buyers shall select visit dates and settle token fees via <code>POST /api/payments</code>.</li>
        <li><strong>FR-3.4:</strong> Seller confirmation via <code>POST /api/appointments/&lt;id&gt;/confirm</code> shall record <code>confirmed_timestamp</code> and calculate <code>time_to_appointment_seconds</code>.</li>
    </ul>

    <div class="page-footer">12</div>
</div>

<!-- ========================================================= -->
<!-- CHAPTER 4: NONFUNCTIONAL REQUIREMENTS                     -->
<!-- ========================================================= -->
<div class="page page-tight">
    <div class="page-header">
        <span>UCS503- Project Report</span>
        <span>Chapter 4 &nbsp; Other Nonfunctional Requirements</span>
    </div>

    <h1>4 &nbsp; Other Nonfunctional Requirements</h1>

    <h2>4.1 &nbsp; Performance Requirements</h2>
    <ul>
        <li><strong>ML Inference Latency:</strong> Price estimation response time shall remain below 100 milliseconds.</li>
        <li><strong>Page Load Time:</strong> Client SPA shall render initial interactive view in &lt; 1.5 seconds.</li>
        <li><strong>Database Latency:</strong> Search queries filtering by city and category shall execute in &lt; 50 milliseconds.</li>
        <li><strong>Service Level Target:</strong> Median Time-to-Appointment shall not exceed 2 hours during pilot evaluation.</li>
    </ul>

    <h2>4.2 &nbsp; Security Requirements</h2>
    <ul>
        <li><strong>SQL Injection Prevention:</strong> All database transactions must strictly utilize parameterized SQL statements.</li>
        <li><strong>XSS Mitigation:</strong> All user inputs (descriptions, chat text) must be escaped before DOM injection.</li>
        <li><strong>Access Control:</strong> Sellers may only edit or delete properties registered to their verified phone numbers.</li>
    </ul>

    <h2>4.3 &nbsp; Software Quality Attributes</h2>
    <ul>
        <li><strong>Usability &amp; Mobile Responsiveness:</strong> Fluid CSS media queries ensuring full touch usability ($\ge 44 \times 44$ px) across mobile and desktop devices.</li>
        <li><strong>Reliability:</strong> Minimum 99% uptime during evaluation sessions; client network errors handled gracefully via toast notifications.</li>
        <li><strong>Maintainability:</strong> Clean 3-tier architectural separation between database (<code>database.py</code>), ML logic (<code>ml_model.py</code>), and API routing (<code>app.py</code>).</li>
    </ul>

    <h2>4.4 &nbsp; Business Rules &amp; Evaluation Metrics</h2>
    <p>
        The predictive valuation engine implements Multiple Linear Regression:
    </p>
    <div class="math-block">
        $$\hat{{y}} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n + \epsilon$$
    </div>
    <p>
        Model accuracy is evaluated using Mean Squared Error (MSE) and Coefficient of Determination ($R^2$):
    </p>
    <div class="math-block">
        $$MSE = \frac{{1}}{{n}} \sum_{{i=1}}^{{n}} (y_i - \hat{{y}}_i)^2 \qquad R^2 = 1 - \frac{{\sum (y_i - \hat{{y}}_i)^2}}{{\sum (y_i - \bar{{y}})^2}}$$
    </div>
    <p>
        The primary software engineering metric, <strong>Time-to-Appointment</strong>, is defined as:
    </p>
    <div class="math-block">
        $$T_{{appt}} = t_{{confirmed}} - t_{{first\_inquiry}}$$
    </div>

    <div class="page-footer">13</div>
</div>

<!-- ========================================================= -->
<!-- CHAPTER 5: OTHER REQUIREMENTS & SIGN OFF                  -->
<!-- ========================================================= -->
<div class="page">
    <div class="page-header">
        <span>UCS503- Project Report</span>
        <span>Chapter 5 &nbsp; Other Requirements</span>
    </div>

    <h1>5 &nbsp; Other Requirements</h1>

    <h2>5.1 &nbsp; Operational Constraints</h2>
    <ul>
        <li><strong>Zero Commercial Dependencies:</strong> System operates entirely on local open-source libraries (Scikit-learn, Flask, SQLite) with no paid API keys required.</li>
        <li><strong>Memory Footprint:</strong> Lightweight server footprint (&lt; 120 MB RAM during active ML inference) ensuring compatibility with low-spec lab environments.</li>
        <li><strong>Time-to-Value Delivery:</strong> Focus on robust engineering workflows, test automation, and measurable metrics rather than speculative algorithm research.</li>
    </ul>

    <h2>5.2 &nbsp; Future System Evolution</h2>
    <ul>
        <li><strong>WebSocket Integration:</strong> Replacing 3-second HTTP chat polling with bi-directional WebSockets (Flask-SocketIO) for instant message delivery.</li>
        <li><strong>Computer Vision Deduplication:</strong> Integrating convolutional neural network perceptual hashing (pHash) to detect duplicate property image uploads.</li>
        <li><strong>Cloud CI/CD Deployment:</strong> Automated GitHub Actions workflow deploying containers to cloud PaaS platforms.</li>
    </ul>

    <div class="page-footer">14</div>
</div>

</body>
</html>
'''

temp_html = 'docs/srs_printable.html'
with open(temp_html, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated {temp_html} ({len(html_content)} bytes).")

edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_exe):
    edge_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

abs_html = os.path.abspath(temp_html)
abs_pdf = os.path.abspath('docs/SRS.pdf')

cmd = [
    edge_exe,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--run-all-compositor-stages-before-draw",
    f"--print-to-pdf={abs_pdf}",
    f"file:///{abs_html}"
]

print("Compiling PDF using Edge headless...")
res = subprocess.run(cmd, capture_output=True, text=True)
print(f"Edge process exited with code {res.returncode}")

if os.path.exists(abs_pdf):
    size = os.path.getsize(abs_pdf)
    print(f"Successfully generated {abs_pdf} ({size} bytes).")
    shutil.copyfile(abs_pdf, 'SRS.pdf')
    print("Copied docs/SRS.pdf to root SRS.pdf.")
else:
    print("PDF generation failed.")
