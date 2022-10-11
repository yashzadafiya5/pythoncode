# 18. QR Code using Python 

# import pyqrcode
# url = pyqrcode.create('http://uca.edu')

# # big_code = pyqrcode.create('9054300736', error='L', version=27, mode='binary')
# # big_code.png('code.png', scale=6, module_color=[0, 0, 0, 30], background=[0xff, 0xff, 0xcc])
# # big_code.show()

# Importing libraries
import qrcode
import numpy as np
# Data which for you want to make QR code
# Here we are using URL of MakeUseOf website
data = "https://www.googlepay.com/"
# Name of the QR code Image file
QRCodefile = "yash.png"
# instantiate QRCode object
qrObject = qrcode.QRCode(version=1, box_size=14)
# add data to the QR code
qrObject.add_data(data)
# compile the data into a QR code array
qrObject.make()
image = qrObject.make_image()
image.save(QRCodefile)
# print the image size (version)
print("Size of the QR image(Version):")
print(np.array(qrObject.get_matrix()).shape)