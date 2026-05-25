import streamlit as st
from datetime import datetime

st.set_page_config(page_title="طباعة الشيكات الحقيقية", layout="wide")

# إعداد قيم المعايرة الافتراضية في الذاكرة
if 'top_pos' not in st.session_state: st.session_state.top_pos = 60
if 'left_pos' not in st.session_state: st.session_state.left_pos = 50
if 'date_pos' not in st.session_state: st.session_state.date_pos = 20
if 'amt_pos' not in st.session_state: st.session_state.amt_pos = 140

# تخصيص واجهة البرنامج وفصل عناصر التحكم تماماً عن الطباعة
st.markdown(f"""
    <style>
    h1, h2, h3, p, label, .stButton {{ text-align: right; direction: rtl; }}
    div.stButton > button:first-child {{ background-color: #E64A19; color:white; font-size:18px; width: 100%; }}
    
    /* عند إرسال الأمر للطابعة الحقيقية: يتم إخفاء كل شيء في الموقع تماماً */
    @media print {{
        .no-print, [data-testid="stSidebar"], [data-testid="stHeader"] {{ display: none !important; }}
        body {{ background-color: white; }}
    }}
    </style>
    """, unsafe_allow_html=True)

# بداية قسم لوحة التحكم (يختفي تماماً عند الطباعة)
st.markdown('<div class="no-print">', unsafe_allow_html=True)
st.title("🖨️ محرك طباعة الشيكات الحقيقية")
st.caption("يقوم النظام بطباعة النصوص الصافية فقط بدقة لتسقط داخل خانات دفتر شيكاتك الأصلي")

with st.form("cheque_data"):
    col1, col2 = st.columns(2)
    with col1:
        ch_name = st.text_input("اسم المستفيد (إدفعوا لأمر)")
        ch_text_amount = st.text_input("المبلغ تفقيطاً (فقط ... لا غير)")
    with col2:
        ch_amount = st.number_input("المبلغ بالأرقام", min_value=0.0, step=50.0)
        ch_date = st.date_input("تاريخ الاستحقاق", datetime.now())
    
    submitted = st.form_submit_button("تحديث الحقول والمعاينة")

st.markdown("### ⚙️ لوحة معايرة الأبعاد (حرك النصوص لتطابق خانات شيكك الورقي الحقيقي)")
col_load1, col_load2 = st.columns(2)
with col_load1:
    st.session_state.top_pos = st.slider("مستوى نص (اسم المستفيد والتفقيط) لأسفل ولأعلى", 10, 300, st.session_state.top_pos)
    st.session_state.amt_pos = st.slider("مستوى (المبلغ بالأرقام) لأسفل ولأعلى", 10, 400, st.session_state.amt_pos)
with col_load2:
    st.session_state.left_pos = st.slider("إزاحة (اسم المستفيد والتفقيط) من اليمين إلى اليسار", 10, 500, st.session_state.left_pos)
    st.session_state.date_pos = st.slider("مكان (التاريخ) لأسفل ولأعلى", 10, 200, st.session_state.date_pos)

st.markdown('</div>', unsafe_allow_html=True)
# نهاية قسم لوحة التحكم

# ----------------------------------------------------
# بناء طبقة البيانات الحقيقية النقية للطباعة
# ----------------------------------------------------
# تجهيز النصوص وتنسيقها برمجياً لتقرأها الطابعة كـ نصوص حرة بدون أكواد ظاهرة
date_str = ch_date.strftime('%d / %m / %Y')
amt_str = f"# {ch_amount:,.2f} #" if ch_amount > 0 else ""

print_layout = f"""
<div style="position: relative; width: 100%; height: 260px; font-family: 'Arial'; font-size: 18px; font-weight: bold; color: black; line-height: 1.6; direction: rtl;">
    <!-- التاريخ أعلى اليسار -->
    <div style="position: absolute; top: {st.session_state.date_pos}px; left: 60px; direction: ltr;">
        {date_str}
    </div>
    
    <!-- اسم المستفيد -->
    <div style="position: absolute; top: {st.session_state.top_pos}px; right: {st.session_state.left_pos}px;">
        {ch_name}
    </div>
    
    <!-- المبلغ تفقيطاً -->
    <div style="position: absolute; top: {st.session_state.top_pos + 45}px; right: {st.session_state.left_pos - 20}px; width: 65%;">
        {ch_text_amount}
    </div>
    
    <!-- المبلغ بالأرقام -->
    <div style="position: absolute; top: {st.session_state.amt_pos}px; left: 50px; font-size: 20px; direction: ltr;">
        {amt_str}
    </div>
</div>
"""

# عرض البيانات الصافية في الصفحة باستخدام المكون المعتمد من المنصة لضمان عدم ظهور الأكواد
st.components.v1.html(print_layout, height=270)

# زر تشغيل أمر الطباعة في المتصفح
st.markdown('<div class="no-print">', unsafe_allow_html=True)
if st.button("🖨️ ابدأ الطباعة على الشيك الورقي الحقيقي"):
    st.markdown("""
        <script>
        var shareMenu = window.parent.document.querySelector('[data-testid="stStatusWidget"]');
        if(shareMenu) shareMenu.style.display = 'none';
        window.print();
        </script>
        """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
