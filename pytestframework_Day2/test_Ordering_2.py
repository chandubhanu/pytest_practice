import pytest


class TestClass:

    @pytest.mark.run(order=6)
    def test_LoginByEmail(self):
        print("This is lgin by email...")
        assert True == True

    @pytest.mark.run(order=5)
    def test_LoginByFacebook(self):
        print("This is lgin by Facebook...")
        assert True == True

    @pytest.mark.run(order=4)
    def test_LoginByTwitter(self):
        print("This is lgin by Twitter...")
        assert True == True

    @pytest.mark.run(order=3)
    def test_SignByEmail(self):
        print("This is lgin by email...")
        assert True == True

    @pytest.mark.run(order=2)
    def test_SignByFacebook(self):
        print("This is lgin by Facebook...")
        assert True == True

    @pytest.mark.run(order=1)
    def test_SignByTwitter(self):
        print("This is lgin by Twitter...")
        assert True == True
