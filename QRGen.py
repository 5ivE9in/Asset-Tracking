import qrcode
import os

def generate_asset_qr(asset_id):
  
    try:
        if not os.path.exists('assets'):
            os.makedirs('assets')

        qr = qrcode.QRCode(version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        
        qr.add_data(asset_id)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        
        filename = f"assets/{asset_id}_qr.png"
        img.save(filename)
        
        return True, filename
        
    except Exception as e:
        return False, str(e)
