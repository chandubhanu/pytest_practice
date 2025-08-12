import pytest

class TestClass:
    @pytest.fixture()
    def setup(self):
        print("Launch Browser")
        print("Open Apllication")
        yield
        print("Closing Browser ")
    def test_Login(self,setup):
        print("This is Login test")

    def test_Search(self,setup):
        print("This is Search test")

    def test_Advancedsearch(self,setup):
        print("This is test_Advancedsearch")