import re
import json
#================================================================
def load_config(config_path):
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
print("LOG Anylaizer Please choose From Menu:")
print(f"Click 1 To Creat A Report File.\nClick 2 To Ener User to show logs")
config = load_config("config.json")
choose = input("enter your chooice: ")

while choose != '1' and choose != '2' :
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
print("all Done")
    
    
