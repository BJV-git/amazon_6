# logs=["t kvr", "r 3 1", "i 403", "7 so", "t 54"]
#
# ll = len(logs)
# numbers=0
# for i in range(ll):
#     if not logs[i].split(' ')[1].isdigit():
#         logs[i],logs[numbers] = logs[numbers], logs[i]
#         numbers+=1
# nums = logs[numbers:]
# logs = logs[:numbers]
#
# logs.sort(key=lambda x: (x.split(' ')[1:], x.split(' ')[0]))
# logs+= nums
#
# print(logs)



logs=["t kvr", "r 3 1", "i 403", "7 so", "t 54"]

ll = len(logs)
numbers=0
for i in range(ll):
    if logs[i].split(' ')[1].isalpha():
        logs[i],logs[numbers] = logs[numbers], logs[i]
        numbers+=1

# print(logs)
nums = logs[numbers:]
logs = logs[:numbers]

print(nums)

logs.sort(key = lambda x: x.split()[1])
logs.sort(key = lambda x: x.split()[1:])
logs+= nums
#
# print(logs)

logs=["t kvr", "r 3 1", "i 403", "7 so", "t 54"]

digits = []
letters = []
# divide logs into two parts, one is digit logs, the other is letter logs
for log in logs:
    if log.split()[1].isdigit():
        digits.append(log)
    else:
        letters.append(log)

print(digits)
letters.sort(key = lambda x: x.split()[1])
letters.sort(key = lambda x: x.split()[1:])
result = letters + digits

print(result)