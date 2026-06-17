start=int(input("a:"))
stop=int(input("b:"))
for i in range(start,stop):
      print(*range(start,(stop-i+1)),sep="*")