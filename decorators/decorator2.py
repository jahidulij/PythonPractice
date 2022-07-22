def display_info(func):

    def inner():
        print("Executing " + func.__name__ + " function")
        func()
        print("Finished executing " + func.__name__ + " function")

    return inner

@display_info
def printer():
    print("Hello from printer function")

printer()
# f = display_info(printer)
# print(f())
