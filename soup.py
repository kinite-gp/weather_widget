import requests
from bs4 import BeautifulSoup
from config import AREA

today_link = f"https://www.google.com/search?q=weather {AREA} province"
tomorrow_link = f"https://www.google.com/search?q=weather {AREA} province tomorrow"

def connector():

    data = {
        "today" : {
            "temp" : None,
            "status" : None,
        },
        "tomorrow" : {
            "status" : None
        }
    }

    response = requests.get(today_link)

    s = BeautifulSoup(response.text, "html.parser")
    s = s.find("body")
    s = s.find("div", attrs={"id":"main"})
    s = s.find("div", attrs={"class":"Gx5Zad xpd EtOod pkphOe"})
    temp = s.find("div" , attrs={"class":"BNeawe iBp4i AP7Wnd"})
    status = s.find("div", attrs={"class":"BNeawe tAd8D AP7Wnd"})

    data["today"]["temp"] = temp.text
    data["today"]["status"] = status.text

    response = requests.get(tomorrow_link)

    s = BeautifulSoup(response.text, "html.parser")
    s = s.find("body")
    s = s.find("div", attrs={"id":"main"})
    s = s.find("div", attrs={"class":"Gx5Zad xpd EtOod pkphOe"})

    status_tomo = s.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"})
    data["tomorrow"]["status"] = status_tomo.text.split("\n")[1]

    return data