"""
Credit card number validator
Enter 16 digit credit card number
Algo
Result
"""

class CardNumber():
    def __init__(self):
        self.cc_number = ''

    def request_number(self):
        print('\n'*25)
        print('\t>>> Credit Card validator <<<')
        while True:
            self.cc_number = input('\nPlease enter a 16 digit credit card number:  ')
            if self.cc_number.isdigit() and len(self.cc_number) == 16:
                calc_process.run_calc()
                break
            else:
                print('\n\tTry again, numbers only (16 digits)\n')
                continue

    def __str__(self):
        return f'Entered Credit Card number: {self.cc_number}'

class Algo():
    def __init__(self):
        pass

    def run_calc(self):
        self.cc_number_doubled = [] # list of the doubles

        # print(f'original cc_number {type(card_num.cc_number)} {card_num.cc_number}')
        self.cc_number_map = map(int, card_num.cc_number)
        self.cc_number_list_int = list(self.cc_number_map)

        # print(f'original cc_number {type(self.cc_number_list_int)} {self.cc_number_list_int}')
        self.last_digit = self.cc_number_list_int.pop(-1)
        # print(f'cc_number without last_digit ({self.last_digit}) {type(self.cc_number_list_int)} {self.cc_number_list_int}')
        self.cc_number_list_int_fixed = []
        for x in self.cc_number_list_int:
            self.cc_number_list_int_fixed.append(x)
        # print(f'self.cc_number_list_int_fixed {self.cc_number_list_int_fixed}')

        for x in self.cc_number_list_int[0:15:2]: # STARTING WITH first digit, multiply every second digit by 2
            self.cc_number_doubled.append(x*2)
        del self.cc_number_list_int[0:15:2]
        # print(f'cc_number_doubled[0:15:2] {self.cc_number_doubled}')
        # print(f'del cc_number_list_int[0:15:2] resulting in {self.cc_number_list_int}')

        self.cc_number_doubled_fixed = []
        for i in self.cc_number_doubled:
            self.cc_number_doubled_fixed.append(i)

        for x in self.cc_number_doubled:
            if x < 10:
                self.cc_number_list_int.append(x)

        self.temp_hold = []
        for y in self.cc_number_doubled:
            if y > 9:
                self.temp_hold.append(y)
        # print(f'temp_hold {self.temp_hold}')
        self.cc_number_doubled = self.temp_hold
        # print(f'cc_number_doubled {self.cc_number_doubled}')

        # print(f'del cc_number_list_int (single digits appended from cc_number_doubled) {self.cc_number_list_int}')
        # print(f'cc_number_doubled (single digits deleted) {self.cc_number_doubled}')

        self.cc_number_doubled_map = map(str, self.cc_number_doubled)
        self.cc_number_doubled_str = list(self.cc_number_doubled_map)
        # print(f'cc_number_doubled (list of strings {type(self.cc_number_doubled_str)} {self.cc_number_doubled_str}')

        self.cc_number_sum_double = []

        self.sum_of_digits = 0
        self.n = 0 
        while self.n < len(self.cc_number_doubled_str):
            for i in self.cc_number_doubled_str[self.n]:
                self.sum_of_digits += int(i)
            self.cc_number_sum_double.append(self.sum_of_digits)
            self.sum_of_digits = 0
            self.n += 1
        # print(self.cc_number_sum_double)
        # print(self.cc_number_list_int)

        self.total = sum(self.cc_number_list_int+self.cc_number_sum_double)
        self.final_number = self.total + self.last_digit
        # print(f'These ({self.cc_number_list_int}) + these ({self.cc_number_sum_double}) = {self.total}')
        # print(f'Total ({self.total}) + last digit ({self.last_digit}) = {self.final_number}')

        check_now.check()

    def __str__(self):
        pass

class CheckSum():
    def __init__(self):
        pass

    def check(self):
        if (calc_process.total + calc_process.last_digit) % 10 == 0:
            print('\n\tVALID card number!!')
            # print(f'{calc_process.final_number} IS a multiple of 10')
            workings.show_results()
        else:
            print('\n\tINVALID card number, please check and try again')
            # print(f'{calc_process.final_number} IS NOT a multiple of 10')
            workings.show_results()

    def __str__(self):
        pass

class Results():
    def __init__(self):
        pass

    def show_results(self):
        self.user_input = input('\nShow calculations? y/n  :')
        while True:
            try:
                if self.user_input[0].lower() == 'y':
                    self.show_calc()
                    break
                elif self.user_input[0].lower() == 'n':
                    print('\n\tThanks for enjoying the program! bye for now\n')
                    break
            except:
                print('invalid option, try again')
                continue

    def show_calc(self):
        print(f'\nCard number: {card_num.cc_number}')
        print(f'Last digit ({calc_process.last_digit})')
        print(f'Card number without last digit {calc_process.cc_number_list_int_fixed}')
        print(f'First digit and every second digit multiplied by 2 {calc_process.cc_number_doubled_fixed}')
        print(f'Double digit numbers {calc_process.temp_hold} digits added together resulting in {calc_process.cc_number_sum_double}')
        print(f'These ({calc_process.cc_number_list_int}) + these ({calc_process.cc_number_sum_double}) = {calc_process.total}')
        print(f'({calc_process.total}) + last digit ({calc_process.last_digit}) = {calc_process.final_number}')
        print(f'\n\tFinal number ({calc_process.final_number})')
        print('\nFinal number must be a multiple of 10 to pass validation\n')


    def __str__(self):
        pass

# 4578423013769219 # example

card_num = CardNumber()
calc_process = Algo()
check_now = CheckSum()
workings = Results()
card_num.request_number()