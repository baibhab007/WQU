def lucas_lehmer(p):
    i = 0
    num1 = 4
    while i<=p:
        num2 = ((num1**2 - 2)%(2**p - 1))
        list1.append(num2)
        num1 = num2
        i+=1
        if i == p-1:
            break
list1 = []

l1 = lucas_lehmer(17)
ll_result = list1 #[4] * 16

print(ll_result)
