import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="نظام إدارة وطباعة الشيكات", layout="wide")

# تخصيص واجهة البرنامج والتصميم المخصص للطباعة
st.markdown("""
    <style>
    h1, h2, h3, p, th, td, label, .stButton { text-align: right; direction: rtl; }
    div.stButton > button:first-child { background-color: #1E88E5; color:white; font-size:18px; width: 100%; }
    
    /* تصميم الشيك المخصص للطباعة فقط وإخفاء بقية عناصر الموقع أثناء الطباعة */
    @media print {
        body * { visibility: hidden; }
        .printable-cheque, .printable-cheque * { visibility: visible; }
        .printable-cheque { 
            position: absolute; 
            left: 0; 
            top: 0; 
            width: 100%; 
            direction: rtl;
        }
        .no-print { display: none !important; }
    }
    
    /* شكل هيكل الشيك المعروض على الشاشة قبل طباعته */
    .cheque-box {
        border: 2px dashed #777;
        padding: 25px;
        border-radius: 10px;
        background-color: #FCFBF7;
        font-family: 'Arial', sans-serif;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# حاوية للتأكد من عدم ظهور أقسام الإدخال عند الطباعة
st.markdown('<div class="no-print">', unsafe_allow_html=True)
st.title("📄 نظام إدارة وتعبئة الشيكات الجاهزة للطباعة")

if 'cheques_db' not in st.session_state:
    st.session_state.cheques_db = pd.DataFrame(columns=["رقم الشيك", "اسم المستفيد", "المبلغ", "تاريخ الاستحقاق", "البنك"])

# نموذج تعبئة بيانات الشيك الحالية
with st.form("cheque_input_form"):
    col1, col2 = st.columns(2)
    with col1:
        ch_num = st.text_input("رقم الشيك")
        ch_name = st.text_input("اسم المستفيد (يُصرف لأمر)")
        ch_bank = st.text_input("اسم البنك")
    with col2:
        ch_amount = st.number_input("المبلغ بالأرقام", min_value=0.0, step=100.0)
        ch_date = st.date_input("تاريخ الاستحقاق", datetime.now())
        ch_text_amount = st.text_input("المبلغ الحروف (تفقيط كالتالي: فقط مائة دينار لا غير)")
    
    submitted = st.form_submit_button("تحديث نموذج الشيك للطباعة وحفظه")

if submitted:
    if ch_name and ch_amount > 0:
        new_data = pd.DataFrame([[ch_num, ch_name, ch_amount, ch_date.strftime('%Y-%m-%d'), ch_bank]], columns=st.session_state.cheques_db.columns)
        st.session_state.cheques_db = pd.concat([st.session_state.cheques_db, new_data], ignore_index=True)
        st.success("تم تحديث بيانات الشيك بنجاح!")
st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# قسم الشيك الجاهز للطباعة (يظهر على الشاشة ويُطبع بشكل منفصل)
# ----------------------------------------------------
st.markdown("### 🖨️ معاينة الشيك الحالي قبل إرساله للطابعة")

# هيكل مرئي يطابق أبعاد الشيكات الافتراضية
st.markdown(f"""
<div class="printable-cheque cheque-box">
    <table width="100%" cellspacing="10" cellpadding="5" style="border:none; font-size:18px;">
        <tr>
            <td width="30%"><strong>التاريخ:</strong> {ch_date.strftime('%Y / %m / %d')}</td>
            <td width="40%"><strong>البنك:</strong> {ch_bank if ch_bank else '.................'}</td>
            <td width="30%" align="left"><strong>رقم الشيك:</strong> {ch_num if ch_num else '.................'}</td>
        </tr>
        <tr>
            <td colspan="3" style="padding-top:20px;">
                <strong>إدفعوا لأمر السيد / الشركة:</strong> {ch_name if ch_name else '......................................................................'}
            </td>
        </tr>
        <tr>
            <td colspan="2" style="padding-top:15px;">
                <strong>مبلغ وقدره (كتابة):</strong> {ch_text_amount if ch_text_amount else '......................................................................'}
            </td>
            <td align="left" style="font-size:22px; font-weight:bold; background:#EEE; padding:5px 15px; border:1px solid #999;">
                {ch_amount:,.2f}
            </td>
        </tr>
        <tr>
            <td colspan="2"></td>
            <td align="left" style="padding-top:40px;">
                <p style="border-top:1px dashed #333; width:150px; text-align:center;">التوقيع المخول</p>
            </td>
        </tr>
    </table>
</div>
""", unsafe_allow_html=True)

# زر جافا سكريبت لتشغيل أمر طباعة المتصفح بشكل مباشر
st.markdown('<div class="no-print" style="margin-top:20px;">', unsafe_allow_html=True)
if st.button("🖨️ اضغط هنا لطباعة هذا الشيك الآن"):
    st.markdown("""
        <script>
        window.print();
        </script>
        """, unsafe_allow_html=True)
    st.info("إذا لم تفتح نافذة الطباعة تلقائياً، اضغط على (Ctrl + P) من لوحة المفاتيح.")

# عرض السجل التاريخي للشيكات الصادرة بالأسفل
if not st.session_state.cheques_db.empty:
    st.markdown("---")
    st.subheader("📋 سجل الشيكات المحفوظة خلال الجلسة الحالية")
    st.dataframe(st.session_state.cheques_db, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

