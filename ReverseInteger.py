def reverse(x):
    org = x
    rev = 0
    prev_rev_num = 0
    if org < 0:
        org = abs(org)

    while org != 0:
        sum = org % 10
        rev = rev * 10 + sum

        if rev >= 2147483647 or rev <= -2147483648:
            rev = 0
        if (rev - sum) // 10 != prev_rev_num:
            return 0
        prev_rev_num = rev
        org = org // 10

    if x < 0:
        return rev * -1
    else:
        return rev


x = 123
print(reverse(x))
