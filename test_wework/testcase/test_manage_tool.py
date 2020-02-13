import pytest

from page.manage_tool import ManageTool


class TestAddMember:
    def setup(self):
        self.ManageTool = ManageTool()

    @pytest.mark.parametrize("pic_path, pic_name", {(r"C:\Users\Alice\Desktop", "h.jpg")})
    def test_add_img(self, pic_path, pic_name):
        self.ManageTool.item_desc(pic_path, pic_name)
        assert pic_name in self.ManageTool.get_message()
