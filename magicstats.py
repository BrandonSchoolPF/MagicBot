import requests
from bs4 import BeautifulSoup

getResponse = requests.get("https://www.basketball-reference.com/leagues/NBA_2023_standings.html#site_menu_link")

standing = ""

# If request successful
if getResponse.status_code == 200:

    soup = BeautifulSoup(getResponse.text, 'html.parser')

    nbaTeams = soup.findAll("th", attrs={"class": "left"})

    # Scan for teams
    for team in nbaTeams:

        # If the substring is in the team's text
        if "Orlando Magic" in team.text:

            # Linear scan left to right through the entire team string
            for i in range(len(team.text)):

                # When the ( is reached
                if team.text[i] == "(":

                    # Append/Concatenate the first digit
                    standing += team.text[i + 1]

                    # If it is NOT closed by the parenthesis yet
                    if team.text[i + 2] != ")":
                        # Append/Concatenate the second digit
                        standing += team.text[i + 2]

            # Break the loop when desired team is found
            break




elif getResponse.status_code == 404:

    print("Not found.")