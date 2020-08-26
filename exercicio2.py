"""
Autor: Samuel Amico
Data: 26/08/2020
Exercicio 02
----------------
Jogue o jogo ate encontrar o numero igual ao dado.

"""

from selenium.webdriver import Chrome
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

browser = Chrome()
browser.get(url)

sleep(3)

# Get the goal value to win the game
ps = browser.find_elements_by_tag_name('p')
value_goal = int((ps[-1].text).split(":")[-1].strip())

ancora_value = browser.find_element_by_tag_name('a')
ancora_value.click()


while True:
    ancora_value = browser.find_element_by_tag_name('a')
    ancora_value.click()

    value = browser.find_elements_by_tag_name('p')[-1].text
    try:
        if (int(value) == value_goal): 
            break
    except:
        break


print(f"VENCI O JOGO!! {value}")

browser.quit()


