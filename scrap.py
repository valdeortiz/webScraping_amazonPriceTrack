
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import smtplib

#URL = 'https://www.amazon.com/EST-ThinkPad-T480-Ordenador-Professional/dp/B07SPRM9Y6/ref=sr_1_1_sspa?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=XTHMXXAOIEM6&keywords=thinkpad+laptop&qid=1573955355&sprefix=laptop+thi%2Caps%2C373&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzSlQ2SzdYUFNKMDFPJmVuY3J5cHRlZElkPUEwMTE5MzI4MkEwVElFNjBOUVdQRyZlbmNyeXB0ZWRBZElkPUEwMTEzMDYwMkE4REZaMURITFk5RSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
# id for url1 = priceblock_ourprice
URL = 'https://www.amazon.com/Xiaomi-Mi-Band-4/dp/B07T4ZH692/ref=sr_1_1?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=my+band+4&qid=1574038098&sr=8-1'

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None,None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.find(id="productTitle", class_='a-size-large').get_text()        
    except AttributeError as e:
    	print("title error")
    	return None,None
    try:
    	price = bsObj.find(id="price_inside_buybox").get_text() #verificar el id en la pagina delcproducto a comprar
    except AttributeError as e:
    	print(f"price error : {e}")
    	return title,None
    return title.strip(), price.strip()


def sendEmail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	#password = input("Password:") #generated password in ->  google app password
	password = 'wazzljlhqrxohbif'
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
	if price < 1000.0:
		print("Email send!")
	else:
		print("The price is big!")


#URL = input("Url: ")
title, price = getTitle(URL)

if title == None:
    print("Title could not be found")
else:
    print(title)

if price == None:
	print("The price could not be found")
else:
	print(price)
	price = price.replace(",","")
	price = float(price[1:6])
	print(price)
	checkPrice(price)
