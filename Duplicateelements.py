# find first duplicate 1
# list=[3,6,7,7,8,4]
# res=[]
# for i in list:
#     if list.count(i)>1:
#         res.append(i)
#         break
# print(res)

# find first duplicate 2
# List=[7,8,9,2,4,3,1,2,3,4,4,4,1]
# for i in List:
#     if List.count(i)>1:
#         print(i)
#         break
# method 3
list=[3,3,6,7,7,8,4] 
l=len(list)
x=0
for i in range (l):
   for j in range(i+1,l):
      if(list[i]==list[j]):
         print(list[i])
         x=1
         break
   if x:
      break