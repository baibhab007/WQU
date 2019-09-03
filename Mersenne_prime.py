def ll_prime(p):
    i = 0
    num1 = 4
    while i <= p:
        num2 = ((num1 ** 2 - 2) % (2 ** p - 1))
        list1.append(num2)
        num1 = num2
        i+=1
        if i == p - 1:
            break
def ll_prime1(num):
    if list1[p-2] == 0:
        return True
    else:
        return False

list1 = []
p=17
p1=ll_prime(p)
m_number = [7, 31, 127, 2047, 8191, 131071, 524287, 8388607, 536870911, 2147483647, 137438953471, 2199023255551, 8796093022207, 140737488355327, 9007199254740991, 576460752303423487, 2305843009213693951]

for j in m_number:
    t = list((tuple(j))
    j+=1

print(t)

