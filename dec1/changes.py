

number_list = []

f = open("input.txt", "r")
for line in f:
    number_list.append(int(line.strip('\n')))

increase = 0
decrease = 0

for i in range(1, len(number_list)):
    if number_list[i - 1] < number_list[i]:
        increase = increase + 1
    else:
        decrease = decrease + 1

print("The number of increases is", increase)

sum_increase = 0

for x in range(len(number_list)):

    if sum(number_list[x:x+3]) < sum(number_list[x+1:x+4]):
        sum_increase+=1

print("sum increases is ", sum_increase)
    
