import web_automation
import helper



def testcases():
    '''
    This function perform 3 testcases scenarios 
        - login 
        - update user info
        - logout            
    '''
    testcases = []
    
    driver_instance, wait = web_automation.test_login(testcases)
    web_automation.test_my_info(driver_instance,wait,testcases)
    web_automation.test_logout(driver_instance,wait,testcases)
    helper.save_data(testcases)


testcases()
