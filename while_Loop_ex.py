num = 0
total = 0.0
while True:
    sval = input('Enter a number')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print("Inavlid input")
        continue
    num = num + 1
    total = total + fval
print('Total:',total ,' Number:', num, ' Average: ', total/num)
