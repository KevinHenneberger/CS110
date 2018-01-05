# function that performs calculation
def cost_per_week(num_weeks, num_classes, tuition):
    return (tuition / num_classes) / num_weeks

def main():
    
    # prompt the user for input
    weeksStr = input("Please enter the number of weeks in a semester: ")
    classesStr = input("Please enter the number of classes you are taking: ")
    tuitionStr = input("Please enter your tuition: ")

    # convert the string to an integer and store it in a new variable
    weeks = int(weeksStr)
    classes = int(classesStr)
    tuition = int(tuitionStr)

    # store the cost_per_week() in a variable
    cost_per_week_val = cost_per_week(weeks, classes, tuition)

    # print to the console
    print("Weeks:", weeks, "Classes:", classes, "Tuition:", tuition)
    print("Cost per week:", cost_per_week_val)
    
    # prompt the user for input and convert it from a string to an integer
    classes_per_week = int(input("Please enter how many times per week your class meets: "))

    # store the result in a variable
    cost_per_class = cost_per_week_val / classes_per_week

    # print to the console
    print("Cost per class:", cost_per_class)

main()
