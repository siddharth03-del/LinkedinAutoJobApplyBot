from Shared.driver import driver
from Utils.ScrolljobList import Scrolljobs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Utils.ChangePage import ChangePage
from Utils.ClickJobApply import ClickJobApply
from FillJobForm.FillJobFrom import FillJobForm
import time
def SelectJobs():
    try:
        job_container = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div[1]/div/ul')
        all_jobs = job_container.find_elements(By.XPATH, value='./child::*')
        for job in all_jobs:
            job.click()
            time.sleep(1)
            ClickJobApply()
            FillJobForm()
            Scrolljobs()
        ChangePage()
        SelectJobs()
    except Exception as e:
        print("Failed to select jobs", e)
