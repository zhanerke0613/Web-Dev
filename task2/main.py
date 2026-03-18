from models import Animal, Dog, Cat


def main():
    animal = Animal("Generic", 5, "black")
    dog = Dog("Bella", 3, "brown", "Labrador")
    cat = Cat("Mia", 2, "white", True)

    animals = [animal, dog, cat]

    for item in animals:
        print(item)
        print(item.info())
        print(item.speak())
        print("-" * 30)

    print(dog.fetch())
    print(cat.scratch())


if __name__ == "__main__":
    main()