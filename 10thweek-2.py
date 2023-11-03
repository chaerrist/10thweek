# import textwrap as tw

# target = "He was a boy."

# # res = tw.shorten(target, width=10)
# longTarget = target * 10

# print(res)
# print("\n")
# print(longTarget)
# print("\n")

# res1 = tw.wrap(longTarget, width = 50)
# print(res1)
# print("\n")
# print("\n".join(res1))

# rs = tw.fill(longTarget, width = 50)
# print(rs)

#문자열 치환

# line = "홍길동의 주민번호는 012345-1234567 입니다. "
# word_rt = []
# for word in line.split(" "):
#     if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
#         word = word[:6] + "-" + "*******"
#     word_rt.append(word)
        
# print(" ".join(word_rt))

#정규표현식

# import re
# line = "홍길동의 주민번호는 012345-1234567 입니다. "

# res = re.compile("(\d{6})[-]\d{7}") 
# print(res.sub("\g<1>-*******", line))