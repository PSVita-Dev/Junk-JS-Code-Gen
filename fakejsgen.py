import string
import random

functions = [
"random();",
"getDate();",
'concat("secret","algo");'
]

def gen_code(lines):
    for i in range(int(lines)):
        fun = str(random.choice(string.ascii_uppercase))
        for a in range(6):
             fun += random.choice(string.ascii_lowercase) 
        index = random.randint(0,2)
        fun += "algo_part"+str(index)
        print("function "+fun+"() {")
        print("var "+fun+"='"+fun+"';")
        print(fun+"+'"+fun+"';")
        print(functions[index])
        print("console.log('"+fun+"');")
        print("}")
if __name__ == "__main__":
    lines = input("How many functions to generate?")
    gen_code(lines)
