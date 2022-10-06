import sys

url = "http://www.credu.com/?page=" + str(1)
print(url)

print("welcome to", "python", sep="~", end="!", file=sys.stderr)

# 파일에 쓰기
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")

print("file write", file=f)
f.close()

#서식지정
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).rjust(3))

# 서식 지정
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).zfill(3))


print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:,}".format(15000000000))