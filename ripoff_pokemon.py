import random

print("Welcome to the rip-off version of Pokemon\n")

player_character_name = input("Enter your bad-ass character name: ")
enemy_character_name = "Russ"

player_hit_points = 100
enemy_hit_points = 100

move_one_name = "Shank"
move_one_desc = "You attempt to shank " + enemy_character_name + "."
move_one_miss_desc = "You missed your shank attempt."

move_two_name = "Roundhouse"
move_two_desc = "You attempt to roundhouse " + enemy_character_name + "."
move_two_miss_desc = "You missed terribly.."

move_three_name = "Heal"

enemy_move_one_name = "Belch"
enemy_move_one_desc = "\n{} attempts to belch on you.".format(enemy_character_name)
enemy_move_one_miss_desc = "{} missed his belch.".format(enemy_character_name)

enemy_move_two_name = "Bitch Slap"
enemy_move_two_desc = "\n{} attempts to bitch slap you.".format(enemy_character_name)
enemy_move_two_miss_desc = "{} whiffed his bitch slap.".format(enemy_character_name)

enemy_move_three_name = "Heal"

while player_hit_points > 0 and enemy_hit_points > 0:
    move_one_accuracy = random.randint(1, 11)
    move_one_damage = random.randint(18, 26)
    move_one_hit_desc = "You shanked his ass for {}.".format(move_one_damage)

    move_two_accuracy = random.randint(1, 11)
    move_two_damage = random.randint(10, 36)
    move_two_hit_desc = "You roundhoused {} in the face for {}!".format(enemy_character_name, move_two_damage)

    enemy_move_choice = random.randint(1, 3)

    enemy_move_one_accuracy = random.randint(1, 11)
    enemy_move_one_damage = random.randint(18, 26)
    enemy_move_one_hit_desc = "{} belched directly in your face for {}. " \
                              "You puke on yourself.".format(enemy_character_name, enemy_move_one_damage)

    enemy_move_two_accuracy = random.randint(1, 11)
    enemy_move_two_damage = random.randint(10, 36)
    enemy_move_two_hit_desc = "{} bitch slaps you right across the face for {}. " \
                              "You start to cry.".format(enemy_character_name, enemy_move_two_damage)

    print("\n" + player_character_name + ", choose your next move.")
    print("\nShank\nRoundhouse\nHeal")
    next_move = input("\nEnter Move: ")
    if next_move == "Shank":
        print(move_one_desc)
        if move_one_accuracy > 3:
            print(move_one_hit_desc)
            enemy_hit_points = enemy_hit_points - move_one_damage
            if enemy_hit_points < 0:
                enemy_hit_points = 0
                print("{} has been killed. You win!".format(enemy_character_name))
                break
            print("{} has {} hit points left.".format(enemy_character_name, enemy_hit_points))
        else:
            print(move_one_miss_desc)
            print("{} has {} left.".format(enemy_character_name, enemy_hit_points))
    elif next_move == "Roundhouse":
        print(move_two_desc)
        if move_two_accuracy > 4:
            print(move_two_hit_desc)
            enemy_hit_points = enemy_hit_points - move_two_damage
            if enemy_hit_points < 0:
                enemy_hit_points = 0
                print("{} has been killed. You win!".format(enemy_character_name))
                break
            print("{} has {} hit points left.".format(enemy_character_name, enemy_hit_points))
        else:
            print(move_two_miss_desc)
            print("{} has {} left.".format(enemy_character_name, enemy_hit_points))
    elif next_move == "Heal":
        if player_hit_points < 76:
            player_hit_points = player_hit_points + 25
            print("You heal yourself for 25.")
            print("Your HP is now {}".format(player_hit_points))
        elif 75 > player_hit_points < 100:
            player_hit_points = 100
            print("You healed yourself to max health")
            print("Your HP is now {}".format(player_hit_points))
        elif player_hit_points == 100:
            print("You were already at full health. You hurt yourself in confusion")
            player_hit_points = player_hit_points - 5
            print("Your HP is now {}".format(player_hit_points))
    if enemy_move_choice == 1:
        print(enemy_move_one_desc)
        if enemy_move_one_accuracy > 3:
            print(enemy_move_one_hit_desc)
            player_hit_points = player_hit_points - enemy_move_one_damage
            if player_hit_points < 0:
                player_hit_points = 0
                print("You have been killed by {}. You lose!".format(enemy_character_name))
            print("You have {} hit points left.".format(player_hit_points))
        else:
            print(enemy_move_one_miss_desc)
            print("You have {} hit points left.".format(player_hit_points))
    elif enemy_move_choice == 2:
        print(enemy_move_two_desc)
        if enemy_move_two_accuracy > 4:
            print(enemy_move_two_hit_desc)
            player_hit_points = player_hit_points - enemy_move_two_damage
            if player_hit_points < 0:
                player_hit_points = 0
                print("You have been killed by {}. You lose!".format(enemy_character_name))
            print("You have {} hit points left.".format(player_hit_points))
        else:
            print(enemy_move_two_miss_desc)
            print("You have {} hit points left.".format(player_hit_points))
    elif next_move == 3:
        if enemy_hit_points < 76:
            enemy_hit_points = enemy_hit_points + 25
            print("{} heals for 25.".format(enemy_character_name))
            print("{}'s HP is now {}".format(enemy_character_name,  enemy_hit_points))
        elif 75 > enemy_hit_points < 100:
            player_hit_points = 100
            print("{} healed to max health".format(enemy_character_name))
            print("{}'s HP is now {}".format(enemy_character_name, enemy_hit_points))
        elif enemy_hit_points == 100:
            print("{} was already at full health. {} hurt their self in "
                  "confusion".format(enemy_character_name, enemy_character_name))
            enemy_hit_points = enemy_hit_points - 5
            print("{}'s HP is now {}".format(enemy_character_name, enemy_hit_points))
            
