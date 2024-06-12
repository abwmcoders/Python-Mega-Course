import datetime

file_names = ["cont_1.txt", "cont_2.txt", "cont_3.txt"]
output_merged = datetime.datetime.now()
file = open(f"{output_merged.strftime("%B-%Y-%d")}.txt", "w")

for filename in file_names:
    with open(filename, "r") as read_filename:
        content = read_filename.read()
        print(content)
        file.write(f"{content}\n")