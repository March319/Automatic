import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage


class Contact(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'

    def add_member(self):
        self.driver.find_element(By.LINK_TEXT, "添加成员").click()

    def input_info(self):
        time.sleep(2)
        # 添加姓名
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys("Add_Name")
        # 添加别名
        self.driver.find_element(By.ID, "memberAdd_english_name").click()
        self.driver.find_element(By.ID, "memberAdd_english_name").send_keys("AliasName")
        # 添加账号
        self.driver.find_element(By.ID, "memberAdd_acctid").click()
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("00002")
        # 选择性别
        self.driver.find_element(By.CSS_SELECTOR, '.ww_radio[value="2"]')
        # 添加手机号码
        self.driver.find_element(By.CSS_SELECTOR, ".ww_telInput_zipCode_input").click()
        self.driver.find_element(By.CSS_SELECTOR, 'li[data-value="852"]').click()
        self.driver.find_element(By.ID, "memberAdd_phone").click()
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("13456789999")
        # 添加座机
        self.driver.find_element(By.ID, "memberAdd_telephone").click()
        self.driver.find_element(By.ID, "memberAdd_telephone").send_keys("13456789999")
        # 添加邮箱
        self.driver.find_element(By.ID, "memberAdd_mail").click()
        self.driver.find_element(By.ID, "memberAdd_mail").send_keys("qq@qq.com")
        # 添加地址
        self.driver.find_element(By.ID, "memberEdit_address").send_keys("GD")
        # Todo选择部门

        # 添加职务
        self.driver.find_element(By.ID, "memberAdd_title").click()
        self.driver.find_element(By.ID, "memberAdd_title").send_keys("CTO")

        # 添加头像
        self.driver.find_element(By.CSS_SELECTOR, '#js_upload_file').click()
        self.driver.find_element(By.CSS_SELECTOR, '.js_file').send_keys(r"C:\Users\Alice\Desktop\g.jpg")
        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_class_name('cropper-face'))
        self.driver.find_element(By.CSS_SELECTOR, '.qui_btn.ww_btn.ww_btn_Blue.js_save').click()

        # 保存
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()

    def modify_member(self, original_name, new_name):
        # 等待用户列表界面
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_class_name('js_title'))
        xpath = "//td[contains(.," + '"' + original_name + '"' + ")]"
        self.driver.find_element(By.XPATH, str(xpath)).click()
        # self.driver.find_element(By.XPATH, '//td[contains(.,"只好")]').click()
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_class_name('js_edit'))
        self.driver.find_element(By.CSS_SELECTOR, '.js_edit').click()
        self.driver.find_element(By.NAME, 'username').clear()
        # 修改姓名
        self.driver.find_element(By.NAME, 'username').send_keys(new_name)
        # 保存
        self.driver.find_element(By.CSS_SELECTOR, '.js_save').click()

    def get_member_msg(self):
        # 判断保存成功
        # toast_loc = (By.XPATH, './/*[@class="ww_tip success"]')
        toast_loc = (By.CSS_SELECTOR, ".ww_tip.success")
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(toast_loc))
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_class_name('js_title'))
        time.sleep(3)
        result = []
        # 获取新增用户的信息
        for element in self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td'):
            result.append(element.get_attribute('textContent'))
            print(result)
        return result

    def get_modify_member_info(self):
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_class_name(
            'member_display_cover_detail_name'))
        member_info = self.driver.find_element(By.CSS_SELECTOR, '.member_display_cover_detail_name').get_attribute(
            'textContent')
        return member_info
