from selenium.webdriver import Chrome
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

browser = Chrome()
browser.get(url)

sleep(3)

a = browser.find_element_by_tag_name('a')
print(a.text)
a.click()
a.click()
ps = browser.find_elements_by_tag_name('p')
print(ps[-1].text)

sleep(3)
browser.quit()