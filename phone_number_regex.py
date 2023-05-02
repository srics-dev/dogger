import re
inputs = []
n = int(input())
for i in range(n):
    input_string = input()
    inputs.append(input_string)
for input_string in inputs:
    charecter=re.findall('.',input_string)
    lenn=len(charecter)
    if 11==lenn:
        if re.search('^7',input_string)=='match' or re.search('^8',input_string)=='match' or re.search('^9',input_string):
            print("Yes")
        else:
            print("No")
    else:
            print("No") 
print(lenn)