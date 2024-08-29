# Match Statement
# Same like Switch in Java

# Write a program to ask user which browser you can run for automation

browser_name = input("Enter the name of browser\n")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        print("Execute the firefox code")
    case "chrome":
        print("Execute the chrome code")
    case "edge":
        print("Execute the edge code")
    case "safari":
        print("Execute the safari code")
    case _:
        print("Browser not found!")
