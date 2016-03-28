def fact(mul, num):
    if num <= 1:
        return mul
    else:
        mul = mul * num
        return fact(mul, num-1)
    


n=5
sum=1
for i in range(1,n+1):
	sum=sum*i
print(sum)


print("p:", fact(1, n))
