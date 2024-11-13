import dog

my_dog = dog.Dog("Rex", "SuperDog")
my_dog.bark()

my_other_dog = dog.Dog("Annie", "SuperDog")
print(my_other_dog.name)

my_dog1 = dog.Dog("John", "Shiba Inu")
my_dog1 = dog.Dog("Hermione", "French Bulldog")
my_dog1 = dog.Dog("Harry", "Golden Retriever")

print(f"My dog's name is {my_dog1.name}. He's a {my_dog1.breed}. He can {my_dog1.sits} and {my_dog.roll_over}")
