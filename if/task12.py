try:
	c = input("Berilgan c: ")

	if c.isupper():
		print("lowerCase")
	elif c.islower():
		print("upperCase")
	elif c.isdigit():
		print("none")
	else:
		print("Dasturga son yoki xarf kiriting!")
except Exception as e:
	print(e)
