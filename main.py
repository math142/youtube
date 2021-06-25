import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import os
import time
def main():
    driver = configuration()
    motcle = sys.argv[1]
    recherche(driver,motcle)

def configuration():
    """
    Permet de faire la configuration nécessaire pour faire le scrapping
    :return: driver
    """

    path = "/usr/lib/chromium-browser/chromedriver"
    driver = webdriver.Chrome(path)
    driver.implicitly_wait(20)
    driver.get("https://www.youtube.com/")
    return driver
def recherche(driver,motcle):
    actionChain = ActionChains(driver)
    search = driver.find_element_by_id("search")
    search.send_keys(motcle)
    search.send_keys(Keys.RETURN)
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div#contents ytd-item-section-renderer>div#contents a#thumbnail')))
    time.sleep(5)
    content =  driver.find_elements(By.CSS_SELECTOR, 'div#contents ytd-item-section-renderer>div#contents a#thumbnail')
    links = []
    for item in content:
        links+= [item.get_attribute('href')]
        title = driver.find_element_by_id('title')
        titre = title.get_attribute('title')
        print(titre)
    #for link in range(len(links)):
     #   os.system('youtube-dl {0}'.format(links[link]))
        

    time.sleep(5)
if __name__ == '__main__':
    main()