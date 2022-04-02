count = 0
while count <= 0:
    count = int(input("Введите большое число: "))

max_count = count % 10
count = count // 10

while count > 0:
    next_count = count % 10
    count = count // 10
    if max_count < next_count:
        max_count = next_count

print(max_count)
