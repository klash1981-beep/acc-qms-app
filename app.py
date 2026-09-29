import streamlit as st
import openpyxl
from datetime import datetime
import io

st.set_page_config(page_title="ACC - Banan WIR Official System", page_icon="🏗️", layout="wide")

st.title("ALEXANDRIA CONSTRUCTION CO. (ACC)")
st.subheader("Banan Al-Riyadh Project (BB1.2) - Work Inspection Request")

# نموذج إدخال البيانات
with st.form("wir_exact_form"):
    c1, c2 = st.columns(2)
    with c1:
        wir_no = st.text_input("WIR Number", value="ACC-BB1.2-WIR-001")
        building = st.text_input("Building / Zone", value="B20")
        floor = st.text_input("Floor / Level", value="GF")
        unit = st.text_input("Unit / Apt", value="Apt 01")
    with c2:
        date_val = st.date_input("Date", value=datetime.now())
        discipline = st.selectbox("Discipline", ["Civil / Structural", "Architectural", "MEP"])
        drawing_ref = st.text_input("Drawing Ref & Rev", value="BANAN-STR-DWG-102 Rev.0")
        inspector = st.text_input("Inspector / QC Engineer", value="Eng. Khaled Samy")

    description = st.text_area("Description of Inspected Work", value="Inspection of reinforcement steel and formwork shuttering for GF columns.")
    
    submit = st.form_submit_button("📑 تعبئة النموذج واستخرج الملف الأصلي")

if submit:
    try:
        # تحميل قالب الإكسيل الأصلي المرفوع على جيثب
        wb = openpyxl.load_workbook("wir_template.xlsx", keep_vba=True)
        sheet = wb.active

        # كتابة البيانات في الخلايا المحددة بحسب القالب الأصلي
        sheet['C4'] = wir_no
        sheet['C5'] = str(date_val)
        sheet['C6'] = building
        sheet['C7'] = floor
        sheet['C8'] = unit
        sheet['G4'] = discipline
        sheet['G5'] = drawing_ref
        sheet['G6'] = inspector
        sheet['C10'] = description

        # حفظ الملف المعبأ في الذاكرة
        output = io.BytesIO()
        wb.save(output)
        output.seek(0)

        st.success("✅ تم تعبئة البيانات في النموذج الأصلي بنجاح مع الحفاظ على كامل التنسيق والشعار!")
        st.download_button(
            label="📥 تحميل نموذج WIR المعبأ (Excel)",
            data=output,
            file_name=f"{wir_no}_Official.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    except Exception as e:
        st.error(f"خطأ في الوصول إلى القالب: {e}. تأكد من رفع ملف 'wir_template.xlsx' إلى المستودع على GitHub بنفس الاسم.")
