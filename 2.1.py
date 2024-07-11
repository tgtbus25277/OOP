n = int(input('Enter numbeer of * = '))
# แสสดงรูปแบบที่ 1
for i in range(0, n):
    print('*' * i)
# แสดงรูปแบบที่ 2
for i in range(n, 0, -1):
    print('*' * i)
# แสดงรูปแบบที่ 3
for i in range(1, n + 1):
    print(' ' * (n - i) + '* ' * i)
# แสดงรูปแบบที่ 4
for i in range(n, 0, -1):
    print(' ' * (n - i) + '* ' * i)
# แสดงรูปแบบที่ 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)
