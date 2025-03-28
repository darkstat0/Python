try:
    a = int(input("Input a: "))
    b = int(input("Input b: "))

    if a > b:
        print(f"katta son {a}")
    elif a < b:
        print(f"katta son {b}")
    else:
        print("Voy ular teng")
except ValueError:
    print("Dasturga son kiriting!")
