list = []
answer = []
number_to_sum_to = 2020
number1 = 0
number2 = 1

with open(r'C:\Users\Gino\Documents\Python Materials\day1-1.txt') as f:
    listtxt = f.read().splitlines()




for text in listtxt:
    number = int(text)
    list.append(number)
    
print(list)

for i in list:
    for j in list:
        if i + j == number_to_sum_to:
            number1 = i
            number2 = j

        


new_answer = number1 * number2
print(new_answer)