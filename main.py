import tkinter as tk
from tkinter import messagebox, simpledialog
import generator
import scanner

def create_qr_button_clicked():
    # ask for asset name
    asset_id = simpledialog.askstring("Input", "Enter Asset ID (any, just for testing):")
    
    if asset_id: 
        success, result = generator.generate_asset_qr(asset_id.strip())
        
        if success:
            messagebox.showinfo("Success", f"th QR Code was generated and saved to:\n{result}")
        else:
            messagebox.showerror("Error", f"failed to generate QR Code try again:\n{result}")
# should execute when the user clicks scanner button
def start_scanner_button_clicked():
    messagebox.showinfo("Starting scaner", "Recording camera. pres q on your keyboard to close camera.")
    # Call the func  from Cam_QR_Scan.py
    scanner.run_scanner()
    messagebox.showinfo("Scanner closed", "Scanner has stopped running Check inventory_log.csv for new logs")

# --------------------------------------------
#    Main UI SETUP
#---------------------------------------------

#Start main window
root = tk.Tk()
root.title("Asset track (QR Code)")
root.geometry("400x300")
root.configure(bg="#232F3E") 


title_label = tk.Label(root, text="Asset Tracker", font=("Arial", 16, "bold"), fg="white", bg="#232F3E")
title_label.pack(pady=20)

instruction_label = tk.Label(root, text="Select a button down below", font=("Arial", 10), fg="white", bg="#232F3E")
instruction_label.pack(pady=10)

btn_generate = tk.Button(root, text="1. Generate asset Qr code", font=("Arial", 12), bg="#FF9900", fg="black", width=25, command=create_qr_button_clicked)
btn_generate.pack(pady=10)

btn_scan = tk.Button(root, text="2. Start scanner", font=("Arial", 12), bg="#FF9900", fg="black", width=25, command=start_scanner_button_clicked)
btn_scan.pack(pady=10)

root.mainloop()
