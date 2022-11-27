f = open("data_for_set.text", "r")
data = {int(numbers) for numbers in f.readlines()}
print(data)


