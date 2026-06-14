import re
from datetime import datetime
log_line = "[2026-06-09 19:22:05] [ERROR] User 'Subhi' failed to database connection timeout."
try:
    mach = re.search(r"\d{2}:\d{2}:\d{2}", log_line)
    print(mach.group())
except Exception as err:
        print("The Error is:", type(err).__name__)
#===========================================================
error_time_text = "15:45:30"

try:
    time_object = datetime.strptime(error_time_text, "%H:%M:%S")
    print(time_object)
except Exception as err:
    print("The Error is:", type(err).__name__)
    
#======================================================
log_time_text = "14:20:00"
given_time = datetime.strptime("12:00:00", "%H:%M:%S")

my_log_time = datetime.strptime(log_time_text, "%H:%M:%S")


if my_log_time >= given_time:
    print("This log is in range")
else:
    print("Log not in range")
#==============================================================
log_line = "[2026-06-09] [INFO] System error."

given_time = datetime.strptime("12:00:00", "%H:%M:%S")
try:
    my_log_time = re.search(r"\d{2}:\d{2}:\d{2}", log_line)
    if my_log_time == None:
        print("Error: Time stamp not found in the log line")
    else:   
        my_log_time_fromline = my_log_time.group()
        my_log_time_fromline = datetime.strptime(my_log_time_fromline, "%H:%M:%S")
        if my_log_time_fromline >= given_time :
            print("This log is in range")
        else:
            print("Log not in range")
except Exception as err:
        print("The Error is:", type(err).__name__)
        



