import streamlit as st
st.set_page_config(
    page_title="Khoa học Màu sắc", layout="wide"
)
# 1. Tạo 3 cột để căn giữa (Cột 2 chứa logo, cột 1 và 3 làm khoảng trống)
# Tỷ lệ [2, 1, 2] giúp logo nằm chính giữa và không bị quá to
col1, col2, col3 = st.columns([2, 1, 2])

with col2:
    # Bạn có thể thay link URL bằng tên file ảnh nếu đã tải về máy ("logo_ute.png")
    st.image("lgo_UTE.jfif", use_container_width=True)

st.write("### Chào mừng bạn đến với project Khoa học Màu sắc của mình!")
st.write("# Mình tên là HOÀNG ĐÔNG, MSSV 23458005")
