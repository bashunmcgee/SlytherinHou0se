name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
di = dict()
count = 0
for line in handle:
    if not line.startswith('From'):
        continue
    line.rstrip()
    words = line.split()
    if words[0] =='From:':
        continue
    #print(words)
    times = words[5]
    time = times.split(':')
    #print(time)
    hr = time[0]
    di[hr] = di.get(hr, 0) + 1
    print(hr)
    #print(di)
