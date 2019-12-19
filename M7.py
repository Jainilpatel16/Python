55bestRecords = open("bestRecords.txt", 'r')
cushingRecords = open("cushingRecords.txt", 'r')
apgarRecords = open("apgarRecords.txt", "w")

bR = []
cR = []

for line in bestRecords:
    bLine = line.rstrip().split(', ')
    if len(bLine) > 1:
        bR.append(bLine)

for row in cushingRecords:
    cRow = row.rstrip().split(', ')
    if len(cRow) > 1:
        cR.append(cRow)

b = 0
c = 0 

aR = []

while b < len(bR) and c < len(cR):
    if bR[b] [0] <= cR[c] [0]:
        aR.append(bR[b])
        b += 1
    else:
        aR.append(cR[c])
        c += 1

while b < len(bR):
    aR.append(bR[b])
    b += 1
while c < len(cR):
    aR.append(cR[c])
    c += 1
for r in aR:
    print (", ".join(r))
    apgarRecords.write(", ".join(r) +"\n")

bestRecords.close()
cushingRecords.close()
apgarRecords.close()
