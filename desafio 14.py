print("Loop with break: ")
for num in range(1,11):
    if num > 5:
        break
    print(num)

print("Loop whit continue: ")
for num in range(1,11):
    if num == 5:
        continue
    print(num)