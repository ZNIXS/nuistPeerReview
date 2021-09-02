from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Edge(executable_path=r"D:\Edge_Driver\msedgedriver.exe") # 相应的浏览器的驱动位置

driver.get("http://stu.nuist.edu.cn/LOGIN.ASPX")
driver.find_element_by_id("userbh").click()
driver.find_element_by_id("userbh").clear()
driver.find_element_by_id("userbh").send_keys()
driver.find_element_by_xpath("//body").click()
driver.find_element_by_id("pas1s").click()
driver.find_element_by_id("pas1s").clear()
driver.find_element_by_id("pas1s").send_keys()
driver.find_element_by_id("vcode").click()
driver.find_element_by_id("vcode").clear()
# driver.find_element_by_id("vcode").send_keys("4496")
sleep(10)

# driver.find_element_by_id("save2").click()
driver.find_element_by_link_text(u"学业学风").click()
driver.find_element_by_id("xq_xz").click()
Select(driver.find_element_by_id("xq_xz")).select_by_visible_text("2020-2021-2")
driver.find_element_by_link_text(u"同学互评").click()

sleep(5)

driver.switch_to.frame('r_3_3')
name1 = "MyDataGrid:_ctl"
name2 = ":cp"
name3 = "_2"
for i in range(2,100):
    for j in range(1,7):
        name = name1 + str(i) + name2 + str(j) + name3
        "//input[@name='wd']"
        name = "//input[@name='" + name +"']"

        if(i == 2 and j == 1):
            driver.find_element_by_xpath(name).click()

        driver.find_element_by_xpath(name).click()
        if(j == 6):
            driver.find_element_by_xpath(name).send_keys("5")
        else:
            driver.find_element_by_xpath(name).send_keys("6")