"""칵테일 한 판의 성공 판정 (D03 요구사항 R-01~R-03)."""

TOLERANCE = 0.10       # R-01: 재료마다 목표량 ±10% 이내
MAX_DROPPED = 0        # R-02: 낙하 0
TIME_LIMIT_S = 240.0   # R-03: 한 판 240초 이내
_EPS = 1e-9            # 경계값(딱 10%)이 부동소수점 오차로 떨어지지 않게


def pour_ok(target_ml: float, poured_ml: float | None) -> bool:
    """재료 하나가 목표량 ±10% 이내인지 본다. 붓지 않은 재료(None)는 실패."""
    if poured_ml is None:
        return False
    return abs(poured_ml - target_ml) <= target_ml * TOLERANCE + _EPS


def judge_episode(
    targets_ml: dict[str, float],
    poured_ml: dict[str, float],
    dropped: int,
    elapsed_s: float,
) -> bool:
    """한 판이 R-01~R-03을 모두 지키면 True.

    targets_ml: 주문 데이터의 목표량(맞춤 반영). 예: {"daiquiri/syrup": 7.5, ...}
    poured_ml:  시뮬레이션에서 실제로 부은 양. targets_ml과 같은 키.
    dropped:    떨어뜨린 병 수
    elapsed_s:  주문을 넣고 마지막 잔이 서빙 위치에 놓일 때까지 걸린 시간(초)
    """
    if not targets_ml:
        return False
    all_poured = all(
        pour_ok(target, poured_ml.get(name)) for name, target in targets_ml.items()
    )
    return all_poured and dropped <= MAX_DROPPED and elapsed_s <= TIME_LIMIT_S
