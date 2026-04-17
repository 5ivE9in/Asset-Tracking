import cv2
from pyzbar.pyzbar import decode
import csv
from datetime import datetime
import os

def run_scanner():
    """
    Opens the webcam, scans for QR codes, and logs them to a CSV file.
    Press 'q' to close the scanner window.
    """
    # Open the CSV file in append mode ('a') so we don't delete old records
    file_exists = os.path.isfile('inventory_log.csv')
    
    with open('inventory_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # If the file was just created, add the column headers first
        if not file_exists:
            writer.writerow(["Timestamp", "Asset_ID"])

        # Initialize the webcam (0 is the default camera)
        cap = cv2.VideoCapture(0)
        
        # We will keep track of recently scanned items so we don't spam the CSV
        # if the user holds the QR code in front of the camera for 5 seconds.
        recently_scanned = set()

        while True:
            # Read the current frame from the camera
            success, frame = cap.read()
            if not success:
                break
            
            # Detect and decode barcodes/QR codes in the frame
            for barcode in decode(frame):
                asset_data = barcode.data.decode('utf-8')
                
                # Draw a visual green targeting box on the video feed
                pts = barcode.polygon
                if len(pts) == 4:
                    pts_array = [pts[0], pts[1], pts[2], pts[3]]
                    cv2.polylines(frame, [pts_array], isClosed=True, color=(0, 255, 0), thickness=3)

                # If we haven't already scanned this exact item in this session...
                if asset_data not in recently_scanned:
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    
                    # Write to our database file
                    writer.writerow([current_time, asset_data])
                    recently_scanned.add(asset_data)
                    print(f"Logged: {asset_data} at {current_time}")

            # Display the video feed
            cv2.imshow('Amazon IT Asset Scanner (Press Q to quit)', frame)

            # Wait for the user to press 'q' to break the loop and quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Clean up the camera resources
    cap.release()
    cv2.destroyAllWindows()
