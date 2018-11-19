input("Привет пользователь ")
a=int(input("Введите кол-во элементов массива и я его заполню: "))
b=input("Введите 0 или 1,взависимости:отрицательные или положительные числа: ")
while True:
    if b.isdigit():
        break
    else:
        b=input("Введите правильное значение: ")
b=int(b)
if b==1:
    c=[i for i in range(1,a+1)]
    print(c)


else:
    c=[i*(-1) for i in range(1,a+int(1))]
    print(c)



    
























