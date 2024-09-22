
def  listmodification(list):
 for i in range(len(list)):
     list[i]=list[i]+10

list=[1,2,3,4]

print("Print list without modification")
for i in range(len(list)):
	print(list[i])

listmodification(list )
print("Print list after  modification")	
	
for i in range(len(list)):
  print(list[i])	
print("Print the first element of the list before  modification")

print (list[0])
list[0]+=100
print("Print the first element of the list after   modification")

print (list[0])


 
	 
	 

	 
	 
	 
	 
