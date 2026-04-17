import qrcode
import os

def generate_asset_qr(asset_id):
    """
    Generates a QR code for the given asset_id and saves it to the assets folder.
    Returns True if successful, False otherwise.
    """
    try:
        # Ensure the 'assets' directory exists so the script doesn't crash
        if not os.path.exists('assets'):
            os.makedirs('assets')

        # Configure the QR code with high error correction
        # This means if the sticker gets scratched, the camera can still read it
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        
        # Inject the text/data into the QR code
        qr.add_data(asset_id)
        qr.make(fit=True)

        # Create the image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the image dynamically based on the asset ID
        filename = f"assets/{asset_id}_qr.png"
        img.save(filename)
        
        return True, filename
        
    except Exception as e:
        return False, str(e)
