c = int(input("buyincost="))
r = int(input("sellprice="))
N = int(input("maybenum="))
s = int(input("Residual="))
j=0
proportion=[0] * (N+1)
max = 0
maxi=-1
u=0
while j<N+1:
   proportion[j] = float(input("proportion"+str(j)+"="))
   j=j+1
i=0
expectreturn = 0
x=0

for q in range(0, N+1):
    if q == 0:
        expectreturn = 0
        print(q,int(expectreturn))
    else :
        for p in range(0, q):
            expectreturn = expectreturn + (x*r-q*c)*proportion[i]
            u = u + proportion[i]
            if q > x :
                expectreturn = expectreturn + s * (q - x) * proportion[i]
            x = x+1
            i = i+1

        expectreturn = expectreturn + q*(r-c)*(1-u)
        if max < expectreturn:
            max = expectreturn
            maxi = q

    i=0
    x=0
    expectreturn=0
    u=0
print(maxi, int(max))
