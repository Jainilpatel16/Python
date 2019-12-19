StudentName = input("Name")
print(StudentName)

GradeList = []
 
for x in range (0,10):
    StudentInput = input("enter your quiz grade")
    GradeList.append(StudentInput)
SortedList = sorted(GradeList, key=float, reverse=True)

for x in range (0,6):
    print(SortedList[x])

