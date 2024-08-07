print(">>>>>>>>>>Basic Calculator>>>>>>>>>>")

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
opr = str(input('''Select operations from "+, -, *, /" :'''))

number1 = int(input("Please enter number 1:"))
number2 = int(input("Please enter number 2:"))

if opr == '+':
    print(number1, opr , number2, "=",number1+number2)
elif opr == '-':
    print(number1, opr , number2, "=",number1-number2)
elif opr == '*':
    print(number1, opr, number2, "=",number1*number2)
elif opr == '/':
    if number2 == 0:
        print('division by zero not allowed it will throw logical error')
    else:
        print(number1, opr, number2, "=",number1/number2)
else:
    print("Selected operation is not available")