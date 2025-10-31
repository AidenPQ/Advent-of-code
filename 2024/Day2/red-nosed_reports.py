import re

def decipher_reports(filename):
    # Transform file into a list of reports (A report is a list of integers)
    reports = []
    with open(filename, 'r') as file:
            for line in file:
                ln = re.split(' |\n', line)
                ln = [int(el) for el in ln if el != '']
                reports.append(ln)
    
    return reports

def evaluate_report_safety(report):
    # Evaluate if a report is safe (1) or Unsafe (0) 
    if all(report[i] <= report[i+1] for i in range(len(report) - 1)) or all(report[i] >= report[i+1] for i in range(len(report) - 1)):
          
        if all(abs(report[i] - report[i+1]) >= 1 and abs(report[i] - report[i+1]) <= 3 for i in range(len(report) - 1)):
            return 1
        else:
            return 0
    else:
         return 0

def evaluate_report_safety_with_dampener(report):
    # Add The problem Dampener by iteratively removing 1 level from a false report to see if there is a case where removing one level make the report safe
    if evaluate_report_safety(report):
          return 1
    else:
        dampener_test = report.copy()
        for i in range(len(report)):
            dampener_test.pop(i)
            if evaluate_report_safety(dampener_test):
                return 1
            dampener_test = report.copy()
        return 0
    

def count_safe_reports(reports):
    number_safe_reports = 0

    for report in reports:
         number_safe_reports += evaluate_report_safety(report=report)

    return number_safe_reports

def count_safe_reports_with_dampener(reports):
    number_safe_reports = 0

    for report in reports:
         number_safe_reports += evaluate_report_safety_with_dampener(report=report)

    return number_safe_reports


reports = decipher_reports("Day2/input.txt")
number_of_safe_reports = count_safe_reports(reports)

number_of_safe_report_with_dampener = count_safe_reports_with_dampener(reports=reports)
print("Number of safe reports:", number_of_safe_reports)
print("Number of safe reports with dampener:", number_of_safe_report_with_dampener)

    