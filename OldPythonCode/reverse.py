'''
a=["a","b","c","d","100","jjj"]
print(a)



b[0]=a[4]
b[1]=a[3]
b[2]=a[2]
b[3]=a[1]
b[4]=a[0]
'''
def rinurev(a):
    size = len(a)
    b=[None] *size
    for i in range(size):
        idx = size-(i+1)
        #print (i, idx)
        b[i] = a[idx]

    return b

'''
c=list(reversed(a))

c.append("rinu")
c.append(a)

print(c)
'''

