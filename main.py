# Kyle's Code
running = True
password = ''

def menu():
    print("\n\nMenu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    choice = int(input("\nPlease enter an option:\n"))
    options(choice)

def options(choice):

    global running, password

    if choice == 1:
        password = input("Please enter your password to encode:\n")
        password = encode(password)
        print("Your password has been encoded and stored!")
    if choice == 3:
        running = False

def encode(password):

    return_str = ''
    digit_list = []

    for char in password:
        digit_list.append(int(char))

    for x in range(0, len(digit_list)):
        digit_list[x] += 3

    for digit in digit_list:
        return_str += str(digit)

    return return_str


def main():

    global running

    while running:
        menu()

if __name__ == '__main__':
    main()