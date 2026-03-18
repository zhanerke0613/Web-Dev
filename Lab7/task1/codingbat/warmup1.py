#1
def sleep_in(weekday, vacation):
    return not weekday or vacation

#2
def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile

#3
def sum_double(a, b):
    if a == b:
        return 2 * (a + b)
    return a + b

#4
def diff21(n):
    if n > 21:
        return 2 * abs(n - 21)
    return abs(n - 21)

#5
def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

#6
def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10
#7
def near_hundred(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10
#8
def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    return (a < 0 and b > 0) or (a > 0 and b < 0)

#9
def not_string(s):
    if s.startswith("not"):
        return s
    return "not " + s

#10
def missing_char(s, n):
    return s[:n] + s[n+1:]

#11
def front_back(s):
    if len(s) <= 1:
        return s
    return s[-1] + s[1:-1] + s[0]

#12
def front3(s):
    front = s[:3]
    return front * 3