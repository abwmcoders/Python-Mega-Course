file = open("exer.txt", "r")
content = file.read()
file.seek(0)
content = file.readlines()
for item in content:
    print(len(item.strip()))
file.close()