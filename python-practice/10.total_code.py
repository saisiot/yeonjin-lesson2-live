"""
이 스크립트는 초보자를 위한 마케팅 업무를 자동화하고 지원하기 위해 설계되었습니다.
다양한 마케팅 관련 작업을 수행할 수 있는 메소드를 포함하고 있습니다.

1. create_marketing_campaign(name, budget, target):
   - 새로운 마케팅 캠페인을 생성합니다.
   - 캠페인의 이름, 예산, 목표 고객층을 입력받아 캠페인 정보를 딕셔너리로 반환합니다.

2. analyze_campaign_results(campaign, clicks, sales):
   - 특정 캠페인의 결과를 분석합니다.
   - 클릭 수와 판매 금액을 기반으로 투자 수익률(ROI)을 계산하고 성공 여부를 판단합니다.

3. generate_ad_copy(product_name, key_features, target_emotion):
   - 제품의 광고 문구를 자동으로 생성합니다.
   - 제품 이름, 주요 특징, 타겟 감정을 입력받아 적합한 광고 문구를 반환합니다.

이 스크립트는 마케팅 캠페인 생성, 성과 분석, 광고 문구 생성과 같은 작업을 간단히 수행할 수 있도록 도와줍니다.
"""

# 초보자를 위한 고양이씨의 마케팅 업무 메소드


# 메소드 1: 마케팅 캠페인 생성
def create_marketing_campaign(name, budget, target):
    """
    새로운 마케팅 캠페인을 생성하는 메소드

    Args:
        name: 캠페인 이름
        budget: 캠페인 예산
        target: 목표 고객층

    Returns:
        생성된 캠페인 정보를 담은 딕셔너리
    """
    # 캠페인 정보를 딕셔너리로 저장
    campaign = {"name": name, "budget": budget, "target": target, "status": "계획됨"}

    # 캠페인 생성 결과 출력
    print(f"'{name}' 캠페인이 생성되었습니다!")
    print(f"예산: {budget}원")
    print(f"타겟: {target}")

    return campaign


# 메소드 2: 마케팅 성과 분석
def analyze_campaign_results(campaign, clicks, sales):
    """
    캠페인 결과를 분석하는 간단한 메소드

    Args:
        campaign: 캠페인 딕셔너리
        clicks: 광고 클릭 수
        sales: 판매 금액

    Returns:
        분석 결과 메시지
    """
    # 투자 수익률(ROI) 계산
    roi = (sales - campaign["budget"]) / campaign["budget"] * 100

    # 캠페인 성공 여부 판단
    if roi > 0:
        result = "성공"
    else:
        result = "실패"

    # 분석 결과 메시지 생성
    analysis = f"""
===== 캠페인 분석 결과 =====
캠페인 이름: {campaign['name']}
투입 예산: {campaign['budget']}원
클릭 수: {clicks}회
판매 금액: {sales}원
수익률(ROI): {roi:.1f}%
결과: {result}
"""

    print(analysis)
    return analysis


# 메소드 3: 마케팅 문구 생성기
def generate_ad_copy(product_name, key_features, target_emotion):
    # 감정별 마케팅 문구 템플릿
    emotion_templates = {
        "기쁨": [
            "당신의 하루가 더 행복해집니다!",
            "웃음이 끊이지 않는 경험",
            "즐거움이 가득한 순간",
        ],
        "안정": [
            "걱정 없는 선택, 확실한 만족",
            "믿을 수 있는 품질을 약속합니다",
            "언제나 변함없는 신뢰",
        ],
        "호기심": [
            "상상해보세요, 어떤 변화가 찾아올까요?",
            "새로운 경험을 시작할 시간",
            "놀라운 비밀이 공개됩니다",
        ],
        "성취": [
            "당신의 목표 달성을 위한 최고의 선택",
            "한 단계 더 높은 결과를 원하신다면",
            "최고의 성과를 경험하세요",
        ],
    }

    # 기본 템플릿 (지정된 감정이 없을 경우)
    default_templates = [
        "더 나은 선택, 더 나은 결과",
        "지금 바로 경험해보세요",
        "당신을 위한 특별한 제안",
    ]

    # 타겟 감정에 맞는 템플릿 선택 (없으면 기본 템플릿 사용)
    templates = emotion_templates.get(target_emotion, default_templates)

    # 랜덤하게 템플릿 선택 (실제 구현에서는 random 모듈 사용)
    import random

    selected_template = random.choice(templates)

    # 특징 문구 생성
    features_text = ""
    for i, feature in enumerate(key_features):
        features_text += f"✓ {feature}"
        if i < len(key_features) - 1:
            features_text += "\n"

    # 최종 광고 문구 생성
    ad_copy = f"""
✨ {product_name} ✨

{selected_template}

{features_text}

지금 바로 만나보세요!
"""

    print(f"{product_name}을(를) 위한 광고 문구가 생성되었습니다:")
    print(ad_copy)

    return ad_copy


# 메소드 사용 예시
if __name__ == "__main__":
    # 예시 1: 캠페인 생성
    summer_campaign = create_marketing_campaign(
        name="여름 냐옹냐옹 프로모션", budget=500000, target="20-30대 고양이 애호가"
    )

    # 예시 2: 캠페인 결과 분석
    analyze_campaign_results(campaign=summer_campaign, clicks=1200, sales=650000)

    # 예시 3: 광고 문구 생성
    generate_ad_copy(
        product_name="냐옹냐옹 3000",
        key_features=["인공지능 털뭉치 장난감", "자동 움직임 센서", "긴 배터리 수명"],
        target_emotion="호기심",
    )
