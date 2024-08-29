user_type = input("Enter user type\n")
user_type = user_type.lower()

match user_type:
    case "admin" | "manager":
        print("Hello, Sir")
    case "guest":
        print("Hello, guest")
    case _:
        print("Hello, There")