# Import Modules

# Classes==============================================

# Unit Common Stat
class Unit:
    ally_counter = 0
    enemy_counter = 0

    # Initialize
    def __init__(self, NAME, TEAM):
        self.TEAM = ""
        self.RACE = ""
        self.NAME = ""
        self.HP = 0
        self.ATK = 0
        self.DEF = 0
        self.POISONED = False
        self.FROZEN = False
        self.RANK = 1
        self.ALIVE = True
        self.EXP = 0
    
    def set_name(self, NAME):
        self.NAME = NAME

    def set_team(self, TEAM):
        self.TEAM = TEAM

    def set_race(self, RACE):
        self.RACE = RACE

    # Attack Function
    def attack(self, TARGET):
        if self.ALIVE == True:
            if self.TEAM == TARGET.TEAM:
                print("NO FRIENDLY FIRE")
            elif TARGET.ALIVE == False:
                print("Can't attack the dead person")
            else:
                if TARGET.DEF >= self.ATK:
                    pass
                else:
                    TARGET.HP = TARGET.HP + TARGET.DEF - self.ATK

                    # EXP GAIN [ALLY]
                    self.EXP += self.ATK

                    # EXP GAIN [ENEMY]
                    TARGET.EXP += TARGET.DEF


                if TARGET.HP <= 0:
                    TARGET.ALIVE = False
        else:
            print("You can't attack when you are dead")

    # Stats of the unit
    def stat(self):
        return self.RACE, self.NAME, self.HP, self.ATK, self.DEF, self.TEAM, self.RANK, self.ALIVE, self.EXP

class Ogre(Unit):
    def __init__(self):
        self.HP = 40
        self.ATK = 7
        self.DEF = 3
        self.ACCURACY = .5
        self.RANK = 1
        self.EXP = 0
        self.ALIVE = True

    def rank_up(self):
        if self.EXP >= 40 and self.RANK == 1:
            self.HP = 45
            self.ATK = 8
            self.DEF = 4
            self.EXP = 0
            self.RANK = 2
        
        elif self.EXP >= 40 and self.RANK == 2:
            self.HP = 50
            self.ATK = 12
            self.DEF = 5
            self.EXP = 0
            self.RANK = 3

class Knight(Unit):
    def __init__(self):
        self.HP = 45
        self.ATK = 5
        self.DEF = 5
        self.RANK = 1
        self.EXP = 0
        self.ALIVE = True

    def rank_up(self):
        if self.EXP >= 40 and self.RANK == 1:
            self.HP = 50
            self.ATK = 6
            self.DEF = 6
            self.EXP = 0
            self.RANK = 2
        
        elif self.EXP >= 40 and self.RANK == 2:
            self.HP = 60
            self.ATK = 8
            self.DEF = 8
            self.EXP = 0
            self.RANK = 3

class Sorcerer(Unit):
    def __init__(self):
        self.HP = 30
        self.ATK = 3
        self.DEF = 2
        self.RANK = 1
        self.EXP = 0
        self.ALIVE = True

    # Magic
    def magic(self):
        def cure(self):
            pass
        
        def poison(self):
            pass

        def freeze(self):
            pass

    def rank_up(self):
        if self.EXP >= 40 and self.RANK == 1:
            self.HP = 35
            self.ATK = 4
            self.DEF = 3
            self.EXP = 0
            self.RANK = 2
        
        elif self.EXP >= 40 and self.RANK == 2:
            self.HP = 40
            self.ATK = 6
            self.DEF = 5
            self.EXP = 0
            self.RANK = 3

# Functions====================================================
def inputChecker(INPUT, END, MESSAGE):
    while not INPUT.isdigit() or int(INPUT) <= 0 or int(INPUT) > END:
        top_line("WRONG VALUE")
        print("You entered wrong value, Please Try again")
        print(MESSAGE)
        INPUT = input("Choose one : ")
    return int(INPUT)

def top_line(TITLE):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n==== " + TITLE +" " +"=" * (43 - len(TITLE)))

def turn_line(NUMBER, PLAYING):
    print("\n==== "+"TURN "+ str(NUMBER) +" ["+ PLAYING +"] "+"=" * (35 - (len(str(NUMBER))+ len(PLAYING))))

# Settings=====================================================

# Start Menu
def start_menu():
    global start

    top_line("MAIN MENU")
    print("Welcome to the game!")
    print("\n1. Start the Game\n2. Quit\n")
    start = input("Choose one : ")
    start = inputChecker(start, 2, "\n1. Start the Game\n2. Quit\n")

# Opponent, # of Players, and Race selection
def setting_game():
    global type_game
    global num_player
    global objs_ally
    global objs_enemy
    objs_ally = []
    objs_enemy = []

    top_line("OPPONENT SETTING")
    print("\n1. Player vs Player\n2. Player vs A.I.\n")
    type_game = input("Choose one : ")
    type_game = inputChecker(type_game, 2, "\n1. Player vs Player\n2. Player vs A.I.\n")

    top_line("# OF PLAYERS")
    print("\n1. 1vs1\n2. 2vs2\n3. 3vs3\n4. 4vs4\n5. 5vs5\n")
    num_player = input("Choose one : ")
    num_player = inputChecker(num_player, 5, "\n1. 1vs1\n2. 2vs2\n3. 3vs3\n4. 4vs4\n5. 5vs5\n")
    
    # Making list of Players
    for units in range(num_player):
        player = f'player_{str(units+1)}'
        enemy = f'enemy_{str(units+1)}'
        objs_ally.append(player)
        objs_enemy.append(enemy)

    # Object setting [Player Side]
    for num in range(num_player):
        temp_1 = num
        top_line("CHOOSE THE RACE OF YOUR [ALLY]")
        print("\n1. [Ogre]\n\tOgres have strong power, but have low accuracy\n")
        print("2. [Knight]\n\tKnight have decent power and strong defence power\n")
        print("3. [Sorcerer]\n\tSorcerer have weak body, but they can cast powerful magics\n")
        num = input("Choose one for player %d: " %(num+1))                     #added "for player" and %d to specify number(easy to recognize)
        num = inputChecker(num, 3, "\n1. [Ogre]\n\tOgres have strong power, but have low accuracy\n\n2. [Knight]\n\tKnight have decent power and strong defence power\n\n3. [Sorcerer]\n\tSorcerer have weak body, but they can cast powerful magics\n")
        if num == 1:
            objs_ally[temp_1] = Ogre()
            objs_ally[temp_1].set_race("Ogre")
        elif num == 2:
            objs_ally[temp_1] = Knight()
            objs_ally[temp_1].set_race("Knight")
        else:
            objs_ally[temp_1] = Sorcerer()
            objs_ally[temp_1].set_race("Sorcerer")

    # Object setting [Enemy Side]
    for num in range(num_player):
        temp_1 = num
        top_line("CHOOSE THE RACE OF YOUR [ENEMY]")
        print("\n1. [Ogre]\n\tOgres have strong power, but have low accuracy\n")
        print("2. [Knight]\n\tKnight have decent power and strong defence power\n")
        print("3. [Sorcerer]\n\tSorcerer have weak body, but they can cast powerful magics\n")
        num = input("Choose one for enemy %d: " %(num+1))                        #added "for enemy" and %d to specify number(easy to recognize)
        num = inputChecker(num, 3, "\n1. [Ogre]\n\tOgres have strong power, but have low accuracy\n\n2. [Knight]\n\tKnight have decent power and strong defence power\n\n3. [Sorcerer]\n\tSorcerer have weak body, but they can cast powerful magics\n")
        if num == 1:
            objs_enemy[temp_1] = Ogre()
            objs_enemy[temp_1].set_race("Ogre")
        elif num == 2:
            objs_enemy[temp_1] = Knight()
            objs_enemy[temp_1].set_race("Knight")
        else:
            objs_enemy[temp_1] = Sorcerer()
            objs_enemy[temp_1].set_race("Sorcerer")

    # Naming the units
    for num in range(num_player):
        top_line("NAME YOUR [PLAYER]")
        name = input(f'\nPlease enter the name of the player_{num+1} : ')
        name = name.strip()
        while name == '':
            top_line("WRONG VALUE")
            name = input(f'\nPlease enter the name of the player_{num+1} : ')
            name = name.strip()
        player = objs_ally[num]
        player.set_name(name)
        # Set TEAM
        player.set_team("ALLY")
        Unit.ally_counter += 1

    for num in range(num_player):
        top_line("NAME YOUR [OPPONENT]")
        name = input(f'\nPlease enter the name of the Enemy_{num+1} : ')
        name = name.strip()
        while name == '':
            top_line("WRONG VALUE")
            name = input(f'\nPlease enter the name of the Enemy_{num+1} : ')
            name = name.strip()
        player = objs_enemy[num]
        player.set_name(name)
        # Set TEAM
        player.set_team("ENEMY")
        Unit.enemy_counter += 1

# GAME ==========================================================
def show_stats():
    top_line("PLAYER'S STAT")
    for a in range(num_player):
        player = objs_ally[a].stat()
        objs_ally[a].rank_up()
        if player[7] == True:
            print("\nRACE : {0} / NAME : {1} / HP : {2} / ATK : {3} / DEF : {4} / TEAM : {5} / RANK : {6} / EXP : {7}" \
                .format(player[0], player[1], player[2], player[3], player[4], player[5], player[6], player[8]))
        else:
            print("\n{0} is DEAD" .format(player[1]))
            Unit.ally_counter -= 1
    
    print()

    for a in range(num_player):
        enemy = objs_enemy[a].stat()
        objs_enemy[a].rank_up()
        if enemy[7] == True:
            print("\nRACE : {0} / NAME : {1} / HP1 : {2} / ATK : {3} / DEF : {4} / TEAM : {5} / RANK : {6} / EXP : {7}" \
                .format(enemy[0], enemy[1], enemy[2], enemy[3], enemy[4], enemy[5], enemy[6], enemy[8]))
        else:
            print("\n{0} is DEAD" .format(enemy[1]))
            Unit.enemy_counter -= 1

def play():
    GAME = True
    turn = 1
    if start == 1:
        while GAME:
            # Exit the game if ther is noone left
            if Unit.ally_counter == 0 or Unit.enemy_counter == 0: break
            print(f"\nTURN : {turn}")
            show_stats()

            # ALLY FIRST
            turn_line(turn, "ALLY'S TURN")
            print()
            for a in range(num_player):
                ally_obj = objs_ally[a].stat()
                if ally_obj[7] == True:
                    print(str(a+1) + ".", objs_ally[a].stat()[1] + " (" + objs_ally[a].stat()[0] + ")")
            player = input("\nChoose your player : ")
            while not player.isdigit() or int(player) < 0 or int(player) > num_player:
                for a in range(num_player):
                    print(str(a+1) + ".", objs_ally[a].stat()[1] + " (" + objs_ally[a].stat()[0] + ")")
                player = input("\nWho would you attack? : ")
            player = int(player)

            for a in range(num_player):
                enemy_obj = objs_enemy[a].stat()
                if enemy_obj[7] == True:
                    print(str(a+1) + ".", objs_enemy[a].stat()[1] + " (" + objs_enemy[a].stat()[0] + ")")
            enemy = input("\nWho would you attack? : ")
            while not enemy.isdigit() or int(enemy) < 0 or int(enemy) > num_player:
                for a in range(num_player):
                    print(str(a+1) + ".", objs_enemy[a].stat()[1] + " (" + objs_enemy[a].stat()[0] + ")")
                enemy = input("\nWho would you attack? : ")
            enemy = int(enemy)
            objs_ally[player-1].attack(objs_enemy[enemy-1])

            show_stats()
            if Unit.ally_counter == 0 or Unit.enemy_counter == 0: break

            # ENEMY'S TURN
            turn_line(turn, "ENEMY'S TURN")
            print()
            for a in range(num_player):
                enemy_obj = objs_enemy[a].stat()
                if enemy_obj[7] == True:
                    print(str(a+1) + ".", enemy_obj[1] + " (" + enemy_obj[0] + ")")
            player = input("\nChoose your player : ")
            while not player.isdigit() or int(player) < 0 or int(player) > num_player:
                for a in range(num_player):
                    print(str(a+1) + ".", objs_enemy[a].stat()[1] + " (" + objs_enemy[a].stat()[0] + ")")
                player = input("\nWho would you attack? : ")
            player = int(player)
            print()
            for a in range(num_player):
                ally_obj = objs_ally[a].stat()
                if ally_obj[7] == True:
                    print(str(a+1) + ".", ally_obj[1] + " (" + ally_obj[0] + ")")
            enemy = input("\nWho would you attack? : ")
            while not enemy.isdigit() or int(enemy) < 0 or int(enemy) > num_player:
                for a in range(num_player):
                    print(str(a+1) + ".", objs_ally[a].stat()[1] + " (" + objs_ally[a].stat()[0] + ")")
                enemy = input("\nWho would you attack? : ")
            enemy = int(enemy)
            objs_enemy[player-1].attack(objs_ally[enemy-1])

            turn += 1


# Start
def main():
    start_menu()
    if start == 1:
        setting_game()
        play()
    
main()
