a = int(input("Berilgan a: "))
son = 0

for i in range(1, a):
	if a%i == 0:
		son += i

if son == a:
	print("Natija:", True)
else:
	print("Natija:", False)
