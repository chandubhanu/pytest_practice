import pytest


class TestClass:
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_LoginByEmail(self):
        print("This is lgin by email...")
        assert True == True

    @pytest.mark.sanity
    def test_LoginByFacebook(self):
        print("This is lgin by Facebook...")
        assert True == True

    @pytest.mark.regression
    def test_LoginByTwitter(self):
        print("This is lgin by Twitter...")
        assert True == True

    @pytest.mark.sanity
    def test_SignByEmail(self):
        print("This is lgin by email...")
        assert True == True

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_SignByFacebook(self):
        print("This is lgin by Facebook...")
        assert True == True

    @pytest.mark.regression
    def test_SignByTwitter(self):
        print("This is lgin by Twitter...")
        assert True == True
