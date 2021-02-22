#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
import time

import flask

app = flask.Flask(__name__)


@app.route('/edp', methods=['GET'])
def home():
    return str(get_edp());

def get_edp():
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920x1080")

        driver = webdriver.Chrome(chrome_options=options)
        driver.get('https://www.dealabs.com/discussions/le-topic-des-erreurs-de-prix-1056379')

        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Dernière page"]'))
        )


        btn_last_page = driver.find_elements(By.XPATH, '//*[@aria-label="Dernière page"]')[0]
        btn_last_page.click()
        nb_edp = len(driver.find_elements(By.XPATH, '//li[contains(@class, "commentList-item")]'))
        driver.quit()
        return nb_edp

    except Exception as e:
        print(e)
        print("Erreur : {0}".format(e))


app.run(host='0.0.0.0')
