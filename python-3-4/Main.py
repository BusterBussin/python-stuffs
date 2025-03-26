print("This program helps us rank astronauts from highest to lowest")
astronaut1 = input("Enter the first astronaut's name: ")
astro1score = int(input("Enter the first astronaut's score: "))
astronaut2 = input("Enter the second astronaut's name: ")
astro2score = int(input("Enter the second astronaut's score: "))
astronaut3 = input("Enter the third astronaut's name: ")
astro3score = int(input("Enter the third astronaut's score: "))
firstPlace = ""
secondPlace = ""
thirdPlace = ""
if astro1score > astro2score and astro1score > astro3score:
    firstPlace = astronaut1
if astro2score > astro1score and astro2score > astro3score:
    firstPlace = astronaut2
if astro3score > astro1score and astro3score > astro1score:
    firstPlace = astronaut3
if astro1score > astro2score and astro1score < astro3score or astro1score > astro3score and astro1score < astro2score:
    secondPlace = astronaut1
if astro2score > astro1score and astro2score < astro3score or astro2score > astro3score and astro2score < astro1score:
    secondPlace = astronaut2
if astro3score > astro1score and astro3score < astro2score or astro3score > astro2score and astro3score < astro1score:
    secondPlace = astronaut3
if astro1score < astro2score and astro1score < astro3score:
    thirdPlace = astronaut1
if astro2score < astro1score and astro2score < astro3score:
    thirdPlace = astronaut2
if astro3score < astro1score and astro3score < astro2score:
    thirdPlace = astronaut3
print("Highest Score:", firstPlace)
print("Second highest score:", secondPlace)
print("Third highest score:", thirdPlace)