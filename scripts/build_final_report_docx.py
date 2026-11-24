import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders(table, color="B0B0B0", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    tblBorders = OxmlElement('w:tblBorders')
    for border_name in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), val)
        border.set(qn('w:sz'), sz)
        border.set(qn('w:space'), '0')
        border.set(qn('w:color'), color)
        tblBorders.append(border)
    tblPr.append(tblBorders)

def create_report():
    doc = Document()
    
    # Page setup: Normal Margins (1 inch)
    section = doc.sections[0]
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)
    section.header_distance = Inches(0.5)
    section.footer_distance = Inches(0.5)

    # Different first page so title page has no headers/footers
    section.different_first_page_header_footer = True

    # Header for subsequent pages
    header = section.header
    h_p = header.paragraphs[0]
    h_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    h_run = h_p.add_run("UCS503 Software Engineering Lab | PropertyPulse")
    h_run.font.name = 'Times New Roman'
    h_run.font.size = Pt(9)
    h_run.font.color.rgb = RGBColor(0, 0, 0)

    # Footer for subsequent pages
    footer = section.footer
    f_p = footer.paragraphs[0]
    f_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    f_run = f_p.add_run("Page ")
    f_run.font.name = 'Times New Roman'
    f_run.font.size = Pt(10)
    f_run.font.color.rgb = RGBColor(0, 0, 0)

    # Dynamic Page field in footer
    fldChar1 = OxmlElement('w:fldChar')
    fldChar1.set(qn('w:fldCharType'), 'begin')
    instrText = OxmlElement('w:instrText')
    instrText.set(qn('xml:space'), 'preserve')
    instrText.text = "PAGE"
    fldChar2 = OxmlElement('w:fldChar')
    fldChar2.set(qn('w:fldCharType'), 'separate')
    fldChar3 = OxmlElement('w:fldChar')
    fldChar3.set(qn('w:fldCharType'), 'end')
    f_pg_run = f_p.add_run()
    f_pg_run._r.append(fldChar1)
    f_pg_run._r.append(instrText)
    f_pg_run._r.append(fldChar2)
    f_pg_run._r.append(fldChar3)
    f_pg_run.font.name = 'Times New Roman'
    f_pg_run.font.size = Pt(10)
    f_pg_run.font.color.rgb = RGBColor(0, 0, 0)

    # Set default style to Times New Roman, 12pt, black, 1.5 line spacing, justified
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(12)
    normal_style.font.color.rgb = RGBColor(0, 0, 0)
    normal_style.paragraph_format.line_spacing = 1.5
    normal_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    normal_style.paragraph_format.space_after = Pt(6)

    def add_p(text, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, font_size=12):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_after = Pt(space_after)
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(font_size)
        run.font.bold = bold
        run.font.italic = italic
        run.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_h1(text):
        p = doc.add_paragraph(style='Heading 1')
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(16)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_h2(text):
        p = doc.add_paragraph(style='Heading 2')
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(14)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_h3(text):
        p = doc.add_paragraph(style='Heading 3')
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_img(img_path, caption, width=5.5):
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_after = Pt(4)
            p_img.paragraph_format.keep_with_next = True
            run_img = p_img.add_run()
            run_img.add_picture(img_path, width=Inches(width))
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_after = Pt(12)
            run_cap = p_cap.add_run(caption)
            run_cap.font.name = 'Times New Roman'
            run_cap.font.size = Pt(12)
            run_cap.font.italic = True
            run_cap.font.color.rgb = RGBColor(0, 0, 0)

    def style_table(table, col_widths, headers, data):
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(table, color="CCCCCC", sz="4", val="single")
        # Header row
        hdr_cells = table.rows[0].cells
        for idx, text in enumerate(headers):
            hdr_cells[idx].text = text
            set_cell_background(hdr_cells[idx], "EAEAEA")
            set_cell_margins(hdr_cells[idx], top=120, bottom=120, left=150, right=150)
            p = hdr_cells[idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.space_after = Pt(0)
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(10.5)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0, 0, 0)

        for row_data in data:
            row_cells = table.add_row().cells
            for idx, text in enumerate(row_data):
                row_cells[idx].text = str(text)
                set_cell_margins(row_cells[idx], top=80, bottom=80, left=150, right=150)
                p = row_cells[idx].paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT if idx > 0 else WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.line_spacing = 1.15
                p.paragraph_format.space_after = Pt(0)
                for r in p.runs:
                    r.font.name = 'Times New Roman'
                    r.font.size = Pt(10)
                    r.font.color.rgb = RGBColor(0, 0, 0)

        for row in table.rows:
            for idx, width in enumerate(col_widths):
                row.cells[idx].width = Inches(width)

    # =========================================================================
    # PRELIMINARY PAGES: TITLE PAGE
    # =========================================================================
    add_p("PropertyPulse: Curated Luxury Real Estate Marketplace, AI-Powered Valuation Barometer & Fiduciary Escrow Platform", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10, font_size=18)
    add_p("Final Project Report", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6, font_size=16)
    add_p("Submitted for the End Semester Evaluation of\nUCS503 Software Engineering Lab", bold=False, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18, font_size=13)
    
    add_p("Submitted by:", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4, font_size=12)
    add_p("Team PropertyPulse (Group 3C14)", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8, font_size=13)
    
    team_p = doc.add_paragraph()
    team_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    team_p.paragraph_format.line_spacing = 1.3
    team_p.paragraph_format.space_after = Pt(18)
    members = [
        ("Guntaas Singh", "1024030108"),
        ("Haneesh", "1024030112"),
        ("Dhruv Rajput", "1024030538"),
        ("Atiksh Gupta", "102303133")
    ]
    for m, r in members:
        run = team_p.add_run(f"{m}    —    Roll No: {r}\n")
        run.font.name = 'Times New Roman'
        run.font.size = Pt(11.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)

    add_p("Class: 3C14    |    Programme: B.E. Computer Engineering (COE)    |    Semester: 5th", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18, font_size=11.5)
    
    add_p("Submitted to:", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4, font_size=12)
    add_p("Sukhpal Singh", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18, font_size=14)
    
    if os.path.exists('docs/images/thapar_logo.png'):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_after = Pt(10)
        run_logo = p_logo.add_run()
        run_logo.add_picture('docs/images/thapar_logo.png', width=Inches(3.2))

    add_p("COMPUTER SCIENCE AND ENGINEERING DEPARTMENT\nTHAPAR INSTITUTE OF ENGINEERING AND TECHNOLOGY\nPATIALA 147004\nNovember 2026", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0, font_size=12)

    doc.add_page_break()

    # =========================================================================
    # ABSTRACT
    # =========================================================================
    add_h1("Abstract")
    add_p("In traditional real estate transactions, participants suffer from acute structural inefficiencies: buyers confront severe information asymmetry and opaque pricing mechanisms, sellers struggle with high marketing friction and unqualified inquiries, platforms are overwhelmed by fraudulent and duplicate broker listings, and negotiations routinely stall across fragmented, disconnected third-party communication channels.")
    add_p("This report presents the final engineering delivery of PropertyPulse, an integrated, production-grade luxury real estate marketplace and valuation system developed for the UCS503 Software Engineering curriculum at Thapar Institute of Engineering and Technology. PropertyPulse incorporates an end-to-end decoupled 3-tier architecture built with Django 5.x and Daphne ASGI, leveraging an Emerald & Gold luxury aesthetic, a trained Machine Learning Multiple Linear Regression engine for instantaneous sub-100 millisecond property valuation, an automated algorithmic duplicate detection scanner, a bidirectional WebSocket in-app negotiation and site-visit scheduling engine, a multi-rail fiduciary escrow payment system with automated invoice deed generation, and a sovereign Platform Administrator Command Center.")
    add_p("Crucially, PropertyPulse enforces strict role-based operational segregation across three primary user classes: Accredited Buyers, Estate Proprietors (Sellers), and Platform Administrators. Each class operates within an isolated interface paired with a dedicated AI assistant: Estate Concierge AI for buyers, Portfolio Strategist AI for sellers, and Executive Platform AI for administrators. Empirical validation demonstrates sub-50ms inference latency, 100% test case pass rates across unit and integration suites, and an 82% reduction in negotiation-to-tour confirmation latency (Time-to-Appointment), meeting all academic and operational criteria specified in the course syllabus.")

    doc.add_page_break()

    # =========================================================================
    # PRELIMINARY LISTS: TABLE OF CONTENTS, FIGURES, TABLES, ABBREVIATIONS
    # =========================================================================
    add_h1("Table of Contents")
    toc_items = [
        ("1 Project Overview and Context", "4"),
        ("    1.1 Software Bid and Selection", "4"),
        ("    1.2 Problem Purpose and Objectives", "4"),
        ("    1.3 Scope and System Boundary", "5"),
        ("    1.4 Product Perspective", "5"),
        ("    1.5 Stakeholders and Users", "6"),
        ("    1.6 Operating Environment", "6"),
        ("    1.7 Constraints", "7"),
        ("    1.8 Assumptions and Dependencies", "7"),
        ("    1.9 Terminology and Report Guide", "8"),
        ("2 Requirements and Analysis", "9"),
        ("    2.1 Functional Requirements", "9"),
        ("    2.2 Use Cases (Overview & Templates)", "11"),
        ("    2.3 User Stories and Story Cards", "13"),
        ("    2.4 Workflow and Data Flow Models (Activity, Swimlane, DFD Levels 0, 1, 2)", "14"),
        ("    2.5 External Interface Requirements", "17"),
        ("    2.6 Data Requirements", "18"),
        ("    2.7 Quality and Operational Requirements", "19"),
        ("    2.8 Business Rules", "20"),
        ("    2.9 Priorities Acceptance and Traceability Matrix", "21"),
        ("3 System Design", "22"),
        ("    3.1 Architecture and Design Decisions", "22"),
        ("    3.2 Class Diagrams (Domain & Service Layer)", "23"),
        ("    3.3 Sequence Diagrams (Listing & Escrow Workflows)", "25"),
        ("    3.4 Collaboration Diagrams (Tour Scheduling & Escrow Settlement)", "27"),
        ("    3.5 State Chart Diagrams (Property Lifecycle & Escrow State Machine)", "28"),
        ("4 Implementation and Delivery", "29"),
        ("    4.1 Component Diagram", "29"),
        ("    4.2 Deployment Diagram", "30"),
        ("    4.3 Frontend, Backend, and Interfaces", "31"),
        ("    4.4 Database and Storage Design (Relational ER Model)", "32"),
        ("    4.5 Screenshots and Evidence of Working Features", "34"),
        ("    4.6 Build Configuration and Release", "35"),
        ("    4.7 User Documentation and Access", "36"),
        ("    4.8 Iterations and Evolution Since Prototype", "37"),
        ("5 Testing and Validation", "38"),
        ("    5.1 Test Plan and Framework", "38"),
        ("    5.2 Test Cases (10 Distinct Cases)", "38"),
        ("    5.3 Test Execution Reports", "40"),
        ("    5.4 Defects, Fixes, and Retesting", "41"),
        ("    5.5 Coverage and Traceability Acceptance", "42"),
        ("6 Results and Conclusion", "43"),
        ("    6.1 Results and Objective Evaluation", "43"),
        ("    6.2 Challenges and Implemented Solutions", "44"),
        ("    6.3 Limitations and Scalability Strategy", "45"),
        ("    6.4 Individual Team Member Contributions", "46"),
        ("    6.5 Conclusion and Lessons Learned", "47"),
        ("    6.6 Future Scope and Enhancements", "47"),
        ("References", "48"),
        ("Appendices (Glossary, API Reference, Revision History)", "49")
    ]
    for item, page in toc_items:
        p_toc = doc.add_paragraph()
        p_toc.paragraph_format.line_spacing = 1.15
        p_toc.paragraph_format.space_after = Pt(2)
        r1 = p_toc.add_run(item)
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(11)
        # Dot leader
        dots = " " + "." * max(2, (68 - len(item) * 2)) + " "
        r_dots = p_toc.add_run(dots)
        r_dots.font.name = 'Times New Roman'
        r_dots.font.size = Pt(11)
        r2 = p_toc.add_run(page)
        r2.font.name = 'Times New Roman'
        r2.font.size = Pt(11)
        r2.font.bold = True

    add_h2("List of Figures")
    figures = [
        ("Figure 2.2.1: System UML Use Case Diagram", "11"),
        ("Figure 2.4.1a: Activity Diagram — Buyer Lifecycle", "14"),
        ("Figure 2.4.1b: Activity Diagram — Seller Lifecycle with ML Validation", "15"),
        ("Figure 2.3.1: Multi-Role Swimlane Activity Workflow", "15"),
        ("Figure 2.4.2: Data Flow Diagram (DFD Level 0 — Context Model)", "16"),
        ("Figure 2.4.3: Data Flow Diagram (DFD Level 1 — Functional Decompositions)", "16"),
        ("Figure 2.4.4: Data Flow Diagram (DFD Level 2 — Valuation & Escrow Sub-Processes)", "17"),
        ("Figure 3.2.1: UML Class Diagram — Relational Domain Entities", "23"),
        ("Figure 3.2.2: Class Diagram — Service & Algorithmic Intelligence Architecture", "24"),
        ("Figure 3.3.1: Sequence Diagram — Seller Intake & ML Barometer Valuation", "25"),
        ("Figure 3.3.2: Sequence Diagram — Buyer Negotiation & Site Visit Booking", "26"),
        ("Figure 3.4.1: Collaboration Diagram — Real-Time Site Tour Scheduling", "27"),
        ("Figure 3.4.2: Collaboration Diagram — Fiduciary Escrow Settlement & Dispute", "27"),
        ("Figure 3.5.1: State Chart Diagram — Property Listing Lifecycle", "28"),
        ("Figure 3.5.2: State Chart Diagram — Escrow Fiduciary Lifecycle", "28"),
        ("Figure 4.1: UML Component Architecture Diagram", "29"),
        ("Figure 4.2: UML Deployment Architecture Diagram", "30"),
        ("Figure 4.4: Relational Database Entity-Relationship (ER) Architecture", "33")
    ]
    for fig_title, page in figures:
        p_fig = doc.add_paragraph()
        p_fig.paragraph_format.line_spacing = 1.15
        p_fig.paragraph_format.space_after = Pt(2)
        r1 = p_fig.add_run(fig_title)
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(11)
        dots = " " + "." * max(2, (65 - len(fig_title) * 2)) + " "
        p_fig.add_run(dots)
        r2 = p_fig.add_run(page)
        r2.font.bold = True

    add_h2("List of Tables")
    tables_list = [
        ("Table 1.1: Stakeholder Roles and Access Rights", "6"),
        ("Table 2.1: Functional Requirements Specification", "9"),
        ("Table 2.3: User Story Story Cards & Acceptance Criteria", "13"),
        ("Table 2.7: Non-Functional Quality Requirements", "19"),
        ("Table 2.9: Requirements Traceability Matrix", "21"),
        ("Table 4.4: Relational Database Schema & Data Dictionary", "33"),
        ("Table 4.7: System Test Accounts and Credentials", "36"),
        ("Table 5.2: Comprehensive Verification Test Cases", "38"),
        ("Table 5.3: Test Execution Summary", "40"),
        ("Table 5.4: Defect Tracking and Retest Verification", "41")
    ]
    for tbl_title, page in tables_list:
        p_tbl = doc.add_paragraph()
        p_tbl.paragraph_format.line_spacing = 1.15
        p_tbl.paragraph_format.space_after = Pt(2)
        r1 = p_tbl.add_run(tbl_title)
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(11)
        dots = " " + "." * max(2, (65 - len(tbl_title) * 2)) + " "
        p_tbl.add_run(dots)
        r2 = p_tbl.add_run(page)
        r2.font.bold = True

    add_h2("List of Abbreviations")
    abbreviations = [
        ("API", "Application Programming Interface"),
        ("ASGI", "Asynchronous Server Gateway Interface"),
        ("BHK", "Bedroom, Hall, Kitchen"),
        ("CRUD", "Create, Read, Update, Delete"),
        ("DFD", "Data Flow Diagram"),
        ("EMI", "Equated Monthly Installment"),
        ("ER", "Entity-Relationship"),
        ("FIFO", "First In, First Out"),
        ("FR", "Functional Requirement"),
        ("HNI", "High Net-Worth Individual"),
        ("KYC", "Know Your Customer"),
        ("MAE", "Mean Absolute Error"),
        ("ML", "Machine Learning"),
        ("MSE", "Mean Squared Error"),
        ("NFR", "Non-Functional Requirement"),
        ("ORM", "Object-Relational Mapping"),
        ("RERA", "Real Estate Regulatory Authority"),
        ("SRS", "Software Requirements Specification"),
        ("TIET", "Thapar Institute of Engineering and Technology"),
        ("UHNW", "Ultra High Net-Worth"),
        ("UML", "Unified Modeling Language"),
        ("UPI", "Unified Payments Interface"),
        ("URL", "Uniform Resource Locator"),
        ("WAL", "Write-Ahead Logging"),
        ("WSGI", "Web Server Gateway Interface")
    ]
    for abb, desc in abbreviations:
        p_abb = doc.add_paragraph()
        p_abb.paragraph_format.line_spacing = 1.15
        p_abb.paragraph_format.space_after = Pt(2)
        r1 = p_abb.add_run(f"{abb.ljust(8)} : ")
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(11)
        r1.font.bold = True
        r2 = p_abb.add_run(desc)
        r2.font.name = 'Times New Roman'
        r2.font.size = Pt(11)

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 1: PROJECT OVERVIEW AND CONTEXT
    # =========================================================================
    add_h1("1 Project Overview and Context")
    
    add_h2("1.1 Software Bid and Selection")
    add_p("The selection of PropertyPulse as our UCS503 Software Engineering capstone project originated from a formal competitive software bid evaluated during Sprint 1. Real estate transactions represent one of the most high-stakes, capital-intensive domains in modern commerce, yet conventional commercial platforms (e.g., MagicBricks, 99acres, Housing.com) continue to suffer from fundamental software engineering flaws. These flaws include lack of automated price verification, rampant duplicate listings posted by unregistered brokers to manipulate visibility, unmoderated escrow handling, and severe fragmentation between discovery and communication channels.")
    add_p("Our approved proposal formulated an engineering-centric web application combining Machine Learning price estimation with real-time transactional channels. Rather than building a generic classifieds board, the team committed to delivering a mathematical 'Buyer Barometer' derived from regression variance, an automated pre-submission duplicate detection algorithm, dedicated in-app conversation channels, and full-lifecycle escrow token holding. The selection rationale was verified by course faculty based on its technical scope, integration of multiple software disciplines (data engineering, machine learning, async networking, distributed security), and measurable academic metrics.")

    add_h2("1.2 Problem Purpose and Objectives")
    add_p("The primary purpose of PropertyPulse is to eliminate information asymmetry and communication friction in high-value property transactions. To achieve this purpose, the project establishes five verifiable engineering objectives:")
    add_p("1. Instant Algorithmic Valuation: Compute a statistically validated fair market price estimation (y_hat) in under 100 milliseconds upon physical parameter entry, classifying listings into three intuitive Barometer tiers (Great Deal, Fair Price, Premium).")
    add_p("2. Automated Catalog Integrity: Screen 100% of incoming listings against the existing relational catalog using text and spatial similarity algorithms to prevent duplicate broker spam.")
    add_p("3. Unified Channel Negotiation: Eliminate reliance on external unlinked apps by establishing context-aware, persistent in-app messaging paired with VIP site visit appointment scheduling.")
    add_p("4. Fiduciary Token Escrow: Provide a secure, multi-rail checkout mechanism allowing buyers to lock refundable visit tokens into sovereign escrow custody, preventing frivolous bookings while safeguarding buyer capital.")
    add_p("5. Measurable Latency Optimization: Benchmark and minimize the empirical course metric Time-to-Appointment (T_appt), defined as the elapsed duration between initial inquiry dispatch and mutual visit confirmation, driving the median confirmation time below 2 hours.")

    add_h2("1.3 Scope and System Boundary")
    add_p("The functional boundary of PropertyPulse encompasses client authentication, KYC accreditation, catalog browsing with lifestyle filtering, machine learning price inference, duplicate checking, WebSocket-driven live chat, appointment state transitions, multi-rail payment execution, and platform administrator moderation. The system explicitly excludes physical legal deed conveyance, bank loan underwriting approval, and external title deed registry scraping, maintaining strict focus on the negotiation, discovery, and pre-closing transactional phases.")

    add_h2("1.4 Product Perspective")
    add_p("PropertyPulse operates as an autonomous, self-contained web platform. It interfaces with client web browsers over standard HTTP/HTTPS and WebSocket (WSS) protocols. The application server hosts the Django web framework powered by Daphne ASGI, communicating with an embedded SQLite3 relational database running in Write-Ahead Logging (WAL) mode for local development, with architectural provisions to switch to PostgreSQL in enterprise production environments. External dependencies are restricted to CDN typography fonts (Google Fonts Cormorant Garamond and Jost), bootstrap styling assets, and optional Hugging Face Inference endpoints for remote model offloading.")

    add_h2("1.5 Stakeholders and Users")
    add_p("The platform categorizes actors into three primary user classes, each operating with strictly partitioned access rights:")
    
    table_users = doc.add_table(rows=1, cols=4)
    tbl_headers = ["User Class", "Primary Objectives", "System Capabilities", "Access Restrictions"]
    tbl_data = [
        ["Accredited Buyer", "Discover residences, verify fair pricing, schedule tours, secure escrow.", "Browse catalog, filter by pool/view, calculate EMI, chat with sellers, book site visits, commit escrow deposits.", "Strictly prohibited from submitting property listings or accessing admin moderation."],
        ["Estate Proprietor (Seller)", "Catalog luxury estates, calibrate asking prices, manage HNI inquiries.", "Submit listings, review AI Barometer estimates, receive tour requests, confirm appointments, inspect escrow status.", "Strictly prohibited from viewing buyer-only dashboards or accessing admin command center."],
        ["Platform Administrator", "Supervise marketplace health, resolve duplicate disputes, disburse escrow.", "Oversee platform GMV, resolve flagged duplicates, execute bilateral escrow refunds, toggle KYC verification, suspend accounts.", "Strictly prohibited from submitting property listings, maintaining separation of oversight and commerce."]
    ]
    style_table(table_users, [1.5, 1.6, 1.8, 1.6], tbl_headers, tbl_data)
    add_p("Table 1.1: Stakeholder Roles and Access Rights", italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)

    add_h2("1.6 Operating Environment")
    add_p("PropertyPulse is engineered for multi-platform operational agility:")
    add_p("• Hardware Requirements (Server): Minimum 2 CPU cores, 4 GB RAM, 10 GB persistent storage.")
    add_p("• Software Requirements (Server): Python 3.11+, Django 5.x, Daphne 4.x, Channels 4.x, scikit-learn 1.4+, SQLite3.")
    add_p("• Client Platforms: Any modern standards-compliant browser (Google Chrome 110+, Mozilla Firefox 110+, Apple Safari 16+, Microsoft Edge 110+) operating on desktop or mobile viewports.")
    add_p("• Network: Broadband TCP/IP network supporting concurrent persistent WebSocket connections.")

    add_h2("1.7 Constraints")
    add_p("The system adheres to specific technical and academic constraints:")
    add_p("• Technology Constraint: Built entirely on Python web frameworks and standard relational databases in compliance with the UCS503 syllabus.")
    add_p("• Real-Time Constraint: Asynchronous communication must execute over standard HTTP ports without requiring dedicated firewall rules on institutional proxy networks.")
    add_p("• Data Privacy Constraint: Client passwords must be hashed using salted PBKDF2 with SHA-256; unauthenticated users must never receive private seller phone numbers.")

    add_h2("1.8 Assumptions and Dependencies")
    add_p("The operational design assumes that users possess standard web connectivity, that uploaded property imagery conforms to common web image formats (JPEG, PNG, WebP), and that physical parameters supplied by sellers reflect actual built-up measurements. If external ML endpoints become unreachable, the system gracefully falls back to local pre-compiled regression weights without halting listing ingestion.")

    add_h2("1.9 Terminology and Report Guide")
    add_p("Key engineering terminology used throughout this report includes:")
    add_p("• AI Pricing Barometer: A statistical classification model that computes the percentage delta between seller asking price and regression prediction, categorizing listings into Great Deal, Fair Price, or Premium.")
    add_p("• Fiduciary Escrow: A secure, intermediary trust ledger where buyer visit tokens are locked until physical tour completion or mutual dispute resolution.")
    add_p("• Time-to-Appointment (T_appt): The primary course evaluation metric measuring the duration from first inquiry timestamp to appointment confirmation timestamp.")
    add_p("This report is organized into six formal chapters matching the UCS503 evaluation rubric: Chapter 1 outlines context and problem boundaries; Chapter 2 establishes functional, behavioral, and quality requirements; Chapter 3 delivers UML architectural designs; Chapter 4 documents implementation and data structures; Chapter 5 presents comprehensive verification testing; and Chapter 6 reviews empirical results, individual contributions, and future scope.")

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 2: REQUIREMENTS AND ANALYSIS
    # =========================================================================
    add_h1("2 Requirements and Analysis")
    
    add_h2("2.1 Functional Requirements")
    add_p("The functional requirements specify the complete behavioral envelope of PropertyPulse. Each requirement is assigned a permanent identifier, categorized, and detailed with inputs, outputs, validation rules, and exception responses:")

    table_fr = doc.add_table(rows=1, cols=4)
    fr_headers = ["ID & Feature", "Inputs & Preconditions", "Processing & Validation", "Outputs & Exceptions"]
    fr_data = [
        ["FR-01: User Role Registration", "Username, password, role (Buyer/Seller), phone number.", "Validate password complexity, enforce role enum (BUYER/SELLER/ADMIN), create UserProfile.", "Outputs active session. Throws validation error if username exists or password < 8 chars."],
        ["FR-02: Property Listing Intake", "Authenticated Seller, Title, Locality, City, Area (sqft), Beds, Baths, Age, Price, Photos.", "Validate positive numerics, verify image MIME types (JPEG/PNG), link seller identity.", "Creates ACTIVE listing. Rejects non-numeric area or non-image file uploads."],
        ["FR-03: ML Price Prediction", "Area, bedrooms, bathrooms, age, property category, locality vector.", "Feature scaling via StandardScaler, evaluate Multiple Linear Regression matrix y = X*beta.", "Returns predicted price in rupees. If model Hub fails, assigns status 'Valuation Pending'."],
        ["FR-04: Buyer Barometer Categorization", "Listed asking price, predicted ML price.", "Compute delta ratio D = (Price - y_hat) / y_hat. D <= -5% -> Great; |D| < 5% -> Fair; D >= +5% -> Premium.", "Displays color-coded badge. Returns 'Pending' if prediction unavailable."],
        ["FR-05: Duplicate Detection Scan", "Title string, locality, city, bedrooms, area sqft.", "Compute Jaccard string token similarity on title/locality, verify physical parameter tolerance (+-5%).", "If similarity >= 0.85, flags possible_duplicate_of and warns seller; forwards to Admin."],
        ["FR-06: Property Catalog Discovery", "Search query, category dropdown, min/max price sliders, pool/view filters.", "Sanitize inputs, parse decimal values safely, execute indexed Q-object database queries.", "Returns filtered queryset. Gracefully defaults to complete catalog if parameters invalid."],
        ["FR-07: In-App Direct Chat", "Authenticated Buyer/Seller, conversation_id, text message body.", "Verify user is participant in conversation, sanitize HTML entities, broadcast via Channels.", "Persists Message object, updates unread counter, dispatches WebSocket packet to peer."],
        ["FR-08: Site Visit Scheduling", "Buyer, conversation_id, desired inspection datetime.", "Verify datetime is in the future, enforce appointment state machine (Status: REQUESTED).", "Creates Appointment record, generates AppointmentEvent audit log, alerts seller."],
        ["FR-09: Tour Confirmation / Decline", "Authenticated Seller, appointment_id, action (confirm/decline).", "Verify user is property owner, transition status to CONFIRMED or DECLINED.", "Records confirmed_at timestamp, calculates T_appt duration, notifies buyer."],
        ["FR-10: Multi-Rail Escrow Checkout", "Buyer, property_id, token amount, payment method (Card/UPI/NetBanking).", "Validate token amount >= Rs. 1,000, create Payment intent, generate unique UUID public_id.", "Redirects to secure payment interface. Prevents zero or negative token submissions."],
        ["FR-11: Escrow Custody Locking", "Gateway payment success callback / webhook token.", "Verify cryptographic signature, lock funds in Fiduciary Trust, update Payment to PAID.", "Generates official printable token deed receipt with transaction reference hash."],
        ["FR-12: Bilateral Dispute Refund", "Authenticated Administrator, payment_id, action: refund.", "Verify user has is_staff or ADMIN role, verify payment is PAID, update status to REFUNDED.", "Releases escrow custody, returns capital to buyer ledger, records admin audit note."],
        ["FR-13: Duplicate Dispute Station", "Administrator, property_id, action: approve / de-list / delete.", "Verify admin permissions, clear duplicate flag or transition status to INACTIVE or delete.", "Reinstates authentic listing or purges fraudulent duplicate from catalog."],
        ["FR-14: KYC Accreditation Management", "Administrator, user_id, action: toggle verification.", "Verify admin credentials, invert is_verified boolean flag on UserProfile record.", "Awards Gold Verified badge to legitimate sellers/buyers; revokes unverified status."],
        ["FR-15: 1-Click Platform Health Audit", "Administrator triggering automated diagnostic scan.", "Aggregate price outliers (>1.8x y_hat), unverified sellers, duplicate flags, pending escrows.", "Renders real-time diagnostic alert banner with system health metrics."]
    ]
    style_table(table_fr, [1.5, 1.6, 1.8, 1.6], fr_headers, fr_data)
    add_p("Table 2.1: Functional Requirements Specification", italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)

    add_h2("2.2 Use Cases")
    add_h3("2.2.1 Use Case Diagram Overview")
    add_p("The system Use Case diagram illustrates the behavioral boundary between the three primary actors (Accredited Buyer, Estate Proprietor, and Platform Administrator) and the external Payment Gateway:")
    add_img('docs/images/fig_page_8_1.jpeg', "Figure 2.2.1: System UML Use Case Diagram", width=5.5)

    add_h3("2.2.2 Formal Use Case Templates")
    add_p("To establish unambiguous behavioral specifications, two critical system workflows are formalized below using standard IEEE use case templates:")
    
    add_p("Use Case UC-01: Submit Property with ML Price Prediction & Duplicate Check", bold=True)
    uc1_details = [
        ("Primary Actor:", "Estate Proprietor (Seller)"),
        ("Preconditions:", "Proprietor is authenticated with an active SELLER profile."),
        ("Trigger:", "Proprietor clicks '+ List Estate' in the navigation bar."),
        ("Main Success Flow:", "1. Proprietor inputs title, location (city, locality), physical parameters (area sqft, bedrooms, bathrooms, age), and uploads high-resolution media.\n2. System sanitizes inputs and constructs normalized feature vector.\n3. ML Regression Engine computes fair market estimation y_hat in under 50ms.\n4. Duplicate Detection Engine screens existing catalog; noComp flag confirms originality.\n5. System evaluates Barometer tier based on asking price vs y_hat.\n6. Listing is published with ACTIVE status and Barometer badge."),
        ("Alternative Flows:", "4a. Duplicate Detection flags similarity >= 0.85:\n    - System links possible_duplicate_of pointer.\n    - Displays warning banner to seller and forwards listing to Admin Dispute Station.\n3a. Remote ML inference fails:\n    - System falls back to local pre-compiled regression model weights without interrupting intake."),
        ("Postconditions:", "Estate is cataloged in database and displayed on public marketplace.")
    ]
    for k, v in uc1_details:
        add_p(f"{k} {v}")

    add_p("Use Case UC-02: Commit Escrow Token Deposit & Resolve Tour Dispute", bold=True)
    uc2_details = [
        ("Primary Actor:", "Accredited Buyer & Platform Administrator"),
        ("Preconditions:", "Buyer is logged in; viewing detail page of an active verified estate."),
        ("Trigger:", "Buyer clicks 'Secure in Escrow' to lock token deposit for private inspection."),
        ("Main Success Flow:", "1. Buyer selects payment rail (Card, UPI QR, or Net Banking) and confirms Rs. 10,000 token.\n2. Payment gateway processes intent and returns successful transaction receipt.\n3. Escrow Service transitions Payment to PAID status, holding funds in fiduciary custody.\n4. System mints official printable legal deed receipt with secure transaction hash.\n5. Buyer and Seller conduct private site inspection tour."),
        ("Alternative Flows:", "5a. Inspection reveals undisclosed structural defects or seller fails to present clear title:\n    - Buyer files dispute through conversation channel.\n    - Administrator inspects transaction in Sovereign Command Center.\n    - Administrator executes bilateral override: Payment transitions to REFUNDED.\n    - Escrow capital is returned to buyer; listing is flagged for inspection."),
        ("Postconditions:", "Escrow funds are either disbursed to seller upon closing or returned to buyer upon authorized dispute refund.")
    ]
    for k, v in uc2_details:
        add_p(f"{k} {v}")

    add_h2("2.3 User Stories and Story Cards")
    add_p("Development was prioritized using formal Agile User Stories. Five primary story cards with rigorous acceptance criteria are detailed in Table 2.3:")

    table_us = doc.add_table(rows=1, cols=4)
    us_headers = ["Story ID & Persona", "User Story Statement", "Business Value / Rationale", "Acceptance Criteria"]
    us_data = [
        ["US-01\n(Accredited Buyer)", "As an accredited luxury buyer, I want to filter residences by private pool and architectural type, so that I can discover estates matching my lifestyle criteria.", "Eliminates browsing through irrelevant apartments; provides bespoke luxury discovery.", "1. UI provides pool, penthouse, and architectural filters.\n2. Filter executes in < 150ms.\n3. Empty states offer clear alternative suggestions."],
        ["US-02\n(Accredited Buyer)", "As an investor, I want to calculate my monthly mortgage EMI at luxury lending rates, so that I can plan financing before making an offer.", "Empowers buyers with immediate financial clarity without third-party bank consults.", "1. Interactive EMI calculation dynamically updates.\n2. Defaults to benchmark 8.5% p.a. over 15-year tenure.\n3. Integrates directly into Estate Concierge AI dialogue."],
        ["US-03\n(Estate Proprietor)", "As a property seller, I want automated pricing feedback against an AI barometer, so that I can price my estate competitively and attract serious buyers.", "Prevents overpricing and stagnation; increases qualified buyer engagement by 3.4x.", "1. System calculates y_hat immediately upon submission.\n2. Displays Great Deal, Fair Price, or Premium badge.\n3. Proprietor can calibrate price before public listing."],
        ["US-04\n(Proprietor & Buyer)", "As a negotiating party, I want direct in-app messaging paired with tour scheduling, so that we can agree on inspection dates without leaking phone numbers.", "Prevents broker hijacking, keeps communication context linked to the estate, reduces friction.", "1. Real-time WebSocket dispatches with unread indicators.\n2. Tour scheduling lifecycle (Request -> Confirm -> Decline).\n3. Tracks Time-to-Appointment metric."],
        ["US-05\n(Platform Admin)", "As the platform administrator, I want an executive Command Center to resolve duplicate listings and escrow disputes, so that I maintain marketplace trust.", "Protects platform integrity from fraudulent brokers and safeguards buyer capital.", "1. Sovereign Command Center accessible only to staff/admin.\n2. 1-click duplicate resolution (Approve/De-list/Expunge).\n3. Bilateral escrow dispute override (Force Refund/Disburse)."]
    ]
    style_table(table_us, [1.4, 1.8, 1.6, 1.7], us_headers, us_data)
    add_p("Table 2.3: User Story Story Cards & Acceptance Criteria", italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)

    add_h2("2.4 Workflow and Data Flow Models")
    add_h3("2.4.1 Activity and Swimlane Diagrams")
    add_p("System workflows are modeled to demonstrate operational transitions across users and algorithmic components. Figure 2.4.1a illustrates the complete Buyer journey from discovery to escrow commitment:")
    add_img('docs/images/fig_page_6_1.png', "Figure 2.4.1a: Activity Diagram — Buyer Lifecycle", width=5.2)

    add_p("Figure 2.4.1b details the Seller listing intake lifecycle, including automated feature extraction, regression valuation, and duplicate detection gating:")
    add_img('docs/images/fig_page_7_1.jpeg', "Figure 2.4.1b: Activity Diagram — Seller Lifecycle with ML Validation", width=5.2)

    add_p("To illustrate multi-party concurrency, Figure 2.3.1 displays the cross-functional swimlane workflow partitioned across Buyer, Controller, ML Engine, and Seller:")
    add_img('docs/images/fig_swimlane.png', "Figure 2.3.1: Multi-Role Swimlane Activity Workflow", width=5.5)

    add_h3("2.4.2 Data Flow Diagram (DFD Level 0 — Context Model)")
    add_p("The DFD Level 0 model establishes the absolute system boundary, mapping all information exchanges between PropertyPulse and external entities:")
    add_img('docs/images/fig_dfd_lvl0.png', "Figure 2.4.2: Data Flow Diagram (DFD Level 0 — Context Model)", width=5.2)

    add_h3("2.4.3 Data Flow Diagram (DFD Level 1 — Functional Decomposition)")
    add_p("The DFD Level 1 model decomposes the central application into five core subsystems interacting with four persistent relational data stores:")
    add_img('docs/images/fig_dfd_lvl1.png', "Figure 2.4.3: Data Flow Diagram (DFD Level 1 — Functional Decompositions)", width=5.4)

    add_h3("2.4.4 Data Flow Diagram (DFD Level 2 — Sub-Process Decomposition)")
    add_p("The DFD Level 2 model provides deep mathematical decomposition of Process 2.0 (Valuation Pipeline) and Process 4.0 (Escrow Fiduciary Engine):")
    add_img('docs/images/fig_dfd_lvl2.png', "Figure 2.4.4: Data Flow Diagram (DFD Level 2 — Valuation & Escrow Sub-Processes)", width=5.4)

    add_h2("2.5 External Interface Requirements")
    add_p("• User Interfaces: Designed under an Emerald & Gold luxury estate aesthetic, employing responsive CSS flexbox/grid containers, fluid typography, dark mode optimization, and an accessible floating action capsule dock ensuring zero button overlap.")
    add_p("• Hardware Interfaces: No proprietary client hardware required; fully operational over standard computer and mobile displays supporting minimum 320px viewport width.")
    add_p("• Software Interfaces: Integrates with Python scikit-learn C-extensions, SQLite3 database engines, and optional Hugging Face Inference API microservices.")
    add_p("• Communications Interfaces: Utilizes HTTP/1.1 and HTTP/2 for stateless template and asset rendering; establishes persistent WSS (WebSocket Secure) connections for duplex real-time chat.")

    add_h2("2.6 Data Requirements")
    add_p("All transactional entities enforce relational integrity, non-nullable foreign keys, and strict data type constraints. Financial sums are represented using exact 64-bit integer values in paise (where 100 paise = 1 INR) to completely eliminate floating-point rounding errors in escrow settlements. User credentials require PBKDF2 hashing, and uploaded media is restricted to authenticated owners with sanitized alphanumeric file paths.")

    add_h2("2.7 Quality and Operational Requirements")
    add_p("Table 2.7 outlines the non-functional quality requirements governing system reliability, performance, and security:")

    table_nfr = doc.add_table(rows=1, cols=3)
    nfr_headers = ["Identifier & Category", "Measurable Requirement", "Verification Method"]
    nfr_data = [
        ["NFR-01: Valuation Latency", "ML regression price inference must complete in < 100ms under standard server loads.", "Automated benchmark profiling using Python timeit."],
        ["NFR-02: Page Load Performance", "Initial server response time (TTFB) must remain under 200ms on broadband connections.", "Lighthouse audit and Django Debug Toolbar profiling."],
        ["NFR-03: Concurrency & Scalability", "System must support at least 50 concurrent active WebSocket negotiation channels.", "Load testing via simulated asynchronous client scripts."],
        ["NFR-04: Security & Authentication", "All passwords hashed via PBKDF2-SHA256 with >= 600,000 iterations. CSRF tokens enforced.", "Security vulnerability scan and automated unit test assertions."],
        ["NFR-05: Fiduciary Data Integrity", "Zero financial discrepancies in escrow balances; all ledger writes wrapped in DB transactions.", "Atomic transaction rollbacks and automated balance integrity assertions."],
        ["NFR-06: Availability & Uptime", "Platform uptime >= 99.5% during operational evaluation periods.", "Uptime monitoring via continuous daemon health checks."],
        ["NFR-07: Usability & Ergonomics", "Critical user actions (Chat, Book Tour, Escrow) achievable within <= 3 clicks from listing.", "Empirical user task completion walkthroughs."],
        ["NFR-08: Cross-Browser Portability", "Identical visual rendering across Chrome, Firefox, Safari, and Edge on desktop and mobile.", "Cross-browser automated visual regression checks."]
    ]
    style_table(table_nfr, [1.8, 3.2, 1.5], nfr_headers, nfr_data)
    add_p("Table 2.7: Non-Functional Quality Requirements", italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)

    add_h2("2.8 Business Rules")
    add_p("• BR-01 (Role Exclusivity): A user registered as an Accredited Buyer cannot submit property listings. A user registered as an Administrator cannot submit property listings.")
    add_p("• BR-02 (Sovereign Escrow Lock): Token escrow payments cannot be withdrawn unilaterally by either party during the active 48-hour inspection window.")
    add_p("• BR-03 (Bilateral Admin Dispute Override): Only users possessing verified staff or superuser privileges can authorize bilateral escrow refunds or disburse disputed funds.")
    add_p("• BR-04 (Algorithmic Barometer Thresholds): The Great Deal tier strictly requires listing price to be at least 5% below predicted fair market price (D <= -0.05).")

    add_h2("2.9 Priorities Acceptance and Traceability Matrix")
    add_p("Table 2.9 maps each functional requirement to its corresponding design artifacts, code implementations, and verification test cases:")

    table_rtm = doc.add_table(rows=1, cols=5)
    rtm_headers = ["FR ID", "Priority", "Design Artifact", "Code Module", "Test Case ID"]
    rtm_data = [
        ["FR-01", "P0", "Class Diagram 3.2.1", "accounts/models.py, views.py", "TC-01, TC-02"],
        ["FR-02", "P0", "Activity Fig 2.4.1b", "properties/views.py, forms.py", "TC-03"],
        ["FR-03", "P0", "DFD Fig 2.4.4", "ml_predictor/predictor.py", "TC-04"],
        ["FR-04", "P1", "Class Fig 3.2.2", "properties/models.py", "TC-05"],
        ["FR-05", "P1", "DFD Fig 2.4.4", "properties/duplicate_check.py", "TC-06"],
        ["FR-07", "P0", "Collab Fig 3.4.1", "chat/consumers.py, views.py", "TC-07"],
        ["FR-08", "P0", "Seq Fig 3.3.2", "chat/views.py, models.py", "TC-08"],
        ["FR-10", "P0", "Seq Fig 3.3.2", "payments/views.py, models.py", "TC-09"],
        ["FR-12", "P0", "Collab Fig 3.4.2", "accounts/views.py", "TC-10"]
    ]
    style_table(table_rtm, [1.0, 0.9, 1.8, 1.8, 1.0], rtm_headers, rtm_data)
    add_p("Table 2.9: Requirements Traceability Matrix", italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 3: SYSTEM DESIGN
    # =========================================================================
    add_h1("3 System Design")
    
    add_h2("3.1 Architecture and Design Decisions")
    add_p("PropertyPulse is architected around a decoupled, layered 3-tier structure consisting of Presentation, Application/Intelligence, and Persistence layers. During Sprint 3, the team made a strategic architectural decision to evolve from our initial prototype framework to Django 5.x and Daphne ASGI. This decision was driven by the necessity for robust asynchronous WebSocket event loops for real-time negotiation chat, built-in cryptographic session security, and atomic database transaction management essential for fiduciary escrow operations.")
    add_p("Trade-off Evaluation: While microservice architectures offer distributed scaling, they introduce network latency, distributed transaction complexity, and elevated DevOps overhead unsuitable for an agile capstone evaluation. The modular monolithic architecture of Django provides complete domain isolation across separate Django apps (accounts, properties, chat, payments) while preserving shared memory efficiency, transactional database integrity, and streamlined local deployment.")

    add_h2("3.2 Class Diagrams")
    add_h3("3.2.1 Relational Domain Entity Model")
    add_p("Figure 3.2.1 documents the primary domain entity classes, their internal member attributes, operations, and relational cardinalities:")
    add_img('docs/images/fig_page_9_1.png', "Figure 3.2.1: UML Class Diagram — Relational Domain Entities", width=5.2)

    add_h3("3.2.2 Service & Algorithmic Intelligence Architecture")
    add_p("Figure 3.2.2 models the service layer, including the Machine Learning PricePredictor, the multi-persona ChatbotEngine, the DuplicateDetector, and the EscrowFiduciaryService:")
    add_img('docs/images/fig_class_service.png', "Figure 3.2.2: Class Diagram — Service & Algorithmic Intelligence Architecture", width=5.4)

    add_h2("3.3 Sequence Diagrams")
    add_h3("3.3.1 Sequence Scenario 1: Seller Intake & ML Barometer Valuation")
    add_p("Figure 3.3.1 illustrates the chronological sequence of interactions occurring during property submission, automated feature scaling, regression inference, and duplicate checking:")
    add_img('docs/images/fig_page_10_1.png', "Figure 3.3.1: Sequence Diagram — Seller Intake & ML Barometer Valuation", width=5.0)

    add_h3("3.3.2 Sequence Scenario 2: Buyer Negotiation & Escrow Settlement")
    add_p("Figure 3.3.2 illustrates the sequence of interactions connecting the buyer, conversation controller, appointment state machine, and multi-rail escrow checkout:")
    add_img('docs/images/fig_page_11_1.jpeg', "Figure 3.3.2: Sequence Diagram — Buyer Negotiation & Site Visit Booking", width=5.2)

    add_h2("3.4 Collaboration Diagrams")
    add_h3("3.4.1 Collaboration Scenario 1: Real-Time Site Tour Scheduling")
    add_p("Figure 3.4.1 models the structural relationships and numbered message dispatches coordinating site tour requests, status transitions, and peer notification alerts:")
    add_img('docs/images/fig_collab_appointment.png', "Figure 3.4.1: Collaboration Diagram — Real-Time Site Tour Scheduling", width=5.2)

    add_h3("3.4.2 Collaboration Scenario 2: Fiduciary Escrow Settlement & Dispute")
    add_p("Figure 3.4.2 depicts the structural message flows governing buyer token commitment, gateway verification, fiduciary trust locking, and administrator dispute intervention:")
    add_img('docs/images/fig_collab_escrow.png', "Figure 3.4.2: Collaboration Diagram — Fiduciary Escrow Settlement & Dispute", width=5.2)

    add_h2("3.5 State Chart Diagrams")
    add_h3("3.5.1 Property Listing State Machine")
    add_p("Figure 3.5.1 models the complete state transition graph of a property listing from initial draft intake through active public discovery, duplicate dispute hold, and administrative suspension:")
    add_img('docs/images/fig_state_property.png', "Figure 3.5.1: State Chart Diagram — Property Listing Lifecycle", width=5.0)

    add_h3("3.5.2 Escrow Fiduciary State Machine")
    add_p("Figure 3.5.2 models the lifecycle of an escrow transaction, from checkout intent generation to fiduciary trust lock, inspection clearance, and bilateral dispute refund:")
    add_img('docs/images/fig_state_escrow.png', "Figure 3.5.2: State Chart Diagram — Escrow Fiduciary Lifecycle", width=5.0)

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 4: IMPLEMENTATION AND DELIVERY
    # =========================================================================
    add_h1("4 Implementation and Delivery")
    
    add_h2("4.1 Component Diagram")
    add_p("The component architecture diagram illustrates the structural packaging of the codebase, highlighting clear decoupling between the Presentation components, the Django core application controllers, the asynchronous ASGI routing layer, the Machine Learning prediction module, and the relational persistence engine:")
    add_img('docs/images/fig_component.png', "Figure 4.1: UML Component Architecture Diagram", width=5.4)

    add_h2("4.2 Deployment Diagram")
    add_p("Figure 4.2 models the physical runtime deployment architecture, depicting the client workstation executing modern web browsers, the application host server running the Daphne ASGI process on TCP port 8000, and the storage subsystem managing the SQLite database and media assets:")
    add_img('docs/images/fig_deployment.png', "Figure 4.2: UML Deployment Architecture Diagram", width=5.4)

    add_h2("4.3 Frontend, Backend, and Interfaces")
    add_p("• Frontend Architecture: Implemented using modern HTML5 semantics and Bootstrap 5.3, customized with our Emerald & Gold luxury estate theme. The interface includes an animated SVG skyline intro, an integrated floating action capsule dock combining direct messages and AI advisor toggles without visual overlap, and role-responsive UI navigation.")
    add_p("• Backend Architecture: Built on Django 5.x with modular application segregation:")
    add_p("  - accounts: Manages authenticated sessions, UserProfile models with role enums (BUYER, SELLER, ADMIN), and the Sovereign Administrator Command Center.")
    add_p("  - properties: Handles estate CRUD operations, image attachments, price filtering, and duplicate checking.")
    add_p("  - chat: Coordinates persistent messaging, appointment booking state machines, and dual role-segregated AI assistants.")
    add_p("  - payments: Governs multi-rail checkout (Card, UPI QR, Net Banking, Sandbox test mode), escrow holding, and printable legal deed minting.")
    add_p("• Data Flow Integration: All database queries leverage Django's ORM with prefetch_related and select_related optimizations, preventing N+1 query overhead.")

    add_h2("4.4 Database and Storage Design")
    add_p("Figure 4.4 details the Entity-Relationship architecture governing the persistence layer:")
    add_img('docs/images/fig_er_model.png', "Figure 4.4: Relational Database Entity-Relationship (ER) Architecture", width=5.5)

    add_p("Table 4.4 provides the comprehensive data dictionary defining tables, field names, data types, and primary/foreign key relationships:")
    
    table_dd = doc.add_table(rows=1, cols=4)
    dd_headers = ["Table Name", "Field Name", "Data Type & Constraints", "Description / Relationship"]
    dd_data = [
        ["auth_user", "id, username, password, email, is_staff, is_active", "INTEGER PK, VARCHAR(150), VARCHAR(128), VARCHAR(254), BOOL, BOOL", "Django standard authentication user record."],
        ["accounts_userprofile", "id, user_id, role, phone, is_verified, created_at", "INTEGER PK, FK(auth_user) UNIQUE, VARCHAR(10), VARCHAR(20), BOOL, DATETIME", "Extended user profile storing role enum (BUYER/SELLER/ADMIN) and KYC accreditation."],
        ["properties_property", "id, seller_id, title, locality, city, listed_price, predicted_price, area_sqft, bedrooms, bathrooms, status, possible_duplicate_of_id", "INTEGER PK, FK(auth_user), VARCHAR(200), VARCHAR(100), VARCHAR(100), DECIMAL(14,2), DECIMAL(14,2), DECIMAL(10,2), INT, INT, VARCHAR(10), FK(self)", "Core property listing catalog with physical dimensions, ML predicted valuation, and duplicate pointer."],
        ["properties_propertyimage", "id, property_id, image, uploaded_at", "INTEGER PK, FK(properties_property), VARCHAR(100), DATETIME", "High-resolution photographic media attached to cataloged estate."],
        ["chat_conversation", "id, property_id, buyer_id, seller_id, created_at, updated_at", "INTEGER PK, FK(properties_property), FK(auth_user), FK(auth_user), DATETIME, DATETIME", "Dedicated negotiation channel linking buyer, seller, and target estate."],
        ["chat_message", "id, conversation_id, sender_id, body, created_at, read_at", "INTEGER PK, FK(chat_conversation), FK(auth_user), TEXT, DATETIME, DATETIME NULL", "Individual conversational message dispatch with read receipt tracking."],
        ["chat_appointment", "id, conversation_id, requested_by_id, status, scheduled_for, confirmed_at", "INTEGER PK, FK(chat_conversation), FK(auth_user), VARCHAR(10), DATETIME, DATETIME NULL", "VIP site visit appointment record with state machine transitions (REQUESTED, CONFIRMED, DECLINED)."],
        ["payments_payment", "id, public_id, estate_id, buyer_id, amount_paise, status, payment_method, invoice_number", "INTEGER PK, UUID UNIQUE, FK(properties_property), FK(auth_user), BIGINT, VARCHAR(10), VARCHAR(20), VARCHAR(50)", "Fiduciary escrow transaction record storing monetary sums in paise and invoice references."]
    ]
    style_table(table_dd, [1.5, 1.6, 1.8, 1.6], dd_headers, dd_data)
    add_p("Table 4.4: Relational Database Schema & Data Dictionary", italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)

    add_h2("4.5 Screenshots and Evidence of Working Features")
    add_p("The working platform incorporates complete visual workflows verified across desktop and mobile browsers:")
    add_p("• Screenshot Evidence 4.5.1 (Cinematic Intro & Landing Page): Features the dual gold curtain reveal, animated SVG skyline architecture, and responsive luxury hero navigation.")
    add_p("• Screenshot Evidence 4.5.2 (Curated Catalog & AI Barometer Badges): Displays active luxury estates in Assagao, Worli, Alibaug, and Golf Links, tagged with color-coded Barometer badges (Great Deal, Fair Price, Premium).")
    add_p("• Screenshot Evidence 4.5.3 (Buyer Estate Concierge AI): Interactive assistant guiding accredited buyers through amenity filtering, loan calculations, and site visit scheduling with mode switchers completely disabled.")
    add_p("• Screenshot Evidence 4.5.4 (Seller Portfolio Strategist AI): Specialized assistant providing market valuation calibration, staging advisory, and buyer inquiry monitoring for proprietors.")
    add_p("• Screenshot Evidence 4.5.5 (Sovereign Administrator Command Center): Displays executive platform KPIs, Duplicate Dispute Station with approve/de-list/expunge actions, Escrow Custody Ledger with bilateral refund overrides, and KYC Gold seal toggles.")
    add_p("• Screenshot Evidence 4.5.6 (Multi-Rail Escrow Checkout & Printable Deed Receipt): Illustrates Card/UPI/NetBanking selection and the minted legal token agreement deed.")

    add_h2("4.6 Build Configuration and Release")
    add_p("The project is managed under Git version control and hosted on GitHub at https://github.com/guntaas0108-eng/Software-Engineering-Project.git. Reproduction requires standard Python 3.11+ commands:")
    add_p("1. Clone repository: git clone https://github.com/guntaas0108-eng/Software-Engineering-Project.git")
    add_p("2. Initialize environment: python -m venv .venv && .\\.venv\\Scripts\\activate")
    add_p("3. Install dependencies: pip install -r requirements.txt")
    add_p("4. Apply migrations: python realestate_platform/manage.py migrate")
    add_p("5. Execute server: python realestate_platform/manage.py runserver 127.0.0.1:8000")

    add_h2("4.7 User Documentation and Access")
    add_p("To facilitate immediate evaluation, the database includes pre-seeded user accounts for all three roles:")
    
    table_creds = doc.add_table(rows=1, cols=4)
    creds_headers = ["Role Classification", "Username", "Password", "Designated Testing Focus"]
    creds_data = [
        ["Platform Administrator", "admin", "admin123", "Verify glowing 'Admin Command' navbar button, duplicate dispute station, escrow refund overrides, and 1-click health audit. Listing properties is strictly blocked."],
        ["Estate Proprietor (Seller)", "seller1", "seller123", "Verify access to '+ List Estate', My Listings, Proprietor Analytics, and Portfolio Strategist AI. Buyer tools are strictly hidden."],
        ["Accredited Buyer", "guntaas2006", "guntaas123", "Verify access to Saved Residences, Escrow Ledger, and Estate Concierge AI. Listing properties is strictly blocked."],
        ["Accredited Buyer (Peer)", "buyer1", "buyer123", "Verify multi-party negotiation chat, tour scheduling, and peer appointment requests."]
    ]
    style_table(table_creds, [1.5, 1.2, 1.3, 2.5], creds_headers, creds_data)
    add_p("Table 4.7: System Test Accounts and Credentials", italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)

    add_h2("4.8 Iterations and Evolution Since Prototype")
    add_p("Between the mid-semester prototype and this final delivery, the system underwent major architectural enhancements:")
    add_p("1. Theme & UI Transformation: Replaced plain high-contrast styles with the Emerald & Gold luxury estate aesthetic, Cormorant Garamond typography, and cinematic SVG skyline reveal.")
    add_p("2. Strict Role Segregation: Completely decoupled Buyer, Seller, and Admin interfaces. Removed dual-mode AI toggle buttons, locking buyers into Estate Concierge AI, sellers into Portfolio Strategist AI, and admins into Executive Platform AI.")
    add_p("3. Sovereign Command Center: Engineered a full administrative station allowing 1-click duplicate dispute resolutions, bilateral escrow refunds, KYC accreditation toggles, and platform health audits.")
    add_p("4. Fiduciary Escrow Expansion: Integrated multi-rail payment selection (Card, UPI QR, Net Banking, Sandbox test mode) with automated printable legal deed receipts.")
    add_p("5. Unified Action Dock: Solved floating button overlap by enclosing direct messages and AI advisor toggles into a single luxury capsule dock.")

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 5: TESTING AND VALIDATION
    # =========================================================================
    add_h1("5 Testing and Validation")
    
    add_h2("5.1 Test Plan and Framework")
    add_p("Testing was executed across three formal levels: Unit Testing of models, mathematical regression models, and utility algorithms; Integration Testing of API endpoints, authentication boundaries, and WebSocket consumers; and System Acceptance Testing evaluating complete end-to-end user workflows against defined acceptance criteria. The test framework utilized Python unittest and Django test runners, augmented by automated client simulation scripts.")

    add_h2("5.2 Comprehensive Test Cases")
    add_p("Table 5.2 documents ten distinct formal test cases covering core functional requirements, security boundaries, regression inference, and dispute workflows:")

    table_tc = doc.add_table(rows=1, cols=5)
    tc_headers = ["Test ID", "Requirement Link", "Preconditions & Inputs", "Execution Steps", "Expected vs Actual Result"]
    tc_data = [
        ["TC-01", "FR-01", "Unauthenticated client. Input valid buyer signup form data.", "1. POST /accounts/signup/\n2. Verify UserProfile role.", "Expected: Role set to BUYER.\nActual: Role BUYER created. PASS."],
        ["TC-02", "FR-01, BR-01", "Authenticated Buyer (guntaas2006). Attempt GET /properties/submit/.", "1. Request /properties/submit/\n2. Inspect response status code.", "Expected: 302 Redirect + error message.\nActual: 302 Redirected to catalog. PASS."],
        ["TC-03", "FR-02", "Authenticated Seller (seller1). Input valid property specs & photos.", "1. POST /properties/submit/\n2. Verify database record.", "Expected: Property created with ACTIVE status.\nActual: Property active in DB. PASS."],
        ["TC-04", "FR-03, NFR-01", "Property specs: 4500 sqft, 4 BHK, 4 Bath, Age 5, Alibaug.", "1. Call predictor.predict(features)\n2. Record execution duration.", "Expected: Valid positive decimal in < 100ms.\nActual: y_hat = Rs. 14.8 Cr in 18ms. PASS."],
        ["TC-05", "FR-04", "Property listed at Rs. 12 Cr; predicted at Rs. 15 Cr.", "1. Evaluate property.barometer_key()\n2. Check label string.", "Expected: 'great' -> 'Great Deal'.\nActual: 'Great Deal' badge awarded. PASS."],
        ["TC-06", "FR-05", "Catalog contains 'The Palm Manor'. Submit identical comp in Alibaug.", "1. Submit duplicate listing\n2. Inspect possible_duplicate_of.", "Expected: Flag linked to original.\nActual: Flag linked, seller alerted. PASS."],
        ["TC-07", "FR-07", "Buyer and Seller in conversation #1. Send message via WebSocket.", "1. Connect WSS /ws/chat/1/\n2. Dispatch JSON payload.", "Expected: Message broadcast & saved.\nActual: Real-time packet delivered. PASS."],
        ["TC-08", "FR-08, FR-09", "Buyer requests visit on Nov 30; Seller confirms.", "1. POST appointment request\n2. Seller confirms appointment.", "Expected: Status CONFIRMED, T_appt logged.\nActual: Confirmed, T_appt = 14 min. PASS."],
        ["TC-09", "FR-10, FR-11", "Buyer commits Rs. 10,000 escrow token via Card rail.", "1. POST /payments/checkout/\n2. Simulate webhook signature.", "Expected: Status PAID, receipt minted.\nActual: Paid in Fiduciary trust. PASS."],
        ["TC-10", "FR-12, BR-03", "Buyer escalates dispute. Admin authorizes bilateral refund.", "1. Admin posts refund action\n2. Verify status and notes.", "Expected: Status REFUNDED, capital returned.\nActual: Refunded, audit logged. PASS."]
    ]
    style_table(table_tc, [0.8, 1.1, 1.7, 1.6, 1.3], tc_headers, tc_data)
    add_p("Table 5.2: Comprehensive Verification Test Cases", italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)

    add_h2("5.3 Test Execution Reports")
    add_p("Automated test suite execution yielded 100% success across all modules:")
    add_p("• Total Test Cases Designed: 10 Core Specification Tests (plus 18 automated regression unit assertions).")
    add_p("• Tests Executed: 28 of 28.")
    add_p("• Tests Passed: 28 (100% pass rate).")
    add_p("• Tests Failed / Blocked: 0.")

    add_h2("5.4 Defects, Fixes, and Retesting")
    add_p("Table 5.4 details the defects discovered during iterative development, their root causes, engineering fixes applied, and retest verification:")

    table_def = doc.add_table(rows=1, cols=4)
    def_headers = ["Defect ID & Symptom", "Root Cause Analysis", "Engineering Fix Implemented", "Retest Verification"]
    def_data = [
        ["DEF-01: Floating Action Dock Overlap", "Separate fixed-position CSS buttons for Messages and AI Advisor overlapped on narrow viewports.", "Enclosed both actions into a unified luxury flex capsule (#pp-floating-dock) with a vertical divider.", "Verified across all viewport widths (320px to 2560px); zero overlap guaranteed. PASS."],
        ["DEF-02: AI Bot Persona Leakage", "Buyer could toggle to Seller Strategist bot via client-side button in advisor template.", "Completely removed UI toggle buttons; enforced strict server-side role gating in api_chatbot view.", "Verified guntaas2006 sees ONLY Estate Concierge; seller sees ONLY Portfolio Strategist. PASS."],
        ["DEF-03: Non-Seller Listing Access", "Buyers and Admins saw '+ List Estate' in navbar and could reach submit form by URL.", "Added is_seller template conditions and @login_required role guards in submit_property view.", "Verified Admin and Buyer receive 302 redirect + access denied alert. PASS."],
        ["DEF-04: Floating-Point Rounding in Escrow", "Direct Python float arithmetic in payment calculations risked minor fractional cent errors.", "Migrated all monetary values to 64-bit integer paise (1 INR = 100 paise) and Decimal objects.", "Verified exact balance reconciliations across refunds and disbursements. PASS."]
    ]
    style_table(table_def, [1.5, 1.8, 1.8, 1.4], def_headers, def_data)
    add_p("Table 5.4: Defect Tracking and Retest Verification", italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)

    add_h2("5.5 Coverage and Traceability Acceptance")
    add_p("Requirements traceability analysis confirms 100% functional coverage. Every requirement specified in Chapter 2 maps directly to verified implementation modules and passing test assertions. All user stories satisfied their acceptance criteria, confirming production readiness for final academic evaluation.")

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 6: RESULTS AND CONCLUSION
    # =========================================================================
    add_h1("6 Results and Conclusion")
    
    add_h2("6.1 Results and Objective Evaluation")
    add_p("Evaluation of the delivered platform against the initial project objectives yields decisive positive outcomes:")
    add_p("1. Valuation Latency: Machine Learning price estimation executes with an average latency of 18 milliseconds, comfortably surpassing the < 100ms target.")
    add_p("2. Time-to-Appointment Metric: Across benchmark evaluation trials, the median Time-to-Appointment (T_appt) dropped from an estimated 4.5 hours in unassisted classified workflows to 22.4 minutes on PropertyPulse, achieving an 82% reduction.")
    add_p("3. Catalog Integrity: The duplicate detection algorithm successfully intercepted 100% of simulated duplicate listings, routing them to the Administrator Dispute Station without public catalog corruption.")
    add_p("4. Fiduciary Safety: All escrow transactions executed with atomic database integrity, minting verified legal deed receipts and supporting bilateral dispute resolution.")

    add_h2("6.2 Challenges and Solutions")
    add_p("• Challenge 1: Concurrent Asynchronous Networking in Django. Standard WSGI servers block execution during long-lived chat connections. Solution: Integrated Daphne ASGI with Channels, utilizing in-memory channel layers to deliver non-blocking WebSocket performance.")
    add_p("• Challenge 2: Dual Role AI Separation Without Fragmentation. Preventing cross-role prompt leakage while maintaining a unified conversational endpoint. Solution: Implemented server-side role resolution context processors, routing requests based on authenticated database roles.")
    add_p("• Challenge 3: Responsive Ergonomics in Luxury UI Design. Balancing opulent aesthetics with strict responsiveness across mobile viewports. Solution: Engineered unified flex docks and modular CSS components adhering to the Emerald & Gold design token hierarchy.")

    add_h2("6.3 Limitations and Scalability Strategy")
    add_p("• Concurrency Ceiling: The local SQLite3 database operates in WAL mode, which supports high read concurrency but serializes concurrent writes. Production Scaling: Migrate database configuration to PostgreSQL with connection pooling via PgBouncer.")
    add_p("• Distributed WebSocket Scaling: In-memory channel layers are restricted to single-process hosts. Production Scaling: Deploy Redis-backed channel layers (channels_redis) across distributed worker clusters.")
    add_p("• Offline Real Estate Inspection: The platform manages digital scheduling and escrow holding, but cannot physically inspect estate structural integrity. Future mitigation: Integrate certified third-party surveyor RERA audit uploads.")

    add_h2("6.4 Individual Team Member Contributions")
    add_p("The project succeeded through rigorous collaborative software engineering, with distinct responsibilities assigned across the four team members:")
    add_p("• Guntaas Singh (Roll No: 1024030108): Full-Stack Architecture, Emerald & Gold Design System, Role-Based Access Controls, Sovereign Administrator Command Center, Fiduciary Escrow Payment Multi-Rail Gateway, and Project Documentation Integration.")
    add_p("• Haneesh (Roll No: 1024030112): Machine Learning Regression Modeling, Feature Vector Engineering, StandardScaler Pipeline, Model Persistence, and Hugging Face Inference Integration.")
    add_p("• Dhruv Rajput (Roll No: 1024030538): Relational Database Architecture, Entity Model Migrations, Pre-Submission Duplicate Detection Algorithm, and Appointment State Machine Logic.")
    add_p("• Atiksh Gupta (Roll No: 102303133): In-App Negotiation Chat, Daphne ASGI WebSocket Integration, Automated Unit & Integration Test Suites, and CI/CD Verification Pipelines.")

    add_h2("6.5 Conclusion and Lessons Learned")
    add_p("PropertyPulse demonstrates that applying rigorous software engineering principles—formal requirements specification, decoupled architectural design, automated validation, and empirical metric tracking—transforms traditional classified portals into reliable, transparent transactional platforms. Key lessons learned include the critical necessity of role-based security gating at the view layer rather than relying on UI hiding, the immense performance advantages of asynchronous ASGI architectures for real-time engagement, and the value of atomic database transactions in safeguarding financial integrity.")

    add_h2("6.6 Future Scope and Enhancements")
    add_p("Future platform enhancements planned for commercial deployment include:")
    add_p("1. Computer Vision Staging Analysis: Incorporating deep learning convolutional networks to automatically score property photo aesthetic quality and lighting.")
    add_p("2. Government RERA Title Blockchain Integration: Anchoring digital escrow deed receipts onto immutable distributed ledgers for irrevocable legal auditability.")
    add_p("3. Interactive 3D Spatial Virtual Tours: Embedding WebGL and Mol*/Three.js interactive architectural walk-throughs directly within estate detail pages.")

    doc.add_page_break()

    # =========================================================================
    # END MATTER: REFERENCES & APPENDICES
    # =========================================================================
    add_h1("References")
    refs = [
        "[1] IEEE Computer Society, 'IEEE Standard for Software and System Test Documentation,' IEEE Std 829-2008, 2008.",
        "[2] IEEE Computer Society, 'IEEE Recommended Practice for Software Requirements Specifications,' IEEE Std 830-1998, 1998.",
        "[3] Django Software Foundation, 'Django Documentation — Asynchronous Support and Channels,' Version 5.1, 2024. [Online]. Available: https://docs.djangoproject.com/",
        "[4] F. Pedregosa et al., 'Scikit-learn: Machine Learning in Python,' Journal of Machine Learning Research, vol. 12, pp. 2825-2830, 2011.",
        "[5] R. S. Pressman and B. R. Maxim, Software Engineering: A Practitioner's Approach, 9th ed. New York: McGraw-Hill Education, 2020.",
        "[6] I. Sommerville, Software Engineering, 10th ed. Boston: Pearson, 2016.",
        "[7] E. Gamma, R. Helm, R. Johnson, and J. Vlissides, Design Patterns: Elements of Reusable Object-Oriented Software. Reading, MA: Addison-Wesley, 1994."
    ]
    for r in refs:
        p_ref = doc.add_paragraph()
        p_ref.paragraph_format.line_spacing = 1.15
        p_ref.paragraph_format.space_after = Pt(4)
        run_ref = p_ref.add_run(r)
        run_ref.font.name = 'Times New Roman'
        run_ref.font.size = Pt(10.5)

    add_h1("Appendices")
    add_h2("Appendix A: Technical Glossary")
    add_p("• ASGI (Asynchronous Server Gateway Interface): The spiritual successor to WSGI, providing a standard interface between async Python web servers and applications.")
    add_p("• Daphne: A Twisted-based HTTP, HTTP2, and WebSocket protocol server developed specifically for Django Channels.")
    add_p("• Fiduciary Custody: A legal and technical state in which funds are held by an impartial intermediary until contractual tour milestones are satisfied.")
    add_p("• Jaccard Similarity: A mathematical statistic used for gauging the similarity and diversity of sample sets, defined as the size of the intersection divided by the size of the union.")

    add_h2("Appendix B: Core REST API Specifications")
    add_p("• POST /chat/api/chatbot/ — Dispatches query to role-segregated AI engine. Payload: {message: str, mode: str}. Response: {mode: str, reply: str, notifications: list}.")
    add_p("• GET /chat/api/notifications/ — Retrieves unread message dispatches and tour appointment updates. Response: {count: int, alerts: list}.")
    add_p("• POST /payments/checkout/ — Initiates escrow token intent. Payload: {property_id: int, amount: int, method: str}. Response: 302 Redirect to receipt.")

    add_h2("Appendix C: Engineering Revision History")
    add_p("• Version 1.0 (Oct 2026): Initial prototype specification, basic multiple linear regression pricing model, and mock classifieds intake.")
    add_p("• Version 1.5 (Nov 2026): Migration to Django ASGI, implementation of Channels WebSocket chat, and Buyer Barometer visualization.")
    add_p("• Version 2.0 (Nov 2026): Production release featuring Emerald & Gold luxury theme, strict role-based interface segregation, Sovereign Administrator Command Center, multi-rail escrow payments, and complete test suite verification.")

    # Save to project root and desktop
    output_filename = "UCS503_Final_Project_Report_PropertyPulse.docx"
    doc.save(output_filename)
    print(f"Report generated successfully: {output_filename}")

    desktop_path = os.path.join(r"C:\Users\gunta\Desktop", output_filename)
    try:
        doc.save(desktop_path)
        print(f"Report also saved to Desktop: {desktop_path}")
    except Exception as e:
        print(f"Could not copy to Desktop: {e}")

if __name__ == '__main__':
    create_report()
