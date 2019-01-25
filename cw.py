# KEY Neither problem solution runs correctly 

def main():
    #problem1
    problem2


#Create a function that has a loop that quits with q.
# If the user doesn't enter q, ask them to input another string.

# KEY: Incomplete. Need to loop and keep asking
def problem1():
    letter= input("Enter a letter.")
    if letter=='q':
        break
    else:
        print("TRY AGAIN")

def exercise2_helper():

# Write 2 functions: exercise2() and exercise2_helper(num1, num2, num3. operation)
# The function exercise2_helper(num1, num2, num3) should expect 3 numbers, and an operation to perform as a String as parameters.
# KEY: Incomplete. 
def problem2():


    def exercise2_helper():
        number = str(int(input("")))
        number2=str(int(input("")))
        number3=str(int(input("")))
        average= str(int("number" +"number2" +"number3", ))
        print(average)


#############################################################
# SEE SOLUTIONS BELOW
#############################################################

# KEY: PROBLEM 1 SOLUTION
def problem1_solution():
    user_input = ""

    while(user_input.lower() != 'q'):
        user_input = input("Enter Something:\n")


# KEY: PROBLEM 2 SOLUTION
def problem2_solution():
    # Helper function can be nested or outside of this function
    def exercise2_helper_solution(num1, num2, num3, operation):
        if (operation.lower() == "sum"):
            return (num1 + num2 + num3)
        elif (operation.lower() == "prod"):
            return (num1 * num2 * num3)
        elif (operation.lower() == "avg"):
            return ((num1 + num2 + num3) / 3)
        else:
            print("ERROR")

    # Some test data/could have user input these
    n1 = 1
    n2 = 20
    n3 = 30

    # Test each operation (note: handles operation in any case)
    print(f"The SUM of the numbers {n1}, {n2}, {n3} is: {exercise2_helper_solution(n1, n2, n3, 'SUM')}")
    print(f"The PRODUCT of the numbers {n1}, {n2}, {n3} is: {exercise2_helper_solution(n1, n2, n3, 'Prod')}")
    print(f"The AVERAGE of the numbers {n1}, {n2}, {n3} is: {exercise2_helper_solution(n1, n2, n3, 'avg')}")


# Run the solution(s)
# problem1_solution()
# problem2_solution()









    if __name__ == '__main__':
        main()