import streamlit as st
from datetime import datetime

st.set_page_config(page_title="طباعة الشيكات الحقيقية", layout="wide")

# إعداد قيم المعايرة الافتراضية في الذاكرة
if 'top_pos' not in st.session_state: st.session_state.top_pos = 60
if 'left_pos' not in st.session_state: st.session_state.left_pos = 50
if 'date_pos' not in st.session_state: st.session_state.date_pos = 20
if 'amt_pos' not in st.session_state: st.session_state.amt_pos = 140

# حيلة برمجية لإخفاء عناصر التحكم والأزرار تماماً داخل المتصفح عند أمر الطباعة
st.markdown("""
    <style>
    h1, h2, h3, p, label, .stButton { text-align: right; direction: rtl; }
    div.stButton > button:first-child { background-color: #E64A19; color:white; font-size:18px; width: 100%; }
    
    /* أمر إخفاء عناصر منصة سريم ليت عند الطباعة */
    @media print {
        [data-testid="stForm"], .no-print, h1, p, span, label, blockquote, hr, .stMarkdown,
        [data-testid="stSidebar"], [data-testid="stHeader"], [data-testid="stBlock"] > div:none-task {
            display: none !important;
            visibility: hidden !important;
        }
        iframe {
            position: absolute !important;
            top: 0 !important;
            left: 0 !important;
            width: 100% !important;
            height: 100% !important;
            border: none !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🖨️ محرك طباعة الشيكات الحقيقية")
st.caption("يقوم النظام بطباعة النصوص الصافية فقط بدقة لتسقط داخل خانات دفتر شيكاتك الأصلي")

with st.form("cheque_data"):
    col1, col2 = st.columns(2)
    with col1:
        ch_name = st.text_input("اسم المستفيد (إدفعوا لأمر)", value="محمد السعيد أحمد")
        ch_text_amount = st.text_input("المبلغ تفقيطاً (فقط ... لا غير)", value="فقط ثلاثمائة وخمسون دينار لا غير")
    with col2:
        ch_amount = st.number_input("المبلغ بالأرقام", min_value=0.0, value=350.0, step=50.0)
        ch_date = st.date_input("تاريخ الاستحقاق", datetime.now())
    
    submitted = st.form_submit_button("تحديث الحقول والمعاينة")

st.markdown("### ⚙️ لوحة معايرة الأبعاد")
col_load1, col_load2 = st.columns(2)
with col_load1:
    st.session_state.top_pos = st.slider("مستوى نص (اسم المستفيد والتفقيط) لأسفل ولأعلى", 10, 300, st.session_state.top_pos)
    st.session_state.amt_pos = st.slider("مستوى (المبلغ بالأرقام) لأسفل ولأعلى", 10, 400, st.session_state.amt_pos)
with col_load2:
    st.session_state.left_pos = st.slider("إزاحة (اسم المستفيد والتفقيط) من اليمين إلى اليسار", 10, 500, st.session_state.left_pos)
    st.session_state.date_pos = st.slider("مكان (التاريخ) لأسفل ولأعلى", 10, 200, st.session_state.date_pos)

# ----------------------------------------------------
# بناء طبقة البيانات مع زر الطباعة الداخلي لتفادي مشاكل الـ iframe
# ----------------------------------------------------
date_str = ch_date.strftime('%d / %m / %Y')
amt_str = f"# {ch_amount:,.2f} #" if ch_amount > 0 else ""

print_layout = f"""
<div style="position: relative; width: 100%; height: 260px; font-family: 'Arial'; font-size: 20px; font-weight: bold; color: black; line-height: 1.6; direction: rtl; background: white;">
    <!-- التاريخ أعلى اليسار -->
    <div style="position: absolute; top: {st.session_state.date_pos}px; left: 60px; direction: ltr;">
        {date_str}
    </div>
    
    <!-- اسم المستفيد -->
    <div style="position: absolute; top: {st.session_state.top_pos}px; right: {st.session_state.left_pos}px;">
        {ch_name}
    </div>
    
    <!-- المبلغ تفقيط -->
    <div style="position: absolute; top: {st.session_state.top_pos + 55}px; right: {st.session_state.left_pos - 20}px; width: 65%;">
        {ch_text_amount}
    </div>
    
    <!-- المبلغ بالأرقام -->
    <div style="position: absolute; top: {st.session_state.amt_pos}px; left: 50px; font-size: 22px; direction: ltr;">
        {amt_str}
    </div>
</div>

<div class="no-print" style="margin-top: 20px; text-align: center;">
    <button onclick="window.print()" style="background-color: #2E7D32; color: white; padding: 10px 30px; font-size: 18px; border: none; border-radius: 5px; cursor: pointer; width: 100%;">
        🖨️ اضغط هنا لبدء الطباعة الصافية المباشرة
    </button>
</div>
"""

# عرض الكتلة البرمجية للطباعة
st.components.v1.html(print_layout, height=330)
