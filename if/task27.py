a = int(input("Berilgan a: "))
b = int(input("Berilgan b: "))
c = int(input("Berilgan c: "))

if a % 2 == 0:
	if b % 2 == 0:
		if c % 2 == 0:
			print("Natija: 1")
	elif b % 2 == 1:
		pass
	elif c % 2 == 1:
		print("Natija: ")
	elif c % 2 == 0:
		print("Natija: ")
elif a % 2 == 1:
	if b % 2 == 0:
		if c % 2 == 0:
			print("Natija: 2")
	elif b % 2 == 1:
		print("Natija: ")
	elif c % 2 == 1:
		print("Natija: ")
	elif c % 2 == 0:
		print("Natija: ")
elif b % 2 == 0:
	if c % 2 == 0:
		print("Natija: 3")
	elif c % 2 == 1:
		pass
elif b % 2 == 1:
	if c % 2 == 0:
		print("Natija: ")
	elif c % 2 == 1:
		print("Natija: ")
elif c % 2 == 0:
	print("Natija: ")
elif c % 2 == 1:
	print("Natija: ")
else:
	print("Natija: 0")
