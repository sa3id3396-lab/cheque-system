import streamlit as st
from datetime import datetime

st.set_page_config(page_title="طباعة الشيكات الحقيقية", layout="wide")

# إعداد قيم الهوامش الافتراضية في الذاكرة (بالبكسل/المليمتر)
if 'top_pos' not in st.session_state: st.session_state.top_pos = 50
if 'left_pos' not in st.session_state: st.session_state.left_pos = 60
if 'date_pos' not in st.session_state: st.session_state.date_pos = 20
if 'amt_pos' not in st.session_state: st.session_state.amt_pos = 40

# تخصيص واجهة البرنامج للتحكم والطباعة الحقيقية
st.markdown(f"""
    <style>
    h1, h2, h3, p, label, .stButton {{ text-align: right; direction: rtl; }}
    div.stButton > button:first-child {{ background-color: #D32F2F; color:white; font-size:18px; width: 100%; }}
    
    /* شكل الشيك الحقيقي على الشاشة للتوضيح فقط */
    .real-cheque-preview {{
        border: 1px solid #ccc;
        padding: 20px;
        position: relative;
        width: 100%;
        height: 250px;
        background-color: #fff;
    }}
    
    /* التوزيع الفعلي للنصوص عند الطباعة الحقيقية */
    .print-field {{ position: absolute; font-family: 'Arial', sans-serif; font-size: 16px; font-weight: bold; color: #000; }}
    
    /* عند إرسال الشيك للطابعة الحقيقية: نخفي كل شيء ما عدا النصوص الصافية */
    @media print {{
        body * {{ visibility: hidden; }}
        .printable-data, .printable-data * {{ visibility: visible; }}
        .printable-data {{
            position: absolute;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
        }}
        .no-print {{ display: none !important; }}
    }}
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="no-print">', unsafe_allow_html=True)
st.title("🖨️ محرك طباعة الشيكات الحقيقية (تحكم بالمليمتر)")
st.caption("هذا النظام يطبع النصوص الصافية فقط فوق دفتر شيكاتك الأصلي")

# مدخلات الشيك
with st.form("cheque_data"):
    col1, col2 = st.columns(2)
    with col1:
        ch_name = st.text_input("اسم المستفيد (إدفعوا لأمر)")
        ch_text_amount = st.text_input("المبلغ تفقيطاً (فقط ... لا غير)")
    with col2:
        ch_amount = st.number_input("المبلغ بالأرقام", min_value=0.0, step=50.0)
        ch_date = st.date_input("تاريخ الاستحقاق", datetime.now())
    
    submitted = st.form_submit_button("تحديث ومعاينة مكان النص")

st.markdown("### ⚙️ لوحة معايرة أبعاد بنكك الخاص (حرك النصوص لتطابق خانات شيكك الحقيقي)")
col_load1, col_load2 = st.columns(2)
with col_load1:
    st.session_state.top_pos = st.slider("مستوى نص (اسم المستفيد) لأسفل ولأعلى", 10, 200, st.session_state.top_pos)
    st.session_state.amt_pos = st.slider("مستوى (المبلغ بالأرقام) لأسفل ولأعلى", 10, 200, st.session_state.amt_pos)
with col_load2:
    st.session_state.left_pos = st.slider("مسافة (اسم المستفيد) من اليمين", 10, 500, st.session_state.left_pos)
    st.session_state.date_pos = st.slider("مكان (التاريخ) لأسفل ولأعلى", 10, 200, st.session_state.date_pos)

st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# بناء طبقة البيانات الصافية التي ستسقط فوق الشيك الورقي
# ----------------------------------------------------
st.markdown("### 👁️ شكل النصوص التي ستطبع فوق ورقة شيكك")

cheque_html = f"""
<div class="printable-data real-cheque-preview">
    <!-- التاريخ -->
    <div class="print-field" style="top: {st.session_state.date_pos}px; left: 50px;">
        {ch_date.strftime('%d / %m / %Y')}
    </div>
    
    <!-- اسم المستفيد -->
    <div class="print-field" style="top: {st.session_state.top_pos}px; right: {st.session_state.left_pos}px;">
        {ch_name if ch_name else ''}
    </div>
    
    <!-- المبلغ تفقيط -->
    <div class="print-field" style="top: {st.session_state.top_pos + 40}px; right: {st.session_state.left_pos - 20}px; width: 60%;">
        {ch_text_amount if ch_text_amount else ''}
    </div>
    
    <!-- المبلغ أرقام -->
    <div class="print-field" style="top: {st.session_state.amt_pos}px; left: 60px; background:#f9f9f9; padding:2px 10px;">
        # {ch_amount:,.2f} #
    </div>
</div>
"""
st.markdown(cheque_html, unsafe_allow_html=True)

st.markdown('<div class="no-print" style="margin-top:20px;">', unsafe_allow_html=True)
if st.button("🖨️ ابدأ الطباعة الحقيقية الآن"):
    st.markdown("<script>window.print();</script>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
