goods =[{"name":"Computer", "price": 1999},{"name":"Cupcake", "price": 10},{"name":"Book", "price": 20},
{"name":"Iphone", "price": 998},]
x=0
salary=int(input("Please input your salary:"))
shoppingcart=[]

while True:
	print('-------------List of product---------------')
	for index,p in enumerate(goods):
		print(index,p.get("name"),p.get("price"))
		
	choice=input('Please input the product number：')
	if choice.isdigit():
		choice=int(choice)
		expect=goods[choice]
		if salary >= expect.get("price"):
			shoppingcart.append(goods[choice])
			print ("Added product %s into shoppingcart."%(expect.get("name")))
			salary = salary-expect.get("price")
			print ("Remaining Balance：%s"%(salary)) 
		else:
			print("Sorry, your remaining balance is not enough. Please select other products.")
			print ("Remaining Balance：%s"%(salary))
			
	elif choice== 'q':
		if shoppingcart==[]:
			pass
		else:
			print("You have purchased:")
			for index,p in enumerate(shoppingcart):
				print(index,p.get("name"),p.get("price"))
			
			
			print("Remaining Balance：%s"%(salary))
			
			
			
		break
	else:
		print("Invalid Input. Please try again.")
		


