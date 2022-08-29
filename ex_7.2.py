# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
ipos = None
value = 0
total = 0
for line in fh:
    line = line.rstrip()
    if not "X-DSPAM-Confidence:" in line:
        continue
    ipos = line.find(':')
    piece = line[ipos + 1:]
    value = float(piece)
    total = total + value
    count = count + 1
   # print(line)
print("Average spam confidence:", total/count)
