try:
	c = input("Berilgan c: ")

	if c.isdigit() == True:
		print("Natija: son")
	elif c.isdigit() == False:
		print("Natija: alpha")
except EOFError:
	print("Dasturga son yoki xarf kiriting!")
