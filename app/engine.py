from __future__ import annotations
from app.models import Knight


def fight(attacker: Knight, defender: Knight) -> None:

    # Calculate damage: attacker's total power -- defender's total protection
    damage = attacker.power - defender.protection
    # If damage is positive, subtract it from the defender's health points
    if damage > 0:
        defender.hp -= damage
    # Ensure health points do not become negative
    if defender.hp < 0:
        defender.hp = 0
