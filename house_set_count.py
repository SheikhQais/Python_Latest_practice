def count_pythagorean_triplets(n):
    count = 0

    for a in range(1, n):
        for b in range(a + 1, n):
            c_squared = a**2 + b**2
            c = int(c_squared**0.5)
            if c <= n and c > b and c * c == c_squared:
                count += 1
                print(a,b,c)

    return count

# Input
N = 20
print(count_pythagorean_triplets(N))