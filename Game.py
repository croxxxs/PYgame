import sys
import random

restart = False
while restart != False:
    # Определяем характеристики

    hiro = 'hiro'
    hiro_dmg = 80
    hiro_hp = 150
    hiro_shield = 35

    ogre = 'ogre'
    ogre_hp = 175
    club_dmg = 30
    ogre_shield = 0

    #Определяем фактор WTF
    WTF_factor = random.randint(1, 3)

    # Характеристики персонажа
    name = input('Enter your hero\'s name >> ')

    def print_stats(hp, dmg, inv, shield):
        print(f'The {name}\'s stats:')
        print(f'{name}\'s hp is {hp}')
        print(f'{name}\'s dmg is {dmg}')
        print(f'{name}\'s inventory capacity is {inv}')
        if WTF_factor == 2 or WTF_factor == 3:
            print(f'Because you are not a child, you can bring a shield with you. Shield\'s toughness is {shield}')

    # Определяем характеристики героя в зависимости от WTF_factor
    if WTF_factor == 1:
        print(f'For an indescribable pity, {name} is a little child.')
        hp = 100
        dmg = 25
        inv = 2
        shield = 0
        inv_list = []
        print_stats(hp, dmg, inv, shield)

    elif WTF_factor == 2:
        print(f'{name} is a base adult knight.')
        hp = 175
        dmg = 75
        inv = 4
        shield = 25
        inv_list = []
        print_stats(hp, dmg, inv, shield)

    elif WTF_factor == 3:
        print(f'For an indescribable luck, {name} is a caster.')
        hp = 150
        dmg = 150
        inv = 5
        shield = 50
        inv_list = []
        print_stats(hp, dmg, inv, shield)

    def attack(hp, e_shield, x, dmg):
        effective_damage = max(0, dmg - e_shield)
        hp -= effective_damage

        if effective_damage > 0:
            print(f"{x} attacks and deals {effective_damage} damage.")
        else:
            print(f"{x} attacks, but damage gets fully absorbed by the armor!")

        return hp

    # Начало боя
    print('You started your long and hard way in the kingdom Headspace.')
    print('At the start of your journey, you\'ve met an Ogre.')
    print('What would you like to do?\n1 - Run away\n2 - Get into a fight')

    answ = int(input('>> '))
    while answ < 1 or answ > 2:
        print('Please, be intelligent and write a number in the range of 1 - 2')
        answ = int(input('>> '))

    if answ == 1:
        print('You\'ve successfully run away, That\'s the first ending \n all the world have forgotten about you so That\'s the worst ending you can have XD')
        print('would u like to restart? \n 1 - yes \n 2 - no')
        answ2 = int(input('>> '))

        while answ2 < 1 or answ2 > 2:
            print('please, be intellegent and write a number in spree of 1 and 2')
            nsw2 = int(input('>> '))
        if answ2 == 2:
            restart = True
        else:
            sys.exit
    else:
        print('You gathered all your bravery and accepted the Ogre\'s battle call.')

        while ogre_hp > 0 and hp > 0:
            # Атака героя
            ogre_hp = attack(ogre_hp, ogre_shield, ogre, dmg)
            if ogre_hp > 0:  # Если огр еще жив, он атакует
                print('The ogre responds with a club smash!')
                hp = attack(hp, shield, name, club_dmg)

        if hp <= 0:
            print(f"{name} has been defeated!")
            print('would u like to restart? \n 1 - yes \n 2 - no')
            answ2 = int(input('>> '))
            while answ2 < 1 or answ2 > 2:
                print('please, be intellegent and write a number in spree of 1 and 2')
                nsw2 = int(input('>> '))
            if answ2 == 2:
                restart = True
            else:
                sys.exit

        elif ogre_hp <= 0:
            print(f"{name} has defeated the ogre!")


    print('After battle with ogre you\'ve found out his strange shaped cloak(+30 hp , + 20 shield, -1 inventory space)')
    print('would you like to take it? \n 1 - yes \n 2 - no')

    answ3 = int(input('>> '))
    if answ3 == 1:
        new_item = 'strange shaped cloak'
        hp += 30
        shield += 20
        inv -= 1
        inv_list.append(new_item)
        print(f'your current inventory >> \n {inv_list}')
    else:
        print('you\'ve left strange shaped cloak')

    print('after some rest you continued the adventure in the Headspace')
    print('one hour of searching something in front of you appeared a new enemy.....')
    print('it was the elite knight Hiro')
    print('he offered you for some frienly battle , would you like to accept it?')
    print('1 - yes \n 2 - no')

    answ4 = int(input('>> '))
    while answ4 < 1 or answ4 > 2:
        print('please, be intellegent and write a number in spree of 1 and 2')
        answ4 = int(input('>> '))

    if answ4 == 1:
        print('You gathered all your bravery and accepted the Hiro\'s battle call.')
        while hiro_hp > 0 and hp > 0:
        
            hiro_hp = attack(hiro_hp, hiro_shield, hiro, dmg)
            if hiro_hp > 0: 
                print('The hiro responds with his attack!')
                hp = attack(hp, shield, name, hiro_dmg)

        if hp <= 25:
            print(f"{name} has been defeated!")
            print('hiro said that you have potential and he can train you(+20hp,+50dmg,)')
            print('you accepted his offer')
            print_stats(hp,dmg,inv,shield)
        elif hiro_hp <= 0:
            print(f"{name} has defeated Hiro!")
            print('will you laugh at Hiro(1) or encourage him(2)?')
            answ4 = int(input('>> '))
            if answ4 == 1:
                hiro_kara = 1
                print('Hiro will remember it....')
            else:
                hiro_kara = 0
                print('Hiro will remember it!')
            