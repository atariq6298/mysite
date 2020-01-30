import pytest
from selenium import webdriver
from time import sleep


# Fixture for Firefox
@pytest.fixture(scope="class")
def driver_init(request):
    web_driver = webdriver.Chrome()
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass


class Test_URL(BasicTest):
    def test_open_url(self):
        self.driver.get("http://localhost:5000")
        str_new_task_name = "new_task"
        str_hour = "5"
        str_minute = "4"
        self.driver.find_element_by_name("name").send_keys(str_new_task_name)
        self.driver.find_element_by_name("hour").send_keys(str_hour)
        self.driver.find_element_by_name("minute").send_keys(str_minute)
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        assert self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[2]/td[1]").text == str_new_task_name
        assert self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[2]/td[2]").text == str_hour + ":" + str_minute
        sleep(5)
