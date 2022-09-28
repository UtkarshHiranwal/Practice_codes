s= [345, 604, 321, 433, 704, 470, 808, 718, 517, 811]
r= [[300, 380], [400, 700]]
l=0
a=[]
print(r[0])
for j in r:
    for i in s:
        if i >j[0] and i<=j[1]:
            l=l+1
    a.append(l)
print(a)





