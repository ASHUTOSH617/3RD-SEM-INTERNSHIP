## add all numbers which divisible by 5  in between 115 through 175
n=110
s=0
for i in range(0,13):
     n=n+5
     if n!=180:
         s=s+n
     else :
         exit
print(s)         
