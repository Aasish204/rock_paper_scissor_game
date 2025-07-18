import random
print("\nWelcome to the game of rock, paper, scissor")
print("rock    = r\npaper   = p\nscissor = s")
print("\nLet's start...")

your_points = 0
computer_points = 0  
draw = 0 

for i in range(10):
    com = {0:"r", 1:"p", 2:"s"}
    computer= com[random.randint(0,2)]

    you= input("\nYour choice: ")
    print(f"Computer choice: {computer}")

    if(you=="r" and computer=="p"):
        print("[Computer win]")
        computer_points += 1
    elif(you=="r" and computer=="s"):
        print("[You win]")
        your_points += 1
 
    elif(you=="p" and computer=="s"):
        print("[Computer win]")
        computer_points += 1
    elif(you=="p" and computer=="r"):
        print("[You win]")
        your_points += 1

    elif(you=="s" and computer=="r"):
        print("[Computer win]")
        computer_points += 1
    elif(you=="s" and computer=="p"):
        print("[You win]")
        your_points += 1

    elif(you=="r" and computer=="r"):
        print("[Draw]")
        draw += 1
    elif(you=="p" and computer=="p"):
        print("[Draw]")
        draw += 1
    elif(you=="s" and computer=="s"):
        print("[Draw]")
        draw += 1

    else:
        print("Error: [Wrong entry]")

print("\nFinal Score:")
print(f"   Your points: {your_points}")
print(f"   Computer points: {computer_points}")
print(f"   Draw : {draw}\n")

if your_points > computer_points:
    print("[You are the overall winner!]\n")
elif your_points < computer_points:
    print("[Computer is the overall winner!]\n")
else:
    print("It's a draw overall!")
 
