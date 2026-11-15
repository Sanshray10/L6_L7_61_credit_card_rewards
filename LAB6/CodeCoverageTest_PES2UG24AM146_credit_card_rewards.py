import pytest
from credit_card_rewards import reward_points, late_payment_fee, card_status


def test_classic_grocery():
    assert reward_points("classic", 1000, "grocery", False) == 10


def test_unknown_tier():
    with pytest.raises(ValueError):
        reward_points("silver", 1000, "grocery", False)


def test_invalid_amount():
    with pytest.raises(ValueError):
        reward_points("gold", 0, "grocery", False)


def test_fuel_no_points():
    assert reward_points("gold", 1000, "fuel", False) == 0


def test_gold_dining_weekend():
    assert reward_points("gold", 1000, "dining", True) == 90


def test_paid_on_time():
    assert late_payment_fee(5000, 0) == 0


def test_small_outstanding_fee():
    assert late_payment_fee(500, 5) == 100


def test_medium_outstanding_fee():
    assert late_payment_fee(5000, 5) == 500


def test_large_outstanding_very_late():
    assert late_payment_fee(20000, 40) == 1750


def test_frozen():
    assert card_status(10, 0, True) == "frozen"


def test_blocked():
    assert card_status(10, 3, False) == "blocked"


def test_over_limit_risk():
    assert card_status(95, 0, False) == "over limit risk"


def test_watch():
    assert card_status(50, 0, False) == "watch"


def test_good():
    assert card_status(10, 0, False) == "good"
