import streamlit as st
st.set_page_config(
    page_title="Khoa học Màu sắc", layout="wide"
)

# Đoạn chia cột căn giữa logo
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    st.image("https://wikimedia.org", use_container_width=True)

st.write("### Chào mừng bạn đến với project Khoa học Màu sắc của mình!")
st.write("# Mình tên là HOÀNG ĐÔNG, MSSV 23458005")
