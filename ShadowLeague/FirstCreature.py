from Units.unit import Unit


class FirstNotUpgraded(Unit):
    """
    Биография:
         Основная роль Scouts на поле боя - вести стрелковую атаку с помощью
         своих самострелов. Но в то же время, они прекрасно тренированы и для
         ближнего боя, и смогут защитить себя в рукопашных схватках.
    """
    def __init__(self):
        super().__init__("Scout",  # name
                         3,  # attack
                         3,  # protection
                         2,  # min_damage
                         4,  # max_damage
                         10,  # health
                         10,  # initiative
                         5,  # speed
                         5,  # shots
                         None,  # mana
                         60,  # cost
                         40,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count


class FirstUpgraded(Unit):
    """
    Биография:
         Основная роль Assassins на поле боя - вести стрелковую атаку своими
         смертельными арбалетами. Используя зачарованные стрелы, они наносят
         тяжкие и отравленные раны своим врагам.
    """
    def __init__(self):
        super().__init__("Assassin",  # name
                         4,  # attack
                         3,  # protection
                         2,  # min_damage
                         4,  # max_damage
                         6,  # health
                         12,  # initiative
                         5,  # speed
                         5,  # shots
                         None,  # mana
                         100,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
