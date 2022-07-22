try:
    numerator = input("Enter numerator: ")
    denominator = input("Enter denominator: ")

    result = int(numerator) / int(denominator)
    print("Result: " + str(result))

    my_list = [1, 2, 3]
    i = int(input("Enter index: "))
    print("List value is: " + str(my_list[i]))

except ZeroDivisionError:
    print("Denominator can't be 0. Please try again")

except IndexError:
    print("Index can't be greater than size list.")

finally:
    print("Will print all the times")

print("Program ends")
