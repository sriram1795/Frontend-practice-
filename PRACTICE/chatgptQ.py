"""name = "Sriram"
age = 22
per = 9.3
per2 = int(per)
x = 5          # int
y = str(x)     # now it's a string, y = "5"


print(name)
print(age)
print(per)
print(type(name))
print(type(age))
print(type(per))
print(per)
print(type(per2))
print(y)
print(type(y)
a= int(input("enter num:"))
b= int(input("enter num:"))
c= a+b
a= c-b
c= a*b
b= a/c
c= a%b
a= a**b
b= c//b
print(a+b)
print(c)
print(a)
print(b)
print(c)
print(a)
print(a+b-c)
print(a*b-c)
#Bill Splitter
#If a dinner bill is ₹1260 and 4 friends are splitting it equally, write a program to calculate how much each pays (add 18% tax to the bill).
bill = 1260
tax = 18
friends = 4
percentage = (b/100) * 1260
d = a + percentage
e = d / c
print (e)
#Voting Eligibility Checker
#Input a person’s age. Use comparison operators to check if they’re eligible to vote (18+).
name = str(input("enter name: "))
age = int(input("enter age: "))
vote = age > 18
print(vote,"eligibility of vote is above 18")
#Password Strength Checker
#Compare two strings: password and confirm_password. Check if they’re the same and if the password length is more than 8 characters.
password = str(input("enter the password: "))
confirm_password = str(input("enter the confirm password: "))
passwords = confirm_password = password
final = len(passwords) > 8
print(final)
#Palindrome Detector
#Check if a given string is the same forwards and backwards using slicing.
a = str(input("enter name: "))
b = a [::-1]
c = b [::-1]
print(b)
print(c)

bill= int(input("enter number: "))#1260
tax= int(input("enter number: "))#18
friends= int(input("enter number: "))#4
per= (tax/100)*bill
final = bill+per
split = final/friends
print("total spliting amount per head: ",split)
->Slice & Dice
Given a string s = "PythonIsAwesome", write a program to:

Print only the word "Python"

Reverse the whole string

Print every second character
s = "PythonIsAwesome"
print(s[:6])
print(s[::-1])
print(s[0::2])
print(s[::2])
print(s[-4::])
print(s[-7::2])
print(s[-2::])
print(len(s))
print(s[15::])
"""
"""A_name = "Sriram kolla"
bank_bal = 50000000
password = "Sriram@1795"
account_num = 20304062612

Name = str(input("enter your user name:"))
Acc_num = int(input("enter account number: "))
passwords = str(input("enter password: "))

check = account_num == Acc_num
is_correct = password == passwords
is_ncorrect = A_name == Name
login_status = check * is_correct * is_ncorrect

print("user name:",Name)
print("account numbers : ",Acc_num)
print("login status: ",bool(login_status))
print("login: "," login Successfull" * login_status + "login failed" * (1 - login_status))

print("your savings is : ",bank_bal * login_status)

deposite = int(input("enter deposite amount: "))* login_status
bank_bal += deposite
print("current balance: ",bank_bal * login_status)
withdraw = int(input("enter withdraw amount: ")) * login_status
print("current_balance: ",bank_bal * login_status)
bank_bal -= withdraw
print("total balance: ",bank_bal* login_status)
"""
a = 10
b = 5
print(a > 3 and b < 10)
x = 7
print(not (x < 10))
x = 4
y = 12
print(x < 5 or y < 10) 

logged_in = True 
admin = False
print(logged_in or admin) 

age = 18 
has_id =False
print(age >= 18 and has_id) 

is_sunny = False 
have_umbrella =True
print(not is_sunny and have_umbrella) 
a = True
b = False
print(not (a or b)) #False
temp = 25
print(temp > 20 and temp < 30) #True
marks = 45
print(not (marks >= 50 or marks == 49)) #True
x = 0
y = 10
print(not x and y > 5) #True
x = 15
y = 10
z = 5
x += 5
print((x > y or z in [5, 6]) and not (x == 20)) #
username = "admin"
roles = ["user", "editor", "admin"]
access_granted = username in roles and username != "guest" 
print(access_granted) #False
marks = 85
status = "Pass" if marks >= 40 else "Fail" 
print(status == "Pass" and marks in range(80, 91))
items = ["pen", "book","bottle"] 
available = "bottle" in items 
stock = 10
stock -= 1
age = 25 
id_card = True

is_verified  =  False
is_verified = age >= 18 and id_card 
print(is_verified and not (age < 18)) 

login = True 
admin = False
privileges = ["read", "write"]
print(("delete" not in privileges) and (login or admin))  #False
x = 8
y = 12
x %= 5
y //= 3
print(x != y and (x not in [0, 1])) #
students = ["Asha", "Ravi", "Mira"]
marks = {"Asha": 78, "Ravi": 65}
print("Mira" in students and students[0] in marks)
x = 100
y = 50
x -= 50
y += 10
print((x == y) or (x > y and "Python" not in ["Java", "C++"])) 
num = 40
num //= 4 
print(num)#
val = 9
val %= 2 
print(val)#
colors = ["red", "green", "blue"] 
print("red" in colors)#True

















