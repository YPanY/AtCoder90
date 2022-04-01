from itertools import product

n = int(input())

if n % 2 != 0:
    print('')
    exit()

valid = True
ans = []
for i, bit in enumerate(product([0, 1], repeat=n)):
    # only when count(1) = count(0)
    if bit.count(0) == n / 2:
        brackets = ''
        valid = True
        left = right = 0
        for b in list(bit):
            if b == 0:
                brackets += str(b)
                left += 1
            else:
                right += 1
                brackets += str(b)
                if right > left:
                    valid = False
                    continue
        if left != right: valid = False
        if valid:
            brackets = brackets.replace('0', '(')
            brackets = brackets.replace('1', ')')
            ans.append(brackets)

print(*ans, sep='\n')