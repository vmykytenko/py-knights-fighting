def fight(attacker, defender) -> None:

    # Calculate damage: attacker's total power minus defender's total protection
    damage = attacker["power"] - defender["protection"]
    # If damage is positive, subtract it from the defender's health points
    if damage > 0:
        defender["hp"] -= damage
    # Ensure health points do not become negative
    if damage < 0:
        defender["hp"] = 0