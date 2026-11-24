import docx
import os

doc = docx.Document('UCS503_Final_Project_Report_PropertyPulse.docx')

fig_map = {
    'Figure 2.2.1': 'docs/images/fig_page_8_1.jpeg',
    'Figure 2.3.1': 'docs/images/fig_swimlane.png',
    'Figure 2.4.1a': 'docs/images/fig_page_6_1.png',
    'Figure 2.4.1b': 'docs/images/fig_page_7_1.jpeg',
    'Figure 2.4.2': 'docs/images/fig_dfd_lvl0.png',
    'Figure 2.4.3': 'docs/images/fig_dfd_lvl1.png',
    'Figure 2.4.4': 'docs/images/fig_dfd_lvl2.png',
    'Figure 3.2.1': 'docs/images/fig_page_9_1.png',
    'Figure 3.2.2': 'docs/images/fig_class_service.png',
    'Figure 3.3.1': 'docs/images/fig_page_10_1.png',
    'Figure 3.3.2': 'docs/images/fig_page_11_1.jpeg',
    'Figure 3.4.1': 'docs/images/fig_collab_appointment.png',
    'Figure 3.4.2': 'docs/images/fig_collab_escrow.png',
    'Figure 3.5.1': 'docs/images/fig_state_property.png',
    'Figure 3.5.2': 'docs/images/fig_state_escrow.png',
    'Figure 4.1': 'docs/images/fig_component.png',
    'Figure 4.2': 'docs/images/fig_deployment.png',
    'Figure 4.4': 'docs/images/fig_er_model.png',
}

tbl_idx = 0
def table_to_md(tbl):
    rows = []
    for r_idx, row in enumerate(tbl.rows):
        cells = [c.text.replace('\n', '<br>') for c in row.cells]
        rows.append('| ' + ' | '.join(cells) + ' |')
        if r_idx == 0:
            rows.append('| ' + ' | '.join(['---'] * len(cells)) + ' |')
    return '\n'.join(rows)

out = []
out.append('# PROPERTYPULSE: CURATED LUXURY REAL ESTATE MARKETPLACE, AI VALUATION BAROMETER, AND FIDUCIARY ESCROW PLATFORM\n')
out.append('**Course**: UCS503 / UCS503P — Software Engineering Lab  ')
out.append('**Academic Institution**: Computer Science and Engineering Department, Thapar Institute of Engineering and Technology, Patiala  ')
out.append('**Evaluator / Faculty Supervisor**: Anushka  ')
out.append('**Laboratory Group**: Group 3C14  ')
out.append('**Student Authors**:  ')
out.append('- Guntaas Singh (Roll No. `1024030108`)  ')
out.append('- Haneesh (Roll No. `1024030112`)  ')
out.append('- Dhruv Rajput (Roll No. `1024030538`)  ')
out.append('- Atiksh Gupta (Roll No. `102303133`)  ')
out.append('**Academic Semester**: End-Semester Evaluation (November 2026)\n')
out.append('---\n')

for p in doc.paragraphs:
    txt = p.text.strip()
    if not txt:
        continue
    style = p.style.name
    if style == 'Heading 1':
        out.append(f'\n# {txt}\n')
    elif style == 'Heading 2':
        out.append(f'\n## {txt}\n')
    elif style == 'Heading 3':
        out.append(f'\n### {txt}\n')
    elif txt.startswith('Figure '):
        fig_key = txt.split(':')[0].strip()
        img_path = fig_map.get(fig_key, '')
        if img_path:
            out.append(f'\n![{txt}]({img_path})\n')
        out.append(f'*{txt}*\n')
    elif txt.startswith('Table '):
        if tbl_idx < len(doc.tables):
            out.append('\n' + table_to_md(doc.tables[tbl_idx]) + '\n')
            tbl_idx += 1
        out.append(f'*{txt}*\n')
    else:
        out.append(f'{txt}\n')

with open('FINAL_PROJECT_REPORT.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print(f'FINAL_PROJECT_REPORT.md updated with {tbl_idx} tables and embedded figures!')
