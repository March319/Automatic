from test_wework.page.main import Main


class TestAddMember:
    def setup(self):
        self.Main = Main()

    def test_save(self):
        self.Main.add_member().save()

    def test_cancel(self):
        pass
