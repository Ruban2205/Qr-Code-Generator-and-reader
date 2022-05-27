import qrcode

def generateForSave(name, text):
    image = qrcode.make(text)
    image.save(name)