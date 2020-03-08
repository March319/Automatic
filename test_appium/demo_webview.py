from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueQiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "emulator"
        caps["udid"] = "emulator-5554"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = True
        caps["dontStopAppOnReset"] = True
        caps["skipServerInstallation"] = True
        caps["unicodeKeyboard"] = True
        caps["chromedriverExecutable"] = r"D:\chromedriver_V2.20.exe"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

    def test_webview(self):
        locator_trade = (By.XPATH, "//*[contains(@resource-id, 'tabs')]//*[@text='交易']")
        locator_hongkong_stock = (By.CSS_SELECTOR, '.trade_home_xueying_SJY')
        locator_phone_number = (By.CSS_SELECTOR, '[placeholder="请输入手机号"]')
        locator_verify_number = (By.CSS_SELECTOR, '[placeholder="请输入验证码"]')
        locator_submit = (By.CSS_SELECTOR, ".open_form-submit_1Ms")
        locator_toast = (By.CSS_SELECTOR, ".Toast_toast_22U")
        # 点击交易
        self.driver.find_element(*locator_trade).click()
        # 切换至webview
        WebDriverWait(self.driver, 20).until(lambda x: len(self.driver.contexts) > 1)
        self.driver.switch_to.context(self.driver.contexts[-1])
        current_windows = len(self.driver.window_handles)
        self.driver.find_element(*locator_hongkong_stock).click()
        # 切换窗口
        WebDriverWait(self.driver, 20).until(lambda x: len(self.driver.window_handles) - current_windows > 0)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator_phone_number))
        self.driver.find_element(*locator_phone_number).send_keys("13412345678")
        self.driver.find_element(*locator_verify_number).send_keys("1234")
        self.driver.find_element(*locator_submit).click()
        toast = self.driver.find_element(*locator_toast).text
        # 切换至Native
        self.driver.switch_to.context(self.driver.contexts[0])
        self.driver.find_element(MobileBy.ID, "action_bar_back").click()
        assert '请输入正确的验证码' in toast

    def teardown(self):
        self.driver.quit()