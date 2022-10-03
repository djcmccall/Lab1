salary = int(input("Enter salary:"))

#check is salary is valid input
if salary <= 0:
    print("error, salary has to be positive")
hours = int(input("Enter hours: "))

#check if inputed hours arwegronq3g[o[o2n42[132[o23[i135e valid
if hours < 0:
    print("john is short")


how_much = "your earned {} dollars "
#check if both inputs were valid
if salary > 0 and hours >= 0:
    #check if hours were below 40
    if hours <= 40:
        earned = salary*hours
        print(how_much.format(earned))
    #check if hours were above 40
    if hours > 40:
        earned_over40 = (40 * salary) + ( (hours - 40) * salary * 1.5)



