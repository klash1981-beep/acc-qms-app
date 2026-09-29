import streamlit as st
from fpdf import FPDF
from datetime import datetime

st.set_page_config(page_title="ACC - Banan WIR Official System", page_icon="🏗️", layout="wide")

st.markdown("""
    <style>
    .wir-header {
        background-color: #1a365d;
        color: white;
        padding: 12px;
        text-align: center;
        font-weight: bold;
        font-size: 22px;
        border-radius: 5px;
        margin-bottom: 15px;
    }
    .sec-title {
        background-color: #2b6cb0;
        color: white;
        padding: 5px 10px;
        font-weight: bold;
        font-size: 14px;
        margin-top: 10px;
        margin-bottom: 10px;
        border-radius: 3px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="wir-header">ALEXANDRIA CONSTRUCTION CO. (ACC)<br><span style="font-size: 16px; font-weight: normal;">Banan Al-Riyadh Project (BB1.2) - Work Inspection Request (WIR)</span></div>', unsafe_allow_html=True)

with st.form("wir_official_form"):
    st.markdown('<div class="sec-title">1. GENERAL & PROJECT INFORMATION</div>', unsafe_allow_html=True)
    f1, f2, f3 = st.columns(3)
    with f1:
        wir_no = st.text_input("WIR No.", value="ACC-BB1.2-WIR-001")
        project_name = st.text_input("Project Name", value="Banan Al-Riyadh (Package BB1.2)")
    with f2:
        date_inp = st.date_input("Date", value=datetime.now())
        contractor = st.text_input("Main Contractor", value="Alexandria Construction Co. (ACC)")
    with f3:
        time_inp = st.time_input("Time", value=datetime.now().time())
        subcontractor = st.text_input("Subcontractor", value="Civil Works Subcontractor")

    st.markdown('<div class="sec-title">2. LOCATION & INSPECTION SCOPE</div>', unsafe_allow_html=True)
    l1, l2, l3 = st.columns(3)
    with l1:
        building = st.text_input("Building / Zone", value="B20")
        floor = st.text_input("Floor / Level", value="GF")
    with l2:
        model = st.text_input("Model / Sector", value="R2")
        unit = st.text_input("Unit / Apt", value="Apt 01")
    with l3:
        space_area = st.text_input("Specific Location / Axis", value="Axes A-D / 1-5")
        drawing_ref = st.text_input("Drawing Ref & Rev", value="BANAN-STR-DWG-102 Rev.0")

    st.markdown('<div class="sec-title">3. WORK DETAILS & SPECIFICATIONS</div>', unsafe_allow_html=True)
    discipline = st.selectbox("Discipline / Trade", ["Civil / Structural", "Architectural", "MEP - Electrical", "MEP - Plumbing"])
    itp_code = st.text_input("ITP Reference Code", value="ITP-03-01")
    spec_ref = st.text_input("Specification Reference", value="Spec Section 033000 - Cast-in-Place Concrete")
    description = st.text_area("Description of Inspected Work", value="Inspection of reinforcement steel, formwork shuttering, and cleanliness prior to concrete casting for GF columns.")

    st.markdown('<div class="sec-title">4. QUALITY CHECKLIST & VERIFICATION</div>', unsafe_allow_html=True)
    c1 = st.checkbox("Work completed in accordance with approved shop drawings", value=True)
    c2 = st.checkbox("Materials used are approved and compliant with specifications", value=True)
    c3 = st.checkbox("Previous non-conformances (if any) closed satisfactorily", value=True)
    c4 = st.checkbox("Safety and housekeeping standards maintained on site", value=True)

    st.markdown('<div class="sec-title">5. CONSULTANT / INSPECTOR RESPONSE</div>', unsafe_allow_html=True)
    status = st.radio("Inspection Decision", ["Approved (A)", "Approved as Noted (B)", "Revise & Resubmit (C)", "Rejected (D)"], index=0)
    comments = st.text_area("Consultant Remarks / Memos", value="Approved to proceed with concrete pouring. Ensure proper compaction and curing.")

    st.markdown('<div class="sec-title">6. APPROVAL SIGNATURES</div>', unsafe_allow_html=True)
    s1, s2, s3 = st.columns(3)
    with s1:
        site_eng = st.text_input("ACC Site Engineer", value="Eng. Mahmoud Amin")
    with s2:
        qc_eng = st.text_input("ACC Quality Manager", value="Eng. Khaled Samy")
    with s3:
        consultant = st.text_input("Consultant Engineer", value="Eng. Hany Mohamed")

    submit = st.form_submit_button("📄 Generate Official Form PDF")

if submit:
    try:
        class OfficialWIRPDF(FPDF):
            def header(self):
                # Top Navy Banner
                self.set_fill_color(26, 54, 93)
                self.rect(10, 10, 190, 22, 'F')
                self.set_text_color(255, 255, 255)
                self.set_font("Arial", 'B', 14)
                self.set_xy(10, 13)
                self.cell(190, 8, "ALEXANDRIA CONSTRUCTION CO. (ACC)", align='C', ln=True)
                self.set_font("Arial", '', 10)
                self.cell(190, 6, "BANAN AL-RIYADH PROJECT (PACKAGE BB1.2) - QUALITY MANAGEMENT SYSTEM", align='C')
                self.ln(10)

            def footer(self):
                self.set_y(-15)
                self.set_font("Arial", 'I', 8)
                self.set_text_color(100, 100, 100)
                self.cell(0, 10, f"Form Ref: ACC-BB1.2-WIR | Generated for WIR: {wir_no} | Page {self.page_no()}", align='C')

        pdf = OfficialWIRPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)

        # Form Title Box
        pdf.set_fill_color(226, 232, 240)
        pdf.set_text_color(26, 54, 93)
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(190, 8, "WORK INSPECTION REQUEST (WIR)", 1, 1, 'C', True)
        pdf.ln(2)

        def draw_sec_hdr(title):
            pdf.set_fill_color(43, 108, 176)
            pdf.set_text_color(255, 255, 255)
            pdf.set_font("Arial", 'B', 9.5)
            pdf.cell(190, 6, f"  {title}", 1, 1, 'L', True)
            pdf.set_text_color(0, 0, 0)

        def draw_field(lbl1, val1, lbl2, val2):
            pdf.set_font("Arial", 'B', 8.5)
            pdf.set_fill_color(240, 244, 248)
            pdf.cell(35, 6, str(lbl1), 1, 0, 'L', True)
            pdf.set_font("Arial", '', 8.5)
            pdf.cell(60, 6, str(val1), 1, 0, 'L')
            pdf.set_font("Arial", 'B', 8.5)
            pdf.cell(35, 6, str(lbl2), 1, 0, 'L', True)
            pdf.set_font("Arial", '', 8.5)
            pdf.cell(60, 6, str(val2), 1, 1, 'L')

        # 1. Project Info
        draw_sec_hdr("1. GENERAL PROJECT & REQUEST INFORMATION")
        draw_field("WIR Reference:", wir_no, "Date / Time:", f"{date_inp} {time_inp}")
        draw_field("Project Name:", "Banan Al-Riyadh BB1.2", "Main Contractor:", contractor)
        draw_field("Discipline:", discipline, "Subcontractor:", subcontractor)
        pdf.ln(2)

        # 2. Location
        draw_sec_hdr("2. LOCATION & DRAWING DETAILS")
        draw_field("Building / Zone:", building, "Model / Sector:", model)
        draw_field("Floor / Level:", floor, "Unit / Apartment:", unit)
        draw_field("Location / Axes:", space_area, "Drawing Ref & Rev:", drawing_ref)
        pdf.ln(2)

        # 3. Work Details
        draw_sec_hdr("3. INSPECTION SCOPE & SPECIFICATIONS")
        draw_field("ITP Code:", itp_code, "Specification Ref:", spec_ref)
        pdf.set_font("Arial", 'B', 8.5)
        pdf.set_fill_color(240, 244, 248)
        pdf.cell(190, 5, "Detailed Description of Inspected Work:", 1, 1, 'L', True)
        pdf.set_font("Arial", '', 8.5)
        pdf.multi_cell(190, 5, str(description), 1, 'L')
        pdf.ln(2)

        # 4. Checklist
        draw_sec_hdr("4. QUALITY CONTROL CHECKLIST")
        pdf.set_font("Arial", '', 8)
        pdf.cell(190, 5, f"  [{'X' if c1 else ' '}] Work completed in accordance with approved shop drawings and BBS", 1, 1, 'L')
        pdf.cell(190, 5, f"  [{'X' if c2 else ' '}] Materials used are approved and compliant with project specifications", 1, 1, 'L')
        pdf.cell(190, 5, f"  [{'X' if c3 else ' '}] Previous non-conformances / observations closed satisfactorily", 1, 1, 'L')
        pdf.cell(190, 5, f"  [{'X' if c4 else ' '}] Safety and housekeeping standards maintained on site", 1, 1, 'L')
        pdf.ln(2)

        # 5. Decision & Remarks
        draw_sec_hdr("5. CONSULTANT / INSPECTOR DECISION")
        pdf.set_font("Arial", 'B', 9.5)
        pdf.cell(190, 6, f"  STATUS: {status}", 1, 1, 'L')
        pdf.set_font("Arial", 'B', 8.5)
        pdf.set_fill_color(240, 244, 248)
        pdf.cell(190, 5, "Consultant Remarks / Instructions:", 1, 1, 'L', True)
        pdf.set_font("Arial", '', 8.5)
        pdf.multi_cell(190, 5, str(comments) if comments else "N/A", 1, 'L')
        pdf.ln(2)

        # 6. Signatures
        draw_sec_hdr("6. SIGNATURES & APPROVAL BLOCK")
        pdf.set_font("Arial", 'B', 8)
        pdf.set_fill_color(240, 244, 248)
        pdf.cell(63, 5, "ACC Site Engineer", 1, 0, 'C', True)
        pdf.cell(63, 5, "ACC Quality Engineer / Manager", 1, 0, 'C', True)
        pdf.cell(64, 5, "Consultant Engineer", 1, 1, 'C', True)
        pdf.set_font("Arial", '', 8)
        pdf.cell(63, 12, f"Name: {site_eng}\n\nSign: __________________", 1, 0, 'L')
        pdf.cell(63, 12, f"Name: {qc_eng}\n\nSign: __________________", 1, 0, 'L')
        pdf.cell(64, 12, f"Name: {consultant}\n\nSign: __________________", 1, 1, 'L')

        pdf_raw = pdf.output(dest='S')
        pdf_bytes = pdf_raw.encode('latin-1', 'replace') if isinstance(pdf_raw, str) else bytes(pdf_raw)

        st.success("✅ Official WIR Form PDF generated successfully!")
        st.download_button(
            label="📥 Download Official WIR PDF Report",
            data=pdf_bytes,
            file_name=f"{wir_no}_Official_WIR.pdf",
            mime="application/pdf"
        )
    except Exception as e:
        st.error(f"Error generating PDF: {e}")
