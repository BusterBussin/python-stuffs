name = ""
filename = input("Please enter the name of a file:")
occurances = 0
letter = input("Please enter the letter you want counted.")
letter = letter[0]
letter = letter.upper()
with open(filename, "r"):
    for line in filename:
        occurances += line.upper().count(letter)
print(f"The letter '{letter}' occured {occurances} times in the file.")