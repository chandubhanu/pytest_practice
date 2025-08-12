import pytest


class TestClass:

    @pytest.mark.second
    def test_LoginByEmail(self):
        print("This is lgin by email...")
        assert True == True

    @pytest.mark.third
    def test_LoginByFacebook(self):
        print("This is lgin by Facebook...")
        assert True == True

    @pytest.mark.fifth
    def test_LoginByTwitter(self):
        print("This is lgin by Twitter...")
        assert True == True

    @pytest.mark.first
    def test_SignByEmail(self):
        print("This is lgin by email...")
        assert True == True

    @pytest.mark.six
    def test_SignByFacebook(self):
        print("This is lgin by Facebook...")
        assert True == True

    @pytest.mark.fouth
    def test_SignByTwitter(self):
        print("This is lgin by Twitter...")
        assert True == True
