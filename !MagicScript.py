import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=orlando+magic&sxsrf=ALiCzsbxhEIoO58P6AzKyu1oaxcPz62Bhw%3A1667710279771&ei=Rz1nY5vZLouxkvQP1Z-i2Ao&oq=orlando+ma&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMgkIIxAnEEYQ_QEyBAgjECcyBAgjECcyCgguELEDEIMBEEMyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATIKCAAQsQMQgwEQQzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMhAIABCABBCHAhCxAxCDARAUOgcIIxDqAhAnOgoILhCDARCxAxBDOgQILhBDOgQIABBDOgcILhDUAhBDOggILhCDARCxAzoNCC4QgwEQsQMQgAQQQzoKCAAQgAQQhwIQFDoICC4QgAQQ1AJKBAhNGAFKBAhBGABKBAhGGABQAFjkCmCXFGgBcAF4AIABYYgBlQaSAQIxMJgBAKABAbABCsABAQ&sclient=gws-wiz-serp"

getResponse = requests.get(url)
soup = BeautifulSoup(getResponse.text, 'html.parser')

schedule = soup.findAll("span", text="Today")

def tonight():
    if schedule == []:
        print("Magic are not playing tonight")
    else:
        print("Magic are playing tonight!")

tonight()