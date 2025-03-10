import random

class Robot:
    def __init__(self, name, hp, attack_power, attack_accuracy):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.attack_accuracy = attack_accuracy

    def attack_enemy(self, enemy):
        if random.random() <= self.attack_accuracy:
            enemy.hp -= self.attack_power
            print(f"{self.name} menyerang {enemy.name} dan menyebabkan {self.attack_power} damage!")
        else:
            print(f"{self.name} gagal menyerang {enemy.name}!")

    def regen_health(self, amount):
        self.hp += amount
        print(f"{self.name} melakukan regenerasi {amount}. HP sekarang: {self.hp}")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} [{self.hp}|{self.attack_power}]"


class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.round = 1

    def play(self):
        while self.robot1.is_alive() and self.robot2.is_alive():
            print(f"\nRound-{self.round} ==========================================================")
            print(self.robot1)
            print(self.robot2)

            for robot in [self.robot1, self.robot2]:
                action = self.get_action(robot)
                if action == 1:
                    robot.attack_enemy(self.robot2 if robot == self.robot1 else self.robot1)
                elif action == 2:
                    robot.regen_health(10)
                elif action == 3:
                    print(f"{robot.name} menyerah!")
                    return

            self.round += 1

        self.declare_winner()

    def get_action(self, robot):
        while True:
            try:
                print(f"\n{robot.name}, pilih aksi:")
                print("1. Attack")
                print("2. Defense (Regenerate Health)")
                print("3. Give up")
                action = int(input("Pilih aksi (1/2/3): "))
                if action in [1, 2, 3]:
                    return action
                else:
                    print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka.")

    def declare_winner(self):
        if self.robot1.is_alive():
            print(f"{self.robot1.name} menang!")
        elif self.robot2.is_alive():
            print(f"{self.robot2.name} menang!")
        else:
            print("Pertarungan berakhir seri!")

robot1 = Robot("Alpha", 500, 10, 0.8)  # 80% akurasi serangan
robot2 = Robot("Uranus", 750, 8, 0.7)  # 70% akurasi serangan

game = Game(robot1, robot2)
game.play()
