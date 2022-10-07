# demoRe.py

import re

result = re.search("[0-9]*th", "35th")
print(result)
print(result.group())

result = re.match("[0-9]*th", "35th")
print(result)
print(result.group())

print( bool(re.search("ap", "this is apple")))
print( bool(re.match("ap", "this is apple")))

result = re.search("\d{4}", "올해는 2022년입니다.")
print(result.group())

result = re.search("\d{5}", "올해는 20222년입니다.")
print(result.group())