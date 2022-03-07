class Character:
    def __init__(self, name, lvl, hp, at, df, exp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.at = at
        self.df = df
        self.exp = exp
        self.maxhp = hp

    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name

    def setlvl(self, lvl):
        self.lvl = lvl

    def getlvl(self):
        return self.lvl

    def sethp(self, hp):
        if hp <= 0:
            self.hp = 0
        else:
            self.hp = int(hp)

    def gethp(self):
        return self.hp

    def setat(self, at):
        self.at = at

    def getat(self):
        return self.at

    def setdf(self, df):
        self.df = df

    def getdf(self):
        return self.df

    def setexp(self, exp):
        self.exp = exp

    def getexp(self):
        return self.exp

    def attack(self, other):

        if self.at > other.df:
            other.hp -= self.at - other.df
        else:
            print(self.name, "'s attack is ", self.at, ". ", other.name, "'s defense is ", other.df, ". ", self.name,
                  " is too weak.", sep="")

        if other.hp <= 0:
            other.hp = 0
            print(self.name, " attacked ", other.name, ". ", self.name, "'s HP is ", self.hp, "/", self.maxhp, ". ",
                  other.name, "'s HP is ", other.hp, "/", other.maxhp, ".", sep="")
            print(other.name, "has been defeated.")
        else:
            print(self.name, " attacked ", other.name, ". ", self.name, "'s HP is ", self.hp, "/", self.maxhp, ". ",
                  other.name, "'s HP is ", other.hp, "/", other.maxhp, ".", sep="")


class Player(Character):
    def __init__(self, name, lvl=1, hp=100, at=10, df=5, exp=0):
        Character.__init__(self, name, lvl, hp, at, df, exp)
        self.maxhp = hp
        self.charged = False
        self.shields = 0

    def recover(self, recoverypts):
        self.hp += recoverypts
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        print(self.name, "'s HP has been restored to ", self.hp, "/", self.maxhp, ".", sep="")

    def fullheal(self):
        self.hp = self.maxhp
        print(self.name, "'s HP has been fully restored (", self.hp, "/", self.maxhp, ").", sep="")

    def shield(self):
        self.shields = 3

    def decr_shield(self):
        self.shields -= 1

    def charge(self):
        self.charged = True

    def attack(self, other):
        if self.charged:
            if (2.5 * self.at) > other.df:
                other.sethp(other.hp - (2.5 * self.at - other.df))
            else:
                print(self.name, "'s attack is ", self.at, ". ", other.name, "'s defense is ", other.df, ". ",
                      self.name, " is too weak.", sep="")
            self.charged = False
        else:
            if self.at > other.df:
                other.sethp(other.hp - (self.at - other.df))
            else:
                print(self.name, "'s attack is ", self.at, ". ", other.name, "'s defense is ", other.df, ". ",
                      self.name, " is too weak.", sep="")

        if other.hp <= 0:
            other.hp = 0
            print(self.name, " attacked ", other.name, ". ", self.name, "'s HP is ", self.hp, "/", self.maxhp, ". ",
                  other.name, "'s HP is ", other.hp, "/", other.maxhp, ".", sep="")
            print(other.name, "has been defeated.")
        else:
            print(self.name, " attacked ", other.name, ". ", self.name, "'s HP is ", self.hp, "/", self.maxhp, ". ",
                  other.name, "'s HP is ", other.hp, "/", other.maxhp, ".", sep="")


class Minion(Character):
    def __init__(self, name, lvl=1, hp=0, at=0, df=0, exp=0):
        Character.__init__(self, name, lvl, hp, at, df, exp)


class Boss(Character):
    def __init__(self, name, lvl=1, hp=100, at=100, df=0, exp=0):
        Character.__init__(self, name, lvl, hp, at, df, exp)
        self.maxhp = 100

    def spawn(self):
        newminion = Minion("Minion", self.lvl, int(int(self.maxhp) / 4), int(self.at / 4))
        print("Boss spawned Minion (", "HP ", newminion.hp, ", AT ", newminion.at, ", DF ", newminion.df, ")", sep="")
        return newminion


'''Test code
mainchar = Player("Alpha", df=5, exp=100)
opponent = Player("Beta", hp=106, at=11, df=2, exp=100)
while (mainchar.gethp() > 0 and opponent.gethp() > 0):
    mainchar.attack(opponent)
    if opponent.gethp() > 0:
        opponent.attack(mainchar)

mainchar.recover(40)
mainchar.recover(40)
opponent.fullheal()
mainchar.charge()
mainchar.charge()
'''

numPlayer = 0
while True:
    numPlayer = input("How many player? ")
    substring = '.'
    if not numPlayer.isnumeric():
        if substring in numPlayer:
            print("Error. Please enter an integer.")
        else:
            print("Error. Please enter a positive integer.")
    else:
        break

playerlist = []
for i in range(int(numPlayer)):
    newplayer = input("Player " + str(i + 1) + " name: ")
    player = Player(str(newplayer))
    playerlist.append(player)

minionlist = []
boss = Boss("Boss", hp=20 * int(numPlayer))
boss.maxhp = boss.hp
minion = boss.spawn()
minionlist.append(minion)

while True:
    for i in range(int(numPlayer)):

        print("1. Attack \n", "2. Charge \n", "3. Shield", sep="")
        action = eval(input(playerlist[i].name + ", what would you like to do? "))

        if action == 1:
            if len(minionlist) == 0:
                print("1. Boss (HP ", boss.gethp(), ")", sep="")
                playerlist[i].attack(boss)
            else:
                for j in range(len(minionlist)):
                    print(j + 1, ". Minion (HP ", minionlist[j].hp, ")", sep="")
                numattack = input(playerlist[i].name + ", who would you like to attack? ")
                playerlist[i].attack(minionlist[int(numattack)-1])
                if minionlist[int(numattack)-1].gethp() == 0:
                    del minionlist[int(numattack)-1]

        if action == 2:
            if playerlist[i].charged:
                print(playerlist[i].name, " already charged. Attack remains as ", playerlist[i].at, ".", sep="")
            else:
                playerlist[i].charge()
                print(playerlist[i].name, " charged. Attack is increased to ", int(2.5*playerlist[i].at), " from ",
                      playerlist[i].at, ".", sep="")

        if action == 3:
            playerlist[i].shield()
            print(playerlist[i].name, "is safe from the next", playerlist[i].shields, "attacks.")

    if boss.hp == 0:
        print("You win!")
        break

    if len(minionlist) == 0:
        print("There are no Minions to attack.")
    else:
        ## Find the index of the player with the lowest HP who was created the last
        hplist = []
        for k in range(len(playerlist)):
            hplist.append(playerlist[k].hp)
        hplist.reverse()
        weakest = len(hplist) - 1 - hplist.index(min(hplist))

        for j in range(len(minionlist)):
            if playerlist[weakest].shields <= 0:
                minionlist[j].attack(playerlist[weakest])
                if playerlist[weakest].hp == 0:
                    del playerlist[weakest]
            else:
                playerlist[weakest].decr_shield()
                print("Minion attached.", playerlist[weakest].name, "is safe from the next",
                      playerlist[weakest].shields, "attacks")

    if len(playerlist) == 0:
        print("You lose.")
        break

    minion = boss.spawn()
    minionlist.append(minion)
