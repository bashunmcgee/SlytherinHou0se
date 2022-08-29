

def computPay(hours, rate):
    print("Compute Pay: ", "Hours :", hours,"Pay :", rate )
    if hours > 40:
        reg = rate * hours
        overTimePay = (hours - 40.0) * (rate * 0.5)
        pay = reg  + overTimePay
    else:
        pay = hours* rate
        return pay
    return pay


#Gets Input
hrs = input("Enter Hours:")
rate = input("Enter Pay:")
#Converts input to float #s also could be a try before input
fr = float(rate)
fh = float(hrs)


xp = computPay(fh, fr)
print("Pay", xp)
