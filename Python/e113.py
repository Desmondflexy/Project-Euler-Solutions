def bouncy(num):
    a = [int(i) for i in str(num)]
    if(all(a[i] >= a[i+1] for i in range(len(a)-1))
       or all(a[i] <= a[i+1] for i in range(len(a)-1))):
        return False
    else: return True

count = 0
for i in range(1,1000000):
    if not bouncy(i): count += 1
print(count)
