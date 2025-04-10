a = int(input("Berilgan a: "))
b = int(input("Berilgan b: "))
c = int(input("Berilgan c: "))

if a % 2 == 1 and b % 2 == 1 and c % 2 == 1:
    print("Natija:", 1)
elif a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    print("Natija:", 2)
elif (
    (a % 2 == 0 and b % 2 == 1 and c % 2 == 1)
    or (a % 2 == 1 and b % 2 == 0 and c % 2 == 1)
    or (a % 2 == 0 and b % 2 == 1 and c % 2 == 0)
    or (a % 2 == 1 and b % 2 == 1 and c % 2 == 0)
):
    print("Natija:", 3)
else:
    print("Natija:", 0)
