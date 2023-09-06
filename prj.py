from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://www.youtube.com/results?search_query=bink+no+sake')
video_element = navegador.find_element('xpath','//*[@id="video-title"]')
video_element.click()
time.sleep(204)
navegador.quit()

