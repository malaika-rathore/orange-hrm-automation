import pandas as pd  # To store data in dataframe
import datetime


def save_data(data):
    todaysdate = datetime.date.today()
    df = pd.DataFrame(data)
    df.to_csv(f"reports/final_data_{todaysdate}.csv", index=False)
    print("Data created successfully")
    total_testcases = len(data)
    passed_count = sum(1 for item in data if item.get('status') == "pass")
    failed_count = total_testcases - passed_count

    print(passed_count,failed_count)

    df = pd.DataFrame([{
        'total testcases' : total_testcases,
        'passed testcases' : passed_count,
        'failed testcases' : failed_count,
    }])
    df.to_csv(f"reports/test_cases_report_{todaysdate}.csv", index=False)


