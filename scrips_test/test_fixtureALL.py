"""
    需求：使用APP，完成内容添加
    细节：1.需要先判断是否登入，若未登入，则进行登入
        2。登入后再执行内容添加操作

"""
import pytest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
def info():
    return [("第一次","第一个公司","第一份工作"),("第二次","第二个公司","第二份工作")]

class Test_a:
    def setup_class(self):
        desire_caps={
            "platformName":'Android',
            "platformVersion":'7.1.2',
            "deviceName":'xxx',
            "unicodeKeyboard":True,
            "resetKeyboard":True,
            "appPackage":'com.android.contacts',
            "appActivity":'.activities.PeopleActivity',
            "noReset":True,
            "automationName":'Uiautomator2'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
    def teardown_class(self):
        self.driver.quit()

    def wait_ele(self,tag,var):
        if tag=="id":
            return WebDriverWait(self.driver,5,0.5).until(lambda x:x.find_element_by_id(var))
        if tag=="class":
            return WebDriverWait(self.driver,5,0.5).until(lambda x:x.find_element_by_class_name(var))
        if tag=="xpath":
            return WebDriverWait(self.driver,5,0.5).until(lambda x:x.find_element_by_xpath(var))

    @pytest.fixture(params=[('xxxx','18888888888',"27387723@qq.com")])
    def first_add(self,request):
        #先输入姓名、电话、邮箱
        name,number,e_mail=request.param
        print("..姓名是%s" %name)
        print("..电话是%s" %number)
        print("..邮箱是%s" %e_mail)
        add_contract=self.wait_ele('id',"com.android.contacts:id/floating_action_button")
        add_contract.click()

        self.wait_ele('xpath',"//*[contains(@text,'姓名')]").send_keys(name)
        self.wait_ele('xpath',"//*[contains(@text,'电话')]").send_keys(number)

    @pytest.mark.usefixtures('first_add')
    @pytest.mark.parametrize('nichen,company,work',info())
    def test_add(self,nichen,company,work):
        self.wait_ele("xpath","//*[contains(@text,'更多')]").click()

        self.wait_ele("xpath","//*[contains(@text,'昵称')]").send_keys(nichen)
        self.wait_ele("xpath","//*[contains(@text,'公司')]").send_keys(company)
        self.wait_ele("xpath","//*[contains(@text,'职务')]").send_keys(work)

        self.wait_ele('id',"com.android.contacts:id/menu_save").click()
        self.driver.implicitly_wait(5)
        self.driver.back()
        assert True



