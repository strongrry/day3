
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_click_login_button(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loginBtn")))
    driver.find_element(By.ID, "loginBtn").click()
