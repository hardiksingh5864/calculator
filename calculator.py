def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operation = { "+":add,  "-":sub, "*":mul,  "/":div}

num1 = int(input("Enter a  number"))
num2 = int(input("Enter another number"))
for symbol in operation:
 print(symbol)    
operation_symbol = input("enter a operation")
calculation = operation[operation_symbol]
answer = calculation(num1,num2)
print(answer)