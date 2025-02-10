from Shared.driver import driver
from selenium.webdriver.common.by import By
import time

def CancelWorkExperience():
    try:
        mainForm  = driver.find_element(By.TAG_NAME, value='form')
        buttons = mainForm.find_elements(By.TAG_NAME, value='button')
        for button in buttons:
            if button.text == 'Cancel':
                button.click()
        
        time.sleep(1)

    except Exception as e:
        print("An error occured while trying to cancel work experience", e)