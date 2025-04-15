a = int(input("Berilgan a: "))
b = int(input("Berilgan b: "))
c = int(input("Berilgan c: "))

if a and b % 2 == 0:
	print("Natija: 1")
elif b and c % 2 == 0:
	print("Natija: 1")
elif a and c % 2 == 0:
	print("Natija: 1")
elif a and b % 2 == 1:	
	print("Natija: 2")
elif b and c % 2 == 1:
	print("Natija: 2")
elif a and c % 2 == 1:
	print("Natija: 2")
else:
	print("Natija: 0")
