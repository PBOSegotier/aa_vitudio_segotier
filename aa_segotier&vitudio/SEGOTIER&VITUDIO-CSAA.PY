# PLANT CLASS
class Plant:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, zombie):
        zombie.health -= self.damage
        print(f"{self.name} attacked {zombie.name}!")
        print(f"Zombie health: {max(0, zombie.health)}")


# ZOMBIE CLASS
class Zombie:
    def __init__(self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.distance = distance

    def attack(self, plant):
        plant.health -= self.damage
        print(f"{self.name} attacked {plant.name}!")
        print(f"{plant.name} health: {max(0, plant.health)}")

    def move_closer(self):
        if self.distance > 0:
            self.distance -= 1
            print(f"The Zombie moved closer!")
            print(f"Distance: {self.distance}")


# MAIN GAME
def run_game():

    # TWO PLANTS WITH DIFFERENT DAMAGE
    peashooter = Plant("Peashooter", 100, 10)
    sunflower = Plant("Sunflower", 80, 5)

    # ZOMBIE
    zombie = Zombie("Basic Zombie", 50, 5, 3)

    print("================================")
    print("     PLANTS VS ZOMBIES GAME")
    print("================================")

    while zombie.health > 0 and (
        peashooter.health > 0 or sunflower.health > 0
    ):

        print("\n-------------------------------")
        print("PLANTS")
        print(f"1. {peashooter.name} - Health: {peashooter.health} - Damage: {peashooter.damage}")
        print(f"2. {sunflower.name} - Health: {sunflower.health} - Damage: {sunflower.damage}")

        print(f"\nZombie Health: {zombie.health}")
        print(f"Zombie Distance: {zombie.distance}")

        # PLAYER CHOOSES PLANT
        print("\nChoose a plant to attack:")
        print("1 - Peashooter")
        print("2 - Sunflower")

        choice = input("Enter your choice: ")

        # PLAYER ATTACK
        if choice == "1":
            if peashooter.health > 0:
                peashooter.attack(zombie)
            else:
                print("Peashooter has been defeated!")

        elif choice == "2":
            if sunflower.health > 0:
                sunflower.attack(zombie)
            else:
                print("Sunflower has been defeated!")

        else:
            print("Invalid choice!")

        # CHECK ZOMBIE
        if zombie.health <= 0:
            print("\n🎉 The Zombie has been defeated!")
            print("YOU WIN!")
            break

        # ZOMBIE MOVES
        zombie.move_closer()

        # ZOMBIE ATTACKS WHEN IT REACHES DISTANCE 0
        if zombie.distance <= 0:

            # Zombie targets Peashooter first
            if peashooter.health > 0:
                zombie.attack(peashooter)

            # Zombie targets Sunflower after Peashooter is defeated
            elif sunflower.health > 0:
                zombie.attack(sunflower)

        # CHECK PLANTS
        if peashooter.health <= 0 and sunflower.health <= 0:
            print("\n💀 Both plants have been defeated!")
            print("GAME OVER!")
            break


# START GAME
if __name__ == "__main__":
    run_game()

