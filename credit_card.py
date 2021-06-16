# Credit card validator
"""
enter 16 digit credit card number
algo_func
result
"""
def card_number():
    global cc_number
    print('\n'*25)
    print('\t>>> Credit Card validator <<<')
    while True:
        cc_number = input('\nPlease enter a 16 digit credit card number:  ')
        if cc_number.isdigit() and len(cc_number) ==16:
            break
        else:
            print('\n\t --- Enter numbers only (16 digits)\n')
            continue

def checksum():
    global total
    global last_digit
    global final_number
    if (total + last_digit) % 10 == 0:
        print('VALID card number!!')
        print(f'{final_number} IS a multiple of 10')
    else:
        print('INVALID card number, please check and try again')
        print(f'{final_number} IS NOT a multiple of 10')

cc_number_doubled = [] # a list of the doubles

# cc_number = '4578423013769219'

cc_number = ''

card_number()

print(f'original cc_number {type(cc_number)} {cc_number}')
cc_number_map = map(int, cc_number)
cc_number_list_int = list(cc_number_map)

print(f'original cc_number {type(cc_number_list_int)} {cc_number_list_int}')
last_digit = cc_number_list_int.pop(-1)
print(f'cc_number without last_digit ({last_digit}) {type(cc_number_list_int)} {cc_number_list_int}')

for x in cc_number_list_int[0:15:2]: # STARTING WITH first digit, multiply every second digit by 2
    cc_number_doubled.append(x*2)
del cc_number_list_int[0:15:2]
print(f'cc_number_doubled[0:15:2] {cc_number_doubled}')
print(f'del cc_number_list_int[0:15:2] {cc_number_list_int}')

for x in cc_number_doubled:
    if x < 10:
        cc_number_list_int.append(x)

temp_hold = []
for y in cc_number_doubled:
    if y > 9:
        temp_hold.append(y)
print(f'temp_hold {temp_hold}')
cc_number_doubled = temp_hold
print(f'cc_number_doubled {cc_number_doubled}')

print(f'del cc_number_list_int (single digits appended from cc_number_doubled) {cc_number_list_int}')
print(f'cc_number_doubled (single digits deleted) {cc_number_doubled}')

cc_number_doubled_map = map(str, cc_number_doubled)
cc_number_doubled_str = list(cc_number_doubled_map)
print(f'cc_number_doubled (list of strings {type(cc_number_doubled_str)} {cc_number_doubled_str}')

cc_number_sum_double = []

sum_of_digits = 0
n = 0 
while n < len(cc_number_doubled_str):
    for i in cc_number_doubled_str[n]:
        sum_of_digits += int(i)
    cc_number_sum_double.append(sum_of_digits)
    sum_of_digits = 0
    n += 1
print(cc_number_sum_double)

print(cc_number_list_int)
print(cc_number_sum_double)

total = sum(cc_number_list_int+cc_number_sum_double)
final_number = total + last_digit
print(f'Total ({total}) + check digit ({last_digit}) = {final_number}')

checksum()