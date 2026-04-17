import tkinter as tk
from tkinter import messagebox, simpledialog
import generator
import scanner

def create_qr_button_clicked():
    """Triggered when the user clicks the Generate button."""
    # Pop up a dialog box asking for the asset name
    asset_id = simpledialog.askstring("Input", "Enter Asset ID (e.g. LAPTOP-001):")
    
    if asset_id: # If the user typed something and didn't hit cancel
        # Call the logic from our generator.py file
        success, result = generator.generate_asset_qr(asset_id.strip())
        
        if success:
            messagebox.showinfo("Success", f"QR Code generated and saved to:\n{result}")
        else:
            messagebox.showerror("Error", f"Failed to generate QR Code:\n{result}")

def start_scanner_button_clicked():
    """Triggered when the user clicks the Scanner button."""
    messagebox.showinfo("Starting Scanner", "The webcam will now open. Press the 'Q' key on your keyboard to close the scanner when you are done.")
    # Call the logic from our scanner.py file
    scanner.run_scanner()
    messagebox.showinfo("Scanner Closed", "Scanner session ended. Check inventory_log.csv for new entries.")

# --- UI Setup ---
# Initialize the main window
root = tk.Tk()
root.title("IT Asset Tracking System")
root.geometry("400x300")
root.configure(bg="#232F3E") # Amazon's classic dark blue hex code!

# Add a title label
title_label = tk.Label(root, text="Asset Tracker Dashboard", font=("Arial", 16, "bold"), fg="white", bg="#232F3E")
title_label.pack(pady=20)

# Add instructions
instruction_label = tk.Label(root, text="Select an operation below:", font=("Arial", 10), fg="white", bg="#232F3E")
instruction_label.pack(pady=10)

# Create the Generate Button
btn_generate = tk.Button(root, text="1. Generate Asset QR Code", font=("Arial", 12), bg="#FF9900", fg="black", width=25, command=create_qr_button_clicked)
btn_generate.pack(pady=10)

# Create the Scanner Button
btn_scan = tk.Button(root, text="2. Start Webcam Scanner", font=("Arial", 12), bg="#FF9900", fg="black", width=25, command=start_scanner_button_clicked)
btn_scan.pack(pady=10)

# Start the application loop
root.mainloop()
