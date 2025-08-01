import streamlit as st
import pandas as pd
import os

st.title("📝 询价信息收集")

# 保存的 Excel 文件路径（本地为桌面路径，云端应改为当前目录）
EXCEL_FILE = "inquiry_data.xlsx"

# 定义字段
fields = {
    "客户名称": "",
    "品牌": "",
    "产品名称": "",
    "货号": "",
    "规格": "",
    "包装": "",
    "原价": 0.0,
    "折扣": 100,
    "折后价": 0.0,
    "备注": "",
    "销售": ""
}

# 初始化 Excel 文件（如果不存在）
if not os.path.exists(EXCEL_FILE):
    df_init = pd.DataFrame(columns=fields.keys())
    df_init.to_excel(EXCEL_FILE, index=False)

# 表单输入
with st.form("inquiry_form"):
    new_data = {}
    for field in fields:
        if field in ["原价", "折扣"]:
            new_data[field] = st.number_input(field, value=float(fields[field]), step=0.1)
        elif field == "备注":
            new_data[field] = st.text_area(field, value=fields[field])
        else:
            new_data[field] = st.text_input(field, value=fields[field])

    # 自动计算折后价
    if new_data["原价"] > 0 and new_data["折扣"] > 0:
        new_data["折后价"] = round(new_data["原价"] * new_data["折扣"] / 100, 2)
        st.info(f"💰 折后价为：{new_data['折后价']}")

    submitted = st.form_submit_button("提交")
    if submitted:
        try:
            df_existing = pd.read_excel(EXCEL_FILE)
        except:
            df_existing = pd.DataFrame(columns=fields.keys())
        df_existing = pd.concat([df_existing, pd.DataFrame([new_data])], ignore_index=True)
        df_existing.to_excel(EXCEL_FILE, index=False)
        st.success("✅ 信息已保存到 Excel！")

# 查看历史记录
if st.checkbox("查看历史记录"):
    try:
        df = pd.read_excel(EXCEL_FILE)
        st.dataframe(df)
    except Exception as e:
        st.error(f"读取 Excel 出错：{e}")
import streamlit as st
import pandas as pd
import os

st.title("📝 询价信息收集")

# 保存的 Excel 文件路径（本地为桌面路径，云端应改为当前目录）
EXCEL_FILE = "inquiry_data.xlsx"

# 定义字段
fields = {
    "客户名称": "",
    "品牌": "",
    "产品名称": "",
    "货号": "",
    "规格": "",
    "包装": "",
    "原价": 0.0,
    "折扣": 100,
    "折后价": 0.0,
    "备注": "",
    "销售": ""
}

# 初始化 Excel 文件（如果不存在）
if not os.path.exists(EXCEL_FILE):
    df_init = pd.DataFrame(columns=fields.keys())
    df_init.to_excel(EXCEL_FILE, index=False)

# 表单输入
with st.form("inquiry_form"):
    new_data = {}
    for field in fields:
        if field in ["原价", "折扣"]:
            new_data[field] = st.number_input(field, value=float(fields[field]), step=0.1)
        elif field == "备注":
            new_data[field] = st.text_area(field, value=fields[field])
        else:
            new_data[field] = st.text_input(field, value=fields[field])

    # 自动计算折后价
    if new_data["原价"] > 0 and new_data["折扣"] > 0:
        new_data["折后价"] = round(new_data["原价"] * new_data["折扣"] / 100, 2)
        st.info(f"💰 折后价为：{new_data['折后价']}")

    submitted = st.form_submit_button("提交")
    if submitted:
        try:
            df_existing = pd.read_excel(EXCEL_FILE)
        except:
            df_existing = pd.DataFrame(columns=fields.keys())
        df_existing = pd.concat([df_existing, pd.DataFrame([new_data])], ignore_index=True)
        df_existing.to_excel(EXCEL_FILE, index=False)
        st.success("✅ 信息已保存到 Excel！")

# 查看历史记录
if st.checkbox("查看历史记录"):
    try:
        df = pd.read_excel(EXCEL_FILE)
        st.dataframe(df)
    except Exception as e:
        st.error(f"读取 Excel 出错：{e}")

    df_existing = pd.concat([df_existing, pd.DataFrame([new_data])], ignore_index=True)
    df_existing.to_excel(EXCEL_FILE, index=False)
    st.success("✅ 信息已保存到 Excel！")
