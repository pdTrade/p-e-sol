for a in range(1, 1000):
  for b in range(a, 1000 - a):
    c = 1000 - a - b
    if a * a + b * b == c * c:
        res = a * b * c
        break

print(res)
