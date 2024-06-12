file = open("created.txt", "w") # create empty file and open it 
file.write("Hello There!\n") # write to the file opened but note this is not an append method i.e it will all be written in one line
file.write("I'm berry\n") # \n push the the next write function to the next line
my_self = ["My name is berry", "I'm a fine boi", "I love to play football", "and i'm a lover boi", "what does that even mean"]
for info in my_self:
    file.write(f"{info}\n")

file.close()