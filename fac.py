rest = float()
cont = 0
while True :
     x = float(input("digite um numero\n"))
     if (x ==0):
         break
     cont  += 1
     rest  += x 
print(rest/cont)
