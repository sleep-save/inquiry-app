import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Excel 文件路径
EXCEL_FILE = 'inquiry_data.xlsx'

# 初始化 Excel 文件（如果不存在）
if not os.path.exists(EXCEL_FILE):
    df_init = pd.DataFrame(columns=[
        '时间', '货号', '规格', '数量', '目录价', '折扣', '折后单价',
        '货期', '税点', '包装', '储存温度', '运输条件', '有效期', '付款方式'
    ])
    df_init.to_excel(EXCEL_FILE, index=False)

st.title("📋 询价登记系统")

# 表单填写
with st.form("inquiry_form"):
    col1, col2 = st.columns(2)
    with col1:
        code = st.text_input("货号")
        spec = st.text_input("规格")
        qty = st.number_input("数量", min_value=0, step=1)
        list_price = st.number_input("目录价", min_value=0.0)
        discount = st.number_input("折扣（0~1之间）", min_value=0.0, max_value=1.0, value=1.0)
        final_price = list_price * discount if list_price else 0.0
        st.write(f"折后单价：**{final_price:.2f}**")
    with col2:
        lead_time = st.text_input("货期")
        tax = st.text_input("税点")
        packaging = st.text_input("包装")
        storage = st.text_input("储存温度")
        shipping = st.text_input("运输条件")
        validity = st.text_input("有效期")
        payment = st.text_input("付款方式")

    submitted = st.form_submit_button("提交")

# 提交保存
if submitted:
    new_data = {
        '时间': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        '货号': code,
        '规格': spec,
        '数量': qty,
        '目录价': list_price,
        '折扣': discount,
        '折后单价': final_price,
        '货期': lead_time,
        '税点': tax,
        '包装': packaging,
        '储存温度': storage,
        '运输条件': shipping,
        '有效期': validity,
        '付款方式': payment
    }

    df_existing = pd.read_excel(EXCEL_FILE)
    df_existing = pd.concat([df_existing, pd.DataFrame([new_data])], ignore_index=True)
    df_existing.to_excel(EXCEL_FILE, index=False)
    st.success("✅ 信息已保存到 Excel！")
