#This program demonstrates mergesort without using any python function
N = int(input("Enter how many elements do you want : "))
L = []
sortedL1 = []
sortedL2 = []
for _ in range(N):
    ele = int(input())
    L.append(ele)
print("This is the array you entered: "+str(L))
L1 = L[0:len(L)//2]
L2 = L[len(L)//2:]
print("This is L1:" +str(L1))
print("This is L2:" +str(L2))
def sorting(L1,L2):
    for i in L1:
        if L1[0]>L1[1]:
            sortedL1.append(L1[1])
        else:
            sortedL1.append(L1[0])

    for j in L2:
        if L2[0]>L2[1]:
            sortedL2.append(L2[1])
        else:
            sortedL2.append(L1[0])

sorting(L1,L2)

print(sortedL1)
print(sortedL2)