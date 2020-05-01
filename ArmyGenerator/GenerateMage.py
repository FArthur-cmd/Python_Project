from Heroes.HeroCatalog.Mage.Orra import Mage
from Heroes.HeroCatalog.Mage.Zexir import Alchemist
from Units.Creator import Creator
from Classes.Mage.FirstCreature import FirstUpgraded, FirstNotUpgraded
from Classes.Mage.SecondCreature import SecondUpgraded, SecondNotUpgraded
from Classes.Mage.ThirdCreature import ThirdUpgraded, ThirdNotUpgraded
from Classes.Mage.FourthCreature import FourthUpgraded, FourthNotUpgraded
from Classes.Mage.FifthCreature import FifthUpgraded, FifthNotUpgraded
from Classes.Mage.SixthCreature import SixthUpgraded, SixthNotUpgraded
from Classes.Mage.SeventhCreature import SeventhUpgraded, SeventhNotUpgraded


class mage(Creator):
    def create_first_type_creatures(self):
        self.first_creature = FirstNotUpgraded()
        self.first_creature_upgraded = FirstUpgraded()

    def create_second_type_creatures(self):
        self.second_creature = SecondNotUpgraded()
        self.second_creature_upgraded = SecondUpgraded()

    def create_third_type_creatures(self):
        self.third_creature = ThirdNotUpgraded()
        self.third_creature_upgraded = ThirdUpgraded()

    def create_fourth_type_creatures(self):
        self.fourth_creature = FourthNotUpgraded()
        self.fourth_creature_upgraded = FourthUpgraded()

    def create_fifth_type_creatures(self):
        self.fifth_creature = FifthNotUpgraded()
        self.fifth_creature_upgraded = FifthUpgraded()

    def create_sixth_type_creatures(self):
        self.sixth_creature = SixthNotUpgraded()
        self.sixth_creature_upgraded = SixthUpgraded()

    def create_seventh_type_creatures(self):
        self.seventh_creature = SeventhNotUpgraded()
        self.seventh_creature_upgraded = SeventhUpgraded()

    def create_hero_First(self):
        self.first_hero = Mage()

    def create_hero_Second(self):
        self.second_hero = Alchemist()
