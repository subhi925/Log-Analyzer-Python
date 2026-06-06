import re

print("LOG Anylaizer Please choose From Menu:")
print(f"Click 1 To Creat A Report File.\nClick 2 To Ener User to show logs")

choose = input("enter your chooice: ")

while choose != '1' and choose != '2' :
    choose = input("Enter a legal chooice: ")

cnt_err = 0
cnt_warning = 0
user_found = False


if choose == '1' :
    try:
        with open('app.log', 'r') as logs:
            for line in logs:
                newLine = line.strip()
                if re.search("WARNING", newLine):
                    cnt_warning += 1
                elif re.search("ERROR", newLine):
                    cnt_err += 1
        if cnt_err > 0 or cnt_warning > 0 :
            with open('my_report.txt', 'w') as final_report :
                final_report.write(f"Total Errors is: {cnt_err}\nTotal WARNING is : {cnt_warning}")
                print("Your file Report is READY cHECK Your Drive")
    except Exception as err:
        print("The Error is:", type(err).__name__)
elif choose == '2' :
    search_name = input("Enter user name to Search: ")
    try:
        with open('app.log', 'r') as logs :
            for line in logs:
                newLine = line.strip()
                if re.search(f"User '{search_name}'", newLine):
                     print(newLine)
                     user_found = True
            if user_found == False :
                print("check the user name we did not found")

    except Exception as err:
        print("The Error is:", type(err).__name__)
print("all Done")
    
    
