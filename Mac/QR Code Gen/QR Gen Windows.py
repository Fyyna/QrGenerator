import qrcode
import PIL.Image
from PIL import Image
import qrcode.image.svg
import qrcode.image.styledpil
from qrcode.main import QRCode
filetype = input("insert file type (png or svg):")
QR_Image_link = "/Users/domi/PyCharmMiscProject/QR Code Gen/Bilder/dtp.png"
logo = Image.open(QR_Image_link)
if filetype == "png":
    basewidth = 100
    wpercent = (basewidth / float(logo.size[0]))
    hsize = int((float(logo.size[1]) * float(wpercent)))
    logo = logo.resize(basewidth,hsize), Image.ANTIALIAS)
    qr = qrcode.QRCode(version=2,
                      error_correction=qrcode.constants.ERROR_CORRECT_H,
                      box_size=20,
                      border=2)
    qr.add_data(input("Input your Link:"))
    qr.make()
    QRimg = QRcode.make_image(fill_color="black", back_color="white"), convert("RGB")
pos = ((QRimg.size[0] - logo.size[0]) // 2,
        (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)





#elif filetype == "svg":
    #factory = qrcode.image.svg.SvgPathImage
    #svg_image = qrcode.make(input("Input your Link:"))
    #svg_image.save(input("insert Filename:")+".svg")