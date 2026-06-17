#  method 1 : add list using append        
a=int(input("a:"))  
res=[]
for i in range(a):
    res.append(int(input()))
print(res)


# method 2 : add list using append  
val=int(input("enter value:"))
empty=[0]*val
for i in range(val):
    empty[i]=int(input())
print(empty)