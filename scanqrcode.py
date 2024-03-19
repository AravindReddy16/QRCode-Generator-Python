import qrcode

link=input('Enter link: ')
qr=qrcode.make(link,version=10,box_size=10,border=3)
qr.save('qrcode.png')