import random

WTF_factor = random.randint(1,3) 

#character stats
name = input('enter ur hero\'s name >> ')

def print_stats(hp,dmg,inv):
    print(f'{name}\'s hp is {hp}')
    print(F'{name}\'s dmg is {dmg}')
    print(f'{name}\'s inventory capacity is {inv} ')

