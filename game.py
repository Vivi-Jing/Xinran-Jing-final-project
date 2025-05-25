import random

class Player:
    def __init__(self):
        self.level = 1
        self.exp = 0
        self.exp_to_level = 100
        self.hp = 100
        self.max_hp = 100


    def gain_exp(self, amount):
        self.exp += amount
        print(f"[EXP +{amount}] Current EXP:{self.exp}/{self.exp_to_level}")
        while self.exp >= self.exp_to_level and self.level < 3:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp -= self.exp_to_level
        self.exp_to_level += 50
        self.max_hp += 20
        self.hp = self.max_hp
        print(f"Level up!Current Level:{self.level},Max HP:{self.max_hp}")

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
        print(f"[Heal +{amount}] Current HP:{self.hp}/{self.max_hp}")

    def take_damage(self, amount):
        self.hp -= amount
        print(f"[Suffer Damage! HP -{amount}] Current HP:{self.hp}/{self.max_hp}")
        if self.hp <= 0:
            print("You die! Game Over!")
            return True
        return False




def explore(player):
    print()
    print("Entering a mysterious place")
    event = random.choice(["healing", "exp_bottle", "battle", "nothing"])
    if event == "healing":
        amount = random.randint(5, 20)
        print(f"You find a Health Potion and restore {amount} HP")
        player.heal(amount)
    elif event == "exp_bottle":
        amount = random.randint(10, 30)
        print(f"You find a Experience Potion and get {amount} EXP")
        player.gain_exp(amount)
    elif event == "battle":
        print("You find a Monster!")
        damage = random.randint(15, 40)
        exp = random.randint(15, 30)
        if not player.take_damage(damage):
            print(f"You win the war and get {exp} EXP")
            player.gain_exp(exp)
    else:
        print("You do not find anything")



def main():
    player = Player()
    print("Your adventure begins now!")

    while player.hp > 0:
        print()
        print("Choose your action")
        print("1. Explore a new area")
        print("2. View your status")
        print("3. Exit the game")

        choice = input("Please enter a number:")
        if choice == "end":
            print("tips: game will stop and exit directly if you enter an end")
            break
        elif choice == "1":
            explore(player)

        elif choice == "2":
            print(f"Level:{player.level}  EXP:{player.exp}/{player.exp_to_level}")
            print(f"HP:{player.hp}/{player.max_hp}")
        elif choice == "3":
            print("Successfully exit the game. Thanks for your playing!")
            break
        else:
            print("Invalid input. Please enter again.")
            
        if player.level >= 3:
            print("Congratulations! You've reached the max level and completed your adventure!")
            break


if __name__ == "__main__":
    main()
