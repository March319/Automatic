import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage


class ManageTool(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#manageTools'

    def item_desc(self, path, pic_name):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "素材库").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "图片").click()
        self.driver.find_element(By.CSS_SELECTOR, '.js_upload_file_selector').click()
        self.driver.find_element(By.CSS_SELECTOR, '#js_upload_input').send_keys(path + '\\' + pic_name)
        # 上传的图片为最后一个元素
        input_pic_name = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_elements_by_class_name("js_pic_name_show"))[-1].get_attribute('textContent')
        if input_pic_name == pic_name:
            self.driver.find_element(By.PARTIAL_LINK_TEXT, '完成').click()

    def get_message(self):
        time.sleep(1)
        get_pic_name = self.driver.find_element(By.CSS_SELECTOR, '.js_pic_name_show').get_attribute('textContent')
        # print(get_pic_name)
        return get_pic_name
