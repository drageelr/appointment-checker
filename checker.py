import os
import logging

from seleniumbase import Driver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check():
    
    driver = Driver(uc=True, incognito=True, headless=True)

    driver.get("https://service2.diplo.de/rktermin/extern/appointment_showForm.do?locationCode=isla&realmId=108&categoryId=1600")

    try:
        elem_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/fieldset/form/div[8]/div[2]/select")))
        print('Select Element Fetched')

        option_elems = elem_select.find_elements(By.TAG_NAME ,"option")
        print('Options Fetched')

        active = False
        active_value = ''
        for opt in option_elems:
            opt_value = opt.get_attribute("value")
            if isinstance(opt_value, str) and os.environ.get('KEYWORD') in opt_value.lower():
                active = True
                print('Found')
                # active_value = opt_value
                break
            
        if active:
            print('ACTIVE')
            driver.quit()
            return (None, True)
            # print(active_value)
        else:
            print('NOT-ACTIVE')
            driver.quit()
            return (None, False)
    except Exception as e:
        print('ERROR')
        logging.error('An error occurred: %s', e)
        driver.quit()
        print(e)
        return (e, False)

if __name__ == '__main__':
    check()
