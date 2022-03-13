from selenium import webdriver
from selenium.webdriver.common.keys import Keys

base_url = "https://testautomation-playground.herokuapp.com"
driver = webdriver.Chrome(executable_path=r'E:\projectme\Selenium\chromedriver.exe')
#driver.get("https://www.google.com")
#search_field = driver.find_element('name', 'q')
#search_field.send_keys("keep simple")
#search_field.send_keys(Keys.RETURN)

driver.get(f"{base_url}/forms.html")
driver.find_element('id','check_python').click()
check1 = driver.find_element('id','check_validate').text
assert check1 == 'PYTHON'
driver.find_element('id','notes').send_keys("hello")
check2 = driver.find_element('id','area_notes_validate').text
assert check2 == 'hello'