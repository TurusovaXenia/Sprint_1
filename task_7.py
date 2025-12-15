def digit_root(num):
    sum = 0
    for digit in str(num):
        sum += int(digit) % 10
        num //= 10
    if sum < 10:
        return sum
    else:
        return digit_root(sum)

root = digit_root(889987)
print(root)
