x=5
if(x== 5):
    print("this X value is ",x)

#Code will evaluate smallest iteration
smallest = None
print("Before:", smallest)
for iteration in [10, 41, 12, 9, 74, 15]:
    if smallest is None or iteration < smallest:
        smallest = iteration
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)
print("Hello")
print(int(98.6))
