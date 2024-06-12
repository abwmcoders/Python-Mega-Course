temperatures=[10,-20,-289,100, 789, -455]

def c_to_f(c):
    if c< -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        return f
    
with open("exer3.txt", "w+") as file:
    for t in temperatures:
        result = c_to_f(t)
        if(type(result) == int or type(result) == float):
            file.write(f"{result}\n")


# def writer(temperatures):
#     with open("temps.txt", 'w') as file:
#         for c in temperatures:
#             if c>-273.15:
#                 f=c*9/5+32
#                 file.write(str(f)+"\n")


# ///// ------

# def writer(temperatures, filepath):
#     with open(filepath, 'w') as file:
#         for c in temperatures:
#             if c>-273.15:
#                 f=c*9/5+32
#                 file.write(str(f)+"\n")


