import random

print("Objectif du jeux : Retirer des allumettes chacun votre tour. L'objectif est de ne pas retirer la derniere.")
print("-------------------------------------")
nbSticks = int(input("Combien d'allumettes pour cette partie : "))
nbDeleteSticks = int(input("Combien d'allumettes peut on retirer maximum : "))

if nbDeleteSticks >= nbSticks:
    print("Configuration impossible")
else :
    
    sticks = nbSticks

    while True :
        print("Nombre total d'allumettes :"), sticks
        table = ['|'] * sticks
        print(' '.join(map(str, table)))

        sticksDelete = int(input("Humain : "))
        
        if sticksDelete > nbDeleteSticks or nbDeleteSticks <= 0:
            print "WARNING : Vous pouvez retirer maximum ",nbDeleteSticks,"allumettes."
            continue

        sticks -= sticksDelete 
        sticksPlayer = sticks
        if sticksPlayer <= 0:
            print("Game over. L'IA a remportee le duel.")
            break

        iaSticks = random.randint(1, nbDeleteSticks)   
        print("IA : "), (iaSticks )
        sticks -= iaSticks
        sticksIA = sticks
        if sticksIA <= 0:
            print("Felicitations ! Vous avez remporte le duel")
            break

