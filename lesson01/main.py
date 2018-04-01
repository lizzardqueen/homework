import math

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


input_a = input('Введите целое неотрицательное число a: ')
a = proof(input_a)
input_b = input('Введите целое неотрицательное число b: ')
b = proof(input_b)

print ('a в степени b: %d' %(a ** b))
print ('логарифм a по основанию b: ' + str((math.log(a,b))))