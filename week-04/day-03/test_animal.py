import unittest
from animal import Animal 

class TestAnimal(unittest.TestCase):
    def test_empty_animal_hunger(self):
        dog = Animal()
        self.assertEqual(dog.hunger, 50)

    def test_empty_animal_thirst(self):
        dog = Animal()
        self.assertEqual(dog.thirst, 50)
    
    def test_given_animal_hunger(self):
        cat = Animal(10, 20)
        self.assertEqual(cat.hunger, 10)         

    def test_given_animal_thirst(self):
        cat = Animal(10, 20)
        self.assertEqual(cat.thirst, 20)
    
    def test_animal_eat(self):
        dog = Animal()
        dog.eat()
        self.assertEqual(dog.hunger, 49)

    def test_animal_eat(self):
        dog = Animal()
        dog.drink()
        self.assertEqual(dog.thirst, 49)    
                
    def test_animal_play(self):
        dog = Animal()
        dog.play()
        self.assertEqual(dog.thirst, 51)  
        self.assertEqual(dog.hunger, 51)

if __name__ == '__main__':
    unittest.main()