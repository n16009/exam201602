# 'hello, {name}!'と出力してください 。
def hello(name):
    print('hello, John!')
    pass


# sentence の文字数を出力してください
def length(sentence):
    s = sentence
    print(len(s))
    pass


# sentence の2文字目から5文字目まで(5文字目は含まない)を出力してください
def slicing2to5(sentence):
    print(sentence[2:5])
    pass


# number の符号を出力してください。ただし、0は'0'と出力してください
def number_sign(number):
    if number < 0:
        print("-")
    elif number == 0:
        print("'0'")
    else:
        print("+")
    pass


# number が素数なら'ok',そうでないなら'ng'と出力してください
def prime_number(number):
    counter = 0
    primes = []

    for n in range(2, 1001):
        prime = True
        for i in range(2, n):
            counter += 1
            if n % i == 0:
                prime = False
                break
            if prime:
                primes.append(n)

    print(primes, len(primes))
    print(u'除算を行った回数:%d' % counter)
    pass


# 1からnumberまでの合計を出力してください
def sum_from_1_to(number):
    ans = 0
    for i in range(number+1):
        ans += i
    return ans
pass


# numberの階乗(factorial)を出力してください
def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number-1)
pass


# リストdataの各要素(整数)を3乗した結果をリスト型として返してください
def cubic_list(data):
    data = ([1, 2, 3, 4, 5])
    cubic_list = [x**3 for x in range(1, 5)]
    pass


# 底辺x,高さyの直角三角形(right angled triangle)の残り1つの辺の長さを返してください
def calc_hypotenuse(x, y):
    print(x ** 2 + y ** 2)
    pass


# 底辺x,斜辺vの直角三角形の残り1つの辺の長さを返してください
def calc_subtense(x, v):
    print(x ** 2 - v ** 2)
    pass


# 三辺の長さがそれぞれx,y,zの三角形の面積を返してください
def calc_area_triangle(x, y, z):
    print(x * y / 2)
    pass


# 引数a,b,cを小数点以下2桁表示で空白切りで表示してください
def point_two_digits(a, b, c):
    pass


# リストdataの内容を小さい順でソートした結果を返してください
def list_sort(data):
    print(data.sort())
    pass


# 文字列の並びを逆にしたものを返してください
def reverse_string(sentence):
    print(sentence[::-1])
    pass


# dateから2016年4月1日までの日数を返してください
from datetime import date


def days_from_date(point):
    a = date(2016, 4, 1)
    print('days_from_date - a')

    # d1, d2 = date(days_from_date), date(2016, 4, 1)
    # str(d2 - d1)
    pass
