"""
    pytest.mark.parametrize(“变量参数名称”，变量数据列表[‘123’,‘34’,‘567’,‘78’])
    上面的变量个数有4个，测试用例传入变量名称后，会依序4次使用变量的数据，执行4次测试用例
    def test001(self,变量参数名称)
         assert 变量名称
"""
import pytest
class Test_A:
    #单个参数 a
    # @pytest.mark.parametrize("a",[1,2,3])
    # def test_001(self,a):
    #     print("参数的数据为 %s"% a)
    #多个参数 a,b ,此时 （1，2）分别为a 的第一次值 和 b的第一次值
    #列表中一个元祖即代表执行一次用例，而元祖内的数据则分别赋值给多个参数
    @pytest.mark.parametrize("a,b,c",[(1,2,3),(4,5,6)])
    #当装饰器的参数有设定里多个的时候，测试用例在调用时需要把所有的参数全部传入
    def test_002(self,a,b,c):
        print("参数a为 %s" % a)
        print("参数b为 %s" % b)
        print("参数c为 %s" % c)
