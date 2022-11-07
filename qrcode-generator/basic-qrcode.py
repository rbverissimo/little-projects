import qrcode
# from PIL import Image, ImageDraw

data = "some data"
qr = qrcode.QRCode(version=1, box_size=50, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')
img.save('FirstQRCode.png')
