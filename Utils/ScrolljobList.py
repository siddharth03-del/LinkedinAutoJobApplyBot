from Shared.driver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
def Scrolljobs():
    try:
        job_container = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div[1]/div/ul')
        scroll_origin = ScrollOrigin.from_element(job_container, 50, 50)
        ActionChains(driver)\
        .scroll_from_origin(scroll_origin, 0, 150)\
        .perform()
    except Exception as e:
        print("Error scrolling jobs", e)

    