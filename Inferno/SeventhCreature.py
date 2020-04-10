from Units.unit import Unit


class SeventhNotUpgraded(Unit):
    """
    Биография:
        Devils призываются из своих пламенных королевств, чтобы повести за
        собой в битву солдат, под командованием героев Sheogh. У них есть
        умение телепортироваться на поле боя, что значит - их враги не смогут
        избежать их жестокости.
    """
    def __init__(self):
        super().__init__("Devil",  # name
                         27,  # attack
                         25,  # protection
                         36,  # min_damage
                         66,  # max_damage
                         166,  # health
                         11,  # initiative
                         7,  # speed
                         None,  # shots
                         None,  # mana
                         2666,  # cost
                         1000,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
        self.special_resource = 1


class SeventhUpgraded(Unit):
    """
    Биография:
        Великие Arch Devils приходят из огненных королевств, чтобы повести за
        собой инфернальное войско. У них есть умение телепортироваться на поле
        боя, что значит - их враги не смогут избежать их жестокости. Из трупов
        поверженных союзников Arch Devils могут призывать Pit Lords, чтобы те
        дрались на их стороне.
    """
    def __init__(self):
        super().__init__("Arch Devil",  # name
                         32,  # attack
                         29,  # protection
                         36,  # min_damage
                         66,  # max_damage
                         199,  # health
                         11,  # initiative
                         7,  # speed
                         None,  # shots
                         None,  # mana
                         3666,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
        self.special_resource = 1
