# Checks every hour if the price for a product is under a certain threshold. Here I chose underwear with a price of under 70.
# If the price falls below that, I'll get notified through email

import requests
from bs4 import BeautifulSoup
import smtplib
import ssl
import time


def check_price():
    URL = "https://ro.factcool.com/boxers-5-pack-42217490"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")
    price = int(soup.find("span", {"class": "pd-price-current"}).get_text()[0:3])

    print("checked")
    return price


def send_mail():
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    f = open("dummyemail.txt")
    sender_email = f.readline()
    receiver_email = "mvictorandrei@gmail.com"
    password = f.readline()
    print(sender_email + password)
    message = """\
    Buy underwear

    From here: https://ro.factcool.com/boxers-5-pack-42217490"""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


while 1:
    if check_price() < 70:
        send_mail()
        print("email was sent")
    time.sleep(3600)
