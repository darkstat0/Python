a = int(input("Berilgan a: "))
b = int(input("Berilgan b: "))
son = []

for i in range(a, b):
	son.append(i)
	result = sum(son)

print("Natija:", result)
