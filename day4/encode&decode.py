#coding: utf-8

L = '你好ab！'
with open('code.txt',mode='w',encoding='utf-8') as f:
    f.write(L)
f = open('code.txt')
print(f.read().encode('utf-8'))