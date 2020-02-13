import pytest

from page.contact import Contact


class TestAddMember:
    def setup(self):
        self.Contact = Contact()

    def test_add_member(self):
        self.Contact.add_member()
        self.Contact.input_info()
        assert 'Add_Name' in '|'.join(self.Contact.get_member_msg())

    @pytest.mark.parametrize("original_name, new_name", {("Add_Name", "New_name")})
    def test_modify_member(self, original_name, new_name):
        self.Contact.modify_member(original_name, new_name)
        assert new_name in self.Contact.get_modify_member_info()
