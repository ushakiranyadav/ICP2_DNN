First_name=input("Enter your first name:")
last_name=input("Enter the last name:")
Full_name= First_name + last_name # string concatenation 
print("your full name :" + Full_name)
str=Full_name
def string_alernative(str):
    Output=""
    for index,char in enumerate (str): # enumerating the string
        if index % 2 == 0: # here we are taking the alternate charcters
            Output += char #appending to the output 
    return Output

resultstr=string_alernative(str)
print(resultstr)