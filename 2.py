def rep(x):
    size=len(x)
    repe=[]
    for i in range(size):
        for j in range(i+1,size):
            if x[i]==x[j] and x[i] not in repe:
               repe.append(x[i])
               
    return repe
        
listA=[1,3,4,5,6,3,5,4,5,2,3,2,4,5]
print(rep(listA))
        













