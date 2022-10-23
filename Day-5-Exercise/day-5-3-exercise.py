total = 0
for i in range(1, 101):
  if i % 2 == 0:
    total += i
print(total)

#   OR 

total1 = 0
for n in range(2, 101, 2):
  total1 += n
print(total1)
