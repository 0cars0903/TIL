# def profile(name, age, main_lang):
#     print("이름 {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

# profile("유재석", 20, "파이썬")

# 같은 학교 같은 학년 같은 반 같은 수업.

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

# profile("유재석")


# 가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t 나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름 : {0}\t 나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("a", 20,"1", "2", "3", "4", "5", "6")
# profile("b", 20,"1", "2")



# 지역변수, 전역변수
gun = 10

def check(s):
    global gun # 전역 공간에 있는 gun 사용
    gun = gun -s
    print("[함수 내] 남은 총 : {0}".format(gun))

def check1(gun, s):
    gun = gun -s
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
check1(gun,2)
print("남은 총 : {0}".format(gun))