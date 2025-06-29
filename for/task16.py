# n = (input("Berilgan n: "))
# l = list(n)
# a = 0

# for i in range(len(l)):
# 	son = int(l[i])
# 	a += son**len(l)
# 	print(a)

# if int(n) == a:
# 	print("Natija:", True)
# else:
# 	print("Natija:", False)

# =============================================================================

# n = input("Berilgan n: ")
# a = sum(int(digit) ** len(n) for digit in n)

# print("Natija:", int(n) == a)

# =============================================================================

n = input("Berilgan n: ")
print("Natija:", int(n) == sum(int(digit) ** len(n) for digit in n))
