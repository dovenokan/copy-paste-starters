from selenium import webdriver
# https://github.com/mozilla/geckodriver/releases

browser = webdriver.Firefox()
website = "website.com"
browser.get(website)

xpath = browser.find_element_by_xpath('//*[@id="username"]')
xpath.send_keys("username")
xpath.click()
