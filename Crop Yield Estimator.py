import tkinter as tk
from tkinter import messagebox
import numpy as np
import pandas as pd
import os
from sklearn.linear_model import LinearRegression

# 1. Dummy Data Generation & Model Training for Backend Simulation
np.random.seed(42)
X_dummy = np.random.rand(100, 3)  # Features: Farm Size, Temp, Rainfall
# Scale features to realistic ranges:
X_dummy[:, 0] = X_dummy[:, 0] * 50 + 1     # Farm Size: 1 to 51 Acres
X_dummy[:, 1] = X_dummy[:, 1] * 30 + 10    # Temp: 10°C to 40°C
X_dummy[:, 2] = X_dummy[:, 2] * 1500 + 200 # Rainfall: 200mm to 1700mm

# Dynamic baseline yield estimation formula for training data
y_dummy = (X_dummy[:, 0] * 2.5) + (X_dummy[:, 1] * 0.4) + (X_dummy[:, 2] * 0.01)

model = LinearRegression()
model.fit(X_dummy, y_dummy)

# CSV Database Setup
csv_filename = "crop_yield_history.csv"

# 2. Prediction Engine with Hybrid Agronomic Constraints
def predict_yield_handler(event=None):
    try:
        # Retrieve and parse inputs
        farm_size = float(entry_farm.get())
        temperature = float(entry_temp.get())
        rainfall = float(entry_rain.get())
        
        if farm_size <= 0 or temperature <= -50 or rainfall < 0:
            messagebox.showerror("Input Error", "Please enter valid realistic environmental attributes.")
            return

        # Core Machine Learning Inference
        input_data = np.array([[farm_size, temperature, rainfall]])
        predicted_yield = model.predict(input_data)[0]
        
        # Default Optimal UI Colors
        bg_color = "#e8f5e9"  # Light Green
        
        # Apply Rule-Based Expert Constraints (Hybrid Intelligence Layer)
        if rainfall > 1500.0:
            predicted_yield = predicted_yield * 0.2  # 80% drop due to severe waterlogging
            advisory = "CRITICAL ALERT: Flood risk / Excessive rainfall! Yield will drop drastically due to waterlogging."
            bg_color = "#ffdddd"  # Light Red
            
        elif temperature < 12.0:
            predicted_yield = predicted_yield * 0.4  # 60% drop due to severe frost/cold stress
            advisory = "CRITICAL ALERT: Extreme Cold / Frost Risk! Low temperature will stunt crop development."
            bg_color = "#e3f2fd"  # Light Ice-Blue
            
        elif rainfall < 500.0:
            advisory = "Warning: Low rainfall detected! Ensure timely artificial irrigation."
            bg_color = "#fff3cd"  # Light Yellow
            
        elif temperature > 32.0:
            advisory = "Warning: High temperature detected! Implement soil mulching to retain moisture."
            bg_color = "#fff3cd"  # Light Yellow
            
        else:
            advisory = "Optimal Weather Conditions! Standard fertilizer cycles recommended."

        # Format output string
        formatted_yield = f"{max(0.0, predicted_yield):.2f} Tons"
        
        # Update Dashboard Interface Elements
        lbl_yield_val.config(text=formatted_yield)
        lbl_advisory_val.config(text=advisory)
        frame_result.config(bg=bg_color)
        lbl_yield_title.config(bg=bg_color)
        lbl_yield_val.config(bg=bg_color)
        lbl_advisory_title.config(bg=bg_color)
        lbl_advisory_val.config(bg=bg_color)
        
        # 3. Persistent Data Logging to CSV Database
        new_record = {
            "Farm Size (Acres)": farm_size,
            "Avg Temperature (°C)": temperature,
            "Annual Rainfall (mm)": rainfall,
            "Estimated Yield (Tons)": round(max(0.0, predicted_yield), 2),
            "System Advisory": advisory
        }
        
        df = pd.DataFrame([new_record])
        if not os.path.isfile(csv_filename):
            df.to_csv(csv_filename, index=False)
        else:
            df.to_csv(csv_filename, mode='a', header=False, index=False)
            
    except ValueError:
        messagebox.showerror("Data Type Error", "Please ensure all fields contain numeric values.")

# 4. Enterprise Desktop Graphical User Interface Setup
root = tk.Tk()
root.title("Crop Yield Estimator Dashboard")
root.state('zoomed')  # Launches application window directly into a maximized state
root.configure(bg="#f4fbf7")

# Global Fonts Configurations
font_title = ("Helvetica", 28, "bold")
font_section = ("Helvetica", 14, "bold")
font_label = ("Helvetica", 12, "bold")
font_entry = ("Helvetica", 12)
font_display = ("Helvetica", 32, "bold")
font_adv = ("Helvetica", 12, "bold")

# Title Banner
lbl_main_title = tk.Label(root, text="Crop Yield Estimator", font=font_title, fg="#1e5631", bg="#f4fbf7")
lbl_main_title.pack(pady=30)

# Main Form Container Card
frame_input = tk.LabelFrame(root, text="Environmental Parameters", font=font_section, fg="#1e5631", bg="white", padx=30, pady=30, bd=1, relief="solid")
frame_input.pack(pady=10, ipady=10, ipadx=40)

# Input Row Layout Matrix
tk.Label(frame_input, text="Farm Size (Acres):", font=font_label, bg="white").grid(row=0, column=0, sticky="w", pady=15, padx=10)
entry_farm = tk.Entry(frame_input, font=font_entry, width=25, bd=1, relief="solid")
entry_farm.grid(row=0, column=1, pady=15, padx=10)
entry_farm.focus()  # Puts cursor in first cell on start

tk.Label(frame_input, text="Avg Temperature (°C):", font=font_label, bg="white").grid(row=1, column=0, sticky="w", pady=15, padx=10)
entry_temp = tk.Entry(frame_input, font=font_entry, width=25, bd=1, relief="solid")
entry_temp.grid(row=1, column=1, pady=15, padx=10)

tk.Label(frame_input, text="Annual Rainfall (mm):", font=font_label, bg="white").grid(row=2, column=0, sticky="w", pady=15, padx=10)
entry_rain = tk.Entry(frame_input, font=font_entry, width=25, bd=1, relief="solid")
entry_rain.grid(row=2, column=1, pady=15, padx=10)

# Action Trigger Button
btn_predict = tk.Button(root, text="PREDICT YIELD", font=font_label, fg="white", bg="#13824b", activebackground="#0f663a", activeforeground="white", width=25, height=2, bd=0, cursor="hand2", command=predict_yield_handler)
btn_predict.pack(pady=25)

# --- Dynamic Focus Traversal Bindings ---
entry_farm.bind('<Return>', lambda event: entry_temp.focus())
entry_temp.bind('<Return>', lambda event: entry_rain.focus())
entry_rain.bind('<Return>', predict_yield_handler)

# Result Output Dashboard Display Card
frame_result = tk.Frame(root, bd=2, relief="solid", highlightthickness=0, highlightbackground="#13824b", bg="#e8f5e9")
frame_result.pack(pady=20, fill="x", padx=200, ipady=20)

lbl_yield_title = tk.Label(frame_result, text="ESTIMATED CROP YIELD", font=("Helvetica", 9, "bold"), fg="#555555", bg="#e8f5e9")
lbl_yield_title.pack(pady=(10, 0))

lbl_yield_val = tk.Label(frame_result, text="-- Tons", font=font_display, fg="#13824b", bg="#e8f5e9")
lbl_yield_val.pack(pady=5)

lbl_advisory_title = tk.Label(frame_result, text="SYSTEM ADVISORY", font=("Helvetica", 9, "bold"), fg="#555555", bg="#e8f5e9")
lbl_advisory_title.pack(pady=(15, 0))

lbl_advisory_val = tk.Label(frame_result, text="Awaiting target parameter inputs...", font=font_adv, fg="#222222", bg="#e8f5e9", wraplength=800, justify="center")
lbl_advisory_val.pack(pady=(5, 10))

# Execute Application Main Loop
root.mainloop()
