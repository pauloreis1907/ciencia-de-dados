a = 2
b = 3
c = 5
d = 9
#primeira condicao
print('primeira condiçao')
if not (d > 5):
    print ((a+b)*d)
else:
    print (((a-b)/c))
    
#Segunda condicao  
print('Segunda condiçao')
if (a > 2) and (b < 7 ):
   print((a+b)*(b - 2)) 
else:
    print((a+b)/d *(c + d))
 
 
#Terceira condicao
print('Terceira condiçao')
if (a == 2) or (b < 7):
    print((a+2)*(b-2))
else:
    print((a + b)/d * (c + d))