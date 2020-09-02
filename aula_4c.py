"""
Atividades:

1. Pegar todos os links da aula
2. Fazer o exercicio 3

"""
from selenium.webdriver import Chrome
from time import sleep

url = 'https://selenium.dunossauro.live/aula_04.html'

browser = Chrome()
browser.get(url)

sleep(2)