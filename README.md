# nuistPeerReview
南京信息工程大学同学互评自动填写

## 1.安装selenium

- 参考自：
  1. [Selenium Python 教程 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/111859925)
  2. [ selenium + Edge 浏览器_tk1023的博客-CSDN博客](https://blog.csdn.net/tk1023/article/details/109078613)

1. 安装selenium

   - 一般：`pip install selenium`
   - 对于edge：`pip install msedge-selenium-tools`

2. 安装浏览器驱动（注意版本一定要对应好）：我的是edge：[Microsoft Edge Driver - Microsoft Edge Developer](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

3. 编写测试代码：

   ```python
   from selenium import webdriver
   
   driver = webdriver.Edge(executable_path=r"D:\Edge_Driver\msedgedriver.exe") # 相应的浏览器的驱动位置
   
   driver.get(r"https://www.baidu.com")
   ```

4. 如果浏览器能自动打开说明安装成功

## 2.代码说明

1. 运行`main.py`
2. 输入学号密码
3. 程序自动打开网站
4. 你需要输入验证码
5. 程序自动打开表单那里
6. 你需要点击下一步
7. 然后程序会自动填写

## 3.漏洞修复

1. 修复了学号不连续导致的问题
