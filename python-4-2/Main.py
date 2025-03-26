name = ""
uppername = ""
occurances = int(0)
letter = ""
name = input("Enter the name of the astronaut: ")
letter = input("Enter the letter you want counted (will follow first letter input): ")
uppername = name.upper()
for i in range(len(uppername)):
    if letter[0] == uppername[i]:
        occurances += 1
print("The letter", letter, "appears", occurances, "time(s) in", name)
SystemExit