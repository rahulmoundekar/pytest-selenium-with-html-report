import pytest
from selenium import webdriver
import time

baseURL = "http://demo.sentrifugo.com/"


class TestSentrifugoHrms:

    @pytest.fixture()
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(baseURL)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_homeTitle(self, setUp):
        assert self.driver.title == "Sentrifugo - Open Source HRMS"

    def test_login(self, setUp):
        self.driver.find_element_by_id("username").send_keys("em01")
        self.driver.find_element_by_id("password").send_keys("sentrifugo")
        self.driver.find_element_by_id("loginsubmit").click()
        time.sleep(5)
        self.driver.find_element_by_id("logoutbutton").click()
        self.driver.find_element_by_link_text("Logout").click()
