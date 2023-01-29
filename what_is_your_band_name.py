
def program():
    #1. Create a greeting for your program.
    print("Hello and welcome to the program")

    #2. Ask the user for the city that they grew up in.
    print("What city did you grow up in")
    city = input()
    #3. Ask the user for the name of a pet.
    print("What is the name of your pet")
    pet = input()
    #4. Combine the name of their city and pet and show them their band name.
    print("your band name is" + city + " " + pet)
    #5. Make sure the input cursor shows on a new line:

if __name__ == '__main__':
    program()