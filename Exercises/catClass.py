class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

def older (age1, age2, age3):
    high = age1
    if(age2 > high):
        high = age2

    if (age3 > high):
        high = age3

    return high

cat1 = Cat('Jack', 11)
cat2 = Cat('Carl', 7)
cat3 = Cat('Hector', 2)

oldest = older(cat1.age, cat2.age, cat3.age)

print(f'The oldest cat is {oldest} years old')