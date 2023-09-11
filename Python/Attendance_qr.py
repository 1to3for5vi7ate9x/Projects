import qrcode
import random
import string
import datetime

# Generate random data for the QR code
random_data = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

# Get the current timestamp
timestamp = datetime.datetime.now()

# Add a validity period of 2 hours
validity_period = datetime.timedelta(hours=2)
valid_until = timestamp + validity_period

# Create a dictionary with the QR code data
qr_data = {
    'data': random_data,
    'timestamp': timestamp,
    'valid_until': valid_until
}

# Create a QR code instance
qr = qrcode.QRCode(version=1, box_size=5, border=5)
qr.add_data(qr_data)
qr.make(fit=True)

# Generate the QR code image
qr_image = qr.make_image(fill_color="black", back_color="white")

# Display the QR code image
qr_image.show()


