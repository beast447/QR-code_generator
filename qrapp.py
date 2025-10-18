import qrcode

url = input(str("Enter URL: " ))

img = qrcode.make(url)
type(img)
img.save("QRcode.png")
print("QRcdode generated and saved")
