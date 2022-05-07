from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

DRIVER_PATH = r"C:\Users\Markazi\Desktop\InstaBot\chromeDriver\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(DRIVER_PATH, chrome_options=options)

url = "https://www.mastersportal.com/?redirect=false"

driver.get(url)
search_box = driver.find_element(By.ID, 'HomeWhat')

search_box.send_keys("Natural Sciences & Mathematics")
search_box.send_keys(Keys.ENTER)

search_box_where = driver.find_element(By.ID, 'HomeWhere')
search_box_where.send_keys("United States")
search_box_where.send_keys(Keys.ENTER)

time.sleep(10)

titles = driver.find_elements(By.CLASS_NAME,'StudyName')
unis = driver.find_elements(By.CLASS_NAME, 'OrganisationName')
fees = driver.find_elements(By.CLASS_NAME, 'TuitionValue')



for (title,uni,fee) in (zip(titles,unis,fees)):

    print(title.text,uni.text,fee.text)
    print('\n')


driver.quit()