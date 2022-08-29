
for line in handle:
    line.rstrip()
    words = line.split()
    for w in words:
        di[w] = di.get(w, 0) + 1
    largest = -1
    theWord = None

for k,v in di.items():
    if v > largest:
        largest = v
        theWord = k
print(k,v)
