a = int(input("Berilgan a: "))
n = int(input("Berilgan n: "))
son = 0
num_str = ""
parts = []

for i in range(son, n):
	num_str += str(a)
	parts.append(num_str)
	son += int(num_str)

expression = " + ".join(parts)

print("Natija:", expression + " =", son)
