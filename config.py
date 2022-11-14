from fake_user_agent.main import user_agent
import random
import requests

s = requests.Session()
browsers = ["firefox", "chrome", "opera", "edge", "safari"]
URL = "https://vip.blokino.org/anime/"

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Cookie": "",
    # "Host": "animego.org",
    # "Referer": "https://animego.org/",
    # "Sec-Fetch-Dest": "document",
    # "Sec-Fetch-Mode": "navigate",
    # "Sec-Fetch-Site": "same-origin",
    # "Sec-Fetch-User": "?1",
    # "Upgrade-Insecure-Requests": "1",
    "User-Agent": "",
}


def connect(url, settings):
    global s
    if settings["User-Agent"] == "":
        settings["User-Agent"] = user_agent(random.choice(browsers))
    src = s.get(url, headers=settings)
    return src


