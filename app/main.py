# Starting project with messy code
from app.config import KNIGHTS
from app.models import Knight
from app.engine import fight


def battle(knights_config: dict) -> dict:
    """
    Run the full battle simulation based on the provided configuration.

    Prepares knight objects, executes scheduled duels
    and returns the final HP status for all participants.
    """
    arthur = Knight(knights_config["arthur"])
    lancelot = Knight(knights_config["lancelot"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    fight(arthur, red_knight)
    fight(red_knight, arthur)

    fight(lancelot, mordred)
    fight(mordred, lancelot)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
