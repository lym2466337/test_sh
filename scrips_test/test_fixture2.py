import pytest
def get_list():
    li_list=[]
    with open("./data.txt",'r') as f:
        for i in f.readlines():
            #eval函数就是实现list、dict、tuple与str之间的转化,从而完成将读取的数据转换回元祖转入列表中，多用于文件读取数据后的转换
            li_list.append(eval(i.split("=")[-1]))
    return li_list



class Test_b:
    @pytest.mark.parametrize("a,b",get_list())
    def test_001(self,a,b):
        print(a,b)