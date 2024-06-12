import datetime


time = 0

date = datetime.datetime.now() # getting the current date time
b_date = datetime.datetime(2024,2,20) # parsing current date and time manually
delta_date = date - b_date
print(delta_date.days)
print(delta_date.seconds)
print(delta_date.microseconds)
print(delta_date.total_seconds())

filename = date
after = date + datetime.timedelta(days=2)
print(after)
def create_file():
    with open(f"{filename.strftime("%B-%Y-%d-%H-%M")}.txt", "w") as file:
        file.write("")

create_file()        

# while time < 200:
#     date = datetime.datetime.now()
#     print(date)


# date.strftime("") ---> perse in formatting characters like %Y, %d ......
"""
%B ---> Month in words
%Y ---> Year in 2045
%d ---> day
%H ---> Hour
%M --> Minute
"""