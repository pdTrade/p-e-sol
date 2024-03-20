numbers_square = [n**2 for n in range(100+1)]
numbers = [n for n in range (100+1)]
x = sum(numbers_square)
y = sum(numbers)**2

res = y - x

print(res)
