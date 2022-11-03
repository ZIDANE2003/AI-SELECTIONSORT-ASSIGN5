stud=[]
n=int(input("Enter no of students in class:")) 
for i in range(n):
  num=float(input("Enter percentage of students:"))
  stud.append(num)
print("List of percentage of Students:",stud,end=" ")
def SelectionSort(stud,n):
  for i in range(n):
    Minimum = i
    for j in range(i+1,n):
      if(stud[j]<stud[Minimum]):
        Minimum = j
    temp=stud[i]
    stud[i]=stud[Minimum]
    stud[Minimum]=temp
SelectionSort(stud,n)  
print("\n Top five scores are")    
print(stud)        


