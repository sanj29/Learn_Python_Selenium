from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

driver: WebDriver = webdriver.Chrome()


def browser_initialization():

    url = "https://www.google.com"
    driver.get(url)


def test_verify_page_title():
    browser_initialization()
    print(" browser launched !!")
    title = driver.title
    print(" Page title is : {}".format(title))
    assert title == "Google", " page title not matched"
