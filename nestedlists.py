#print(grocerylist)
#grocerylist= [['Bpple','23'],['Anana','23']] This is practice .
#print(grocerylist)
#grocerylist.sort()

#Real program starts here.
marksheet = []
score_list = []
for _ in range(int(input())):
    name = input()
    marks = float(input())
    marksheet.append([name,marks])
    score_list.append(marks)
sec_low_marks = sorted(list(dict.fromkeys(score_list)))[1]
for name,marks in sorted(marksheet):
    if marks == sec_low_marks:
        print(name)

