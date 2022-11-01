from random import randint
import json
import pandas as pd
from abc import ABC


class ZenArt:
    resultant_list = []
    resultant_dict = {}

    def random_number_gen(self):
        for i in range(10):
            self.resultant_list.append(randint(0,100))
        return self.resultant_list

    def dic_generator(self):
        for i in self.resultant_list:
            if i not in self.resultant_dict.keys():
                self.resultant_dict[i] = 1
            else:
                self.resultant_dict[i] = self.resultant_dict[i] +1
        return self.resultant_dict

    def arithmetic_error(self):
        try:
            # Type any arithmetic operation
            arithmetic=5/0
            print(arithmetic)
        # If any arithmetic operation fails it will be handeled by this exception
        except ArithmeticError as e:
            print(f'ArithmeticError occured: {e}, {e.__class__}')
        # Handling other than any arithmetic operation
        except:
            print('Some error occurred.')


# Abstract Class
class Animal(ABC):
    def traits(self):
        pass

# Parent Class
class Dog(Animal):
    def intro(self):
        print(f'Hi I am a dog.')
        print(f'I have 4 legs.')
    def skills(self):
        print('Dogs are emotionally intelligent.')
    # def traits(self):
    #     print('Dog is an animal.')


# Child Class
class Tommy(Dog):
    def __init__(self,skill):
        self.skill = skill
        # invoking init of parent class
        Dog.__init__(self)

    def skills(self):
        print(f'Hi I am tommy I can {self.skill}.')


if __name__=='__main__':
    try:
        # making the object of the class zen_art
        Test_cases = ZenArt()
        # method for generating the list of random numbers of length10
        random_numbers = Test_cases.random_number_gen()
        # method for generating the dictionary containing number as key and value as the number of occurrences
        count_dict = Test_cases.dic_generator()
        print(random_numbers)
        print(count_dict)
        # lambda function for generating squares
        square_gen = lambda x:x**2
        # lambda function for generating cubes
        cube_gen = lambda x:x**3
        print([square_gen(x) for x in random_numbers])
        print([cube_gen(x) for x in random_numbers])
        # arithmetic error testing
        Test_cases.arithmetic_error()
        # Loading the dictionary into txt file Staging.txt in the form of Json
        with open('Staging.txt','w') as output:
            output.write(json.dumps(count_dict,indent=4))
        # Getting the data from the txt file
        txt_file_data = json.load(open('Staging.txt'))
        # Putting the data into pandas dataframe
        df=pd.DataFrame(txt_file_data,index=[0]).T
        # generating the CSV File from the txt file with the name Zenart_test.csv
        df.to_csv('Zenart_test.csv',header=False,index=True)
        # Inheritance
        dog1 = Tommy('Run very fast')
        # Calling the function of the parent class using its intance
        dog1.intro()
        # skills method is overrided
        dog1.skills()
        #Abstraction
        animal1 = Dog()
        #traits method is taken from the dog class
        animal1.traits()
        animal1.skills()
    except Exception as e:
        print('The following error occurred: '+ str(e))


