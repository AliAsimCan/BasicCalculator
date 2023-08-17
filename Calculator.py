first_number = input("Enter first number: ")
process = input("Enter process (+, -, *, /): ")
second_number = input("Enter second number: ")

def calculate():
        try:
            if process == "+":
                collection_result = float(first_number) + float(second_number)
                print(collection_result)

            if process == "-":
                collection_result = float(first_number) - float(second_number)
                print(collection_result)

            if process == "*":
                collection_result = float(first_number) * float(second_number)
                print(collection_result)

            if process == "/":
                collection_result = float(first_number) / float(second_number)
                print(collection_result)

        except ValueError:
            pass

calculate()