import time
v=[]
primi=[True]*100000
t=time.time()
for i in range(2,100000):
    if primi[i]:
        v.append(i)
        for j in range(2*i,100000,i):
            primi[j]=False     
print(v)
print(time.time()-t)
