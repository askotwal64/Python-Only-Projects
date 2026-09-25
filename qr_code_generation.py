import qrcode

data = input("Enter text or URL to convert to qr code image: ").strip()
filename = input("Enter file name: ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")

image.save(filename)

print(f'image saved as {filename}')
