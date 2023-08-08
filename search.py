from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")

searchbox = driver.find_element_by_xpath('/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
searchbox.send_keys("selenium and python automation")

searchButton = driver.find_element_by_xpath("/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button")
searchButton.click()