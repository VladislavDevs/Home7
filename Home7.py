from concurrent.futures import ThreadPoolExecutor
import time

def calculations_processes(x1 : int, x2 : int, counter : int):
    n = 0
    t1 = 0
    t2 = 0
    t3 = 0
    while n < counter:
        with ThreadPoolExecutor() as executor1:
            result1 = executor1.submit(formula1_calc, x1)
            time.sleep(1)
            t1 += 1
        with ThreadPoolExecutor() as executor2:
            result2 = executor2.submit(formula2_calc, x2)
            time.sleep(1)
            t2 += 1
        with ThreadPoolExecutor() as executor3:
            result3 = executor3.submit(formula3_calc, result1.result(), result2.result())
            time.sleep(1)
            t3 += 1

        n += 1
    print(f"{t1}---{t2}---{t3}\n\nВсего: {t1+t2+t3}")

def formula1_calc(x : int):
    print(x^2-x^2+x*4-x*5+x+x)
    return x^2-x^2+x*4-x*5+x+x

def formula2_calc(x : int):
    print(x + x)
    return x + x

def formula3_calc(x : int, y : int):
    print(x + y)
    return x + y

def main():
    x = input("Введите число x: ")
    y = input("Введите число y: ")
    counter = input("Введите количество операций: ")

    calculations_processes(int(x), int(y), int(counter))

main()