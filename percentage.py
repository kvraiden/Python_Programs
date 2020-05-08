n = int(input()) # How many students
student_marks = {} #Dictonary to save the name and marks
for _ in range(n): #for iteration of taking inputs
    name, *line = input().split() #Splitting inputs in name and marks
    scores = list(map(float, line)) #scores are the float ones
    scores = sum(scores) / 3    #finding average
    student_marks[name] = scores  #here name is the key to values of score
query_name = input()  #Taking name for whose average you want to see
print('%.2f' % student_marks[query_name]) #%.2f tells that only go 2 decimals after the integer part
#% student_marks[query_name] will give you the marks of entered query name (last marks that gets printed)
