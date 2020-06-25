import requests
from telegrambot import Bot

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup


def get_elem():
    url = "https://freesteam.ru/category/active/"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")

    for Elem in soup.find_all("div"):
        if Elem.get("id") == "blog-grid":
            return Elem


bot = Bot('1277615985:AAGLGt-_Kgw82mIhvwwjjor_yOifJuhh8Ng')


@bot.command('/start')
def send_message(ctx):
    return "type /get to get halava"


@bot.command('/get')
def send_message(ctx):
    result = []
    for link in get_elem().find_all("a"):
        if "Раздача" in link.text:
            result.append("\n>{}".format(link.text) + " {}".format(link.get("href")))
    return ' '.join(result)


bot.start()
