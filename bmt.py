# find the smallest number with a digit sum of n
def lowest_digsum(n):
    lead = n % 9
    tail = n // 9
    if lead == 0:
        return 10 ** tail - 1
    if tail == 0:
        return lead
    return (lead+1) * 10**tail -1

# find the smallest number x such that digitsum(x) and digitsum(x+1) are multiples of n
def bmt(n):
    if n % 3 == 0:
        return -1
    start = lowest_digsum(n)
    nines = pow(9, -1, n)
    if nines > 0:
        return start * 10**nines - 1
    return start

# code golf version for OEIS
def bmt_golf(n):
    return (((n%9)+1)*10**(n//9)-1)*(10**pow(9,-1,n))-1 if n%3 > 0 else -1


# check against known values
def test():
    test = [1, 19, -1, 39, 49999, -1, 69999, 79, -1, 18999999999, 2899999, -1, 48999, 5899999999999, -1, 78999999999, 8899, -1, 19899999999999999999, 298999999999, -1, 49899999, 598999999999999999999, -1, 79899999999999999, 898999, -1, 19989999999999999999999999999, 29989999999999999, -1]
    for i in range(1,30):
        print ( f"{i:3d} {bmt(i):30d} {test[i-1]:30d} {bmt(i) == test[i-1]}")

if __name__ == "__main__":
    for i in range(100):
        print(f"{i:4d}  {bmt(i)}" )
