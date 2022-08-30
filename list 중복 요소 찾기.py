# 리스트 중복 요소 개수 찾기
C = {}
for i in B: 
    try: 
        C[i] += 1
    except:
        C[i] = 1
print(C)
