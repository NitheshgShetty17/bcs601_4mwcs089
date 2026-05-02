from flask import Flask

app = Flask(__name__)

def find_hcf(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_lcm(a, b, hcf_val):
    return (a * b) // hcf_val

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

@app.route('/')
def home():
    a = 18
    b = 12

    hcf_val = find_hcf(a, b)
    lcm_val = find_lcm(a, b, hcf_val)

    result = ""
    result += f"HCF: {hcf_val}<br>"
    result += f"LCM: {lcm_val}<br><br>"

    text = "Fun with Programming"
    result += f"Reversed: {text[::-1]}<br><br>"

    result += "Factorials:<br>"
    for i in range(4, 9):
        result += f"{i} : {factorial(i)}<br>"

    return result

app.run(host='0.0.0.0', port=10000)
