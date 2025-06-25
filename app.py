import pandas as pd
import matplotlib.pyplot as plt
import re
from datetime import datetime
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def parse_log_file(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

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
        return df
    except Exception as e:
        messagebox.showerror("Error", f"Failed to parse log file: {e}")
        return None

def plot_graph(df, interval):
    try:
        request_counts = df.resample(interval).size()
        plt.figure(figsize=(15, 6))
        plt.plot(request_counts.index, request_counts.values, label=f"Requests per {interval}", color='blue')
        plt.xlabel("Time")
        plt.ylabel("Number of Requests")
        plt.title(f"Requests per {interval}")
        plt.grid(True)
        plt.tight_layout()
        plt.legend()
        plt.xticks(rotation=45)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to plot graph: {e}")

def upload_file():
    file_path = filedialog.askopenfilename(title="Select Log File", filetypes=[("CSV Files", "*.csv"), ("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        df = parse_log_file(file_path)
        if df is not None:
            interval = interval_var.get()
            if interval in valid_intervals:
                plot_graph(df, interval)
            else:
                messagebox.showerror("Error", "Invalid interval selected.")

# GUI setup
root = tk.Tk()
root.title("Log Request Analyzer")
root.geometry("500x200")
root.configure(bg="#f0f4f7")

frame = tk.Frame(root, bg="#f0f4f7")
frame.pack(padx=30, pady=30)

label = tk.Label(frame, text="เลือกช่วงเวลาในการแสดงผล:", font=("Arial", 12), bg="#f0f4f7")
label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

interval_var = tk.StringVar()
interval_dropdown = ttk.Combobox(frame, textvariable=interval_var, font=("Arial", 11), width=15)
valid_intervals = ["S", "1Min", "30Min", "1H"]
interval_dropdown['values'] = valid_intervals
interval_dropdown.current(1)
interval_dropdown.grid(row=0, column=1, padx=10, pady=10)

upload_button = tk.Button(frame, text="อัปโหลดไฟล์และแสดงกราฟ", command=upload_file, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
upload_button.grid(row=1, column=0, columnspan=2, pady=20)

root.mainloop()

