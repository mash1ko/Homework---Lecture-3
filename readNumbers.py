
file = open("data.text", "r")
data = [int(numbers) for numbers in file.readlines()]
max_num = max(data)

file = open("data.text", "w")
file.write(str(max_num))

print(max_num)


