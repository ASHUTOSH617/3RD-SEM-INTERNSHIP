sentence = 'An abstract class provides default implementation'
arrlist = sentence.split()
biglen =0
for i in arrlist:
    if len(i) > biglen:
        biglen = len(i)
print(biglen)     
for i in range(0,biglen+4):
    print("*",end="")
print()       
for i in arrlist :
    print("* ",i.ljust(biglen)," *",sep="")
for i in range(0,biglen+4):
    print("*",end="")
print()           
    