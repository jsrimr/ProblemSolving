import re

# Head : 문자 , 한글자 이상
# Number : 한글자~다섯글자, 연속된 숫자, 앞쪽에 0 가능
# TAIL : 나머지 부분, 숫자도 가능. 아무글자 없는 것도 가능
# 대소문자 구분 x
# 영문 대소문자, 숫자, 공백(" ), 마침표(.), 빼기 부호(-")
files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]

def solution(files):
    # p = re.compile('\w+\d{1,5}*')
    sort_keys = []
    p = re.compile('([a-zA-Z-\.\s]+)(\d{1,5})(.*)')
    for file in files:
        m = p.search(file)
        head = m.group(1).lower()
        number = int(m.group(2))
        # tail = m.group(3)
        sort_keys.append((file, head, number))

    sorted_files = sorted(sorted(sort_keys, key=lambda x: x[2]), key = lambda x: x[1])
    return list(map(lambda x: x[0], sorted_files))


print(solution(files))
