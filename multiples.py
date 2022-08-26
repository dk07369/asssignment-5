n=int(input("Enter a number:"))
for i in range(0,n+1):
    if(i%6==0):
        continue
    Sum = sum+i
    print(int(sum))

print(sum)