import cv2
from pyzbar.pyzbar import decode
import csv
from datetime import datetime
import os

def run_scanner():

    # Open the CSV file in "a" mode so no pr2evious records is deleted
    file_exists = os.path.isfile('inventory_log.csv')
    
    with open('inventory_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        
        if not file_exists:
            writer.writerow(["Timestamp", "Asset_ID"])

        # Initialize the webcam 
        cap = cv2.VideoCapture(0)
        
    
        # if qr code is held infront of cam for 5 secs
        recently_scanned = set()

        while True:
            # current frame
            success, frame = cap.read()
            if not success:
                break
            
            # Detect a qr code if any and if there is decode it
            for barcode in decode(frame):
                asset_data = barcode.data.decode('utf-8')
                
                # when detecetd this just draws a green box around it
                pts = barcode.polygon
                if len(pts) == 4:
                    pts_array = [pts[0], pts[1], pts[2], pts[3]]
                    cv2.polylines(frame, [pts_array], isClosed=True, color=(0, 255, 0), thickness=3)

                # checks if we have already scanned that item./qrcode in this running session
                if asset_data not in recently_scanned:
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    
                    writer.writerow([current_time, asset_data])
                    recently_scanned.add(asset_data)
                    print(f"Logged: {asset_data} at {current_time}")

            cv2.imshow('Amazon IT Asset Scanner (Press Q to quit)', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()
