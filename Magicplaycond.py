import requests
from bs4 import BeautifulSoup
#Actual Orlando Magic
url = "https://www.google.com/search?q=orlando+magic&sxsrf=ALiCzsbxhEIoO58P6AzKyu1oaxcPz62Bhw%3A1667710279771&ei=Rz1nY5vZLouxkvQP1Z-i2Ao&oq=orlando+ma&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMgkIIxAnEEYQ_QEyBAgjECcyBAgjECcyCgguELEDEIMBEEMyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATIKCAAQsQMQgwEQQzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMhAIABCABBCHAhCxAxCDARAUOgcIIxDqAhAnOgoILhCDARCxAxBDOgQILhBDOgQIABBDOgcILhDUAhBDOggILhCDARCxAzoNCC4QgwEQsQMQgAQQQzoKCAAQgAQQhwIQFDoICC4QgAQQ1AJKBAhNGAFKBAhBGABKBAhGGABQAFjkCmCXFGgBcAF4AIABYYgBlQaSAQIxMJgBAKABAbABCsABAQ&sclient=gws-wiz-serp"

#Test
#url = "https://www.google.com/search?q=cavs&sxsrf=ALiCzsYGOoRgLk2aJG1iRsaODemo183O0A%3A1667710777639&ei=OT9nY8_cJq-rwbkP5d6ZwAc&ved=0ahUKEwiP3fTj4pj7AhWvVTABHWVvBngQ4dUDCBA&uact=5&oq=cavs&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIJCCMQJxBGEP0BMgoILhCxAxCDARBDMgsIABCABBCxAxCDATIICAAQgAQQsQMyCwgAEIAEELEDEIMBMgoIABCxAxCDARBDMgsIABCABBCxAxCDATIKCAAQsQMQgwEQQzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBOgcIIxDqAhAnOgQIIxAnOgQILhBDOgoILhCDARCxAxBDOgQIABBDOg0IABCABBCHAhCxAxAUOggIABCxAxCDAUoECE0YAUoECEEYAEoECEYYAFAAWPEMYPMNaAFwAXgAgAFiiAG9ApIBATSYAQCgAQGwAQrAAQE&sclient=gws-wiz-serp"

#test2
#url = "https://www.google.com/search?q=wizards&oq=wizards&aqs=chrome..69i57.1124j0j9&sourceid=chrome&ie=UTF-8"

#Finding out when they play
getResponse = requests.get(url)
soup = BeautifulSoup(getResponse.text, 'html.parser')

schedule = soup.findAll("span", text="Today")

time = soup.findAll("span")[12]

time2 = time.string


#Finding out when they play next
nextplay = soup.findAll("span")[25]
next = nextplay.string



def tonight():
    if schedule == []:
        return "Magic are not playing tonight"
    else:
       return "Magic are playing tonight at " + time2 + "!"


