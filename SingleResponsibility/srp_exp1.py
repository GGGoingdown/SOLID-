food_bowl = 10


class Cat:
    def __init__(self, name: str, food_level: int, cleanliness_level: int) -> None:
        self.name = name
        self.food_level = food_level
        self.cleanliness_level = cleanliness_level

    def meow(self) -> None:
        print("meow~")

    def eat(self) -> None:
        self.food_level -= 10

    def sleep(self) -> None:
        print(f"{self.name} is sleeping")

    # breaking SRP
    # def prepare_food_bowl(self) -> None:
    #     global food_bowl
    #     food_bowl += 10

    # breaking SRP
    # def shower(self) -> None:
    #     self.cleanliness_level += 5


class Owner:
    @staticmethod
    def prepare_food_bowl() -> None:
        global food_bowl
        food_bowl += 10

    @staticmethod
    def shower(cat: Cat) -> None:
        cat.cleanliness_level += 10


if __name__ == "__main__":
    cat = Cat(name="hello kitty", food_level=10, cleanliness_level=10)

    ower = Owner()
    print(f"Before prepare food bowl -> {food_bowl}")
    ower.prepare_food_bowl()
    print(f"After prepare food bowl -> {food_bowl}")

    print(f"Before take a shower -> {cat.cleanliness_level}")
    ower.shower(cat)
    print(f"After take a shower -> {cat.cleanliness_level}")
