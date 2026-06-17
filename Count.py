List=[2,4,3,1,2,3,4,4,4,1]
count=0
a=int(input("enter number:"))

for i in List:
    if i == a:
        count=count+1
    
print(count)     
# inbuild function           
print(List.count(a))