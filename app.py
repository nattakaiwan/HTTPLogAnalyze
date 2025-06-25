import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re
from datetime import datetime

st.set_page_config(page_title="Log Analyzer", layout="wide")

st.title("📊 Log Request Analyzer")

uploaded_file = st.file_uploader("📁 อัปโหลดไฟล์ log (.csv หรือ .txt)", type=["csv", "txt"])

interval = st.selectbox(
    "⏱️ เลือกช่วงเวลาในการแสดงผล",
    options=["S", "1Min", "30Min", "1H"],
    index=1,
    help="S = ต่อวินาที, 1Min = ต่อ 1 นาที, 30Min = ต่อ 30 นาที, 1H = ต่อ 1 ชั่วโมง"
)

if uploaded_file is not None:
    try:
        lines = uploaded_file.read().decode("utf-8").splitlines()
        timestamp_pattern = re.compile(r'\[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})')
        timestamps = []

        for line in lines:
            match = timestamp_pattern.search(line)
            if match:
                timestamp_str = match.group(1)
                timestamp = datetime.strptime(timestamp_str, "%d/%b/%Y:%H:%M:%S")
                timestamps.append(timestamp)

        df = pd.DataFrame(timestamps, columns=["Timestamp"])
        df.set_index("Timestamp", inplace=True)
        request_counts = df.resample(interval).size()

        st.subheader(f"📈 กราฟจำนวนคำขอ ({interval})")
        fig, ax = plt.subplots(figsize=(15, 5))
        ax.plot(request_counts.index, request_counts.values, label=f"Requests per {interval}", color="blue")
        ax.set_xlabel("Time")
        ax.set_ylabel("Number of Requests")
        ax.set_title(f"Requests per {interval}")
        ax.grid(True)
        ax.legend()
        plt.xticks(rotation=45)
        st.pyplot(fig)

    except Exception as e:
        st.error(f"เกิดข้อผิดพลาด: {e}")

# แสดงชื่อผู้สร้าง
st.markdown("---")
st.caption("👨‍💻 Project by: Nattakaiwan")

