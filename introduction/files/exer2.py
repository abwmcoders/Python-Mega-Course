numbers = [1, 2, 3]
file = open("exer2.txt", "w")
for number in numbers:
    file.write(f"{number}\n")

file.close()    