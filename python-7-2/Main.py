from SecurityAuthenticator import SecurityAuthenticator
auth = SecurityAuthenticator()
securityNumber = int(input("Enter your security authentication number: "))
valid = bool(auth.isValid(securityNumber))
if valid:
    print("The security number is valid")
else:
    print("The security number is invalid.")
SystemExit