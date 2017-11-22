from random import randint

# HAS-A Boat


class Boat:
    def __init__(self, capacity):
        if capacity > 60:
            raise BaseException('Boat capacity can not be greater that 60 kg.')

        self.capacity = capacity

# HAS-A TreasureChest


class TreasureChest:
    def __init__(self):
        self.weight = randint(4, 10)
        content = randint(1, 3)
        if content == 1:
            self.content = Content()
        elif content == 2:
            self.content = GoldCoins(randint(15, 100))
        elif content == 3:
            self.content = Illness(randint(3, 10))

#  TreasureChest HAS-A Gold coins/Illness/Null content


class Content:
    def __init__(self):
        self.amount = 0


class GoldCoins(Content):
    def __init__(self, gold_amount):
        self.amount = gold_amount


class Illness(Content):
    def __init__(self, illness_time):
        self.amount = illness_time


class Pirate:
    def __init__(self, name, boat_capacity):
        self.name = name
        self.boat = Boat(boat_capacity)
        self.goldAmount = 0
        self.illTime = 0
        self.illTimes = 0
        self.chestAmount = 0
        self.emptyChests = 0

        while self.boat.capacity > 0:
            chest = TreasureChest()
            self.boat.capacity -= chest.weight

            if self.boat.capacity < 0:
                self.boat.capacity = 0
                break

            self.chestAmount += 1
            if isinstance(chest.content, Illness):
                self.illTime += chest.content.amount
                self.illTimes += 1
            elif isinstance(chest.content, GoldCoins):
                self.goldAmount += chest.content.amount
            else:
                self.emptyChests += 1

    def get_chests_amount(self):
        return self.chestAmount

    def get_pirate_gold(self):
        return self.goldAmount

    def get_pirate_illness(self):
        return self.illTimes, self.illTime

    def get_empty_chests(self):
        return self.emptyChests


def main():
    p1 = Pirate('Vasya', 30)
    p2 = Pirate('Kirill', 40)
    p3 = Pirate('Kostya', 60)
    p4 = Pirate('Artashes', 10)

    pirate_list = [p1, p2, p3, p4]

    max_gold = -1
    ill_times = -1
    empty_chests = -1

    for each in pirate_list:
        print('{} carried {} chests.'.format(each.name, each.chestAmount))
        if max_gold < each.get_pirate_gold():
            max_gold = each.get_pirate_gold()
        if ill_times < each.get_pirate_illness()[0]:
            ill_times = each.get_pirate_illness()[0]
        if empty_chests < each.get_empty_chests():
            empty_chests = each.get_empty_chests()

    for each in pirate_list:
        if each.get_pirate_gold() == max_gold:
            print('{} got {} gold.'.format(each.name, max_gold))
        if each.get_pirate_illness()[0] == ill_times:
            print('{} got sick {} times and was sick for {} days.'.format(each.name, each.illTimes, each.illTime))
        if each.get_empty_chests() == empty_chests:
            print('{} got {} empty chests'.format(each.name, each.get_empty_chests()))


if __name__ == '__main__':
    main()   
