# add numbers till the range
'''def add_it_up(number):
    return sum(range(number+1))
t=add_it_up(200000)
print(t)'''

# Check if the input is number
'''number1=input("Enter the number\n")
if number1.isdigit():
   print(number1)
else:
    print("Not a number")'''

# print even string (in PYTHON negative means STARTS from END)
'''def even(str):
    for i in range(0,len(str)-1, 2):
        print(str[i])

str= input("Enter the string\n")
print(type(str))
even(str)'''

# Remove characters in a string
'''def removeChars(str,n):
    return str[:n]

str= input("Enter the string\n")
n=input("Enter number\n")
n=int(n)
print(removeChars(str,n))'''


#print triangle

'''for i in range(10):
    for j in range(i):
        print(i,end=" ")
    print("\n")'''

# Tables in perticular range
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print("\t\t")



