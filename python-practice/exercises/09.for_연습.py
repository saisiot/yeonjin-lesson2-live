# 1. 리스트 ['one', 'two', 'three']의 각 요소를 출력하는 for 문을 작성해보세요.
# (힌트: 리스트 요소를 차례대로 변수에 대입하여 출력하세요.)

# 2. 리스트 [(1, 2), (3, 4), (5, 6)]에서 각 튜플의 두 요소를 더해 출력하는 for 문을 작성해보세요.
# (힌트: 튜플의 두 값을 더하는 방식으로 코드를 작성하세요.)

# 3. 리스트 [90, 25, 67, 45, 80]에서 60점 이상이면 합격, 그렇지 않으면 불합격을 출력하는 for 문을 작성해보세요.
# (힌트: if 문을 사용해 조건을 걸고, 번호를 부여하는 변수를 활용하세요.)

# 4. 리스트 [90, 25, 67, 45, 80]에서 60점 이상인 사람만 합격 메시지를 출력하고, 그렇지 않은 사람은 건너뛰는 for 문을 작성해보세요.
# (힌트: continue 문을 사용해 60점 미만일 때 건너뛰세요.)

# 5. for와 range 함수를 사용해 1부터 10까지의 숫자를 더하는 코드를 작성해보세요.
# (힌트: range 함수를 사용해 1부터 10까지 반복하면서 합을 구하세요.)


# 정답
# 1번 답: test_list = ['one', 'two', 'three']; for i in test_list: print(i)
# 2번 답: a = [(1, 2), (3, 4), (5, 6)]; for (first, last) in a: print(first + last)
# 3번 답: marks = [90, 25, 67, 45, 80]; number = 0; for mark in marks: number += 1; if mark >= 60: print(f"{number}번 학생은 합격입니다."); else: print(f"{number}번 학생은 불합격입니다.")
# 4번 답: marks = [90, 25, 67, 45, 80]; number = 0; for mark in marks: number += 1; if mark < 60: continue; print(f"{number}번 학생 축하합니다. 합격입니다.")
# 5번 답: add = 0; for i in range(1, 11): add += i; print(add)
