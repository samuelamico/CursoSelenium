from selenium.webdriver import Chrome
from time import sleep

url = 'https://selenium.dunossauro.live/aula_04_a.html'

browser = Chrome()
browser.get(url)

sleep(3)

def find_by_href(browser,link):
    """
      Encontrar o elemento 'a' com o link = 'link'

    Argumentos:
        - browser: Instancia do browser
        - link: Link que será procurado   
    """
    elementos = browser.find_elements_by_tag_value('a')

    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento

lista_n_ordenada = browser.find_element_by_tag_name('ul') # 1

lis = lista_n_ordenada.find_elements_by_tag_name('li') # 2

lis[0].find_element_by_tag_name('a').text # 3

