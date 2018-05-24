L=[56,69,80,46,98]
l=[]
i=[]
# for x in range(len(L)):
#     if L[x]<60:
#         l.append(L[x])
for x in L:
    if x<60:
        l.append(x) 
    else:
        i.append(x)
L=i
print(l,'\n',L)
