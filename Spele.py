import random

pirma_sp_punkti = 0
otra_sp_punkti = 0

for x in range(7):

    pirma_sp_skaitlis = random.randint(1, 6)
    otra_sp_skaitlis = random.randint(1, 6)

    print("Player 1 rolled: ")
    if pirma_sp_skaitlis == 1:
        print(" _____")
        print("|     |")
        print("|  O  |")
        print("|     |")
        print(" ‾‾‾‾‾")
    elif pirma_sp_skaitlis == 2:
        print(" _____")
        print("|  O  |")
        print("|     |")
        print("|  O  |")
        print(" ‾‾‾‾‾")
    elif pirma_sp_skaitlis == 3:
        print(" _____")
        print("| O   |")
        print("|  O  |")
        print("|   O |")
        print(" ‾‾‾‾‾")
    elif pirma_sp_skaitlis == 4:
        print(" _____")
        print("| O O |")
        print("|     |")
        print("| O O |")
        print(" ‾‾‾‾‾")    
    elif pirma_sp_skaitlis == 5:
        print(" _____")
        print("| O O |")
        print("|  O  |")
        print("| O O |")
        print(" ‾‾‾‾‾") 
    elif pirma_sp_skaitlis == 6:
        print(" _____")
        print("| O O |")
        print("| O O |")
        print("| O O |")
        print(" ‾‾‾‾‾") 
    print("Player 2 rolled: ")
    if otra_sp_skaitlis == 1:
        print(" _____")
        print("|     |")
        print("|  O  |")
        print("|     |")
        print(" ‾‾‾‾‾")
    elif otra_sp_skaitlis == 2:
        print(" _____")
        print("|  O  |")
        print("|     |")
        print("|  O  |")
        print(" ‾‾‾‾‾")
    elif otra_sp_skaitlis == 3:
        print(" _____")
        print("| O   |")
        print("|  O  |")
        print("|   O |")
        print(" ‾‾‾‾‾")
    elif otra_sp_skaitlis == 4:
        print(" _____")
        print("| O O |")
        print("|     |")
        print("| O O |")
        print(" ‾‾‾‾‾")    
    elif otra_sp_skaitlis == 5:
        print(" _____")
        print("| O O |")
        print("|  O  |")
        print("| O O |")
        print(" ‾‾‾‾‾") 
    elif otra_sp_skaitlis == 6:
        print(" _____")
        print("| O O |")
        print("| O O |")
        print("| O O |")
        print(" ‾‾‾‾‾") 


    if pirma_sp_skaitlis > otra_sp_skaitlis:
        print("1. spēlētājs uzvarēja")
        pirma_sp_punkti = pirma_sp_punkti + 1 
    elif otra_sp_skaitlis > pirma_sp_skaitlis:
        print("2. spēlētājs uzvarēja")
        otra_sp_punkti = otra_sp_punkti + 1
    else:
        print("Neizšķirts")

    input("Spiedied <ENTER> ,lai turpinātu.") 

print("Spēle beidzās")
print("1. spēlētāja punkti:", pirma_sp_skaitlis)
print("2. spēlētāja punkti:", otra_sp_skaitlis)
