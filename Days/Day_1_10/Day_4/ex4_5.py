import random

# opções do jogo
pc = ["rock", "paper", "scissor"]

# imagens na MESMA ordem da lista pc
rock = """
 _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
 _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissor = """
( _\    /_ )
 \ _\  /_ / 
  \ _\/_ /_ _ 
  |_____/_/ /|
  (  (_)__)J-)
  (  /`.,   /
   \/  ;   /
    | === |dwb
"""

# lista de imagens
Images = [rock, paper, scissor]

# sorteio do PC
hand_pc = random.choice(pc)
# escolha do usuário
you = input("What do you choose? (rock/paper/scissor): ").lower().strip()

# transformar escolha em índice
if you in pc:
    you_index = pc.index(you)
    pc_index = pc.index(hand_pc)

    if you_index == pc_index:
        print("TIE")
    elif (you_index == 0 and pc_index == 2) or \
         (you_index == 1 and pc_index == 0) or \
         (you_index == 2 and pc_index == 1):
        print("YOU WIN!")
    else:
        print("YOU LOSE!")

    print(f"YOU CHOICE:\n{Images[you_index]}\nPC CHOICE:\n{Images[pc_index]}")

else:
    print("Invalid choice! Please type rock, paper or scissor.")
