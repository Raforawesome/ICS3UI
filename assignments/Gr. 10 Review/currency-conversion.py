# Class template - to be used for all questions
"""
Assignment Question 1/1
Author: Raforawesome
Due Date: Feb 10, 2022 11:58 PM
Question or problem: Week 1 Question 1 - Funds Conversion
Class: ICS3UI-02
"""
from urllib.request import urlopen, Request  # HTTP Utils
import json  # Decoding HTTP requests

hdr = {  # http request headers to ensure our request doesn't get denied
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    # 'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "en-CA,en-US;q=0.7,en;q=0.3"
}
req = Request('https://www.raforaweso.me/ics/currencyrates/', headers=hdr)  # Create the request object
rates_raw = urlopen(req).read()  # Execute the request and read the return
rates_json = rates_raw.decode('utf-8')  # Decode the bytes object into a string

rates = json.loads(rates_json)  # Decode json string into dictionary (Contains rates for USD, JPY, AED, and ILS)
symbols = {
    'USD': '$',
    'JPY': '¥',
    'AED': 'د.إ',
    'ILS': '₪'
}

print(
    "This program calculates currencies converted to amounts in other currencies."
    "\nPlease enter a dollar value in CAD, including decimals (i.e. 200.0):"
)
amount = input()
assert float(amount) != 0.0, "Please enter a valid and non-zero float."  # Validating input


def getConversionString(c_code, money):
    rate = rates[c_code]
    assert type(rate) is not None, "Invalid currency code!"
    converted_money = float(money) * rate
    return str(round(converted_money, 2)) + " " + c_code + ", at an exchange rate of " + symbols[c_code] + str(
        rate) + " per $1.00"


formatted = "$" + amount  # Just for cleaner code inside the print statement
final_message = formatted + " in Canadian dollars is equivalent to:"

for code in list(rates):
    final_message += "\n" + getConversionString(code, amount)

print(final_message)
