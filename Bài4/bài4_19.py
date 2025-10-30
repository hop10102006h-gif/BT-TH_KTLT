# Dương Phúc Hợp msv: 245752021610047
def isprime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5 + 1)):
        if x % i == 0:
            return False
    return True
p = tuple(i for i in range(2, 1_000_000) if isprime(i)) 
print('tuple P gồm các số nhỏ hơn 1 triệu.')
print('Ví dụ 10 số đầu tiên.', p[:10])