from itertools import product

n = int(input())
bit_map = list(product([0, 1], repeat=n))

if n % 2 != 0:
    print('')
    exit()

valid = True
ans = []
for i, bit in enumerate(bit_map):
    valid = True
    left = right = 0
    for b in list(bit):
        if b == 0:
            left += 1
        else:
            right += 1
            if right > left:
                valid = False
                continue
    if left != right: valid = False
    if valid:
        bit_str = ''.join([str(b) for b in bit])
        bit_str = bit_str.replace('0', '(')
        bit_str = bit_str.replace('1', ')')
        ans.append(bit_str)

print(*ans, sep='\n')