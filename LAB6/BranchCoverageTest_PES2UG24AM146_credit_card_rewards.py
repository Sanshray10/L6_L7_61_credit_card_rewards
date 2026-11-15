import pytest
from credit_card_rewards import reward_points, late_payment_fee, card_status


def test_classic_grocery():
    assert reward_points("classic", 1000, "grocery", False) == 10


def test_unknown_tier():
    with pytest.raises(ValueError):
        reward_points("silver", 1000, "grocery", False)


def test_zero_amount():
    with pytest.raises(ValueError):
        reward_points("gold", 0, "grocery", False)


def test_negative_amount():
    with pytest.raises(ValueError):
        reward_points("gold", -500, "grocery", False)


def test_fuel_no_points():
    assert reward_points("gold", 1000, "fuel", False) == 0


def test_gold_dining_weekend():
    assert reward_points("gold", 1000, "dining", True) == 90


def test_platinum_travel_weekday():
    assert reward_points("platinum", 1000, "travel", False) == 80


def test_classic_weekend_no_bonus():
    assert reward_points("classic", 1000, "dining", True) == 20


def test_gold_grocery_weekday():
    assert reward_points("gold", 1000, "grocery", False) == 20


def test_amount_below_100():
    assert reward_points("platinum", 99, "grocery", False) == 0


def test_paid_on_time():
    assert late_payment_fee(5000, 0) == 0


def test_no_outstanding():
    assert late_payment_fee(0, 10) == 0


def test_small_outstanding_fee():
    assert late_payment_fee(500, 5) == 100


def test_outstanding_1000_boundary():
    assert late_payment_fee(1000, 5) == 100


def test_medium_outstanding_fee():
    assert late_payment_fee(5000, 5) == 500


def test_outstanding_10000_boundary():
    assert late_payment_fee(10000, 5) == 500


def test_large_outstanding_fee():
    assert late_payment_fee(20000, 5) == 1000


def test_30_days_late_boundary():
    assert late_payment_fee(500, 30) == 100


def test_small_outstanding_very_late():
    assert late_payment_fee(500, 31) == 850


def test_large_outstanding_very_late():
    assert late_payment_fee(20000, 40) == 1750


def test_frozen():
    assert card_status(10, 0, True) == "frozen"


def test_frozen_with_missed_payments():
    assert card_status(95, 5, True) == "frozen"


def test_blocked():
    assert card_status(10, 3, False) == "blocked"


def test_over_limit_risk():
    assert card_status(95, 0, False) == "over limit risk"


def test_utilisation_90_boundary():
    assert card_status(90, 0, False) == "watch"


def test_watch_high_utilisation():
    assert card_status(50, 0, False) == "watch"


def test_watch_missed_payment():
    assert card_status(10, 1, False) == "watch"


def test_utilisation_30_boundary():
    assert card_status(30, 0, False) == "good"


def test_good():
    assert card_status(10, 0, False) == "good"
