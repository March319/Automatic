import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_wework.page.base_page import BasePage


class AddMember(BasePage):

    def save(self):
        # element_add_user = ()
        # self._element_wait(10, element_add_user)
        time.sleep(3)
        # self.driver.find_element(By.LINK_TEXT, "添加成员").click()

        # 添加姓名
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys("小子")
        # 添加别名
        self.driver.find_element(By.ID, "memberAdd_english_name").click()
        self.driver.find_element(By.ID, "memberAdd_english_name").send_keys("alice")
        # 添加账号
        self.driver.find_element(By.ID, "memberAdd_acctid").click()
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("00001")
        # 选择性别
        # 添加手机号码
        self.driver.find_element(By.ID, "memberAdd_phone").click()
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("13456789999")
        # 添加座机
        self.driver.find_element(By.ID, "memberAdd_telephone").click()
        self.driver.find_element(By.ID, "memberAdd_telephone").send_keys("13456789999")
        # 添加邮箱
        self.driver.find_element(By.ID, "memberAdd_mail").click()
        self.driver.find_element(By.ID, "memberAdd_mail").send_keys("qq@qq.com")
        # 添加地址
        self.driver.find_element(By.ID, "memberEdit_address").send_keys("深圳")
        # 选择部门

        # 待细化
        self.driver.find_element(By.CSS_SELECTOR, ".ww_commonImg_SmallGrayMore").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ww_groupSelBtn_item").click()
        # 添加职务
        self.driver.find_element(By.ID, "memberAdd_title").click()
        self.driver.find_element(By.ID, "memberAdd_title").send_keys("CEO")

        # self.driver.find_element(By.CSS_SELECTOR, ".member_edit_item:nth-child(1) .ww_label > span").click()

        # 保存
        self.driver.find_element(By.CSS_SELECTOR, ".member_colRight_operationBar:nth-child(3) > .js_btn_save").click()
        # 判断保存成功
        toast_loc = (By.XPATH, './/*[@class="ww_tip success"]')
        # toast_loc = (By.CSS_SELECTOR, ".ww_tip success")
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(toast_loc))
        # 增加断言判断保存成功

    def cancel(self):
        pass

    def save_and_continue(self):
        pass
