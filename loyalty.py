"""Customer loyalty point calculations."""

from collections.abc import Sequence
from dataclasses import dataclass

GROCERY_BONUS_MULTIPLIER = 1.5
STANDARD_MULTIPLIER = 1.0
MINIMUM_PURCHASE_AMOUNT = 0.0


@dataclass(frozen=True)
class Purchase:
    """One completed customer purchase."""

    amount: float
    category: str


def calculate_points(
    purchases: Sequence[Purchase],
    *,
    multiplier: float = STANDARD_MULTIPLIER,
) -> int:
    """Calculate loyalty points for completed purchases.

    Args:
        purchases: Completed purchases for one account.
        multiplier: Campaign multiplier applied to all eligible purchases.
    """
    total = 0.0
    for purchase in purchases:
        if purchase.amount <= MINIMUM_PURCHASE_AMOUNT:
            continue
        category_multiplier = (
            GROCERY_BONUS_MULTIPLIER
            if purchase.category == "grocery"
            else STANDARD_MULTIPLIER
        )
        total += purchase.amount * category_multiplier * multiplier
    return int(total)
