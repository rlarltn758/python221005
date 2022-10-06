# try1.py

from cmath import exp
from typing import Type


def divide(a,b):
    return a/b

try:
    result = divide(5,2.5)
    print("결과:{0}".format(result))
except ZeroDivisionError:
    print("0으로 나눌수없음")
except TypeError:
    print("숫자여야함")
else:
    print("결과:{0}".format(result))
finally:
    print("무조건 실행")

print("종료")