
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/EST-ThinkPad-T480-Ordenador-Professional/dp/B07SPRM9Y6/ref=sr_1_1_sspa?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=XTHMXXAOIEM6&keywords=thinkpad+laptop&qid=1573955355&sprefix=laptop+thi%2Caps%2C373&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzSlQ2SzdYUFNKMDFPJmVuY3J5cHRlZElkPUEwMTE5MzI4MkEwVElFNjBOUVdQRyZlbmNyeXB0ZWRBZElkPUEwMTEzMDYwMkE4REZaMURITFk5RSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.find(id="productTitle").get_text()
        price = bsObj.find(id="priceblock_ourprice").get_text()
    except AttributeError as e:
        return None
    return title, price

def sendEmail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	password = input("Password:") #generated password in ->  google app password
	server.login('valdeortiz15@gmail.com', password)
	subject = 'price fell down!'
	body = f"check de amazon link: {URL} "
	msg = f"subject: {subject} \n\n {body}"
	server.sendmail(
		'valdeortiz15@gmail.com',
		'valdemar_@live.com.ar',
		msg)

	print("The email has been sent!")
	server.quit()

def checkPrice(price):
	if price < 1.5:
		sendEmail()


title, price = getTitle(URL)

if title == None:
    print("Title could not be found")
else:
    print(title.strip())

if price == None:
	print("The price could not be found")
else:
	print(price)
	price = price.replace(",",".")
	price = float(price[1:6])
	print(price)
	checkPrice(price)



