# Starting project with messy code
from app.config import KNIGHTS
from app.models import Knight
from app.engine import fight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    # Create knight objects (they calculate everything automatically now!)
    # lancelot
    lancelot = Knight(knights_config["lancelot"])
    # arthur
    arthur = Knight(knights_config["arthur"])
    # mordred
    mordred = Knight(knights_config["mordred"])
    # red_knight
    red_knight = Knight(knights_config["red_knight"])

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    fight(lancelot, mordred)
    fight(mordred, lancelot)

    # 2 Arthur vs Red Knight:
    fight(arthur, red_knight)
    fight(red_knight, arthur)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
