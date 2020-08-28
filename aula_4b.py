from selenium.webdriver import Chrome
from time import sleep

url = 'https://selenium.dunossauro.live/aula_04_b.html'

browser = Chrome()
browser.get(url)

sleep(2)


def find_by_text(browser,tag,text):
    elementos = browser.find_elements_by_tag_name(tag)

    for elemento in elementos:
        if text == elemento.text:
            return elemento


for nome in ['um','dois','tres','quatro']:
    find_by_text(browser,'div',nome).click()

browser.back()