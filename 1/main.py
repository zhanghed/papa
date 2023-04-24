import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def main():
    # 启动浏览器驱动
    service = Service(r"./chromedriver.exe")
    # 有头模式
    driver_chrome = webdriver.Chrome(service=service)
    print(driver_chrome)
    # 无头模式
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-gpu")
    # driver_chrome = webdriver.Chrome(service=service, options=chrome_options)
if __name__ == '__main__':
    a = default_timer()

    main = Main()
    asyncio.run(main.run())

    b = default_timer()
    print(b - a)
