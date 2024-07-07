import threading
import time

class Knights(threading.Thread):
    def __init__(self, name, skill):
        super().__init__()
        self.name = name
        self.skill = skill

    def enemy(self):
        damage = 100
        day = 0
        while damage > 0:
            day += 1
            damage = damage - self.skill
            print(f'День: {day}, {self.name} оставил {damage} врагов')
            time.sleep(1)
            if damage <= 0:
                print(f'Рыцарь {self.name} одержал победу спустя {day} дней!')

    def run(self):
        self.enemy()

Knight_1 = Knights('Sir Lancelot', 10)
Knight_2 = Knights('Sir Galahad', 20)
Knight_1.start()
Knight_2.start()
Knight_1.join()
Knight_2.join()