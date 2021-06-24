"""
Credit card number validator
"""
import tkinter as tk
import random

class CardNumber(): # card_num = CardNumber()
    def __init__(self):
        self.cc_number = ''

    def request_number(self): # When check button clicked
        while True:
            for widget in frame.winfo_children():
                widget.destroy()
            self.cc_number = myEntry.get()
            if self.cc_number.isdigit() and len(self.cc_number) == 16:
                workings.show_results_count = 0
                calc_process.run_calc()
                break
            else:
                workings.show_results_count = 0
                self.try_again = '\nMUST be 16 digits. Check number and try again\n'
                myLabel = tk.Label(frame, text=self.try_again, bg='gray', fg='black',font=('Courier',14))
                myLabel.pack()
                break

    def __str__(self):
        return f'Entered Credit Card number: {self.cc_number}'

class Algo(): # calc_process = Algo()
    def __init__(self):
        pass

    def run_calc(self):

        self.doubles = []
        self.doubles_sum = []
        self.doubles_sum_temp = []
        self.cc_number_2_dbls_summed = []

        self.cc_number_2 = list(map(int, card_num.cc_number))

        # first digit then every 2nd digit multiplied by two
        for x in range(0, len(self.cc_number_2), 2):
            self.cc_number_2[x] *=2

        for double_digit in self.cc_number_2:
            if double_digit > 9:
                self.doubles.append(double_digit)

        self.sum_of_digits = 0
        self.n = 0 
        self.doubles_str = list(map(str, self.doubles))
        while self.n < len(self.doubles_str):
            for i in self.doubles_str[self.n]:
                self.sum_of_digits += int(i)
            self.doubles_sum.append(self.sum_of_digits)
            self.sum_of_digits = 0
            self.n += 1

        for x in self.doubles_sum:
            self.doubles_sum_temp.append(x)
        for y in self.cc_number_2:
            self.cc_number_2_dbls_summed.append(y)

        while len(self.doubles_sum_temp) >0:
            for i in range(len (self.cc_number_2_dbls_summed)):
                if (self.cc_number_2_dbls_summed[i] >9):
                    self.cc_number_2_dbls_summed[i] = self.doubles_sum_temp[0]
                    del self.doubles_sum_temp[0]
        
        self.last_digit = self.cc_number_2.pop(-1)
        self.total = sum(self.cc_number_2_dbls_summed[0:15])
        self.final_number = self.total + self.last_digit
        
        check_now.cc_str_formatted1(card_num.cc_number)
        check_now.check()

    def __str__(self):
        pass

class CheckSum(): # check_now = CheckSum()
    def __init__(self):
        pass

    def check(self):
        if (calc_process.total + calc_process.last_digit) % 10 == 0:
            self.num = f'\n{check_now.cc_num_formatted1}'
            self.valid = '\nVALID card number\n'
            myLabel = tk.Label(frame, text=self.num, bg='green', fg='white', font=('Courier', 14))
            myLabel.pack()
            myLabel = tk.Label(frame, text=self.valid, bg='green', fg='white', font=('Courier', 14))
            myLabel.pack()
        else:
            self.num = f'\n{check_now.cc_num_formatted1}'
            self.valid = '\nINVALID card number\n'
            myLabel = tk.Label(frame, text=self.num, bg='red', fg='white', font=('Courier', 14))
            myLabel.pack()
            myLabel = tk.Label(frame, text=self.valid, bg='red', fg='white', font=('Courier', 14))
            myLabel.pack()

    # method to change format from 1234123412341234 to 1234-1234-1234-1234
    def cc_str_formatted1(self,cc_num):
        str1 = cc_num[0:4]
        str2 = cc_num[4:8]
        str3 = cc_num[8:12]
        str4 = cc_num[12:16]
        self.cc_num_formatted1 = (f'{str1}-{str2}-{str3}-{str4}')

    def __str__(self):
        pass

class Results(): # workings = Results()
    def __init__(self):
        self.show_results_count = 0
        pass

    def show_results(self):
        if card_num.cc_number.isdigit() and len(card_num.cc_number) == 16 and self.show_results_count == 0:
            text1 = f'\nCard number: {check_now.cc_num_formatted1}'
            text2 = f'Last digit {calc_process.last_digit}'
            text3 = f'Card number (last digit removed) {check_now.cc_num_formatted1[:-1]}'
            text4 = f'First digit and every second digit multiplied by two {calc_process.cc_number_2}'
            text5 = f'Double digit numbers {calc_process.doubles} digits added together resulting in {calc_process.doubles_sum}'
            text6 = f'({calc_process.cc_number_2_dbls_summed[0:15]}) + last digit ({calc_process.last_digit}) = {calc_process.final_number}'
            text7 = f'\nTotal {calc_process.final_number}'
            text8 = '\nCard number passes validation when total is a multiple of 10\n'

            myLabel = tk.Label(frame, text=text1, bg='white', fg='black', font=('Courier',14))
            myLabel.pack()
            myLabel = tk.Label(frame, text=text2, bg='white', fg='black', font=('Courier',14))
            myLabel.pack()
            myLabel = tk.Label(frame, text=text3, bg='white', fg='black', font=('Courier',14))
            myLabel.pack()
            myLabel = tk.Label(frame, text=text4, bg='white', fg='black', font=('Courier',14))
            myLabel.pack()
            myLabel = tk.Label(frame, text=text5, bg='white', fg='black', font=('Courier',14))
            myLabel.pack()
            myLabel = tk.Label(frame, text=text6, bg='white', fg='black', font=('Courier',14))
            myLabel.pack()
            myLabel = tk.Label(frame, text=text7, bg='white', fg='black', font=('Courier',14))
            myLabel.pack()
            myLabel = tk.Label(frame, text=text8, bg='white', fg='black', font=('Courier',14))
            myLabel.pack()

            self.show_results_count = 1

        elif self.show_results_count == 0:
            self.try_again = '\nERROR: Unable to calculate. Check number and try again\n'
            myLabel = tk.Label(frame, text=self.try_again, bg='gray', fg='black',font=('Courier',14))
            myLabel.pack()

            self.show_results_count = 1

    def __str__(self):
        pass

muk_list = []
mukas_count = 0
def mukas():
    global muk_list
    global mukas_count
    mukas = ['m','u','k','a','s']
    random.shuffle(mukas)
    muk_list.append(mukas[2])
    muk_list_length = len(muk_list)
    display_clicks = f'\nClicks: {muk_list_length}'
    display_bingo = f'\nMukas count: {mukas_count}'
    muk_list_str = ''.join(str(i) for i in muk_list)
    if 'mukas' in muk_list_str:
        mukas_count += 1

    for widget in frame.winfo_children():
            widget.destroy()
    myLabel = tk.Label(frame, text=muk_list, bg='purple', fg='white', font=('Courier',66))
    myLabel.pack()
    myLabel = tk.Label(frame, text=display_clicks, bg='purple', fg='white', font=('Courier',20))
    myLabel.pack()
    myLabel = tk.Label(frame, text=display_bingo, bg='purple', fg='white', font=('Courier',20))
    myLabel.pack()
    


def clear():
    global muk_list
    global mukas_count
    muk_list = []
    mukas_count = 0
    for widget in frame.winfo_children():
            widget.destroy()

# 4578423013769219 # example

card_num = CardNumber()
calc_process = Algo()
check_now = CheckSum()
workings = Results()

root = tk.Tk()
root.title('Credit Card Validation')

canvas = tk.Canvas(root, height=500, width=1100, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.05)

myEntry = tk.Entry(root, width=16, bg='gray', fg='black')
myEntry.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.05)
myEntry.pack()

welcome_message = '\nWelcome to Credit Card Validation\n\nTo begin, enter a 16 digit credit card number\n'

myLabel = tk.Label(frame, text=welcome_message, bg='orange', fg='white', font=('Courier',20))
myLabel.pack()

check = tk.Button(root, text="Submit", padx=10, pady=5, fg="blue", command=card_num.request_number) # bg='#263D42' BACKGROUND COLOUR DOESN"T WORK ON Mac
check.pack()
#########################
#########################
######################### Maybe remove the show calc button and make it automated part of 'check' button
######################### 
showCalc = tk.Button(root, text="Show Calc", padx=10, pady=5, fg="blue", command=workings.show_results) # bg='#263D42' BACKGROUND COLOUR DOESN"T WORK ON Mac
showCalc.pack()

test = tk.Button(root, text="Game", padx=10, pady=5, fg="blue", command=mukas) # bg='#263D42' BACKGROUND COLOUR DOESN"T WORK ON Mac
test.pack()

clearScreen = tk.Button(root, text="Clear Screen", padx=10, pady=5, fg="blue", command=clear) # bg='#263D42' BACKGROUND COLOUR DOESN"T WORK ON Mac
clearScreen.pack()

root.mainloop()