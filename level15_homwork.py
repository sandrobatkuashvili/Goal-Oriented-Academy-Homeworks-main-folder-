# 0) კომენტარის სახით ახსენი რა სიტუაციებში რომელი ციკლის გამოყენება  ჯობია
# for ციკლი უნდა გამოვიყენოთ როდესაც ვიცით კოდი რამდენჯერ გამეორდება
# while ის დროს კი არვიცით მოცემული პირობა როდის არის დაკმაყოფილებული ანუ არვიცით რამდენჯერ მეორდება


# 1) გამოიტანეთ რიცხვები 0-იდან 20-მდე, for ციკლით
for i in range(20):
    print(i)



num = 10
while num > 46:
    print(num)
    num += 1

# 3) გამოიტანეთ ყველა ლუწი რიცხვი 17-დან 60-მდე

for i in range(18, 46, 2):
    print(i)


# 4)მომხმარებელს შემოატანინე სახელი და გამოიტანე ყველა ასო
name = input("Enter your name ")
for char in name:
    print(char)

# 5)დაპრინტე რიცხვები 10-დან 0-მდ

number = 10
while number > 0:
    print(number)
    number += 1





mainemail = "sandrobatkuashvili@gmail.com"
mainpassword = "password123"
email = input("Enter your email ")

while email != mainemail:
    print("Incorrect email ")
    email = input("Enter your email")

password = input("Enter your password ")
while password != mainpassword:
    print("Incorrect password ")
    password = input("Enter your password ")


