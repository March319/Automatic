from selenium.webdriver.common.by import By
from test_wework.page.contact import Contact
from test_wework.page.base_page import BasePage
from test_wework.page.manage_tool import ManageTool


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_contact(self):
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_item_title").click()
        return Contact(self.driver)

    def goto_manage_tool(self):
        self.driver.find_element(By.LINK_TEXT, '管理工具').click()
        # self.driver.find_element(By.CSS_SELECTOR, ".frame_nav_item frame_nav_item_Curr").click()
        return ManageTool(self.driver)
