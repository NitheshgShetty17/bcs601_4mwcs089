def find_hcf(a, b):
    steps = []
    while b != 0:
        steps.append(f"{a} % {b} = {a % b}")
        a, b = b, a % b
    return a, steps

def find_lcm(a, b, hcf_val):
    return (a * b) // hcf_val

def reverse_text(text):
    return "".join(reversed(text))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print("---- MINI PROJECT ----")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

hcf_val, steps = find_hcf(a, b)
lcm_val = find_lcm(a, b, hcf_val)

print("\nHCF Steps:")
for s in steps:
    print(s)

print("HCF:", hcf_val)
print("LCM:", lcm_val)

text = input("\nEnter a string: ")
print("Reversed:", reverse_text(text))

print("\nFactorials from 4 to 8:")
for i in range(4, 9):
    print(i, ":", factorial(i))