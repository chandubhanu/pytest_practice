import pytest


class TestClass:
    @pytest.mark.skip
    def test_LoginByEmail(self):
        print("This is lgin by email...")
        assert True == True

    @pytest.mark.skip
    def test_LoginByFacebook(self):
        print("This is lgin by Facebook...")
        assert True == True

    @pytest.mark.skip
    def test_LoginByTwitter(self):
        print("This is lgin by Twitter...")
        assert True == True

    def test_SignByEmail(self):
        print("This is lgin by email...")
        assert True == True

    def test_SignByFacebook(self):
        print("This is lgin by Facebook...")
        assert True == True

    def test_SignByTwitter(self):
        print("This is lgin by Twitter...")
        assert True == True
