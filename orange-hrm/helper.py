import datetime
import pandas as pd

def append_data(data_list,description,excpected_result,actual_result, status):
    '''
    This function appends data in the data list of test steps
    '''
    print(description)
    data_list.append({
        'step'                  : len(data_list) + 1,
        'test step'             : description,
        'excpected result'      : excpected_result,
        'actual result'         : actual_result,
        'status'                : status
        })

    return data_list


def save_data(testcases):
    '''
    This function saves test steps and total test cases reports in csv format with todays date.
    '''
    todaysdate = datetime.date.today()
    df = pd.DataFrame(testcases)
    df.to_csv(f"reports/final_data_{todaysdate}.csv", index=False)
    total_testcases = len(testcases)
    passed_count = sum(1 for item in testcases if item.get('status') == "pass")
    failed_count = total_testcases - passed_count

    print(passed_count,failed_count)

    df = pd.DataFrame([{
        'total testcases' : total_testcases,
        'passed testcases' : passed_count,
        'failed testcases' : failed_count,
    }])
    df.to_csv(f"reports/test_cases_report_{todaysdate}.csv", index=False)




