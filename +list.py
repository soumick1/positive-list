n=int(input("enter the number of inputs in the list: "))
list1=[]
print("enter the list:")
for i in range(n):
    list1.append(int(input()))
list2=[]
for i in range(n):
    if(list1[i]>0):
        list2.append(list1[i])
print("The list of positive inputs are: ",list2)        
