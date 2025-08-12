import pytest

class TestLogin:

    def test_LoginByEmail(self,setup):
        print("This is lgin by email...")
        assert True==True

    def test_LoginByFacebook(self,setup):
        print("This is lgin by Facebook...")
        assert True == True

    def test_LoginByTwitter(self,setup):
        print("This is lgin by Twitter...")
        assert True == True