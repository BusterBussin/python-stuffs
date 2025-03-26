def file_opener(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        average_steps = [0] * 12
        currentMonth = 0
        currentDate = 0
        runningTotal = 0
        index = 0
        for line in lines:
            line_steps = int(line.strip())
            runningTotal += line_steps
            currentDate += 1
            if currentDate == num_of_days[currentMonth]:
                average_steps[currentMonth] = runningTotal // num_of_days[currentMonth]
                currentMonth += 1
                currentDate = 0
                runningTotal = 0
            index += 1
        result = "\n".join(f"Average steps for {month_names[i]}: {average_steps[i]}" for i in range(12))
        return result
    except FileNotFoundError:
        return "Error: File Not Found"
if __name__ == "__main__":
    print(file_opener("steps.txt"))