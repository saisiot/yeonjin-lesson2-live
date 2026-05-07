"""
파이썬의 함수(Function), 쉽게 이해하기
함수는 특정 작업을 수행하는 코드 묶음입니다.
마치 요리 레시피처럼, 필요할 때마다 사용할 수 있는 재사용 가능한 지시사항 모음이라고 생각하면 됩니다.

함수의 주요 특징:

특정 기능을 수행하는 코드 블록입니다
이름을 붙여 필요할 때마다 호출(실행)할 수 있습니다
입력값(매개변수)을 받아 처리한 후 결과값을 돌려줄 수 있습니다
복잡한 작업을 간단하게 만들고 코드 재사용성을 높입니다

일상생활에 비유하자면:

커피 머신의 "아메리카노" 버튼 (버튼만 누르면 정해진 과정이 실행됨)
세탁기의 "표준 세탁" 프로그램 (옷과 세제를 넣고 버튼만 누르면 됨)
요리책의 레시피 (재료를 넣고 지시대로 하면 요리가 완성됨)
"""

def write_ad_copy(campaign_name, product_features):
    """
    광고 문구를 생성하는 함수입니다.

    Args:
        campaign_name (str): 캠페인 이름을 나타내는 문자열입니다.
        product_features (list): 제품의 특징을 나타내는 문자열 리스트입니다.

    Returns:
        str: 생성된 광고 문구를 반환합니다.
    """
    ad_copy = f"지금 바로 확인하세요! {campaign_name}에서 {', '.join(product_features)}를 경험하세요!"
    return ad_copy


# 함수 호출 시 캠페인 이름과 제품 특징을 인수로 전달
generated_copy = write_ad_copy(
    "가을 특별 할인", ["최고 품질", "합리적인 가격", "다양한 디자인"]
)
print(generated_copy)


def generate_daily_report():
    """
    일일 광고 성과 보고서를 생성하는 함수입니다.

    Returns:
        dict: 광고 성과 데이터를 포함하는 딕셔너리를 반환합니다.
              - "클릭수": 광고 클릭 수
              - "노출수": 광고 노출 수
              - "전환율": 클릭 대비 전환율
    """
    # (가정) 광고 성과 데이터를 가져오는 코드
    clicks = 1200
    impressions = 25000
    conversion_rate = 0.048
    daily_report = {"클릭수": clicks, "노출수": impressions, "전환율": conversion_rate}
    return daily_report


# 함수 호출 후 결과 출력
today_report = generate_daily_report()
print(today_report)


# ============================================================
# ⚠️ 여기까지가 2회차 강의 범위입니다.
# 아래 클래스(class) 부분은 다음 회차(또는 본인 학습용).
# 라이브에선 건너뛰세요. 눈으로만 한 번 훑고 넘어가요.
#
# "함수에 이름표를 더 크게 붙인 게 클래스다" 정도로만 알아두면 충분.
# ============================================================


class PRTeam:
    """
    홍보팀을 나타내는 클래스입니다.

    Attributes:
        team_name (str): 홍보팀의 이름입니다.
    """

    def __init__(self, team_name):
        """
        PRTeam 클래스의 생성자입니다.

        Args:
            team_name (str): 홍보팀 이름을 초기화합니다.
        """
        self.team_name = team_name


class PublicRelationsOfficer:
    """
    홍보 담당자를 나타내는 클래스입니다.

    Attributes:
        name (str): 홍보 담당자의 이름입니다.
    """

    def __init__(self, name):
        """
        PublicRelationsOfficer 클래스의 생성자입니다.

        Args:
            name (str): 홍보 담당자의 이름을 초기화합니다.
        """
        self.name = name

    def distribute_press_release(self, press_release_content):
        """
        보도자료를 배포하는 메소드입니다.

        Args:
            press_release_content (str): 배포할 보도자료의 내용을 나타내는 문자열입니다.

        Example:
            distribute_press_release("오늘 저희 회사는 혁신적인 신제품 출시를 발표하게 되어 기쁩니다...")
            -> 멍멍씨 홍보 담당자가 보도자료 '오늘 저희 회사는 혁신적인...'을 배포합니다.
        """
        print(
            f"{self.name} 홍보 담당자가 보도자료 '{press_release_content[:20]}...'을 배포합니다."
        )
        # 보도자료 배포를 위한 실제 코드


# PublicRelationsOfficer 클래스의 인스턴스 생성 및 메소드 호출
pr_officer = PublicRelationsOfficer("멍멍씨")
press_release = "오늘 저희 회사는 혁신적인 신제품 출시를 발표하게 되어 기쁩니다..."
pr_officer.distribute_press_release(press_release)

