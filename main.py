# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# This function asks for user name and prints to screen.
# Asks for a number and prints the number multiplied by itself
# Asks user for a word and prints word character count
def my_function():
    # Get user name
    name = input("Tell me your name:")
    # Print user name
    print(f'Hello {name}')
    # asks for number from user
    numberX2 = int (input("Input a number you would like multiplied by itself:"))
    # Multiplies user number by itself
    numberX2 *= numberX2
    # Prints users multiplied number
    print(numberX2)
    # Asks for a word from user so that they can have the characters counted
    userWord = input("Tell me a word and ill tell you how many characters are in it:")
    # counts letters an
    letterCount = len(userWord)
    # Prints letter count of users word
    print( name,f'I counted all of the characters in {userWord} and it totals {letterCount} character(s)!')
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Why will this not change? please tell me {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('Guido!')
    my_function()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/