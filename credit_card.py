"""
Credit card number validator
Enter 16 digit credit card number
Algo
Result
"""
import tkinter as tk
# from tkinter import *
# from tkinter import Frame, filedialog, Text
# import os
import random

class CardNumber(): # card_num = CardNumber()
    def __init__(self):
        self.cc_number = ''
        self.run_count = 0

    def request_number(self):
        print('\n'*25)
        print('\t>>> Credit Card validator <<<')
        while True:
            self.cc_number = e.get() # for GUI
            # self.cc_number = input('\nPlease enter a 16 digit credit card number:  ')
            if self.cc_number.isdigit() and len(self.cc_number) == 16:
                calc_process.run_calc()
                break
            else:
                self.try_again = '\nMUST be 16 digits, try again\n'
                myLabel = tk.Label(frame, text=self.try_again, bg='gray', fg='black',font=('Courier',14))
                myLabel.pack()
                self.run_count+=1
                if self.run_count == 4:
                    for widget in frame.winfo_children():
                        widget.destroy()
                        self.run_count = 0
                # print('\n\tTry again, numbers only (16 digits)\n')
                # continue
                break # for GUI

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

        # first digit then every 2nd digit multiplied by 2
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

    # def run_calc(self): ################### CAN UN-COMMENT THIS IF THE NEW VERSION DOESN'T WORK ###########
    #     self.cc_number_doubled = []

    #     self.cc_number_map = map(int, card_num.cc_number)
    #     self.cc_number_list_int = list(self.cc_number_map)

    #     self.last_digit = self.cc_number_list_int.pop(-1)
    #     self.cc_number_list_int_fixed = []
    #     for x in self.cc_number_list_int:
    #         self.cc_number_list_int_fixed.append(x)

    #     ###################### STARTING WITH first digit, multiply every second digit by 2 #################
    #     for x in self.cc_number_list_int[0:15:2]: 
    #         self.cc_number_doubled.append(x*2)
    #     del self.cc_number_list_int[0:15:2]

    #     self.cc_number_doubled_fixed = []
    #     for i in self.cc_number_doubled:
    #         self.cc_number_doubled_fixed.append(i)

    #     for x in self.cc_number_doubled:
    #         if x < 10:
    #             self.cc_number_list_int.append(x)

    #     self.temp_hold = []
    #     for y in self.cc_number_doubled:
    #         if y > 9:
    #             self.temp_hold.append(y)
    #     self.cc_number_doubled = self.temp_hold

    #     self.cc_number_doubled_map = map(str, self.cc_number_doubled)
    #     self.cc_number_doubled_str = list(self.cc_number_doubled_map)

    #     self.cc_number_sum_double = []

    #     self.sum_of_digits = 0
    #     self.n = 0 
    #     while self.n < len(self.cc_number_doubled_str):
    #         for i in self.cc_number_doubled_str[self.n]:
    #             self.sum_of_digits += int(i)
    #         self.cc_number_sum_double.append(self.sum_of_digits)
    #         self.sum_of_digits = 0
    #         self.n += 1

    #     self.total = sum(self.cc_number_list_int+self.cc_number_sum_double)
    #     self.final_number = self.total + self.last_digit
        
    #     card_num.cc_str_formatted1(card_num.cc_number)
    #     check_now.check()

    def __str__(self):
        pass

class CheckSum(): # check_now = CheckSum()
    def __init__(self):
        self.run_count = 0

    def check(self):
        if (calc_process.total + calc_process.last_digit) % 10 == 0:
            #self.num = f'\n{calc_process.card_number_format}'
            self.num = f'\n{check_now.cc_num_formatted1}'
            self.valid = '\nVALID card number!!\n'
            myLabel = tk.Label(frame, text=self.num, bg='green', fg='white', font=('Courier', 14))
            myLabel.pack()
            myLabel = tk.Label(frame, text=self.valid, bg='green', fg='white', font=('Courier', 14))
            myLabel.pack()
            # print('\n\tVALID card number!!')
            self.run_count+=1
            if self.run_count == 4:
                for widget in frame.winfo_children():
                    widget.destroy()
                    self.run_count = 0

            # workings.show_results() # rem for GUI
        else:
            self.num = f'\n{check_now.cc_num_formatted1}'
            # self.num = f'\n{calc_process.card_number_format}'
            self.valid = '\nINVALID card number, please try again\n'
            myLabel = tk.Label(frame, text=self.num, bg='red', fg='white', font=('Courier', 14))
            myLabel.pack()
            myLabel = tk.Label(frame, text=self.valid, bg='red', fg='white', font=('Courier', 14))
            myLabel.pack()
            # print('\n\tINVALID card number, please check and try again')
            self.run_count+=1
            if self.run_count == 4:
                for widget in frame.winfo_children():
                    widget.destroy()
                    self.run_count = 0
            # workings.show_results() # rem for GUI

    # func to change 1234123412341234 to 1234-1234-1234-1234
    def cc_str_formatted1(self,cc_num):
        str1 = cc_num[0:4]
        str2 = cc_num[4:8]
        str3 = cc_num[8:12]
        str4 = cc_num[12:16]
        self.cc_num_formatted1 = (f'{str1}-{str2}-{str3}-{str4}')

    def __str__(self):
        pass

class Results():
    def __init__(self):
        pass

    def show_results(self):
        self.show_calc()

    # rem for GUI
    #     # self.user_input = input('\nShow calculations? y/n  :')
    #     # while True:
    #     #     try:
    #     #         if self.user_input[0].lower() == 'y':
    #     #             self.show_calc()
    #     #             break
    #     #         elif self.user_input[0].lower() == 'n':
    #     #             print('\n\tThanks for enjoying the program! bye for now\n')
    #     #             break
    #     #     except:
    #     #         print('invalid option, try again')
    #     #         continue

    def show_calc(self):
        text1 = f'\nCard number: {check_now.cc_num_formatted1}'
        text2 = f'Last digit {calc_process.last_digit}'
        text3 = f'Card number (last digit removed) {check_now.cc_num_formatted1[:-1]}'
        text4 = f'First digit and every second digit multiplied by two {calc_process.cc_number_2}'
        text5 = f'Double digit numbers {calc_process.doubles} digits added together resulting in {calc_process.doubles_sum}'
        text6 = f'({calc_process.cc_number_2_dbls_summed[0:15]}) + last digit ({calc_process.last_digit}) = {calc_process.final_number}'
        text7 = f'\nTotal ({calc_process.final_number})'
        text8 = '\nTotal must be a multiple of 10 to pass validation\n'

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

        # print(f'\nCard number: {card_num.cc_number}')
        # print(f'Last digit ({calc_process.last_digit})')
        # print(f'Card number without last digit {calc_process.cc_number_list_int_fixed}')
        # print(f'First digit and every second digit multiplied by 2 {calc_process.cc_number_doubled_fixed}')
        # print(f'Double digit numbers {calc_process.temp_hold} digits added together resulting in {calc_process.cc_number_sum_double}')
        # print(f'These ({calc_process.cc_number_list_int}) + these ({calc_process.cc_number_sum_double}) = {calc_process.total}')
        # print(f'({calc_process.total}) + last digit ({calc_process.last_digit}) = {calc_process.final_number}')
        # print(f'\n\tFinal number ({calc_process.final_number})')
        # print('\nFinal number must be a multiple of 10 to pass validation\n')

    def __str__(self):
        pass

# muk = 0
# def mukas():
#     global muk
#     mukas = ['m','u','k','a','s']
#     random.shuffle(mukas)
#     myLabel = tk.Label(frame, text=mukas[0], bg='purple', fg='white', font=('Courier',66))
#     myLabel.pack()
#     muk+=1
#     if muk > 5:
#         for widget in frame.winfo_children():
#             widget.destroy()
#             muk = 0

muk = 0
def mukas():
    global muk
    mukas = ['m','u','k','a','s']
    random.shuffle(mukas)
    muk_list = []
    myLabel = tk.Label(frame, text=mukas[0], bg='purple', fg='white', font=('Courier',66))
    myLabel.pack()
    muk+=1
    if muk > 5:
        for widget in frame.winfo_children():
            widget.destroy()
            muk = 0

def clear():
    for widget in frame.winfo_children():
            widget.destroy()


# 4578423013769219 # example

card_num = CardNumber()
calc_process = Algo()
check_now = CheckSum()
workings = Results()
# card_num.request_number()

root = tk.Tk()
root.title('Credit Card Validation')
# root.geometry('450x350')

canvas = tk.Canvas(root, height=500, width=1100, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.05)

e = tk.Entry(root, width=16, bg='gray', fg='black')
e.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.05)
e.pack()

check = tk.Button(root, text="Check", padx=10, pady=5, fg="blue", command=card_num.request_number) # bg='#263D42' BACKGROUND COLOUR DOESN"T WORK ON Mac
check.pack()
# check.grid(row=0, column=0)

showCalc = tk.Button(root, text="Show Calc", padx=10, pady=5, fg="blue", command=workings.show_results) # bg='#263D42' BACKGROUND COLOUR DOESN"T WORK ON Mac
showCalc.pack()

mukButton = tk.Button(root, text="Test", padx=10, pady=5, fg="blue", command=mukas) # bg='#263D42' BACKGROUND COLOUR DOESN"T WORK ON Mac
mukButton.pack()

clearScreen = tk.Button(root, text="Clear Screen", padx=10, pady=5, fg="blue", command=clear) # bg='#263D42' BACKGROUND COLOUR DOESN"T WORK ON Mac
clearScreen.pack()

root.mainloop()