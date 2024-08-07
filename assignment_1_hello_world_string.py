#1-Basic Printing:
print("Hello World!")
print("Ali")


#2-Printing Multiple Items
first_name = "Ali"
last_name = "Hassan Malik"
print(f"{first_name} {last_name}")

first_number = 1
second_number = 2
third_number = 3
print(f"{first_number} {second_number} {third_number}")

#3-Printing Special Characters:
print("Hello\nWorld")

print("Hello\tWorld")

#4-Using the sep Parameter
print("Apple","Banana","Cherry", sep=",")

print(1,2,3, sep="-")

#5-Using the end Parameter:
print("Hello",end=" ")
print("world")

print("1",end="")
print("2")

#6-Escape Characters
print("He Said \"Hello World!\"")
print("This is a backslash:\\")

#7-Combining Text and Numbers
my_age = 20
print(f"I am {my_age} years old")

number = 5
print(f"This number is {number}")

#8-Basic Loop for Printing:
for i in range(1,6):
    print(i)