# function definition

def greet():
    print("Hello there!!!")

    def _():
        print("Hi...")

        def nikita():
            print("Hi Nikita!!")
            _()

    # function calling
    result = greet()
    _()
    print(result)

