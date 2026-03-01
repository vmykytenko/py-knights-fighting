class Knight:

    def __init__(self, knight_data: dict) -> None:

        self.name = knight_data["name"]
        self.hp = knight_data["hp"]
        self.power = knight_data["power"]
        self.protection = 0

        # 1. Calculate protection from all armour pieces
        for item in knight_data["armour"]:
            self.protection += item["protection"]

        # 2. Add weapon power to base power
        self.power += knight_data["weapon"]["power"]

        # 3. Apply potion effects if present
        potion = knight_data["potion"]
        if potion:
            effect = potion.get("effect", {})
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
