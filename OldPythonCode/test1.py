a = [11,2,4,5,76]
'''
#make a list b which looks like [2,4,6,8,10]
#make a list c tht is [1,2,3,4,5,1,2,3,4,5]
#you have to use a
b=[1,2,3,4,5]


print(b)
c=(a+a)

print(c)


-------------------------------------------------------------------------------
'''
length=len(a)

b=[None] * length

#print(b)


for number in range(length):
    #print(a[number], number)
    #print (number)
    b[number]=a[number]*2

print (a)
print (b)


