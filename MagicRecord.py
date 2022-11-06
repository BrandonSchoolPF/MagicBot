from bs4 import BeautifulSoup
import requests

import requests
from bs4 import BeautifulSoup

getResponse = requests.get("https://www.basketball-reference.com/teams/ORL/")


soup = BeautifulSoup(getResponse.text, 'html.parser')


html_wins = soup.find("td", attrs={"class": "right"},)

wins = html_wins.string



rows = soup.findAll("td", attrs={"class": "right"},)[1]

loss = rows.string









#loss = html_loss.string

#print(loss)


