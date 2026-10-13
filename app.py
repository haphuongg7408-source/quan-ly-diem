import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Tiêu đề ứng dụng
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Tạo dữ liệu mẫu
data = {
    'Ho_ten': ['Nguyen Van A', 'Tran Thi B', 'Le Van C', 'Pham Thi D', 'Hoang Van E', 
               'Vu Thi F', 'Ngo Van G', 'Bui Thi H', 'Dang Van I', 'Do Thi K'],
    'Chuyen_can': [8.0, 9.0, 7.5, 6.0, 8.5, 9.5, 5.0, 7.0, 8.0, 6.5],
    'Giua_ky': [7.0, 8.5, 6.5, 5.0, 8.0, 9.0, 4.5, 6.0, 7.5, 5.5],
    'Cuoi_ky': [7.5, 8.0, 7.0, 5.5, 8.5, 9.0, 5.0, 6.5, 8.0, 6.0]
}

df = pd.DataFrame(data)
df['Tong_ket'] = (0.2 * df['Chuyen_can'] + 0.3 * df['Giua_ky'] + 0.5 * df['Cuoi_ky']).round(2)

def xep_loai(diem):
    if diem >= 8.5: return "Giỏi"
    elif diem >= 7.0: return "Khá"
    elif diem >= 5.0: return "Trung bình"
    else: return "Yếu"

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

# 1. Hiển thị bảng điểm
st.subheader("1. Bảng điểm chi tiết của 10 sinh viên")
st.dataframe(df)

# 2. Hiển thị các thông tin thống kê
st.subheader("2. Thống kê chung")
dtb_lop = df['Tong_ket'].mean()
sv_max = df.loc[df['Tong_ket'].idxmax()]
sv_min = df.loc[df['Tong_ket'].idxmin()]
so_sv_dat = (df['Tong_ket'] >= 5).sum()

st.write(f"- **Điểm tổng kết trung bình của lớp:** {dtb_lop:.2f}")
st.write(f"- **Sinh viên cao điểm nhất:** {sv_max['Ho_ten']} ({sv_max['Tong_ket']} điểm)")
st.write(f"- **Sinh viên thấp điểm nhất:** {sv_min['Ho_ten']} ({sv_min['Tong_ket']} điểm)")
st.write(f"- **Số sinh viên đạt (≥ 5.0):** {so_sv_dat}")

# 3. Chọn sinh viên xem thông tin chi tiết qua Selectbox
st.subheader("3. Tra cứu thông tin sinh viên")
selected_student = st.selectbox("Chọn họ tên sinh viên:", df['Ho_ten'].tolist())

student_info = df[df['Ho_ten'] == selected_student].iloc[0]
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Chuyên cần", student_info['Chuyen_can'])
col2.metric("Giữa kỳ", student_info['Giua_ky'])
col3.metric("Cuối kỳ", student_info['Cuoi_ky'])
col4.metric("Tổng kết", student_info['Tong_ket'])
col5.metric("Xếp loại", student_info['Xep_loai'])

# 4. Hiển thị biểu đồ cột
st.subheader("4. Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df['Ho_ten'], df['Tong_ket'], color='skyblue', edgecolor='black')
ax.set_xlabel("Họ và tên")
ax.set_ylabel("Điểm tổng kết")
ax.set_xticklabels(df['Ho_ten'], rotation=45, ha='right')
ax.set_ylim(0, 10)

for i, val in enumerate(df['Tong_ket']):
    ax.text(i, val + 0.1, f"{val}", ha='center', fontsize=9)

st.pyplot(fig)

# 5. Footer: Họ tên và MSSV
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px; color: gray;'>Ứng dụng được thực hiện bởi: [Hoàng Nguyễn Hà Phương] - [034308015334]</p>", unsafe_allow_html=True)

