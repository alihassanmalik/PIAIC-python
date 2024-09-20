def add(number1,number2):
    return number1 + number2

def subtract(number1,number2):
    return number1 - number2

def multiply(number1,number2):
    return number1 * number2

def divide(number1,number2):
    if number2 == 0:
        return "Error: Division by zero is not allowed."
    return number1 / number2


def display_menu():
    print("\nWelcome to the Python Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    
def calculator():
    while True:
        display_menu()
                
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
         
        
        if choice in ['1', '2', '3', '4']:
             
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
        
            if choice == '1':
                result = add(number1, number2)
                print(f"The result of addition: {result}")
            elif choice == '2':
                result = subtract(number1, number2)
                print(f"The result of subtract: {result}")
            elif choice == '3':
                result = multiply(number1, number2)
                print(f"The result of multiply: {result}")
            elif choice == '3':
                result = divide(number1, number2)
                print(f"The result of divide: {result}")
        else:
            print("Invalid choice. Please select a valid option.")

            

calculator()