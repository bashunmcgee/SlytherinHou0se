largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        ival = int(num)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest = ival
    if largest < ival:
        largest = ival
    if smallest is None:
        smallest = ival
    if smallest > ival:
        smallest = ival
print("Maximum is", largest)
print("Minimum is", smallest)
