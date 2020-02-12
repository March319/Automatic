from test_wework.page.main import Main


class TestAddMember:
    def setup(self):
        self.Main = Main()

    def test_add_member(self):
        self.Main.goto_contact().add_member()

    def test_add_img(self):
        self.Main.goto_contact().add_img()

    def test_modify_dept(self):
        self.Main.goto_contact().modify_dept()

    def test_cancel(self):
        pass
