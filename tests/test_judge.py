"""D03 요구사항 R-01~R-03 판정 테스트.

한 판 = 하이볼·진토닉·다이키리 한 잔씩(병 7개).
키는 "레시피/재료", 값은 ml.
"""

from judge import judge_episode

# 기본 레시피 목표량 (docs/requirements.md '레시피와 목표량')
STANDARD = {
    "highball/whisky": 45.0,
    "highball/soda": 120.0,
    "gin_tonic/gin": 45.0,
    "gin_tonic/tonic": 120.0,
    "daiquiri/rum": 45.0,
    "daiquiri/lime": 20.0,
    "daiquiri/syrup": 15.0,
}

# 맞춤 주문: 다이키리 "덜 달게" → 설탕 시럽 50%
CUSTOM = {**STANDARD, "daiquiri/syrup": 7.5}


# R-01 목표량 ±10% 이내 -------------------------------------------------

def test_exact_pour_is_success():
    assert judge_episode(STANDARD, dict(STANDARD), dropped=0, elapsed_s=200.0)


def test_error_exactly_10_percent_is_success():
    poured = {**STANDARD, "daiquiri/syrup": 16.5, "highball/soda": 108.0}
    assert judge_episode(STANDARD, poured, dropped=0, elapsed_s=200.0)


def test_error_over_10_percent_is_fail():
    poured = {**STANDARD, "daiquiri/syrup": 16.6}
    assert not judge_episode(STANDARD, poured, dropped=0, elapsed_s=200.0)


def test_missing_ingredient_is_fail():
    poured = {k: v for k, v in STANDARD.items() if k != "daiquiri/lime"}
    assert not judge_episode(STANDARD, poured, dropped=0, elapsed_s=200.0)


def test_custom_order_is_judged_by_custom_target():
    assert judge_episode(CUSTOM, dict(CUSTOM), dropped=0, elapsed_s=200.0)


def test_custom_order_with_standard_amount_is_fail():
    # 맞춤 주문(시럽 7.5ml)인데 기본량(15ml)을 부으면 실패
    assert not judge_episode(CUSTOM, dict(STANDARD), dropped=0, elapsed_s=200.0)


def test_empty_order_is_fail():
    assert not judge_episode({}, {}, dropped=0, elapsed_s=200.0)


# R-02 낙하 0 ------------------------------------------------------------

def test_drop_is_fail():
    assert not judge_episode(STANDARD, dict(STANDARD), dropped=1, elapsed_s=200.0)


# R-03 한 판 240초 이내 ---------------------------------------------------

def test_exactly_240s_is_success():
    assert judge_episode(STANDARD, dict(STANDARD), dropped=0, elapsed_s=240.0)


def test_over_240s_is_fail():
    assert not judge_episode(STANDARD, dict(STANDARD), dropped=0, elapsed_s=240.1)
