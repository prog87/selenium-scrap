from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

website = 'https://www.adamchoi.co.uk/overs/detailed'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get(website)
