try:
    a = int(input("Input: "))
    print("Output: juft" if a % 2 == 0 else "Output: toq")
except (ValueError, EOFError):
    print("Dasturga son kiriting!")
