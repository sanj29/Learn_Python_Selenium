from selenium import webdriver

driver = webdriver.Chrome()
url = "https://www.google.com"
driver.get(url)
print(" browser launched !!")
title = driver.title
print(" Page title is : {}".format(title))
assert title == "Google"," page title not matched"
