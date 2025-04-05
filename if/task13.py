id = int(input("Berilgan son: "))

data = {1: "Dushanba", 2: "Seshanba", 3: "Chorshanba", 4: "Payshanba", 5: "Juma", 6: "Shanba", 7: "Yakshanba"}

if id:
	print("Natija:", data[id])
else:
	print('none')
