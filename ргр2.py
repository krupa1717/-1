import numpy as np
import pandas as pd

# Функции:
'''
a, b - пределы интегрирования
h - шаг
n - количество шагов разбиения
'''
# Прямоугольники:
def pryamougulniki(f, a, b, h):
    n = int((b - a) / h)
    x_mid = np.linspace(a + h/2, b - h/2, n)
    return h * np.sum(f(x_mid))
    
# Трапеции:
def trapezoidal(f, a, b, h):
    n = int((b - a) /h)
    x = np.linspace(a, b, n + 1)      
    y = f(x)
    return h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])
    
# Симпсон:
def simpson(f, a, b, h):
    n = int((b - a) /h)
    if n % 2 != 0:
        n += 1
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return (h/3) * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2]))
# Метод 3/8:
def tri_vosmih(f, a, b, h):
    n = int((b - a) /h)
    while n % 3 != 0: 
        n += 1
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    result = 0
    for i in range(0,n,3):
        result+=(3*h/8)*(y[i] + 3*y[i+1] +3*y[i+2]+y[i+3])
    return result

if __name__ == "__main__":
    # Вводим тестовую функцию
    def f(x):
        return np.sin(x) #<-функция
    a, b = 0, np.pi/2 #<- пределы интегрирования
    exact_value = 1  #<- точное значения интеграла для вычисления ошибки
    
h_values= [np.pi/4,	np.pi/6,np.pi/16,np.pi/32,	np.pi/64,	np.pi/128] #<- задаем шаг
methods = [
    ('Прямоугольники', pryamougulniki),
    ('Трапеции', trapezoidal),
    ('Симпсон', simpson),
    ('3/8', tri_vosmih)
]

results = []
# выводит табличку со значениями
for name, method in methods:
    for h in h_values:
        I = method(f, a, b, h)
        error = abs(I - exact_value)
        results.append({
            'Метод': name,
            'h': h,
            'Приближение': I,
            'Ошибка': error
        })

df = pd.DataFrame(results)
print(df.to_string(index=False))

'''
 /\_/\  
| o o |  \ /
\  u  /  |_|   типа кот
'''