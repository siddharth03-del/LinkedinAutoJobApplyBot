from Shared.driver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def PerformSignin(email, password):
    enter_sigin_button = driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
    enter_sigin_button.click()
    time.sleep(0.1)

    email_input =driver.find_element(By.ID, value='base-sign-in-modal_session_key')
    password_input = driver.find_element(By.ID, value='base-sign-in-modal_session_password')
    email_input.send_keys(email)
    password_input.send_keys(password)

    signin_button = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
    signin_button.click()
    time.sleep(5)