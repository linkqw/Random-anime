# basic imports

from config import connect, headers, URL, requests
from bs4 import BeautifulSoup
from functions import *

cookie = requests.get(url=URL, headers=headers).cookies
src = connect(url=URL, settings=headers)
soup = BeautifulSoup(src.text, "lxml")

result = [x.text for x in soup.find_all(class_="perehod")]

print(choice_of(result))
