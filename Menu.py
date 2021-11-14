import os

class Menu():
    '''
    Formats menu choices and validates inputs. Also clears screen.
    '''

    # formats menu choices and validates input
    def mainMenu(self, inputs, choices):
        choose = 0
        
        for i in range(len(choices)):
            print("[{}] - {}".format(inputs[i], choices[i]))
        print("")
        while True:
            try:
                choose = int(input("Enter number of choice: "))
                if choose in inputs:
                    break
            except ValueError:
                pass
            print("Invalid Input. Please input only {} to {}.\n".format(inputs[0],inputs[len(inputs)-1]))

        return choose

    # validates integer inputs and ensures input is within range
    def inputInteger(self, first, last, prompt):
        num = 0

        while True:
            try:
                num = int(input("{}: ".format(prompt)))
                if num >= first and num <= last:
                    break
            except ValueError:
                pass
            print("Invalid Input. Please input only {} to {}.\n".format(first, last))

        return num
        
    # clears the screen
    def clearScreen(self):
        if os.name == 'nt' or os.name == 'dos':
            os.system('cls')
        else:
            os.system('clear')