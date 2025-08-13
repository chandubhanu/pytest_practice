import pytest

class TestClass:
    @pytest.mark.parametrize('num1,num2',[(1,1),(1,2),(3,3),(10,20)])
    def test_Calculation(self,num1,num2):
        assert num1==num2