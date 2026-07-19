import tkinter as tk
from tkinter import messagebox
import numpy as np
import pandas as pd
import os
from sklearn.linear_model import LinearRegression

# ---------------------------------------------------------
# STEP 1: ML MODEL SETUP & DATASET
# ---------------------------------------------------------
X_train = np.array([
    [5, 25, 500], [10, 28, 600], [15, 30, 450],
    [2, 22, 300], [20, 32, 700], [8, 26, 550], [12, 29, 400]
])
y_train = np.array([12, 25, 32, 5, 50, 18, 24])

model = LinearRegression()
model.fit(X_train, y_train)

CSV_FILE = "crop_yield_history.csv"

# ---------------------------------------------------------
# STEP 2: LOGIC & EVENT HANDLING WITH FLOOD CONTROLS
# ---------------------------------------------------------
def save_to_csv(size, temp, rain, yield_pred, advisory_msg):
    """Appends simulation outputs and metrics safely into a CSV dataset."""
    new_data = {
        "Farm Size (Acres)": [size],
        "Avg Temperature (°C)": [temp],
        "Annual Rainfall (mm)": [rain],
        "Estimated Yield (Tons)": [round(yield_pred, 2)],
        "System Advisory": [advisory_msg]
    }
    df_new = pd.DataFrame(new_data)
    if os.path.exists(CSV_FILE):
        df_existing = pd.read_csv(CSV_FILE)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.to_csv(CSV_FILE, index=False)
    else:
        df_new.to_csv(CSV_FILE, index=False)

def focus_next(event, next_widget):
    """Transfers widget keyboard focus sequentially on Return/Enter key."""
    next_widget.focus()
    return "break"

def predict_yield(event=None):
    """Processes environmental vectors, handles ML inference, and overrides flood bounds."""
    try:
        size = float(entry_size.get())
        temp = float(entry_temp.get())
        rain = float(entry_rain.get())
        
        if size <= 0 or temp <= 0 or rain <= 0:
            messagebox.showerror("Input Error", "Please enter positive values greater than zero.")
            return

        input_data = np.array([[size, temp, rain]])
        prediction = model.predict(input_data)[0]
        
        if prediction < 0: 
            prediction = 0
            
        if rain < 400:
            advisory = "Warning: Low rainfall detected! Ensure timely artificial irrigation."
            output_container.config(highlightbackground="#ef4444", highlightthickness=3)
            label_result.config(fg="#dc2626")
        elif rain > 1500:
            advisory = "CRITICAL ALERT: Flood risk / Excessive rainfall! Yield will drop drastically due to waterlogging."
            output_container.config(highlightbackground="#7c3aed", highlightthickness=3) 
            label_result.config(fg="#7c3aed")
            prediction = prediction * 0.2  
        elif temp > 32:
            advisory = "Alert: High temperature detected! Apply mulching to retain soil moisture."
            output_container.config(highlightbackground="#f59e0b", highlightthickness=3)
            label_result.config(fg="#d97706")
        else:
            advisory = "Optimal Weather Conditions! Standard fertilizer cycles recommended."
            output_container.config(highlightbackground="#10b981", highlightthickness=3)
            label_result.config(fg="#059669")

        label_result.config(text=f"{prediction:.2f} Tons")
        label_advisory.config(text=advisory, fg="#1e293b")
        
        save_to_csv(size, temp, rain, prediction, advisory)
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

def on_enter(e):
    btn_predict.config(bg="#0f5132")

def on_leave(e):
    btn_predict.config(bg="#198754")

# ---------------------------------------------------------
# STEP 3: SCALE-UP MAXIMIZED UI DESIGN
# ---------------------------------------------------------
root = tk.Tk()
root.title("Crop Yield Estimator Dashboard")

# Force window to launch directly in maximized screen state
root.state('zoomed')
root.resizable(False, False)
root.configure(bg="#f0fdf4") 

# Main responsive layout container (Takes up 65% width of the massive screen)
main_layout = tk.Frame(root, bg="#f0fdf4")
main_layout.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.65)

# Scaled up application title
header = tk.Label(
    main_layout, text="Crop Yield Estimator", 
    font=("Arial Rounded MT Bold", 32), bg="#f0fdf4", fg="#14532d"
)
header.pack(pady=(0, 25))

# 1. Environmental Parameters Input Card (Expanded size & padding)
input_container = tk.Frame(main_layout, bg="#ffffff", highlightbackground="#bbf7d0", highlightthickness=2, padx=45, pady=35)
input_container.pack(pady=15, fill="x")

input_title = tk.Label(input_container, text="Environmental Parameters", font=("Segoe UI", 18, "bold"), bg="#ffffff", fg="#166534")
input_title.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 25))

label_opts = {"bg": "#ffffff", "font": ("Segoe UI", 14, "bold"), "fg": "#374151"}
entry_opts = {
    "font": ("Segoe UI", 14, "bold"), 
    "bg": "#ffffff", 
    "bd": 0, 
    "highlightthickness": 1, 
    "highlightbackground": "#9ca3af", 
    "highlightcolor": "#166534", 
    "width": 25, 
    "fg": "#111827"
}

tk.Label(input_container, text="Farm Size (Acres):", **label_opts).grid(row=1, column=0, sticky="w", pady=15)
entry_size = tk.Entry(input_container, **entry_opts)
entry_size.grid(row=1, column=1, pady=15, sticky="e")
entry_size.focus()

tk.Label(input_container, text="Avg Temperature (°C):", **label_opts).grid(row=2, column=0, sticky="w", pady=15)
entry_temp = tk.Entry(input_container, **entry_opts)
entry_temp.grid(row=2, column=1, pady=15, sticky="e")

tk.Label(input_container, text="Annual Rainfall (mm):", **label_opts).grid(row=3, column=0, sticky="w", pady=15)
entry_rain = tk.Entry(input_container, **entry_opts)
entry_rain.grid(row=3, column=1, pady=15, sticky="e")

input_container.grid_columnconfigure(1, weight=1)

# Keyboard Event Navigation Configurations
entry_size.bind("<Return>", lambda e: focus_next(e, entry_temp))
entry_temp.bind("<Return>", lambda e: focus_next(e, entry_rain))
entry_rain.bind("<Return>", predict_yield)

# 2. Large Action Button to fit the widescreen dashboard structure
btn_predict = tk.Button(
    main_layout, text="PREDICT YIELD", font=("Segoe UI", 14, "bold"), 
    bg="#198754", fg="white", activebackground="#0f5132", activeforeground="white",
    bd=0, cursor="hand2", command=predict_yield, width=30, height=1, pady=12
)
btn_predict.pack(pady=25)
btn_predict.bind("<Enter>", on_enter)
btn_predict.bind("<Leave>", on_leave)

# 3. Dynamic Output Analytics Display Card (Sized perfectly for widescreen text wrap)
output_container = tk.Frame(main_layout, bg="#ffffff", highlightbackground="#cbd5e1", highlightthickness=1, padx=45, pady=35)
output_container.pack(pady=15, fill="x")

tk.Label(output_container, text="ESTIMATED CROP YIELD", font=("Segoe UI Black", 12), bg="#ffffff", fg="#6b7280").pack()
label_result = tk.Label(output_container, text="-- Tons", font=("Arial Rounded MT Bold", 36), bg="#ffffff", fg="#374151")
label_result.pack(pady=(5, 20))

tk.Label(output_container, text="SYSTEM ADVISORY", font=("Segoe UI Black", 12), bg="#ffffff", fg="#6b7280").pack()
label_advisory = tk.Label(
    output_container, text="Awaiting system parameters...", 
    font=("Segoe UI Semibold", 14), bg="#ffffff", fg="#4b5563", 
    wraplength=800, justify="center" # Expanded text wrap limit to prevent cutting off text on full-screen
)
label_advisory.pack(pady=(10, 0))

root.mainloop()