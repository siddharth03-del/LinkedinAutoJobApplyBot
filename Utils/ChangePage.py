from Shared.driver import driver
from Utils.ScrolljobList import Scrolljobs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

currentPage = 2

def ChangePage():
    found = False
    global currentPage
    try:
        # Wait for the whole_div element to be present and visible
        whole_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div'))
        )

        # Ensure the element is scrollable
        driver.execute_script("arguments[0].style.overflow = 'auto';", whole_div)

        # Scroll the div element to the bottom incrementally
        last_height = driver.execute_script("return arguments[0].scrollTop;", whole_div)
        while True:
            driver.execute_script("arguments[0].scrollTop += arguments[0].clientHeight;", whole_div)
            time.sleep(1)  # Wait for the scroll to complete
            
            new_height = driver.execute_script("return arguments[0].scrollTop;", whole_div)
            if new_height == last_height:
                break
            last_height = new_height

        print("Scrolled the div element completely")

        # Locate the pages_ul element
        job_search_div = driver.find_element(By.ID, value = 'jobs-search-results-footer')
        # print("found job_search_div", job_search_div)
        job_search_div_childrens = job_search_div.find_elements(By.XPATH, value='./child::*')
        # print("found job_search_div_childrens", job_search_div_childrens)
        pages_div = job_search_div_childrens[1]
        # print("found pages-div", pages_div)
        pages_ul = pages_div.find_elements(By.XPATH, value='./child::*')[0]
        # print("found pages-ul", pages_ul)
        page_list = pages_ul.find_elements(By.XPATH, value ='./child::*')
        # print("page list matches")
        for page in page_list:
            if page.get_attribute('data-test-pagination-page-btn') == str(currentPage):
                print("Page found")
                page.click()
                found = True
                currentPage += 1
                time.sleep(3)
                break
        
        if not found:
            for page in page_list:
                if not page.get_attribute('data-test-pagination-page-btn'):
                    page.click()
                    break
            for page in page_list:
                if page.get_attribute('data-test-pagination-page-btn') == str(currentPage):
                    page.click()
                    currentPage += 1
                    found = True
                    time.sleep(3)
            if not found:
                driver.quit()
                
    except Exception as e:
        print("Error finding the page", e)

    





