from Shared.driver import driver
from selenium.webdriver.common.by import By
import time

def SubmitApplication(form):
    try:
        footer = form.find_element(By.TAG_NAME, value="footer")
        footer_child = footer.find_elements(By.XPATH, value='./child::*')
        div_button = footer_child[1]
        buttons = div_button.find_elements(By.XPATH, value="./child::*")
        for i in buttons:
            if i.text == 'Submit application':
                i.click()
        time.sleep(3)
        mainDiv = driver.find_element(By.ID, value='artdeco-modal-outlet')
        buttons = mainDiv.find_elements(By.TAG_NAME, value='button')
        for button in buttons:
            if button.get_attribute('aria-label') == 'Dismiss':
                button.click()
        time.sleep(1)
    except Exception as e:
        print("Error occurred while submitting application: " , e)
