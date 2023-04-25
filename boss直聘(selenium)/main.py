import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def main():
    arr = []
    driver = webdriver.Chrome(r'./chromedriver.exe')
    driver.get(r"https://www.zhipin.com/web/geek/job?query=Python&city=101010100")
    time.sleep(10)
    a = driver.find_elements(By.CLASS_NAME, 'job-card-wrapper')
    for i in a:
        a1 = i.find_element(By.CLASS_NAME, 'job-card-body').text
        a2 = i.find_element(By.CLASS_NAME, 'job-card-footer').text
        arr.append([a1, a2])
    print(arr)


if __name__ == '__main__':

    main()