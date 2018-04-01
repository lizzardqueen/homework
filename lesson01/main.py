import random

def proof(n):
    try:
        n = float(n)
    except:
        print ('Надо было ввести число!')
        quit()

    if n >= 0 and n == int(n):
        n = int (n)
        return n
    else:
        print ('Надо было ввести целое неотрицательно цисло')
        quit()


def massive(n):
    a = []
    for i in range(n):
        a.append(random.randint(0, 999))
    return a

def puzurek(a):
    for i in range(len(a)):
        min = a[i]
        b = i
        for j in range(i+1, len(a)):
            if a[j] < min:
                min = a[j]
                b = j
        if min != a[i]:
            a[i],a[b] = a[b],a[i]
    return a

n = input('Введите целое положительное число: ')
n = proof(n)

m = massive(n)

print(m)
print(puzurek(m))
print(sorted(m))

x = 55.362
print('x = %f' %x)
print('Целая часть от x: %i' %x)
print('X с округлением до 1 знака после запятой: %.1f' %x)