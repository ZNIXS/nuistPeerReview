from selenium import webdriver

driver = webdriver.Edge(executable_path=r"D:\Edge_Driver\msedgedriver.exe") # 相应的浏览器的驱动位置

driver.get(r"https://www.baidu.com")