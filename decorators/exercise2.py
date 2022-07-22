def print_message(message):
    greeting = "Hello, "

    def printer():
        print(greeting, message)

    printer()

print_message("Decorator is awsome")
