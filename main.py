import random 

player_health = 100
monster_health = 100

print("Un monstre vous attaque, préparez-vous à attaquer.")
while player_health > 0 and monster_health > 0:
    print(f"\nVous: {player_health}. Le monstre: {monster_health}")
    try:
        choice = int(input("[1] Attaquer\n[2] Bloquer\n"))
        if not choice in [1, 2]:
            raise ValueError
    except ValueError:
        print("Entrez une option valide.")
        continue
    else:
        monster_pick = random.randint(1, 6)
        player_pick = random.randint(1, 6)
        print(f"Le monstre a tiré un {monster_pick}")
        print(f"Vous avez tiré un {player_pick}")
        damage = random.randint(1, 100)
        if monster_pick == player_pick:
            print("Vous avez tiré la même chose. L'attaque s'annule.")
        elif monster_pick > player_pick:
            print(f"Le monstre remporte la manche...")
            if choice == 2:
                print("Vous avez décidez de bloquer, le monstre ne vous enlève pas de vie.")
                continue
            player_health -= damage
            print(f"Le monstre vous enlève {damage}. Il vous reste {player_health} de vie")
        else:
            print(f"Vous remportez la manche!")
            if choice == 2:
                print("Vous avez décidez de bloquer, vous n'attaquez pas.")
                continue
            monster_health -= damage
            print(f"Vous enlevez {damage}. Il lui reste {monster_health} de vie")

if player_health <= 0:
    print("Vous avez perdu la partie :-(")
else: 
    print("Bravo ! Vous remportez la partie")