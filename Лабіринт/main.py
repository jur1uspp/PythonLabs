from abc import ABC, abstractmethod

# Абстрактні класи
class MazeFactory(ABC):
    @abstractmethod
    def create_room(self):
        pass
    
    @abstractmethod
    def create_wall(self):
        pass
    
    @abstractmethod
    def create_enemy(self):
        pass

class Room(ABC):
    @abstractmethod
    def __str__(self):
        pass

class Wall(ABC):
    @abstractmethod
    def __str__(self):
        pass

class Enemy(ABC):
    @abstractmethod
    def __str__(self):
        pass

# Конкретні продукти
class WinterRoom(Room):
    def __str__(self):
        return "Winter Room"

class WinterWall(Wall):
    def __str__(self):
        return "Winter Wall"

class WinterEnemy(Enemy):
    def __str__(self):
        return "Winter Enemy"

class DesertRoom(Room):
    def __str__(self):
        return "Desert Room"

class DesertWall(Wall):
    def __str__(self):
        return "Desert Wall"

class DesertEnemy(Enemy):
    def __str__(self):
        return "Desert Enemy"

class JungleRoom(Room):
    def __str__(self):
        return "Jungle Room"

class JungleWall(Wall):
    def __str__(self):
        return "Jungle Wall"

class JungleEnemy(Enemy):
    def __str__(self):
        return "Jungle Enemy"

# Конкретні фабрики
class WinterMazeFactory(MazeFactory):
    def create_room(self):
        return WinterRoom()

    def create_wall(self):
        return WinterWall()

    def create_enemy(self):
        return WinterEnemy()

class DesertMazeFactory(MazeFactory):
    def create_room(self):
        return DesertRoom()

    def create_wall(self):
        return DesertWall()

    def create_enemy(self):
        return DesertEnemy()

class JungleMazeFactory(MazeFactory):
    def create_room(self):
        return JungleRoom()

    def create_wall(self):
        return JungleWall()

    def create_enemy(self):
        return JungleEnemy()

# Клієнтський код
def create_maze(factory):
    print(f"Room created: {factory.create_room()}")
    print(f"Wall created: {factory.create_wall()}")
    print(f"Enemy created: {factory.create_enemy()}")

def main():
    factories = [WinterMazeFactory(), DesertMazeFactory(), JungleMazeFactory()]
    themes = ["Winter", "Desert", "Jungle"]
    
    for theme, factory in zip(themes, factories):
        print(f"Creating {theme} Maze:")
        create_maze(factory)
        print()

if __name__ == "__main__":
    main()
