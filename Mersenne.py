def mersenne_numbers(p):
    for k in p:
        a = 2**k - 1
        another_list.append(a)
    return another_list

def is_prime(x):
    if x < 2:
        return False
    else:
        if x == 2:
            return True
        else:
            for i in range(2, x):
                if x % i == 0:
                    return False
            return True


def get_primes(n_start, n_end):
    rng = range(n_start, n_end + 1)
    my_list = [num for num in rng if is_prime(num)]
    return my_list

another_list = []
my_list = []
mersennes = get_primes(3,65) #[7] * 17
m_number = mersenne_numbers(mersennes)

print(m_number)
