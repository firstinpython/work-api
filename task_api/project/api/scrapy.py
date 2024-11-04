from enum import verify

from bs4 import BeautifulSoup
import requests
def get_response(page):
    response = requests.get(url = "https://rus.hitmotop.com/artists",verify=False)
    return response
def find_links():
    links_mass = []
    id_counter = 1
    for i in range(1,23):
        response = get_response(i * 46)
        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.find("ul",class_ = "singers-list album-list")
        links = items.find_all("li")

        for link in links:
            dictionary = {
                'id':id_counter,
                'name':link.find("a").get_text(strip=True),
                'link':f"https://rus.hitmotop.com{link.find('a').get('href')}"

            }
            links_mass.append(dictionary)
            id_counter+=1
    return links_mass
