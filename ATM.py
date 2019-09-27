print("wel come NARAS bank:")
restart=("yes")
chances= 3
balance=100000000
while chances >= 0:
	pin=int(input("please enter the 4 digits pin:"))
	if pin == (1432): 
		print("you entered pin is correct:")
		while restart not in ("n","no"):
			print("prlease press 1 for your balance\n:")
			print("please press 2 for your withdrawl\n:")
			print("please press 3 for your pay in\n:")
			print("please press 4 for your return card\n:")
			option=int(input("what would u like to choose\n:"))
			if option == 1: 
				print("your balance is ae",balance,"\n")
				restart=input("would u like to go back ?")
				if restart in ("n","no"):
					print(" thak you")
					break
			elif option ==2:
				option= ("yes")
				withdrawl =float(input("how much money do u want to with drawl:"))
				if withdrawl in [500,1000,50000,100000,100000]:

					balance=balance-withdrawl
					print("ur balance now in ac",balance)
					restart =input("would u like to go back ?")
					if restart in ("n","no"):
						print("thank you")
						break
				elif  withdrawl != [500,1000,50000,100000,10000000]:
					print("invalid amount entered ")
					restart =("yes")
				elif withdrawl == 1:
					withdrawl =float(input("please enter desired amount")) 
			elif option ==3:
				pay_in =float(input("how much amount would u like it ?"))
				balance = balance + pay_in
				print("your balance in ac ",balance)
				restart =input("would you like to go back ?")
				if restart in ("n","no"):
					print("thank you")
			elif option == 4:
				print("please wait ur card is returned...\n")
				print("thanlk you:")
				break
			else :
				print("please enter a correct number:")
				restart=("yes")
	elif pin != ("1234"):
		print("incorrect password")
		chances=chances-1
		if chances==0:
			print("today limits is cross:")
			break






		
