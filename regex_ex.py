import re
sum = 0
name = input('Enter File Name')
if len(name) < 1:
    name = 'regex_sum_42.txt'
handle = open(name)
for line in handle:
    line.rstrip()
    num = re.findall('[0-9]+', line)
    if len(num) < 1:
        continue
    for n in num:
        n = int(n)
        sum = sum + n
        #print(n)
print("Total : ",sum)

    #words = line.split()
    #for word in words:
        #x = re.findall('[0-9]', word)
        #print(x)
