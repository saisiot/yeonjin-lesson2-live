# 파이썬 함수 연습문제

# 주어진 시험 점수
scoreList = [85, 30, 76, 45, 90]

# 문제 1. 합격/불합격 판단 함수
# 목표: 주어진 점수가 40점 이상이면 "Pass", 그렇지 않으면 "Fail"을 출력하는 함수를 작성하세요.
# 함수 이름: checkPass
# 설명: 점수 리스트의 각 점수에 대해 Pass 또는 Fail 여부를 출력하세요.


# 아래에 코드를 작성해주세요. print 관련 코드는 잘 활용해보세요.
def checkPass(scoreList):
    print(f"{score} : Pass")
    print(f"{score} : Fail")


# 결과 확인
checkPass(scoreList)

# 코드 실행 결과
# 85 : Pass
# 30 : Fail
# 76 : Pass
# 45 : Pass
# 90 : Pass


# 문제 2. 최종 결과 함수
# 목표: 학생의 총점과 평균을 계산하고, 평균이 60점 이상이면 "Final Pass", 그렇지 않으면 "Final Fail"을 출력하는 함수를 작성하세요.
# 함수 이름: getFinalResult
# 설명: 점수 리스트의 총점과 평균을 구하고, 평균을 기준으로 합격 여부를 판단해 출력하세요.


# 아래에 코드를 작성해주세요. print 관련 코드는 잘 활용해보세요.
def getFinalResult(scoreList):
    print(f"총점 : {total}")
    print(f"평균 : {round(average, 2)}")
    print(f"결과 : {result}")


# 결과 확인
getFinalResult(scoreList)

# 코드 실행 결과
# 총점 : 326
# 평균 : 65.2
# 결과 : Final Pass


# ---------- 답안 -----------
# 문제1
# def checkPass(scoreList):
#     for score in scoreList:
#         if score >= 40:
#             print(f'{score} : Pass')
#         else:
#             print(f'{score} : Fail')


# 문제2
# def getFinalResult(scoreList):
#     total = sum(scoreList)
#     average = total / len(scoreList)
#     result = 'Final Pass' if average >= 60 else 'Final Fail'
#     print(f'총점 : {total}')
#     print(f'평균 : {round(average, 2)}')
#     print(f'결과 : {result}')
