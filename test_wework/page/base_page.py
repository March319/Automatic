from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            chrome_option = Options()
            # chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenium\AutomationProfile"
            chrome_option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=chrome_option)
            self.driver.implicitly_wait(5)  # seconds
            self.driver.get(self._base_url)
        else:
            self.driver = driver

    # def _element_wait(self, timeout, method):
    #     # element1 = (By.CSS_SELECTOR, '[title="MTSC2020 中国互联网测试开发大会议题征集"]')
    #     return WebDriverWait(self.driver, timeout).until(
    #         expected_conditions.element_to_be_clickable(method))
