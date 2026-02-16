def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def display_menu():
    """Display a clean formatted menu"""
    print("\n" + "="*40)
    print("        SIMPLE CALCULATOR")
    print("="*40)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("="*40)

def get_valid_input(prompt):
    """Get valid numeric input from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def main():
    """Main calculator loop"""
    print("\n✓ Welcome to Simple Calculator!")
    
    while True:
        display_menu()
        choice = input("Enter choice (1/2/3/4/5): ").strip()
        
        # Check for exit option
        if choice == '5':
            print("\n" + "="*40)
            print("Thank you for using Calculator!")
            print("="*40 + "\n")
            break
        
        # Validate choice
        if choice not in ['1', '2', '3', '4']:
            print("❌ Invalid choice! Please select 1, 2, 3, 4, or 5.")
            continue
        
        try:
            # Get numbers from user
            num1 = get_valid_input("Enter first number: ")
            num2 = get_valid_input("Enter second number: ")
            
            # Perform calculation
            result = None
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"
            
            # Display result with formatting
            print("-"*40)
            print(f"✓ Result: {num1} {operation} {num2} = {result}")
            print("-"*40)
            
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()