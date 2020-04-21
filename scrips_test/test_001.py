import pytest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
#使用使用params传入参数到工厂函数中的方式，让测试用例重复执行3次，即==传入的参数个数

@pytest.fixture(params=[1, 4, 'wl'])
def index1(request):
    return request.param
class Test_A:
    def setup_class(self):
        desired_caps = {
            'platformName': 'Android',  # 被测手机是安卓
            'platformVersion': '7.1.2',  # 手机安卓版本
            'deviceName': 'xxx',  # 设备名，安卓手机可以随意填写
            'appPackage': 'com.android.settings',  # 启动APP Package名称
            'appActivity': '.Settings',  # 启动Activity名称
            'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
            'resetKeyboard': True,  # 执行完程序恢复原来输入法
            # 'noReset': True,  # 不要重置App，特别注意 对于启动缓慢的APP，需要先打开过APP后，再使用软件打开APP才能正常打开
            'newCommandTimeout': 6000,  # 设置等待APP无响应时间,必须设置
            'automationName': 'UiAutomator2'
            # 'app': r'd:\apk\bili.apk',
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def teardown_class(self):

        self.driver.quit()

    # @pytest.fixture()
    # def first_page1(self):
    #     Driver_fuction.wait_ele("xpath","//*[contains(@test,('更多'))]").click()
    def wait_ele(self, tag, var):
        if tag == "xpath":
            return WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element_by_xpath(var))
        if tag == "id":
            return WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element_by_id(var))
        if tag == "class":
            return WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element_by_class_name(var))




    def test_001(self,index1):
        print("执行一次 ")
        self.wait_ele("id", "com.android.settings:id/search").click()
        input_num = self.wait_ele("id", "android:id/search_src_text")
        input_num.clear()
        input_num.send_keys(index1)
        if index1=='wl':
            self.wait_ele("xpath","//*[contain(@text,'WLAN直')]").click()
    #     assert index1==2
    # # def test_002(self):
    # #     self.wait_ele("xpath", "//*[contains(@text,'模式')]").click()
    # #     self.wait_ele("xpath", "//*[contains(@text,'低耗')]").click()


if __name__ == '__main__':
    pytest.main('-s test_001.py')
