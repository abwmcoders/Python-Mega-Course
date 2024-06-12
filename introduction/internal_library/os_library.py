import os

with open("os_docs.txt", "w+") as file: 
    result = help(os)
    file.write(str(help(os)))


r"""
Multiline comment in python
Also categorize as doc string in python
include "r" at the front to not treat any special character as special in put
"""