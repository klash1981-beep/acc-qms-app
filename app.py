import streamlit as st
from fpdf import FPDF
import base64

st.set_page_config(page_title="ACC - Banan QMS", page_icon="🏗️", layout="centered")

# Custom CSS for ACC Branding
st.markdown("""
    <style>
    .main-header {
        font-size: 24px;
        font-weight: bold;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        width: 100%;
        background-color: #1E3A8A;
        color: white;
        font-weight: bold;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">Alexandria Construction Co. (ACC)</div>', unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #4B5563;'>Banan Al-Riyadh Project (Package BB1.2)</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #2563EB;'>Work Inspection Request (WIR) System</h4>", unsafe_allow_html=True)

st.divider()

# WIR Form Inputs
with st.form("wir_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        wir_no = st.text_input("WIR Number", value="ACC-BANAN-WIR-001")
        building_no = st.text_input("Building Number", value="Bldg-05")
        floor = st.text_input("Floor", value="First Floor")
        
    with col2:
        itp_stage = st.selectbox("ITP Stage Code", [
            "Civil - Excavation & Backfilling",
            "Civil - Foundation Reinforcement",
            "Civil - Concrete Casting",
            "Architectural - Brickwork & Blockwork",
            "MEP - First Fix Inspection"
        ])
        drawing_no = st.text_input("Drawing Reference No.", value="BANAN-STR-DWG-102")
        inspector = st.text_input("Inspector Engineer", value="Eng. Khaled Samy")

    submit_button = st.form_submit_button(label="Generate WIR PDF Report")

if submit_button:
    try:
        # Generate PDF using FPDF
        pdf = FPDF()
        pdf.add_page()
        
        # Header Box
        pdf.set_fill_color(30, 58, 138) # ACC Blue
        pdf.rect(10, 10, 190, 20, 'F')
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("Arial", 'B', 14)
        pdf.set_xy(10, 15)
        pdf.cell(190, 10, "ALEXANDRIA CONSTRUCTION CO. (ACC)", align='C', ln=True)
        
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Arial", 'B', 12)
        pdf.ln(15)
        pdf.cell(0, 10, "PROJECT: Banan Al-Riyadh (Package BB1.2)", ln=True, align='C')
        pdf.cell(0, 10, "WORK INSPECTION REQUEST (WIR) REPORT", ln=True, align='C')
        pdf.ln(5)
        
        # Details Table
        pdf.set_font("Arial", 'B', 10)
        pdf.set_fill_color(240, 240, 240)
        
        def add_row(label, value):
            pdf.cell(60, 8, label, 1, 0, 'L', True)
            pdf.set_font("Arial", '', 10)
            pdf.cell(130, 8, str(value), 1, 1, 'L')
            pdf.set_font("Arial", 'B', 10)

        add_row("WIR Number:", wir_no)
        add_row("Building No:", building_no)
        add_row("Floor:", floor)
        add_row("ITP Stage Code:", itp_stage)
        add_row("Drawing Reference:", drawing_no)
        add_row("Inspector Engineer:", inspector)
        
        pdf.ln(20)
        pdf.set_font("Arial", 'I', 9)
        pdf.cell(0, 10, "This is a digital quality report generated automatically via ACC QMS Cloud System.", ln=True, align='C')
        
        # Output PDF as bytes
        pdf_bytes = pdf.output(dest='S').encode('latin1')
        
        st.success("WIR Report generated successfully!")
        st.download_button(
            label="Download Official WIR PDF",
            data=pdf_bytes,
            file_name=f"{wir_no}.pdf",
            mime="application/pdf"
        )
    except Exception as e:
        st.error(f"An error occurred during PDF generation: {e}")
