import qrcode

QR_VERSION  = 10 # Version of QR means QR complexity
QR_BOX_SIZE = 10 # Size of QR image  
QR_BORDER   = 5  # White border along QR code

qr = qrcode.QRCode(
    version  = QR_VERSION,
    box_size = QR_BOX_SIZE,
    border   = QR_BORDER 
)

data_to_encode = "https://google.com"
qr.add_data(data_to_encode)
qr.make(fit = True)
img = qr.make_image(fill = 'black', back_color = 'white')
img.save('qr.png')