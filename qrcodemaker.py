import qrcode

img = qrcode.make('https://ascsn.github.io/dft-video-resources/landing.html')
img.save('website_qr.png')