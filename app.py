import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="نظام إدارة الشيكات المجاني", layout="wide")
st.title(" 📄 نظام إدارة وتتبع الشيكات المتكامل")

# إنشاء قاعدة بيانات مؤقتة في ذاكرة المتصفح
if 'cheques_db' not in st.session_state:
    st.session_state.cheques_db = pd.DataFrame(columns=[
        "رقم الشيك", "اسم المستفيد", "المبلغ", "تاريخ الاستحقاق", "البنك", "الحالة"
    ])

# واجهة إضافة شيك جديد
with st.form("إضافة شيك جديد"):
    col1, col2, col3 = st.columns(3)
    with col1:
        ch_num = st.text_input("رقم الشيك")
        ch_bank = st.text_input("البنك المسحوب عليه")
    with col2:
        ch_name = st.text_input("اسم المستفيد / الساحب")
        ch_status = st.selectbox("حالة الشيك", ["معلق", "تم الصرف", "مرتجع"])
    with col3:
        ch_amount = st.number_input("المبلغ", min_value=0.0)
        ch_date = st.date_input("تاريخ الاستحقاق", datetime.now())
    
    submit = st.form_submit_button("حفظ الشيك في النظام")

if submit:
    new_data = pd.DataFrame([[ch_num, ch_name, ch_amount, ch_date, ch_bank, ch_status]], 
                            columns=st.session_state.cheques_db.columns)
    st.session_state.cheques_db = pd.concat([st.session_state.cheques_db, new_data], ignore_index=True)
    st.success("تم حفظ الشيك بنجاح!")

# عرض الشيكات المسجلة
st.subheader("📋 جدول الشيكات الحالية")
st.dataframe(st.session_state.cheques_db, use_container_width=True)
