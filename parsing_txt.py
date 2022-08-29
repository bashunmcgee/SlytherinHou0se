fname = input("Enter file name: ")
fh = open(fname)
count = 0
lst = list()
for line in fh:
    if not line.startswith('From'):
        continue
    words = line.split()
    if words[0] == 'From':
        email = words[1]
        print(email)
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
