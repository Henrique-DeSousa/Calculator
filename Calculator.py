def main():
    def addition(x, y):
        return x + y

    def subtraction(x, y):
        return x - y

    def multiplication(x, y):
        return x * y

    def division(x, y):
        if y == 0:
            return "Cannot divide by 0"
        return x / y

    print("Select operation.")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")

    while True:
        choice = input("Enter choice(1/2/3/4): ")

        if choice in '1' '2' '3' '4':
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", addition(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtraction(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiplication(num1, num2))
            elif choice == '4':
                print(num1, "/", num2, "=", division(num1, num2))

            next_calculation = input("Let's go again? (y/n): ")
            # if next_calculation == "no" or next_calculation == "n":
            if next_calculation[0].upper() == "N":
                break

        else:
            print("Invalid input")


if __name__ == '__main__':
    main()
