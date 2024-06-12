file = open("example.txt", "r") # grab the file and open in read in only mode
content = file.read() # read content of the file
file.seek(0) # enable the content to be printed in the list per lines
content = file.readline() # read the first line of the file
content = file.readlines() # read the content of the file in a list
content = [i.rstrip("\n") for i in content] # remove the backslash N from the list
print(content) # print the output of the file being read
file.close() # close the file after use very essential to prevent python from using the file after words


