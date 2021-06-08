########################### BUBBLE SORT #################
print("------------------------BUBBLE SORT:-----------------------\n")
num=[6,8,3,4,9,5,2]

def bubbleSort(num):
    i=0
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j] > num[j+1]:
                temp=num[j]
                num[j]=num[j+1]
                num[j+1]=temp
                print(num)


bubbleSort(num)
print("\nFinal Output of BUBBLE SORT:\n")
print(num)



########################## selection sort ##########################
print("\n---------------------SELECTION SORT:----------------------------\n")
num=[6,8,3,4,9,5,2]

def selectionSort(num):
    for i in range(len(num)-1):
        minPos = i
        for j in range(i,len(num)):
            if num[j]<num[minPos]:
                minPos=j

        temp=num[i]
        num[i]=num[minPos]
        num[minPos]=temp
        print(num)

selectionSort(num)
print("\nFinal output of selection sort:\n" , num)

######################### Linear Search ######################
print("-------------------Linear Search:----------------")

num=[6,8,3,4,9,5,2]
pos=-1
def linearSearch(num,n):

    for i in range(len(num)):
        if num[i]==n:
            globals()['pos'] = i+1
            return True
    else:
        return False

n=int(input("please enter the element to be searched for:\n"))

if linearSearch(num,n):
    print("element found at position:" , pos)
else:
    print("element not found in list")

print(num)



############################## Binary Search ###########################

print("\n----------------------BINARY SEARCH:-----------------------------------\n")
num=[6,8,3,4,9,5,2]

sortedNumbers=sorted(num)
print('sortedNumbers', sortedNumbers)
pos=-1
def binarySearch(sortedNumbers,n):
    l=0
    u=len(sortedNumbers)
    while l <= u:
        mid = (l + u) // 2
        if n==sortedNumbers[mid]:
            globals()['pos']=mid+1
            return True
        else:
            if sortedNumbers[mid]<n:
                l=mid
            else:
                u=mid


n = int(input("please enter the element to be searched for:\n"))
if binarySearch(sortedNumbers,n):
    print("element found at position:\n",pos)
else:
    print("element not found")
