#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

def program():
    print("Welcome to the tip calculator")

    bill = float(input("How much did you spend on the bill: $"))
    tip_percentage = int(input("What percentage of tip would you like to give? 10, 12, or 15? %"))
    people = int(input("How many people are you splitting the bill with? "))

    tip_percentage = 1 + (tip_percentage / 100)

    split_bill = (bill*tip_percentage) / people

    print("everyone owes: $" + str(round(split_bill,2)))

if __name__ == '__main__':
    program()