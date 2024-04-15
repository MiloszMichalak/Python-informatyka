def QuickPotega(a, n): # 2^8 = 4^4 = 8^2. Podstawa ^2, wykladnik / 2
    w = 1
    while n > 0:
        if n % 2 == 1:
            w *= a
            n -= 1
        a *= a
        n //= 2
    return w


print(QuickPotega(2, 8))
