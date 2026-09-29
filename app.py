import streamlit as st
from fpdf import FPDF
from datetime import datetime

st.set_page_config(page_title="ACC - Banan WIR Official System", page_icon="🏗️", layout="wide")

st.markdown("""
    <style>
    .main-header {
        background-color: #1a365d;
        color: white;
        padding: 12px;
        text-align: center;
        font-weight: bold;
        font-size: 22px;
        border-radius: 5px;
        margin-bottom: 15px;
    }
    .sec-header {
        background-color: #2b6cb0;
        color: white;
        padding: 6px 12px;
        font-weight: bold;
        font-size: 14px;
        border-radius: 3px;
        margin-top: 15px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">ALEXANDRIA CONSTRUCTION CO. (ACC)<br><span style="font-size: 15px; font-weight: normal;">Banan Al-Riyadh Project (BB1.2) - Work Inspection Request (WIR)</span></div>', unsafe_allow_html=True)

with st.form("wir_complete_form"):
    st.markdown('<div class="sec-header">1. GENERAL PROJECT & REQUEST INFORMATION</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        wir_no = st.text_input("WIR Reference No.", value="ACC-BB1.2-WIR-001")
        date_raised = st.date_input("Inspection Date", value=datetime.now())
    with c2:
        time_raised = st.time_input("Inspection Time", value=datetime.now().time())
        contractor = st.text_input("Main Contractor", value="Alexandria Construction Co. (ACC)")
    with c3:
        subcontractor = st.text_input("Subcontractor Name", value="Civil Works Subcontractor")
        discipline = st.selectbox("Discipline / Trade", ["Civil / Structural", "Architectural", "MEP - Electrical", "MEP - Plumbing", "Infrastructure"])

    st.markdown('<div class="sec-header">2. LOCATION & SCOPE DETAILS</div>', unsafe_allow_html=True)
    c4, c5, c6 = st.columns(3)
    with c4:
        building_no = st.text_input("Building / Zone No.", value="B20")
        model = st.text_input("Model / Sector", value="R2")
    with c5:
        floor = st.text_input("Floor / Level", value="Ground Floor (GF)")
        unit = st.text_input("Unit / Apartment No.", value="Apt 01")
    with c6:
        grid_axes = st.text_input("Grid Lines / Axes / Space", value="Axes A-D / 1-5")
        drawing_no = st.text_input("Approved Drawing Ref & Rev", value="BANAN-STR-DWG-102 Rev.0")

    st.markdown('<div class="sec-header">3. WORK DETAILS & SPECIFICATIONS</div>', unsafe_allow_html=True)
    c7, c8, c9 = st.columns(3)
    with c7:
        itp_ref = st.text_input("ITP Ref / Stage Code", value="ITP-03-01 (Concrete)")
    with c8:
        activity_id = st.text_input("Activity ID (Schedule)", value="ACT-CIV-2026-089")
    with c9:
        quality_spec = st.text_input("Specification Ref / Standard", value="Spec 033000 - Cast-in-Place Concrete")

    description = st.text_area("Detailed Description of Work to be Inspected", 
                               value="Inspection of reinforcement steel, formwork shuttering, and cleanliness prior to concrete casting for GF columns.")

    st.markdown('<div class="sec-header">4. QUALITY CONTROL CHECKLIST</div>', unsafe_allow_html=True)
    ck1 = st.checkbox("Approved Shop Drawings & BBS available on site", value=True)
    ck2 = st.checkbox("Materials inspected, approved, and compliant with specifications", value=True)
    ck3 = st.checkbox("Levels, alignment, and structural dimensions verified", value=True)
    ck4 = st.checkbox("Previous non-conformances / observations closed satisfactorily", value=True)
    ck5 = st.checkbox("Site cleanliness and safety standards maintained", value=True)

    st.markdown('<div class="sec-header">5. INSPECTION DECISION & CONSULTANT REMARKS</div>', unsafe_allow_html=True)
    status = st.radio("Inspection Decision Status", ["Approved (A)", "Approved with Comments (B)", "Revise & Resubmit (C)", "Rejected (D)"], index=0)
    comments = st.text_area("Consultant / Inspector Remarks", value="Approved to proceed with concrete pouring. Ensure proper vibration during casting.")

    st.markdown('<div class="sec-header">6. SIGNATURES & PERSONNEL</div>', unsafe_allow_html=True)
    s1, s2, s3 = st.columns(3)
    with s1:
        site_engineer = st.text_input("ACC Site Engineer", value="Eng. Mahmoud Amin")
    with s2:
        qc_engineer = st.text_input("ACC Quality Engineer / Manager", value="Eng. Khaled Samy")
    with s3:
        consultant_eng = st.text_input("Consultant Engineer Name", value="Eng. Hany Mohamed")

    submit_btn = st.form_submit_button("🔨 إصدار تقرير WIR الرسمي (PDF)")

if submit_btn:
    try:
        class FullWIRPDF(FPDF):
            def header(self):
                # Header Banner
                self.set_fill_color(26, 54, 93)
                self.rect(10, 8, 190, 20, 'F')
                self.set_text_color(255, 255, 255)
                self.set_font("Arial", 'B', 13)
                self.set_xy(10, 11)
                self.cell(190, 7, "ALEXANDRIA CONSTRUCTION CO. (ACC)", align='C', ln=True)
                self.set_font("Arial", '', 9.5)
                self.cell(190, 6, "BANAN AL-RIYADH PROJECT (BB1.2) - QUALITY MANAGEMENT SYSTEM", align='C')
                self.ln(9)

            def footer(self):
                self.set_y(-15)
                self.set_font("Arial", 'I', 8)
                self.set_text_color(100, 100, 100)
                self.cell(0, 10, f"ACC QMS | WIR Ref: {wir_no} | Page {self.page_no()}", align='C')

        pdf = FullWIRPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)

        # Title
        pdf.set_fill_color(226, 232, 240)
        pdf.set_text_color(26, 54, 93)
        pdf.set_font("Arial", 'B', 11)
        pdf.cell(190, 7, "WORK INSPECTION REQUEST (WIR)", 1, 1, 'C', True)
        pdf.ln(2)

        def sec_hdr(title):
            pdf.set_fill_color(43, 108, 176)
            pdf.set_text_color(255, 255, 255)
            pdf.set_font("Arial", 'B', 9)
            pdf.cell(190, 5.5, f"  {title}", 1, 1, 'L', True)
            pdf.set_text_color(0, 0, 0)

        def field_pair(l1, v1, l2, v2):
            pdf.set_font("Arial", 'B', 8)
            pdf.set_fill_color(240, 244, 248)
            pdf.cell(35, 5.5, str(l1), 1, 0, 'L', True)
            pdf.set_font("Arial", '', 8)
            pdf.cell(60, 5.5, str(v1), 1, 0, 'L')
            pdf.set_font("Arial", 'B', 8)
            pdf.cell(35, 5.5, str(l2), 1, 0, 'L', True)
            pdf.set_font("Arial", '', 8)
            pdf.cell(60, 5.5, str(v2), 1, 1, 'L')

        # 1. Project Info
        sec_hdr("1. GENERAL PROJECT & REQUEST INFORMATION")
        field_pair("WIR Ref No:", wir_no, "Date / Time:", f"{date_raised} @ {time_raised}")
        field_pair("Main Contractor:", contractor, "Subcontractor:", subcontractor)
        field_pair("Discipline:", discipline, "ITP Ref Code:", itp_ref)
        pdf.ln(1.5)

        # 2. Location Info
        sec_hdr("2. LOCATION & SCOPE DETAILS")
        field_pair("Building / Zone:", building_no, "Model / Sector:", model)
        field_pair("Floor / Level:", floor, "Unit / Apt No:", unit)
        field_pair("Grid Axes / Space:", grid_axes, "Drawing Ref & Rev:", drawing_no)
        pdf.ln(1.5)

        # 3. Work Scope
        sec_hdr("3. WORK DETAILS & SPECIFICATIONS")
        field_pair("Activity ID:", activity_id, "Specification Ref:", quality_spec)
        pdf.set_font("Arial", 'B', 8)
        pdf.set_fill_color(240, 244, 248)
        pdf.cell(190, 5, "Detailed Description of Inspected Work:", 1, 1, 'L', True)
        pdf.set_font("Arial", '', 8)
        pdf.multi_cell(190, 4.5, str(description), 1, 'L')
        pdf.ln(1.5)

        # 4. Checklist
        sec_hdr("4. QUALITY CONTROL CHECKLIST")
        pdf.set_font("Arial", '', 7.5)
        pdf.cell(190, 4.5, f"  [{'X' if ck1 else ' '}] Approved Shop Drawings & BBS available on site", 1, 1, 'L')
        pdf.cell(190, 4.5, f"  [{'X' if ck2 else ' '}] Materials inspected, approved, and compliant with project specifications", 1, 1, 'L')
        pdf.cell(190, 4.5, f"  [{'X' if ck3 else ' '}] Levels, alignment, and structural dimensions verified", 1, 1, 'L')
        pdf.cell(190, 4.5, f"  [{'X' if ck4 else ' '}] Previous non-conformances / observations closed satisfactorily", 1, 1, 'L')
        pdf.cell(190, 4.5, f"  [{'X' if ck5 else ' '}] Site cleanliness and safety standards maintained", 1, 1, 'L')
        pdf.ln(1.5)

        # 5. Status
        sec_hdr("5. INSPECTION DECISION & CONSULTANT REMARKS")
        pdf.set_font("Arial", 'B', 9)
        pdf.cell(190, 5.5, f"  RECOMMENDATION STATUS: {status}", 1, 1, 'L')
        pdf.set_font("Arial", 'B', 8)
        pdf.set_fill_color(240, 244, 248)
        pdf.cell(190, 5, "Consultant Remarks / Instructions:", 1, 1, 'L', True)
        pdf.set_font("Arial", '', 8)
        pdf.multi_cell(190, 4.5, str(comments) if comments else "N/A", 1, 'L')
        pdf.ln(1.5)

        # 6. Signatures
        sec_hdr("6. SIGNATURES & APPROVAL BLOCK")
        pdf.set_font("Arial", 'B', 8)
        pdf.set_fill_color(240, 244, 248)
        pdf.cell(63, 5, "ACC Site Engineer", 1, 0, 'C', True)
        pdf.cell(63, 5, "ACC Quality Engineer / Manager", 1, 0, 'C', True)
        pdf.cell(64, 5, "Consultant Engineer", 1, 1, 'C', True)
        pdf.set_font("Arial", '', 7.5)
        pdf.cell(63, 11, f"Name: {site_engineer}\n\nSign: __________________", 1, 0, 'L')
        pdf.cell(63, 11, f"Name: {qc_engineer}\n\nSign: __________________", 1, 0, 'L')
        pdf.cell(64, 11, f"Name: {consultant_eng}\n\nSign: __________________", 1, 1, 'L')

        pdf_raw = pdf.output(dest='S')
        pdf_bytes = pdf_raw.encode('latin-1', 'replace') if isinstance(pdf_raw, str) else bytes(pdf_raw)

        st.success("✅ تم إصدار تقرير WIR الشامل بنجاح!")
        st.download_button(
            label="📥 تحميل تقرير الـ WIR الرسمي (PDF)",
            data=pdf_bytes,
            file_name=f"{wir_no}_Official.pdf",
            mime="application/pdf"
        )
    except Exception as e:
        st.error(f"خطأ أثناء إنشاء الـ PDF: {e}")
