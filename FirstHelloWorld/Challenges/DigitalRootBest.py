def digital_root(n):
    if len(str(n)) == 1:
        return n
    else:
        nums = [int(x) for x in str(n)]
        sum = 0
        for x in nums:
            sum += x
        return digital_root(sum)

print(digital_root(1237))