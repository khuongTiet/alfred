from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1366x768")

chrome_driver = './chrome/chromedriver'

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

driver.get("https://google.com/")

driver.get_screenshot_as_file("test.png")
