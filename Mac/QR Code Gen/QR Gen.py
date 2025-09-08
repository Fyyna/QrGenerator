import qrcode.image.svg
import qrcode.image.styledpil
#Asks for preferred filetype
filetype = input("insert file type (png or svg):")
#sets the path to the used logo
QR_Image = "/Users/domi/PyCharmMiscProject/QR Code Gen/Bilder/dtp.png"
#If PNG is chosen this will execute
if filetype == "png":
    qr = qrcode.QRCode(version=2,
                      error_correction=qrcode.constants.ERROR_CORRECT_H,
                      box_size=20,
                      border=2,
                         image_factory=qrcode.image.styledpil.StyledPilImage)
   #asks for the data used in QRCode
    qr.add_data(input("Input your Link:"))
   #generates the code based on inputs
    qr.make(fit=True)
    #tells the qr.make to use variable QR_Image as filepath
    img = qr.make_image(embeded_image_path=QR_Image)
    #saves generated picture based on input and adds file extension .png at the end automatically
    img.save(input("insert Filename:")+".png")
#if SVG is chosen this will execute
elif filetype == "svg":
    factory = qrcode.image.svg.SvgPathImage
    svg_image = qrcode.make(input("Input your Link:"))
    svg_image.save(input("insert Filename:")+".svg")