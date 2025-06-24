import io

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from PIL import Image

st.title("Phân tích dữ liệu điểm số học sinh")

# Upload file
upload_file = st.file_uploader("Chọn file Excel (có cột 'Điểm số')", type=["xlsx"])


# Hàm tính điểm trung bình
def calculate_average(scores):
    return sum(scores) / len(scores)


# Hàm phân loại điểm số
def percentage_distribution(scores):
    bins = {"90-100": 0, "80-89": 0, "70-79": 0, "60-69": 0, "<60": 0}
    for score in scores:
        if score >= 90:
            bins["90-100"] += 1
        elif score >= 80:
            bins["80-89"] += 1
        elif score >= 70:
            bins["70-79"] += 1
        elif score >= 60:
            bins["60-69"] += 1
        else:
            bins["<60"] += 1
    return bins


# Khi có file
if upload_file:
    df = pd.read_excel(upload_file)
    # Xử lý danh sách điểm số (bỏ dòng nào trống, chuyển type thành float và chuyển thành list)
    scores = df["Điểm số"].dropna().astype(float).tolist()
    # Hiển thị các chỉ số
    if scores:
        st.write(
            "Tổng số học sinh:",
            len(scores),
            "Điểm trung bình:",
            round(calculate_average(scores), 2),
        )

        # Phân loại điểm
        dist = percentage_distribution(scores)
        labels = list(dist.keys())
        values = list(dist.values())

        fig, ax = plt.subplots(figsize=(1, 1))
        ax.pie(
            values,
            labels=labels,
            autopct="%1.1f%%",
            textprops={"fontsize": 3.5},
        )
        ax.axis("equal")
        plt.tight_layout(pad=0.1)
        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=300)
        buf.seek(0)
        st.markdown("Biểu đồ phân bố điểm số")
        img = Image.open(buf)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, width=300)
            st.markdown("Biểu đồ phân bố điểm số.")
