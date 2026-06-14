import re
import json
from datetime import datetime
#================================================================
def load_config(config_path):
    """
    To load from the JSON file
    details about your log app
    Args:
        config_path: your file name .JSON

    Returns:
        A Dictionary list contains level logs and file log path
    """
    my_dict = {}
    
    try:
        with open(config_path, 'r') as myPath_file:
           my_dict = json.load(myPath_file)
    except Exception as err:
            print("Teh Error is :", type(err).__name__)
    return my_dict

    
#=========================================================

def get_all_lines_in_file(path_file):
    my_lst_line = []
    try:
        with open(path_file, 'r') as logs:
            for line in logs:
                my_lst_line.append(line.strip())  
    except Exception as err:
        print("The Error is:", type(err).__name__)
    return my_lst_line
#=============================================================================================
def count_in_lst(lst,logType):
    cnt=0
    for item in lst:
        if re.search(logType, item):
            cnt += 1
    return cnt
#=================================================================================
def user_Report_byTime(lst,time,user):
    final_lst = []
    for item in lst:
        if re.search(f"User '{user}'",item):
            try:
                log_time = re.search(r"\d{2}:\d{2}:\d{2}", item)
                if log_time ==None:
                    final_lst.append(item)
                else:
                    log_time = log_time.group()
                    log_time = datetime.strptime(log_time, "%H:%M:%S")
                    if log_time >= time:
                        final_lst.append(item)
            except Exception as err:
                 print("The Error is:", type(err).__name__)
    return final_lst                  
                
#==================================Menue================================================
def main ():
    print("LOG Anylaizer Please choose From Menu:")
    print(f"Click 1 To Creat A Report File.\nClick 2 To Ener User to show logs\
            \nClick 3 to input User and Time to check log after it in new File.")
    choose = input("enter your chooice: ")
    return choose
    

#===============================================================================

choose = main()
config = load_config("config.json")

while choose != '1' and choose != '2' and choose != '3' :
    choose = input("Enter a legal chooice: ")

user_found = False
my_lst = get_all_lines_in_file(config["file_path"])

if choose == '1' :
    res_dict={}
    for item in config["log_levels"]:
        res_dict[item] = count_in_lst(my_lst, item)
    if len(res_dict) > 0 :
        with open('my_report.txt', 'w') as final_rep:
            final_rep.write("=== LOG ANALYZER REPORT ===\n")
            for log_level, count in res_dict.items():
                final_rep.write(f"Total {log_level}s: {count}\n")   
        print("Your file Report is READY. Check your directory!")
elif choose == '2' :
    search_name = input("Enter user name to Search: ")
    for item in my_lst:
        if re.search(f"User '{search_name}'", item):
            print(item)
            user_found = True
    if user_found == False :
        print("check the user name we did not found")
elif choose == '3':
    search_name = input("Enter user name to Search: ")
    time_after = input("Enter The time format hh:mm:ss: ")
    while True:        
        try:
            given_time = datetime.strptime(time_after, "%H:%M:%S")
            break
        except Exception as err:
            time_after = input("Enter A Legal time format or Legal Time hh:mm:ss: ")
    user_lst = user_Report_byTime(my_lst,given_time,search_name)
    if len(user_lst) > 0:
        repo_dict = {}
        for item in config["log_levels"]:
           repo_dict[item] = count_in_lst(user_lst, item) 
        with open (f"{search_name}_report.txt", 'w') as f_report:
            f_report.write(f"==========Log Analyzer for '{search_name}'=======\n")
            for level , cnt in repo_dict.items():
                f_report.write(f"Total {level}s: {cnt}\n")
            f_report.write(f"==================LOGS===================\n")
            for item in user_lst:
                f_report.write(f"'{item}'\n")
        print("your file is Ready")
    else:
        print("make sure of user name")
print("all Done")
    
    
