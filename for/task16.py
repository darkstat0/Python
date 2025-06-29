n = (input("Berilgan n: "))
l = list(n)
a = 0

for i in range(len(l)):
	son = int(l[i])
	a += son**len(l)
	print(a)

if int(n) == a:
	print("Natija:", True)
else:
	print("Natija:", False)
