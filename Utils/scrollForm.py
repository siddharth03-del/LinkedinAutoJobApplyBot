from Shared.driver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

def ScrollForm(val):
    try:
        scrollable_div = driver.find_element(By.XPATH, value='/html/body/div[4]/div/div/div[2]')
        scroll_origin = ScrollOrigin.from_element(scrollable_div, 50, 50)
        ActionChains(driver)\
            .scroll_from_origin(scroll_origin, 0,val)\
            .perform()
    except Exception as e:
        print(f"An error occurred: {e}")