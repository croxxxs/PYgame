import random

ogre_hp = 175
ogre_dmg = 30
ogre_shield = 0

WTF_factor = random.randint(1,3) 
#character stats
name = input('enter ur hero\'s name >> ')

def print_stats(hp,dmg,inv,shield,):
    print(f'the {name}\'s stats:')
    print(f'{name}\'s hp is {hp}')
    print(F'{name}\'s dmg is {dmg}')
    print(f'{name}\'s inventory capacity is {inv} ')
    if WTF_factor == 2 or WTF_factor == 3:
        print(f'because u are not a child u can bring a shield with you \n shield\'s toughness is {shield}')


if WTF_factor == 1:
    print(f'for an undescribeble pity, {name} is a little child')
    hp1 = 100
    dmg1 = 25
    inv1 = 2
    shield1 = 0
    print_stats(hp1,dmg1,inv1,shield1)

if WTF_factor == 2:
    print(F'{name} is base adult knight')
    hp2 = 175
    dmg2 = 75
    inv2 = 4
    shield2 = 50
    print_stats(hp2,dmg2,inv2,shield2)

if WTF_factor == 3:
    print(f'for an undiscribeble luck, {name} is caster')
    hp3 = 150
    dmg3 = 150
    inv3 = 5
    shield3 = 150
    print_stats(hp3,dmg3,inv3,shield3)

def chosing():
    print('what would you like to do?\n 1 - run away \n 2 - get the fight')
    action = 0
    answ = int(input('>>'))
    while answ < 1 or answ > 2:
        print('please, be intellegent and write number in spree of 1 - 2')
        answ = int(input('>>'))

    if answ == 1:
        if Fight_count ==1:
            print('you\'ve succsesfully run away')
        action = 1

    if answ == 2:
        print('u got all your braveness to a hand and claimed an Ogre\'s battle call')
        action = 2
    return answ

def attack(hp,e_shield):
    print(f'{name} attacks')
    overall_hp = hp + e_shield
    if WTF_factor == 1:
        if overall_hp > 0:
            overall_hp -= dmg1
            print(f'enemy\'s hp is {overall_hp}')
        if overall_hp < 0:
            overall_hp = 0
            print('enemy died, you\'ve won')
    return overall_hp




#first fight
Fight_count = 1
print('u started ur long and hard way in the kingdom Headspace \n at the start of ur way you\'ve met an Ogre')

chosing()


    

