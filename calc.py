# calc.py
def main():
    print("--- Simple Calculator ---")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    addition = num1 + num2
    subtraction = num1 - num2

    print(f"Subtraction: {num1} - {num2} = {subtraction}")


if __name__ == "__main__":
    main()
