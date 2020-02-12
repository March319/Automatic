import time
from selenium.webdriver.common.by import By
from test_wework.page.base_page import BasePage


class Contact(BasePage):

    def add_member(self):
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
        # self.driver.find_element(By.CSS_SELECTOR, ".member_colRight_operationBar:nth-child(3) > .js_btn_save").click()
        # # 判断保存成功
        # toast_loc = (By.XPATH, './/*[@class="ww_tip success"]')
        # # toast_loc = (By.CSS_SELECTOR, ".ww_tip success")
        # WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(toast_loc))
        # # 增加断言判断保存成功

    def cancel(self):
        pass

    def save_and_continue(self):
        pass
        # 保存并添加
        print(123)

    def add_img(self):
        self.driver.find_element(By.CSS_SELECTOR, '#js_upload_file').click()
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '.js_file').send_keys(r"C:\Users\Alice\Desktop\g.jpg")
        self.driver.find_element(By.CSS_SELECTOR, '.qui_btn.ww_btn.ww_btn_Blue.js_save').click()
        # self.driver.find_element(By.CSS_SELECTOR, '.js_no_img').click()

    def modify_dept(self):
        self.driver.find_element(By.CSS_SELECTOR, '.js_show_party_selector').click()
        time.sleep(1)
        self.driver.switch_to.default_content()
        # time.sleep(3)
        # self.driver.find_element(By.CSS_SELECTOR, '.jstree-children:nth-child(1)').click()
        time.sleep(1)
        # 删除部门
        self.driver.find_element(By.CSS_SELECTOR, '.ww_commonImg.ww_commonImg_DeleteItem.js_delete').click()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           '.js_left_col.jstree.jstree-2.jstree-default >ul>li>ul>li:nth-child(3)')
        element.click()
        text = element.get_attribute('textContent')
        children = self.driver.find_elements(By.CSS_SELECTOR,
                                             '.js_left_col.jstree.jstree-2.jstree-default >ul>li>ul>li')
        print(len(children))
        print(text)

        # self.driver.find_element(By.CSS_SELECTOR, '.js_submit').click()
        # self.driver.find_element(By.LINK_TEXT, '总裁办').click()
