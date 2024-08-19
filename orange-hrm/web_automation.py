import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import helper
import time



def test_login(testcases):
    '''
    This function performs the Login and check that the user is landed on dashboard
    '''
    print("Step 1: Open website")
    driver_instance = driver.setup_driver()

    wait = WebDriverWait(driver_instance, 10)  # Wait for up to 10 seconds
    url = "https://opensource-demo.orangehrmlive.com/"
    driver_instance.get(url)
    
    # Perform actions
    print("Step 2: Perform login")
    # Wait for the username field to be clickable
    username_field = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
    helper.append_data(testcases,"Loading login screen","login screen loaded successfully","login screen loaded successfully","pass")

    
    # Interact with the username field
    username_field.send_keys("admin")

    password_field = wait.until(EC.element_to_be_clickable((By.NAME, "password")))

    # Interact with the password field
    password_field.send_keys("admin123")

    helper.append_data(testcases,"fill credentials","credentials filled successfully","credentials filled successfully","pass")
    # Perform login click
    print("Step 3: Verify login success")
    login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "oxd-button")))
    
    # Interact with the password field
    login_button.click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h6.oxd-text--h6")))
    helper.append_data(testcases,"Login and move to dashboard","Logged in and Dashboard loaded successfully","Logged in and Dashboard loaded successfully","pass")
    
    return driver_instance, wait


def test_my_info(driver_instance,wait,testcases):
    '''
    This function updates the date of birth of the logged In user and make sure that the date is updated.
    '''
    print("my info")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/web/index.php/pim/viewMyDetails']")))
    my_info = driver_instance.find_element(By.CSS_SELECTOR,"a[href='/web/index.php/pim/viewMyDetails']")
    my_info.click()


    wait.until(EC.element_to_be_clickable((By.NAME, "firstName")))

    helper.append_data(testcases,"Loading my info page","my info page loaded successfully","my info page loaded successfully","pass")
    

    date_of_birth_field, current_value =  check_dob_value(driver_instance,wait)

    # Check if the input field has any value
    if current_value:
        helper.append_data(testcases,"Date of birth value check","Date of birth is already filled","Date of birth is already filled","pass")

    else:
        helper.append_data(testcases,"Date of birth value check","Date of birth is already filled","Date of birth is already not filled","fail")


    date_of_birth_field[1].click()

    # Locate the desired date (replace with actual locator)
    date_of_birth_field[1].send_keys(Keys.CONTROL, "a")
    date_of_birth_field[1].send_keys(Keys.BACKSPACE)
    my_date_value = "2023-02-02"
    date_of_birth_field[1].send_keys(my_date_value)

    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "oxd-button")))
    #Locate the save button and click 
    save_button = driver_instance.find_elements(By.CLASS_NAME,"oxd-button")
    save_button[0].click()
    
    # locate the success message
    notification_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#oxd-toaster_1 .oxd-toast--success")))
    date_of_birth_field, updated_value =  check_dob_value(driver_instance,wait)
    if updated_value == my_date_value:
        helper.append_data(testcases,"Date of birth value updated","Date of birth successfully updated","Date of birth successfully updated","pass")


def check_dob_value(driver_instance,wait):
    '''
    This function get the date of birth of the user and return that value
    '''
    # Wait for the "Date of Birth" field to be filled in (replace with actual locator)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='yyyy-mm-dd']")))
    date_of_birth_field = driver_instance.find_elements(By.CSS_SELECTOR, "input[placeholder='yyyy-mm-dd']")
    time.sleep(2)
    # Get the current value of the input field
    current_value = driver_instance.execute_script('return arguments[0].value', date_of_birth_field[1])
    print("data==============", current_value)
    return date_of_birth_field,current_value

def test_logout(driver_instance,wait,testcases):
    '''
    This function logout the user and check that the user is logged out and is landed on login page
    '''
    # Locate user dropdown and click
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown")))
    user_dropdown = driver_instance.find_element(By.CLASS_NAME, "oxd-userdropdown")

    user_dropdown.click()


    # Locate logout button and click 
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-dropdown-menu a[href='/web/index.php/auth/logout']")))
    logout_option = driver_instance.find_element(By.CSS_SELECTOR, ".oxd-dropdown-menu a[href='/web/index.php/auth/logout']")

    logout_option.click()

    # Locate the Login title class after logout success
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "orangehrm-login-title")))
    helper.append_data(testcases,"Logging out","Logged out successfully","Logged out successfully","pass")
