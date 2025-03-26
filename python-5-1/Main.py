def get_area(length, width):
    area = length * width
    return area
def display(length, width, area):
    print ("The landing dimensions are as follows: \nLength:", length, "\nWidth:", width, "\nArea:", area)
length = float(0)
width = float(0)
area = float(0)
length = float(input("Enter the landing zone's length in feet: "))
width = float(input("Enter the landing zone's width in feet: "))
area = get_area(length, width)
display(length, width, area)
