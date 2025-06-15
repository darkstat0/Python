a = int(input("Berilgan a: "))
b = int(input("Berilgan b: "))

son = 0

for i in range(a, b+1):
	if i > 0:
		son += 1

print("Natija:", son)
