file = open("exer2.txt", "a")
file.write("Not just numbers is allowed")
file.write("Not just numbers is allowed 12")

file.close()


# r+ -----> Allow reading and writing
# w+ -----> Allow reading and writing
# a+ -----> Allow reading and appending

with open("exer2.txt", "a+") as file:
    file.write("\ni love you")

    file.seek(0)
    content = file.readlines()
    for item in content:
        print(item.strip())