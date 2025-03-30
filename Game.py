import sys
import random
import json
from cryptography.fernet import Fernet
import os


def generate_key():
    return Fernet.generate_key()


def save_key(key, filename='secret.key'):
    with open(filename, 'wb') as key_file:
        key_file.write(key)


def load_key(filename='secret.key'):
    return open(filename, 'rb').read()


def encrypt_data(data, key):
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data


def decrypt_data(encrypted_data, key):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data).decode()
    return decrypted_data


def save_progress(progress, filename='progress.enc'):
    key = load_key()
    encrypted_progress = encrypt_data(json.dumps(progress), key)
    with open(filename, 'wb') as file:
        file.write(encrypted_progress)


def load_progress(filename='progress.enc'):
    if not os.path.exists(filename):
        return None
    key = load_key()
    with open(filename, 'rb') as file:
        encrypted_progress = file.read()
    return json.loads(decrypt_data(encrypted_progress, key))


if __name__ == "__main__":
    
    key = generate_key()
    save_key(key)

    # Загрузка ключа
    key = load_key()

restart = False
while restart != False:
    # Определяем характеристики

    wizard = 'Buddy'
    wizard_dmg = 125
    wizard_hp = 100
    wizard_shield = 50

    hiro = 'Hiro'
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
        WTF = '1'
        print_stats(hp, dmg, inv, shield)

    elif WTF_factor == 2:
        print(f'{name} is a base adult knight.')
        hp = 175
        dmg = 75
        inv = 4
        shield = 25
        inv_list = []
        WTF = '2'
        print_stats(hp, dmg, inv, shield)

    elif WTF_factor == 3:
        print(f'For an indescribable luck, {name} is a caster.')
        hp = 120
        dmg = 150
        inv = 5
        shield = 50
        inv_list = []
        WTF = '3'
        print_stats(hp, dmg, inv, shield)

    progress = [WTF]
    save_progress(progress)
    
    def attack(hp, x, dmg):
            
            hp -= dmg
            print(f"{x} attacks and deals {dmg} damage.")

            return hp

    def attack_shield(hp, e_shield, x, dmg):
        effective_damage = max(0, dmg - e_shield)
        hp -= effective_damage

        if effective_damage > 0:
            print(f"{x} attacks and deals {effective_damage} damage.")
        else:
            print(f"{x} attacks, but damage gets fully absorbed by the shield!")

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
            print('your action?(1 - attack , 2 - block)')
            answ5 = int(input('>> '))
            enemy_action = random.randint(1,2)

            while answ5 < 1 or answ2 > 2:
                print('please, be intellegent and write a number in spree of 1 and 2')
                answ5 = int(input('>> '))
            if answ5 == 1:
                ogre_hp = attack(ogre_hp,name,dmg)
                e_skip = False
            else:
                if ogre_hp > 0:  
                    print('The ogre responds with a club smash but you block part of dmg with your shield!')
                    hp = attack_shield(hp, shield, ogre, club_dmg)
                    e_skip = True
            
                if ogre_hp > 0:  
                    print('The ogre responds with a club smash!')
                    hp = attack_shield(hp, shield, ogre, club_dmg)
            if enemy_action == 1:
                if e_skip != True:
                    if ogre_hp > 0:  
                        print('The ogre responds with a club smash!')
                        hp = attack(hp, ogre, club_dmg)
                else:
                    print(f'{name} attacks ogre')
                    ogre_hp = attack(ogre_hp,name,dmg)
            else:
                ogre_hp = attack_shield(ogre_hp,ogre_shield,name,dmg)

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
            Fight_complete = '1'

        progress = [WTF,Fight_complete]
        save_progress(progress)


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
    print(' 1 - yes \n 2 - no')

    answ4 = int(input('>> '))
    while answ4 < 1 or answ4 > 2:
        print('please, be intellegent and write a number in spree of 1 and 2')
        answ4 = int(input('>> '))

    if answ4 == 1:
        print('You gathered all your bravery and accepted the Hiro\'s battle call.')
        while hiro_hp > 0 and hp > 0:
            print('your action?(1 - attack , 2 - block)')
            answ5 = int(input('>> '))
            enemy_action = random.randint(1,2)

            while answ5 < 1 or answ2 > 2:
                print('please, be intellegent and write a number in spree of 1 and 2')
                answ5 = int(input('>> '))
            if answ5 == 1:
                hiro_hp = attack(hiro_hp,name,dmg)
                e_skip = False
            else:
                if hiro_hp > 0:  
                    print('Hiro responds with his attack')
                    hp = attack_shield(hp, shield, hiro, hiro_dmg)
                    e_skip = True
            
                if ogre_hp > 0:  
                    print('The Hiro responds with his attack')
                    hp = attack_shield(hp, shield, hiro, hiro_dmg)
            if enemy_action == 1:
                if e_skip != True:
                    if ogre_hp > 0:  
                        print('The Hiro responds with his attack')
                        hp = attack(hp, hiro, hiro_dmg)
                else:
                    print(f'{name} attacks Hiro')
                    hiro_hp = attack(hiro_hp,name,dmg)
            else:
                print(f'{name} attacks Hiro but he uses shield')
                hiro_hp = attack_shield(hiro_hp,hiro_shield,name,dmg)

        if hp <= 25:
            print(f"{name} has been defeated!")
            print('hiro said that you have potential and he can train you(+20hp,+50dmg,)')
            print('you accepted his offer')
            print_stats(hp,dmg,inv,shield)
        elif hiro_hp <= 0:
            print(f"{name} has defeated Hiro!")
            print('will you laugh at Hiro(1) or encourage him(2)?')
            answ4 = int(input('>> '))
            while answ4 < 1 or answ4 > 2:
                print('write down correct number')
                answ4 = int(input('>> '))   
            if answ4 == 1:
                hiro_kara = 1
                print('Hiro will remember it....')
            else:
                hiro_kara = 0
                print('Hiro will remember it!')

        Fight_complete = '2'
        progress = [WTF,Fight_complete]
        save_progress(progress)

        
        print('after some rest you continued the adventure in the Headspace')
        print('one hour of searching something in front of you appeared a new enemy.....')
        print('it was Buddy the wizer!')
        print('he attacks you and misses')
        print('you have no way to run from fight')
        while wizard_hp > 0 and hp > 0:
        
           while wizard_hp > 0 and hp > 0:
            print('your action?(1 - attack , 2 - block)')
            answ5 = int(input('>> '))
            enemy_action = random.randint(1,2)

            while answ5 < 1 or answ2 > 2:
                print('please, be intellegent and write a number in spree of 1 and 2')
                answ5 = int(input('>> '))
            if answ5 == 1:
                wizard_hp = attack(wizard_hp,name,dmg)
                e_skip = False
            else:
                if hiro_hp > 0:  
                    print('Buddy responds with his attack')
                    hp = attack_shield(hp, shield, wizard, wizard_dmg)
                    e_skip = True
            
                if ogre_hp > 0:  
                    print('The Buddy responds with his attack')
                    hp = attack_shield(hp, shield, wizard, wizard_dmg)
            if enemy_action == 1:
                if e_skip != True:
                    if wizard_hp > 0:  
                        print('The Buddy responds with his attack')
                        hp = attack(hp, wizard, club_dmg)
                else:
                    print(f'{name} attacks Buddy')
                    wizard_hp = attack(hiro_hp,name,dmg)
            else:
                print(f'{name} attacks Buddy but he uses shield')
                wizard_hp = attack_shield(wizard_hp,wizard_shield,name,dmg)

        if hp <= 0:
            print(f"{name} has been defeated!")
            
            print_stats(hp,dmg,inv,shield)
        elif wizard_hp <= 25:
            print('suddently Hiro appears in the back of Buddy and gives him last hit')
        Fight_complete = '3'
        progress = [WTF,Fight_complete]
        save_progress(progress)
        if hiro_kara == 0:
            print('After fight , you thanked Hiro for the help and you both went to the village')
            print('in the vilage Hiro spreads you fame for the all people')
            print('that\'s the best ending, congrants!!')
        
        if hiro_kara == 1:
            print('After the fight , Hiro gets his revenge by killing you from the back')
            print('it was the secret(bad) ending , congrats!!!')