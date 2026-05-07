"""
# 파이썬의 라이브러리(Library), 쉽게 이해하기

라이브러리는 미리 작성된 유용한 코드 모음집입니다.
마치 도서관에 책이 모여 있듯이, 프로그래밍에 필요한 다양한 기능들이 잘 정리되어 있는 도구 상자라고 생각하면 됩니다.

라이브러리의 주요 특징:
- 자주 사용되는 기능들을 모아놓은 코드 묶음입니다
- 직접 모든 기능을 처음부터 만들 필요 없이 가져다 쓸 수 있습니다
- 전문가들이 최적화하고 테스트한 코드를 사용할 수 있어 안정적입니다
- 필요한 부분만 가져와서(import) 사용할 수 있습니다

일상생활에 비유하자면:
- 요리할 때 모든 재료를 직접 농사짓는 대신 마트에서 구매하는 것
- 집을 지을 때 모든 도구와 재료를 직접 만드는 대신 하드웨어 스토어에서 구매하는 것
- 직접 그림을 그리는 대신 스티커북에서 원하는 스티커만 골라 사용하는 것

파이썬의 대표적인 라이브러리 예시:
- 수학 계산을 위한 NumPy
- 데이터 분석을 위한 Pandas
- 그래프 그리기를 위한 Matplotlib
- 웹 페이지 정보 가져오기를 위한 Requests

라이브러리는 "바퀴를 다시 발명하지 마라"라는 프로그래밍 원칙을 따르는 방법입니다.
즉, 이미 누군가 잘 만들어 놓은 기능을 다시 만들기보다는 가져다 쓰는 것이 시간과 노력을 절약하고 더 안정적인 프로그램을 만들 수 있게 해줍니다.
"""


# Example 1: `math` 라이브러리를 사용한 기본 수학 연산
import math

# 16의 제곱근 계산
# `math.sqrt` 함수는 숫자의 제곱근을 반환합니다
square_root = math.sqrt(16)
print(f"16의 제곱근은 {square_root}입니다")

# Example 2: `random` 라이브러리를 사용하여 랜덤 숫자 생성
import random

# 1과 10 사이의 랜덤 숫자 생성
# `random.randint` 함수는 지정된 범위 내의 랜덤 정수를 생성합니다
random_number = random.randint(1, 10)
print(f"1과 10 사이의 랜덤 숫자는 {random_number}입니다")

# Example 3: `datetime` 라이브러리를 사용하여 날짜와 시간 다루기
from datetime import datetime

# 현재 날짜와 시간 가져오기
# `datetime.now` 함수는 현재 날짜와 시간을 반환합니다
current_time = datetime.now()
print(f"현재 날짜와 시간은 {current_time}입니다")

# Example 4: `os` 라이브러리를 사용하여 운영 체제와 상호작용
import os

# 현재 작업 디렉토리 가져오기
# `os.getcwd` 함수는 현재 작업 디렉토리를 반환합니다
current_directory = os.getcwd()
print(f"현재 작업 디렉토리는 {current_directory}입니다")

# Example 5: `collections` 라이브러리를 사용한 특수 데이터 구조
from collections import Counter

# 리스트에서 각 요소의 개수 세기
# `Counter` 클래스는 요소를 키로, 개수를 값으로 가지는 딕셔너리와 유사한 객체를 생성합니다
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
fruit_count = Counter(fruits)
print(f"각 과일의 개수는 {fruit_count}입니다")
