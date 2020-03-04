from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestXueQiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = True
        # caps["dontStopAppOnReset"] = True
        caps["skipServerInstallation"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(40)

    def test_search(self):
        # 搜索
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(By.XPATH, "//*[@text='09988']").click()
        self.driver.find_element(MobileBy.ID, "follow_btn").click()
        # 验证已添加
        self.driver.find_element(MobileBy.ID, "action_close").click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        self.driver.find_element(By.XPATH, "//*[contains(@resource-id, 'title_container')]//*[@text='股票']").click()
        resource_id = self.driver.find_element(By.XPATH,
                                               "//*[@text='09988']/../../..//*[contains(@resource-id, 'followed_btn')]").get_attribute(
            'resource-id')
        assert 'followed_btn' in resource_id

    def teardown(self):
        pass
        # self.driver.quit()
