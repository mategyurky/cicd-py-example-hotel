import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure
import pytest


class TestHootel(object):
    def setup_method(self):
        URL = 'http://hotel-v3.progmasters.hu/'
        options = Options()

        # headless mode kell hogy felhőben is lefusson
        options.add_argument("--headless")
        # headless módban nem lehet start maximized helyette self.browser.set_window_size(1920, 1080) kell alulra
        # options.add_argument("start-maximized")

        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=options)
        self.browser.get(URL)

        self.browser.set_window_size(1920, 1080)


    def teardown_method(self):
        self.browser.quit()

    # allure riportok tesztreszabása, olvashatóvá tétele dekorátorral
    @allure.title("Hootel Login")
    @allure.description("A belépés tesztelése")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("login" , "hootel" , "selenium" , "e2e")
    def test_login(self):
        email = "hiwasi1765@wisnick.com"
        password = "tesztelek2021"

        login_btn = self.browser.find_element(By.XPATH, '//a[@class="nav-link"]')
        time.sleep(1)
        login_btn.click()

        email_input = self.browser.find_element(By.ID, 'email')
        email_input.send_keys(email)

        password_input = self.browser.find_element(By.ID, 'password')
        password_input.send_keys(password)

        submit_btn = self.browser.find_element(By.NAME, 'submit')
        submit_btn.click()
        time.sleep(1)

        logout_btn = self.browser.find_element(By.ID, 'logout-link')

        # dinamkikus allure description felülírja a statikusat:
        allure.dynamic.description(f"email : {email} password: {password}")

        assert logout_btn.text == "Kilépés"

    @allure.title("Hootel List")
    @allure.description("A szállásokat listázom ki")
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag("hootel" , "e2e")
    def test_hotel_list(self):
        hotel_list_btn = self.browser.find_element(By.XPATH, '//button[@class="btn btn-outline-primary btn-block"]')
        hotel_list_btn.click()
        time.sleep(1)

        hotel_list = self.browser.find_elements(By.XPATH, '//h4[@style="cursor: pointer"]')
        assert len(hotel_list) != 0
        assert len(hotel_list) == 10
