import qrtools
import requests

URL = 'http://tunnel.web.easyctf.com/images/'
TEMP_IMG = 'temp.png'
qrcode = 'DaicO7460493nYSuvLPW'


counter = 1
while True:
	print str(counter) + '    ' + qrcode
	counter += 1
	
	resp = requests.get(URL + qrcode + '.png')
	
	with open(TEMP_IMG, 'wb') as f:
		f.write(resp.content)
	
	qr = qrtools.QR()
	qr.decode(TEMP_IMG)
	qrcode = qr.data
