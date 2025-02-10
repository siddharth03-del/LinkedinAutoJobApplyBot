from Shared.driver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def ClickJobApply():
    try:
        job_apply_div = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/div[5]/div/div/div')
        print(job_apply_div)
        job_apply_button = job_apply_div.find_elements(By.XPATH, value='./child::*')[0]
        job_apply_button.click()
        print("clicked job apply")
        time.sleep(0.2)
    except Exception as e:
        print("could not click job apply", e)
