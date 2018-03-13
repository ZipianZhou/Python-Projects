l=[["USER1","ASD123",0],["USER2","QWE123",0],["USER3","ZXC123",0]]
time=0
count=0
x=1
while time < 3 :
	unit='True'
	a=0
	username=input('ENTER USERNAME：')
	password=input('ENTER PASSWORD：')		
	while a < len(l)-1:
		if l[a][2]>=3:
			print("You account has been locked.")
			time=3
			break
		elif username==l[a][0] and password==l[a][1]:
			print ("welcome, %s"%(username))
			unit='False'
			time=3
			break
		elif username==l[a][0] and password!=l[a][1]:
			l[a][2]=x
			x+=1
			print(l[a])
			a+=1
		else:
			a+=1
	time+=1
	if unit=='True':
		print("WRONG PASSWORD OR USERNAME TRY AGAIN。")
			
