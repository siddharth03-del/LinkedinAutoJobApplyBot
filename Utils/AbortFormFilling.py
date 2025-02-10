from Shared.driver import driver
from selenium.webdriver.common.by import By
import time
def AbortFormFilling():
    try:
        mainDiv = driver.find_element(By.ID, value='artdeco-modal-outlet')
        buttons = mainDiv.find_elements(By.TAG_NAME, value='button')
        for button in buttons:
            if button.get_attribute('aria-label') == 'Dismiss':
                button.click()
        time.sleep(1)

        new_buttons = driver.find_elements(By.TAG_NAME, value='button')
        for button in new_buttons:
            if button.text == 'Discard':
                button.click()
        
    except Exception as e:
        print("Failed to abort form filling: " + e)