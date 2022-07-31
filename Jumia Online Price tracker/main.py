import requests
from bs4 import BeautifulSoup
import smtplib
URL = 'https://www.jumia.com.ng/oraimo-riff-smaller-for-comfort-true-wireless-earbuds-black-89937317.html'
BUY_PRICE = 85000
MY_EMAIL = 'name@gmail.com'
PWD = 'YOUR OWN'

response = requests.get(url=URL)
web_data = response.text
soup = BeautifulSoup(web_data, 'html.parser')
price_tag = soup.find(name='span', class_='-b -ltr -tal -fs24').getText().strip('₦')
product_name = soup.find(name='h1', class_='-fs20 -pts -pbxs').text

price_as_float = float(price_tag.replace(',', ''))
# print(price_as_float)

if price_as_float <= BUY_PRICE:
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        # Secure the connection
        connection.starttls()
        # login the user
        connection.login(user=MY_EMAIL, password=PWD)
        # send email
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f'Subject:Jumia Price drop alert!!!.\n\nYour desired product {product_name} price has dropped to ₦{price_tag}\n{URL} '
            .encode("utf-8")
        )

