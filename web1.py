# web1.py
from bs4 import BeautifulSoup

# 문자열 로딩
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()

# 검색에 용이한 스프 객체
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())

#<p> 전체를 검색
#print(soup.find_all("p"))

#첫번쨰<p>태그
#print(soup.find("p"))

#id=first
#print(soup.find_all(id="first"))

#조건 : <p class='outer-text'>컨텐츠<p>
#print(soup.find_all("p", class_="outer-text"))

#결국은 컨텐츠를 가져오기
for tag in soup.find_all("a"):
    #print(tag.text)
    content = tag.text.strip()
    content = content.replace("\n","")
    print(content)


