#!/usr/bin/env python3
"""대한민국 여행 추천 프로그램

사용자의 성별, 여행자 수, 여행지역, 예산을 입력받아 간단한 추천을 제공합니다.
"""


def get_budget_level(budget):
    if budget < 100000:
        return "low"
    elif budget < 500000:
        return "medium"
    else:
        return "high"


def recommend(gender, travelers, region, budget):
    destinations = {
        "서울": {
            "low": "저예산 서울 도심 여행 코스",
            "medium": "가성비 좋은 서울 명소 투어",
            "high": "프리미엄 서울 문화 체험"
        },
        "부산": {
            "low": "광안리와 자갈치시장 산책",
            "medium": "해운대와 태종대 투어",
            "high": "요트 체험과 해산물 미식 여행"
        },
        "제주": {
            "low": "올레길 트레킹",
            "medium": "성산일출봉과 중문 관광",
            "high": "프리미엄 리조트 휴양"
        }
    }

    if region not in destinations:
        return "지원하지 않는 지역입니다."

    level = get_budget_level(budget)
    course = destinations[region][level]
    return f"{gender} 여행자 {travelers}명께 추천: {course} (예산 기준: {budget}원)"
def main():
    gender = input("성별을 입력하세요 (남/여): ").strip()
    travelers = int(input("여행자 수를 입력하세요: ").strip())
    region = input("여행 지역을 입력하세요 (서울/부산/제주): ").strip()
    budget = int(input("예산을 입력하세요(숫자만): ").strip())

    print(recommend(gender, travelers, region, budget))


if __name__ == "__main__":
    main()
