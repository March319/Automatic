from selenium.webdriver.common.by import By
from test_wework.page.add_member import AddMember
from test_wework.page.base_page import BasePage


class Main(BasePage):

    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def add_member(self):
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_item_title").click()
        return AddMember(self.driver)

    def import_contact(self):
        pass

    def member_join(self):
        pass

    def group_msg(self):
        pass

    def service_contact(self):
        pass

    def attendance(self):
        pass
