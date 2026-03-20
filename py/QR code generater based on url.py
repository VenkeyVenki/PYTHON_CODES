import qrcode
url = input("Enter URL: ")
img = qrcode.make(url)
img.show()