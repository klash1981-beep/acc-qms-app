import streamlit as st
from fpdf import FPDF
from datetime import datetime

st.set_page_config(page_title="ACC - Banan WIR System", page_icon="🏗️", layout="wide")

st.markdown("""
    <style>
    .main-title {
        font-size: 26px;
        font-weight: bold;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 18px;
        color: #374151;
        text-align: center;
        margin-bottom: 20px;
    }
    .section-header {
        background-color: #1E3A8A;
        color: white;
        padding: 6px 12px;
        font-weight: bold;
        border-radius: 4px;
        margin-top: 15px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">ALEXANDRIA CONSTRUCTION CO. (ACC)</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Banan Al-Riyadh Project (Package BB1.2) — Work Inspection Request (WIR)</div>', unsafe_allow_html=True)

with st.form("wir_full_form"):
    st.markdown('<div class="section-header">1. General Project & Request Information</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        wir_no = st.text_input("WIR Reference No.", value="ACC-BB1.2-WIR-001")
        date_raised = st.date_input("Inspection Date", value=datetime.now())
    with c2:
        time_raised = st.time_input("Inspection Time", value=datetime.now().time())
        subcontractor = st.text_input("Subcontractor Name", value="Civil Contracting Co.")
    with c3:
        discipline = st.selectbox("Discipline", ["Civil / Structural", "Architectural", "MEP", "Infrastructure"])
        itp_ref = st.text_input("ITP Ref / Stage Code", value="ITP-03-01 (Concrete)")

    st.markdown('<div class="section-header">2. Location & Element Details</div>', unsafe_allow_html=True)
    c4, c5, c6 = st.columns(3)
    with c4:
        building_no = st.text_input("Building / Zone No.", value="B20")
        model = st.text_input("Model / Sector", value="R2")
    with c5:
        floor = st.text_input("Floor / Level", value="Ground Floor (GF)")
        unit = st.text_input("Unit / Apartment No.", value="Apt 01")
    with c6:
        grid_axes = st.text_input("Grid Lines / Axes", value="Axes A-D / 1-5")
        drawing_no = st.text_input("Approved Drawing Ref & Rev", value="BANAN-STR-DWG-102 Rev.0")

    st.markdown('<div class="section-header">3. Inspection Details & Description</div>', unsafe_allow_html=True)
    description = st.text_area("Detailed Description of Work to be Inspected", 
                               value="Inspection of reinforcement steel, formwork shuttering, and cleanliness prior to concrete casting for GF columns.")
    
    c7, c8 = st.columns(2)
    with c7:
        activity_id = st.text_input("Activity ID (Primavera/Schedule)", value="ACT-CIV-2026-089")
    with c8:
        quality_spec = st.text_input("Specification Ref / Standard", value="Spec 033000 - Cast-in-Place Concrete")

    st.markdown('<div class="section-header">4. Quality & Verification Checklist</div>', unsafe_allow_html=True)
    ck1 = st.checkbox("Approved Shop Drawings & Bar Bending Schedules (BBS) available on site", value=True)
    ck2 = st.checkbox("Materials inspected, approved, and matching project specifications", value=True)
    ck3 = st.checkbox("Levels, alignment, and structural dimensions verified", value=True)
    ck4 = st.checkbox("Site cleanliness and safety requirements fulfilled", value=True)

    st.markdown('<div class="section-header">5. Inspection Result & Comments</div>', unsafe_allow_html=True)
    status = st.radio("Inspection Status / Recommendation", ["Approved (A)", ["Approved with Comments (B)"], "Rejected (C)"], index=0)
    comments = st.text_area("Consultant / Inspector Comments (if any)", value="Approved to proceed with casting. Ensure proper vibration during pouring.")

    st.markdown('<div class="section-header">6. Signatures & Personnel</div>', unsafe_allow_html=True)
    c9, c10 = st.columns(2)
    with c9:
        site_engineer = st.text_input("ACC Site Engineer", value="Eng. Mahmoud Amin")
        qc_engineer = st.text_input("ACC Quality Manager / QC Engineer", value="Eng. Khaled Samy")
    with c10:
        consultant_eng = st.text_input("Consultant Engineer Name", value="Eng. Hany Mohamed")

    submit_btn = st.form_submit_button("🔨 Generate Official WIR PDF Report")

if submit_btn:
    try:
        class WIR_PDF(FPDF):
            def header(self):
                self.set_fill_color(30, 58, 138)
                self.rect(10, 8, 190, 18, 'F')
                self.set_text_color(255, 255, 255)
                self.set_font("Arial", 'B', 13)
                self.set_xy(10, 12)
                self.cell(190, 10, "ALEXANDRIA CONSTRUCTION CO. (ACC) — QUALITY SYSTEM", align='C')
                self.ln(12)

            def footer(self):
                self.set_y(-15)
                self.set_font("Arial", 'I', 8)
                self.set_text_color(128, 128, 128)
                self.cell(0, 10, f"Banan Al-Riyadh Project (BB1.2) | WIR Ref: {wir_no} | Page {self.page_no()}", align='C')

        pdf = WIR_PDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)

        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 8, "WORK INSPECTION REQUEST (WIR)", ln=True, align='C')
        pdf.ln(3)

        def make_table_header(title):
            pdf.set_fill_color(220, 230, 242)
            pdf.set_font("Arial", 'B', 10)
            pdf.set_text_color(30, 58, 138)
            pdf.cell(190, 7, f"  {title}", 1, 1, 'L', True)
            pdf.set_text_color(0, 0, 0)

        def cell_pair(l1, v1, l2, v2, w1=35, w2=60, w3=35, w4=60):
            pdf.set_font("Arial", 'B', 9)
            pdf.set_fill_color(245, 247, 250)
            pdf.cell(w1, 6, str(l1), 1, 0, 'L', True)
            pdf.set_font("Arial", '', 9)
            pdf.cell(w2, 6, str(v1), 1, 0, 'L')
            pdf.set_font("Arial", 'B', 9)
            pdf.cell(w3, 6, str(l2), 1, 0, 'L', True)
            pdf.set_font("Arial", '', 9)
            pdf.cell(w4, 6, str(v2), 1, 1, 'L')

        # Section 1
        make_table_header("1. GENERAL INFORMATION")
        cell_pair("WIR Ref No:", wir_no, "Date / Time:", f"{date_raised} @ {time_raised}")
        cell_pair("Discipline:", discipline, "Subcontractor:", subcontractor)
        cell_pair("ITP Ref Code:", itp_ref, "Activity ID:", activity_id)
        pdf.ln(3)

        # Section 2
        make_table_header("2. LOCATION & DRAWING REFERENCE")
        cell_pair("Building / Zone:", building_no, "Model / Sector:", model)
        cell_pair("Floor / Level:", floor, "Unit / Apt No:", unit)
        cell_pair("Grid Axes:", grid_axes, "Drawing Ref:", drawing_no)
        pdf.ln(3)

        # Section 3
        make_table_header("3. WORK DESCRIPTION & SPECIFICATION")
        pdf.set_font("Arial", 'B', 9)
        pdf.set_fill_color(245, 247, 250)
        pdf.cell(40, 6, "Specification Ref:", 1, 0, 'L', True)
        pdf.set_font("Arial", '', 9)
        pdf.cell(150, 6, str(quality_spec), 1, 1, 'L')
        pdf.set_font("Arial", 'B', 9)
        pdf.cell(190, 6, "Description of Inspected Work:", 1, 1, 'L', True)
        pdf.set_font("Arial", '', 9)
        pdf.multi_cell(190, 5, str(description), 1, 'L')
        pdf.ln(3)

        # Section 4
        make_table_header("4. VERIFICATION CHECKLIST")
        pdf.set_font("Arial", '', 8.5)
        pdf.cell(190, 5, f"[{'X' if ck1 else ' '}] Approved Shop Drawings & BBS available on site", 1, 1, 'L')
        pdf.cell(190, 5, f"[{'X' if ck2 else ' '}] Materials inspected, approved, and matching project specifications", 1, 1, 'L')
        pdf.cell(190, 5, f"[{'X' if ck3 else ' '}] Levels, alignment, and structural dimensions verified", 1, 1, 'L')
        pdf.cell(190, 5, f"[{'X' if ck4 else ' '}] Site cleanliness and safety requirements fulfilled", 1, 1, 'L')
        pdf.ln(3)

        # Section 5
        make_table_header("5. INSPECTION STATUS & CONSULTANT COMMENTS")
        pdf.set_font("Arial", 'B', 10)
        status_text = f"RECOMMENDATION STATUS: {status}"
        pdf.cell(190, 7, status_text, 1, 1, 'C', False)
        pdf.set_font("Arial", 'B', 9)
        pdf.set_fill_color(245, 247, 250)
        pdf.cell(190, 6, "Consultant Remarks / Instructions:", 1, 1, 'L', True)
        pdf.set_font("Arial", '', 9)
        pdf.multi_cell(190, 5, str(comments) if comments else "N/A", 1, 'L')
        pdf.ln(3)

        # Section 6
        make_table_header("6. SIGNATURES & APPROVALS")
        pdf.set_font("Arial", 'B', 8.5)
        pdf.cell(63, 6, "ACC Site Engineer", 1, 0, 'C', True)
        pdf.cell(63, 6, "ACC Quality Engineer", 1, 0, 'C', True)
        pdf.cell(64, 6, "Consultant Engineer", 1, 1, 'C', True)
        pdf.set_font("Arial", '', 8.5)
        pdf.cell(63, 10, f"Name: {site_engineer}\nSign: _____________", 1, 0, 'C')
        pdf.cell(63, 10, f"Name: {qc_engineer}\nSign: _____________", 1, 0, 'C')
        pdf.cell(64, 10, f"Name: {consultant_eng}\nSign: _____________", 1, 1, 'C')

        pdf_bytes = pdf.output(dest='S').encode('latin1')

        st.success("✅ WIR Report generated successfully with full project fields!")
        st.download_button(
            label="📥 Download Official WIR PDF Report",
            data=pdf_bytes,
            file_name=f"{wir_no}.pdf",
            mime="application/pdf"
        )
    except Exception as e:
        st.error(f"Error generating PDF: {e}")
