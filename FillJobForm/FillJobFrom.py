from Shared.driver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Shared.data import Form_data
from selenium.webdriver.support.ui import Select
from Utils.scrollForm import ScrollForm
from Utils.CancelWorkExperience import CancelWorkExperience
from Utils.ClickNextFrom import ClickNextOnJobForm
from Utils.AbortFormFilling import AbortFormFilling
import time
def FillJobForm():
    try:
        mainForm = driver.find_element(By.TAG_NAME, value='form')
        h3 = mainForm.find_element(By.TAG_NAME, value='h3')
        heading = h3.text
        all_lables = mainForm.find_elements(By.TAG_NAME, value='label')
        print(all_lables)
        all_input = mainForm.find_elements(By.TAG_NAME, value='input')
        print(all_input)
        all_select = mainForm.find_elements(By.TAG_NAME, value='select')
        print(all_select)
        filling_dict = {}
        if (heading == 'Work experience'):
            ScrollForm(val=500)
            time.sleep(1)
            CancelWorkExperience()
            ClickNextOnJobForm(form=mainForm)
            time.sleep(1)
            FillJobForm()
        elif (heading == 'Resume'):
            ScrollForm(500)
            ClickNextOnJobForm(mainForm)
            time.sleep(1)
            FillJobForm()
        for i in all_lables:
            For = i.get_attribute('for')
            for j in all_input:
                if j.get_attribute('id') == For:
                    filling_dict[i] = j
            for j in all_select:
                if j.get_attribute('id') == For:
                    filling_dict[i] = j

        print(filling_dict)
        for (key, value) in filling_dict.items():
            print(f"key = {key}, value = {value}")
            field = key.text.split('\n')[0].lower()
            print(field)
            tag_name = value.tag_name
            print(tag_name)
            value_to_fill = Form_data[field]
            print(value_to_fill)
            if tag_name == 'input':
                if value.get_attribute('type') == 'file':
                    driver.execute_script('arguments[0].classList.remove("hidden");', value)
                value.clear()
                value.send_keys(value_to_fill)
                print("succcessfully entered value")
                # value.send_keys(Keys.ENTER)
                # print('successfully clicked enter')
                time.sleep(0.5)
                mainForm.click()
                print("successfully clicked mainForm")
                time.sleep(0.5)
            elif tag_name == 'select':
                select = Select(value)
                select.select_by_visible_text(value_to_fill)
            print("finished form filling now scroll it")
            ScrollForm(val=90)
        print("ended form filling")
        ScrollForm(val=500)
        ClickNextOnJobForm(form=mainForm)
        time.sleep(1)
        FillJobForm()
    except Exception as e:
        print("An unexpected error occured ",  e)
        AbortFormFilling()
