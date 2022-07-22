def print_message(message):
    greeting = "Hello, "

    def printer():
        print(greeting, message)

    return printer

func = print_message("Decorator is awesome")
func()
