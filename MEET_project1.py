from multiprocessing.sharedctypes import Value
from Interface import *
from math import sqrt
import sys


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_QDialog()
        self.ui.setupUi(self)

        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        def print_instructions():  # prints the print_instructions
            return ' - If you want to use Exponents, then type it this way "x^y" \n' \
                   '  - If you want to use Square Root, type it this way "sqrt x" \n ' \
                   ' - If you want to use a Factorial, type it this way "x!" \n  ' \
                   '- Press "I" if you want to see the Instructions again. \n ' \
                   ' - Press "H" if you want to see the history of your calculations \n  ' \
                   '- Type "Exit" if you want to exit our amazing program.      You will regret it :) \n   \n       ' \
                   'Good luck! :D'

        signs_list = ['+', '-', '*', '/', '^', '!', ':']  # list that consists of all mathematical signs that might be used while using the calculator.

        # math functions =====================================================================================================
        def SQRT(num):  # returns the square root of the variable num
            new_num = sqrt(num)
            if new_num % 1 == 0:  # checks if new_num could be converted to the int, that way we get rid of the .0
                new_num = int(new_num)
            else:
                new_num = round(new_num, 2)  # rounds answer to 4 digits after decimal point
            return new_num

        def factorial(num):  # Returns the factorial of the number inserted.
            num = int(num)
            new_num = 1
            for i in range(1, num + 1):
                new_num *= i
            return new_num

        def power_of(num1, num2):  # Returns the num1 in power of num2
            new_num = num1 ** num2
            if new_num % 1 == 0:  # checks if new_num could be converted to the int, that way we get rid of the .0
                new_num = int(new_num)
            else:
                new_num = round(new_num, 2)  # rounds answer to 4 digits after decimal point
            return new_num

        def addition(num1, num2):  # this will return the sum of two numbers
            new_num = num1 + num2
            if new_num % 1 == 0:  # checks if new_num could be converted to the int, that way we get rid of the .0
                new_num = int(new_num)
            else:
                new_num = round(new_num, 2)  # rounds answer to 4 digits after decimal point
            return new_num

        def multiplication(num1, num2):  # this will return multiplication of two nums
            new_num = num1 * num2
            if new_num % 1 == 0:  # checks if new_num could be converted to the int, that way we get rid of the .0
                new_num = int(new_num)
            else:
                new_num = round(new_num, 2)  # rounds answer to 2 digits after decimal point
            return new_num

        def division(num1, num2):  # this will return the division of two nums
            new_num = num1 / num2
            if new_num % 1 == 0:  # checks if new_num could be converted to the int, that way we get rid of the .0
                new_num = int(new_num)
            else:
                new_num = round(new_num, 2)  # rounds answer to 2 digits after decimal point
            return new_num

        def subtraction(num1, num2):  # this will return the subtraction of two nums
            new_num = num1 - num2
            if new_num % 1 == 0:  # checks if new_num could be converted to the int, that way we get rid of the .0
                new_num = int(new_num)
            else:
                new_num = round(new_num, 2)  # rounds answer to 2 digits after decimal point
            return new_num

        # MATH INPUT -----------------------------------------------------------------------------------------------
        history_list = []  # this list will have all the previous operations in str format in itself.
        rooterror = 'The root of a negative number does not exist'
        # Math input ===============================================================================================

        def math_input():  # main function : takes the input and processes it.
            txt = self.ui.Main_String.text()
            if("Answer:" in txt):
                txt = txt[7:]

            get_num = ''
            sign = ' '
            counter = 0  # counts how many mathematical signs (+,-,*,/,^) were found in the txt .
            is_action = True

            if '!' in txt:  # if there is '!' in the string, we return the value of factorial(num)
                is_action = False
                index_exc = txt.find('!')
                for i in range(0, index_exc + 1):
                    if txt[i] in digits:
                        get_num += txt[i]
                get_num = int(get_num)
                ans = factorial(get_num)
                print('Answer: ' + str(ans))
                history_list.append(txt + ' = ' + str(ans))
                self.ui.Main_String.setText('Answer: ' + str(ans))

            if '√' in txt:  # this will return the sqrt of the num
                is_action = False
                if '-' in txt:
                    self.ui.Main_String.setText('NegativeRootError')
                    return
                h, num = txt.split(' ')  # splits the string to number and exponents

                if '.' not in num:  # checks if the str(num) can be converted to an int type.
                    num = int(num)  # makes the str(num) an integer
                else:
                    num = float(num)  # makes the str(num) a float, if it's impossible to convert it to an int.

                ans = SQRT(num)
                history_list.append(txt + ' = ' + str(ans))
                self.ui.Main_String.setText('Answer: ' + str(ans) + ' ; ' + str(-1 * ans))

            for element in signs_list:
                if element in txt:  # Searches for the mathematical sign in the txt
                    sign = element

                # Counts how many math signs were found in txt variable
            for symbol in txt:
                if symbol in signs_list:
                    counter += 1

            #     # The Eval part; this will calculate math operation with more than 2 nums
            if counter > 1:
                is_action = False
                try:
                    solution = eval(self.ui.Main_String.text())
                except SyntaxError:
                    self.ui.Main_String.setText("WrongInputError")
                    return

                if solution % 1 == 0:
                    solution = int(solution)
                solution = round(solution, 2)
                self.ui.Main_String.setText('Answer: ' + str(solution))
                history_list.append(txt + ' = ' + str(solution))

            if (counter == 0 and is_action):   # If there is no any mathematical sign (+,-, etc), txt is considered as a wrong input which leads to Input Error raising.
                self.ui.Main_String.setText('WrongInputError')
                return

            elif is_action and counter < 2 and sign is not None:  # If it's a mathematical operation and if there are 2 numbers only
                a, b = txt.split(sign)  # splits the input by math operation sign.
                try:
                    a = float(a)
                    b = float(b)

                except ValueError:
                    self.ui.Main_String.setText("WrongInputError")
                    return

                    

                if sign == '^':
                    ans = str(power_of(a, b))
                    self.ui.Main_String.setText('Answer: ' + ans)  # returns a in power of b as an answer
                    history_list.append(txt + ' = ' + ans)

                if sign == '+':
                    ans = str(addition(a, b))
                    print('Answer: ' + ans)  # returns a + b as an answer
                    history_list.append(txt + ' = ' + ans)
                    self.ui.Main_String.setText('Answer: ' + ans)

                if sign == '-':
                    ans = str(subtraction(a, b))
                    history_list.append(txt + ' = ' + ans)
                    self.ui.Main_String.setText('Answer: ' + ans)  # Writes down the answer straight in the QLineEdit

                if sign == '*':
                    ans = str(multiplication(a, b))
                    history_list.append(txt + ' = ' + ans)
                    self.ui.Main_String.setText('Answer: ' + ans)  # Writes down the answer straight in the QLineEdit

                if sign == '/' or sign == ':':
                    try:
                        ans = str(division(a, b))

                        history_list.append(txt + ' = ' + ans)
                        self.ui.Main_String.setText('Answer: ' + ans)  # Writes down the answer straight in the QLineEdit
                    except ZeroDivisionError:
                        self.ui.Main_String.setText('ZeroDivisionError')

        # The end

        # Buttons and stuff --------------------------------------

        def erase():
            self.ui.Main_String.setText(self.ui.Main_String.setText(''))

        def backspace():
            if("Answer:" in self.ui.Main_String.text() or "WrongInputError" == self.ui.Main_String.text()):
                return
            self.ui.Main_String.setText(self.ui.Main_String.text()[:-1])

        def parentheses_1():
            self.ui.Main_String.setText(self.ui.Main_String.text() + '(')

        def parentheses_2():
            self.ui.Main_String.setText(self.ui.Main_String.text() + ')')

        def press_1():
            self.ui.Main_String.setText(self.ui.Main_String.text() + '1')

        def press_2():
            self.ui.Main_String.setText(self.ui.Main_String.text() + '2')

        def press_3():
            self.ui.Main_String.setText(self.ui.Main_String.text() + '3')

        def press_4():
            self.ui.Main_String.setText(self.ui.Main_String.text() + '4')

        def press_5():
            self.ui.Main_String.setText(self.ui.Main_String.text() + '5')

        def press_6():
            self.ui.Main_String.setText(self.ui.Main_String.text() + '6')

        def press_7():
            self.ui.Main_String.setText(self.ui.Main_String.text() + '7')

        def press_8():
            self.ui.Main_String.setText(self.ui.Main_String.text() + '8')

        def press_9():
            self.ui.Main_String.setText(self.ui.Main_String.text() + '9')

        def press_0():
            self.ui.Main_String.setText(self.ui.Main_String.text() + '0')

        def add_dot():
            self.ui.Main_String.setText(self.ui.Main_String.text() + '.')

        def add_plus():
            self.ui.Main_String.setText(self.ui.Main_String.text() + ' + ')

        def add_minus():
            self.ui.Main_String.setText(self.ui.Main_String.text() + ' - ')

        def add_msign():
            self.ui.Main_String.setText(self.ui.Main_String.text() + ' * ')

        def add_dsign():
            self.ui.Main_String.setText(self.ui.Main_String.text() + ' / ')

        def add_fsign():
            self.ui.Main_String.setText(self.ui.Main_String.text() + '!')

        def add_exp():
            self.ui.Main_String.setText(self.ui.Main_String.text() + ' ^ ')

        def add_root():
            self.ui.Main_String.setText(self.ui.Main_String.text() + '√ ')

        def show_instructions():
            msg = QMessageBox()
            msg.setWindowTitle("Instructions: ")
            msg.setBaseSize(QSize(600, 600))
            msg.setIcon(QMessageBox.Question)
            msg.setText(print_instructions())
            msg.setStyleSheet("background-color:rgb(37,37,56);\n"
                              "border-style: outset;\n"
                              "color: rgb(170, 170, 255);")
            button = QMessageBox.Ok
            msg.addButton(button)
            x = msg.exec()
            history_list.append('I')

        def get_history():
            txt = ''
            lines = len(history_list)
            if lines == 0:
                return ' Your search history is still empty. Go ahead!'
            for i in range(lines):
                if history_list[i] == 'H':
                    history_list[i] = "History Search"
                if history_list[i] == 'I':
                    history_list[i] = "Show Instructions"
                txt += '#' + str(i + 1) + ': ' + history_list[i] + '\n'
            return txt

        def show_history():
            msg2 = QMessageBox()
            msg2.setWindowTitle("History: ")
            msg2.setBaseSize(QSize(600, 600))
            msg2.setIcon(QMessageBox.Information)
            msg2.setText(get_history())
            msg2.setStyleSheet("background-color:rgb(37,37,56);\n"
                               "border-style: outset;\n"
                               "color: rgb(170, 170, 255);")
            button = QMessageBox.Ok
            msg2.addButton(button)
            x2 = msg2.exec()
            history_list.append("H")

        def show_rooterror():
            msg3 = QMessageBox()
            msg3.setWindowTitle("NegativeRootError")
            msg3.setBaseSize(QSize(600, 600))
            msg3.setIcon(QMessageBox.Abort)
            msg3.setText(rooterror)
            msg3.setStyleSheet("background-color:rgb(37,37,56);\n"
                               "border-style: outset;\n"
                               "color: rgb(170, 170, 255);")
            button = QMessageBox.Ok
            msg3.addButton(button)
            x3 = msg3.exec()



        self.ui.Button_0.clicked.connect(press_0)
        self.ui.Button_1.clicked.connect(press_1)
        self.ui.Button_2.clicked.connect(press_2)
        self.ui.Button_3.clicked.connect(press_3)
        self.ui.Button_4.clicked.connect(press_4)
        self.ui.Button_5.clicked.connect(press_5)
        self.ui.Button_6.clicked.connect(press_6)
        self.ui.Button_7.clicked.connect(press_7)
        self.ui.Button_8.clicked.connect(press_8)
        self.ui.Button_9.clicked.connect(press_9)
        self.ui.button_left.clicked.connect(parentheses_1)
        self.ui.button_right.clicked.connect(parentheses_2)
        self.ui.Dot_Button.clicked.connect(add_dot)
        self.ui.Backspace.clicked.connect(backspace)
        self.ui.plus_button.clicked.connect(add_plus)
        self.ui.minus_button.clicked.connect(add_minus)
        self.ui.mult_button.clicked.connect(add_msign)
        self.ui.division_button.clicked.connect(add_dsign)
        self.ui.factorial_button.clicked.connect(add_fsign)
        self.ui.exp_button.clicked.connect(add_exp)
        self.ui.Enter.clicked.connect(math_input)
        self.ui.erase_button.clicked.connect(erase)
        self.ui.mult_button_2.clicked.connect(add_root)
        self.ui.instructions.clicked.connect(show_instructions)
        self.ui.history.clicked.connect(show_history)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my_app = MyWin()
    my_app.show()
    sys.exit(app.exec_())
