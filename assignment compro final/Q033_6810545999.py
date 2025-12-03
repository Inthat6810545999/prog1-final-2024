# Name: Inthat # Student ID: 68010545999

while True:
    try:
        expression = input("Enter expression: ")
        lst_op = expression.split()

        if expression == "EXIT":
            break

        valid_format = True
        for i in range(len(lst_op)):
            if lst_op[i] not in "+-*/" and i % 2 != 0:
                valid_format = False
                break

        for i in range(len(lst_op)):
            if i % 2 == 0 and lst_op[i] not in "+-*/":
                float(lst_op[i])

        if not valid_format or lst_op[-1] in "+-*/":
            print("Error: Invalid expression format.")

        else:
            try:
                while len(lst_op) > 1:
                    num_1 = float(lst_op[0])
                    op_type = lst_op[1]
                    num_2 = float(lst_op[2])

                    if op_type == "+":
                        result = num_1 + num_2
                    elif op_type == "-":
                        result = num_1 - num_2
                    elif op_type == "*":
                        result = num_1 * num_2
                    elif op_type == "/":
                        result = num_1 / num_2

                    lst_op = lst_op[3:]
                    lst_op.insert(0, str(result))

                result = lst_op[0]
                print(f"Result: {float(result):.1f}")

            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")

    except ValueError as value_error:
        value_error = str(value_error).replace("could not convert string to float: ", "")
        print(f"Error: Invalid number {value_error} in expression.")

print("Goodbye!")