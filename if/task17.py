try:
	a = int(input("Berilgan a: "))
	b = int(input("Berilgan b: "))
	c = int(input("Berilgan c: "))

	if a > 0 and b > 0 and c > 0:
		print("Natija: 3")
	elif a > 0 and b < 0 and c < 0:
		print("Natija: 2")
	elif a < 0 and b < 0 and c > 0:
		print("Natija: 2")
	elif a < 0 and b > 0 and c < 0:
		print("Natija: 2")
except Exception as e:
	print("Error:", e)
