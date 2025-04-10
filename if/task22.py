try:
	a = int(input("Berilgan a: "))
	b = int(input("Berilgan b: "))

	if a > b:
		print(a-b)
	elif a < b:
		print(b-a)
	else:
		print(0)
except Exception as e:
	print("Xatolik:", e)
