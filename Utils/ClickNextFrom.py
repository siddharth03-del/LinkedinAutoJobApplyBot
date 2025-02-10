from Shared.driver import driver
from selenium.webdriver.common.by import By
from Utils.SubmitApplication import SubmitApplication
import time
def ClickNextOnJobForm(form):
    try:
        footer = form.find_element(By.TAG_NAME, value="footer")
        footer_child = footer.find_elements(By.XPATH, value='./child::*')
        div_button = footer_child[1]
        buttons = div_button.find_elements(By.XPATH, value="./child::*")
        for i in buttons:
            if i.text == 'Next' or i.text == 'Review':
                i.click()
            elif i.text == 'Submit application':
                SubmitApplication(form=form)
        time.sleep(1)
    except Exception as e:
        print("Error occurred while clicking on next on job form: " , e)
