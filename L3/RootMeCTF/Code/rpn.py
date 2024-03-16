import operator
from pwn import *

ops = { '+': operator.add,
        '-': operator.sub,
        'x': operator.mul
}

def eval_expression(tokens, stack):
    for token in tokens:
        if set(token).issubset(set("0123456789.")):
            stack.append(int(token))
        elif token in ops:
            if len(stack) < 2:
                raise ValueError('Must have at least two parameters to perform op')
            a = stack.pop()
            b = stack.pop()
            op = ops[token]
            stack.append(op(b,a))
    return stack

r = remote('ctf10k.root-me.org', 8002)
response = r.recv(2048)
correctResp = response.decode().replace("Can you solve this for me?\n", "")
correctResp = correctResp.split()
correctResp = correctResp[:-1]
correctResp = " ".join(correctResp)
# print (correctResp)
print(correctResp.split())

stack = []
stack = eval_expression(correctResp.split(), stack)

result = "".join(map(str,stack))
print(result.encode())

r.sendline(result.encode())

while True:
    resp = r.recv(2048)
    print(resp)
    resp = resp.decode().replace("That's correct!", " ")
    resp = resp.split()
    resp = resp[:-1]
    del resp[0]
    del resp[0]
    resp = " ".join(resp)
    print(resp)
    stack = []
    stack = eval_expression(resp.split(), stack)
    print(stack)
    res = "".join(map(str,stack))
    print(res)
    r.sendline(res.encode())

print("END\n")

