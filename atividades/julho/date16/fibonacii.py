num = int(input('Digite oo termo que encontrar a fibo: '))
x = 1
y = 1

if num == 1:
    print(f'O 1° termo da fibonaci é {num}')
elif num == 2:
    print(f'O 2° termo da fiboonaci é {num}')
else:
    for i in range(2, num):
        total = x + y
        x = y
        y = total
        i += 1
        print(total)

