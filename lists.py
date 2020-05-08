N = int(input())
result = []
for n in range:
    x = input().split()
    cmd = x[0]
    if cmd == 'insert':
        result.insert(int(x[1]),int(x[2]))
    if cmd == 'append':
        result.append(int(x[1]))
    if cmd == 'remove':
        result.remove(x[1])
    if cmd == 'print':
        print(result)
    if cmd == 'reverse':
        result.reverse()
    if cmd == 'pop':
        result.pop()
    if cmd == 'sort':
        result == sorted(result)
print(result)

