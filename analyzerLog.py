import re


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

choose = input("enter your chooice: ")

while choose != '1' and choose != '2' :
    choose = input("Enter a legal chooice: ")

user_found = False
my_lst = get_all_lines_in_file('app.log')

if choose == '1' :
    cnt_err = count_in_lst(my_lst,"ERROR")
    cnt_warning = count_in_lst(my_lst,"WARNING")
    if cnt_err > 0 or cnt_warning > 0 :
        with open('my_report.txt', 'w') as final_report :
            final_report.write(f"Total Errors is: {cnt_err}\nTotal WARNING is : {cnt_warning}")
            print("Your file Report is READY cHECK Your Drive")
     
elif choose == '2' :
    search_name = input("Enter user name to Search: ")
    for item in my_lst:
        if re.search(f"User '{search_name}'", item):
            print(item)
            user_found = True
    if user_found == False :
        print("check the user name we did not found")
    
print("all Done")
    
    
