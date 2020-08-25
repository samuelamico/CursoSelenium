"""
Autor: Samuel Amico
Data: 25/08/2020
Exercicio 01
----------------
Gere um dicionario, onde a chave é a tag H1
* O valor deve ser um novo dicionario
* cada chave do valor devera ser o valor do 'atributo'
* cada valor deve ser o texto contido no elemento

"""

from selenium.webdriver import Chrome 
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

browser = Chrome()
browser.get(url)

# waiting delay time
sleep(3)

# Lendo as tags:
h1 = browser.find_element_by_tag_name('h1')
ps_list = browser.find_elements_by_tag_name('p')

dict_atributos = {}
for ps in ps_list:
    chave = ps.get_attribute("atributo")
    dict_atributos[chave] = ps.text

dict_pag = {h1.text : dict_atributos}

print(dict_pag)

browser.quit()