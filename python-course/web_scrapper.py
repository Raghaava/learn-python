import requests
import smtplib
import time
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Sony-Mirrorless-Digital-Camera-28-70mm/dp/B00PX8CNCM/ref=pd_lpo_sbs_421_t_0?_encoding=UTF8&psc=1&refRID=D6H75S80FHM3GWXEHVW4"


def check_price():
    # get page
    page = requests.get(url)
    soup = BeautifulSoup(page.content, features="html.parser")
    print(soup.find(id="productTitle").get_text().strip())
    price = soup.find(id="priceblock_ourprice").get_text().strip()

    converted_price = float(price[1:2]+price[3:])
    if converted_price < 2000:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('raghava@gmail.com', 'password')
    subject = 'price is down!'
    body = f"check your email link {url}"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'raghava@gmail.com',
        'raghava@gmail.com',
        msg
    )

    print('mail has been sent.')
    server.quit()


while True:
    check_price()
    time.sleep(3600)
