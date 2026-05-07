from lunardate import LunarDate

# 양력 날짜를 음력 날짜로 변환하는 함수
def 양력_음력_변환기(양력_YYMMDD):
    if len(양력_YYMMDD) != 6 or not 양력_YYMMDD.isdigit():
        return "잘못된 형식입니다. YYMMDD 형식으로 입력해주세요."

    try:
        year = int("20" + 양력_YYMMDD[:2])  # 21세기로 가정
        month = int(양력_YYMMDD[2:4])
        day = int(양력_YYMMDD[4:])

        lunar_date = LunarDate(year, month, day)
        return f"{lunar_date.year}-{lunar_date.month:02d}-{lunar_date.day:02d}"
    except ValueError:
        return "존재하지 않는 양력 날짜입니다."
    except Exception as e:
        return f"변환 중 오류가 발생했습니다: {e}"


# 사용자로부터 양력 날짜 입력 받기
양력_입력 = input("양력 날짜를 YYMMDD 형식으로 입력하라 (예: 250325): ")

# 음력 날짜로 변환 및 결과 출력
음력_날짜 = 양력_음력_변환기(양력_입력)
print(f"입력하신 양력 날짜의 음력 날짜는 {음력_날짜} 이다.")
