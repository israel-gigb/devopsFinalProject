from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 

options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get("localhost:3000/")
driver.find_element_by_link_text("About Us").click()
try:
     driver.find_element_by_xpath('//p[@id="PID-ab2-pg" and text()="This is "]')
     print ("no")
except NoSuchElementException:
     print ("nooo")
driver.quit()
