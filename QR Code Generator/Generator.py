import os
import qrcode
import qrcode.image.svg
filetype = input("insert file type (png or svg):")
if filetype == "png":
    qr = qrcode.QRCode(version=1,
                      error_correction=qrcode.constants.ERROR_CORRECT_L,
                      box_size=20,
                      border=2,)
    qr.add_data(input("Input your Link:"))
    qr.make(fit=True)
    img = qr.make_image(fillcolor="black", back_color="white")
    img.save(input("insert Filename:")+".png")
elif filetype == "svg":
    factory = qrcode.image.svg.SvgPathImage
    svg_image = qrcode.make(input("Input your Link:"))
    svg_image.save(input("insert Filename:")+".svg")
