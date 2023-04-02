import random
import time
import os
import colorama
from colorama import *

def loading():
	for i in range(3):
		os.system("clear")
		print(Fore.WHITE + """






				0.........   

			""")
		time.sleep(0.5)
		os.system("clear")
		print(Fore.RED + """






				                   .........   

			""")
		time.sleep(0.5)
		os.system("clear")
		print(Fore.BLUE + """






				                                     .........0

			""")
		time.sleep(0.5)

color = colorama.init()

print("Welcome To WarriorxRPG By NotSuperSaiyan. Hope You Enjoy!")
os.system("clear")
time.sleep(3)

print(f"\n|---Long ago... far in a galaxy was a planet named Doomster\nThere lived a warrior named MadaraUchiha. The planet was attacked by aliens and you need to save the planet. You will play the role of Madara Uchiha---|\n\nYou will have to customize your character now\n")

print(Fore.YELLOW + """
   ___------~~~~~~~~~~~----__         .:.         __----~~~~~~~~~~~------___   
 ~~ ~--__          ......====\\~~    .:::.    ~~//====......          __--~ ~~ 
         ~\ ...::::~~~~~~  //|||    .:::::.    |||\\  ~~~~~~::::... /~         
        -~~\_            //  |||***.(:::::).***|||  \\            _/~~-        
             ~\_        // *******.:|\^^^/|:.******* \\        _/~             
                \      / ********.::(>: :<)::.******** \      /                
                 \   /  ********.::::\\|//::::.********  \   /                 
                  \ /   *******.:::::(o o):::::.*******   \ /                  
                   /.   ******.::::'*|V_V|***`::.******   .\                   
                     ~~--****.:::'***|___|*****`:.****--~~                     
                           *.::'***//|___|\\*****`.*                           
                           .:'  **/##|___|##\**    .                           
                          .    (v(VVV)___(VVV)v)
	""")

time.sleep(10)

os.system("clear")

print(Fore.WHITE + "What colour you want your hair to be?\nWrite the number of the colour\n")
print(Fore.WHITE + "WHITE(1)\n")
print(Fore.BLUE + "BLUE(2)\n")
print(Fore.GREEN + "GREEN(3)\n")
print(Fore.RED + "RED(4)\n")
print(Fore.YELLOW + "YELLOW(5)\n")

user_input = input("\n")

if user_input=="1":
	hair_color = "white"
elif user_input=="2":
	hair_color = "blue"
elif user_input=="3":
	hair_color = "green"
elif user_input=="4":
	hair_color = "red"
elif user_input=="5":
	hair_color = "yellow"
else:
	print("Not in the list")

time.sleep(2)

print(Fore.WHITE + "Set your hair colour to " + hair_color)

os.system("clear")
time.sleep(2)

print("What colour you want your skin to be?\nWrite the number of the skin\n")
print(Fore.RED + "RED(1)\n")
print(Fore.YELLOW + "MEDIUM(2)\n")
print(Fore.WHITE + "WHITE(3)\n")

user_input = input("\n")

if user_input=="1":
	skin_color = "red"
elif user_input=="2":
	skin_color = "medium"
elif user_input=="3":
	skin_color = "white"

time.sleep(2)

print(Fore.WHITE + "Set your skin colour to " + skin_color)

os.system("clear")
time.sleep(1)

print("You have successfully customized your character.\n")
print(Fore.RED + """



⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⢤⣤⣤⣀⣹⣿⣿⣿⣷⣼⣿⣿⣷⡄⢠⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡖⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶
⠀⠀⠀⠀⠀⣀⣴⡾⠿⢿⣿⡀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿
⠀⠀⠀⠀⠈⠁⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿
⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⠿⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈
⣶⣄⡀⠀⣠⣾⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠈⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠉⠁⣴⠟⠉⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠁⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⣠⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⡴⣾⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⡿⢻⣿⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⡿⠐⣧⡘⠻⠍⠉⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠙⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢰⠏⢀⣿⣇⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢸⠃⠀⠃⠉⠻⡖⠢⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣆⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠈⣀⢀⠀⠀⠀⠙⡄⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣀⣀⣿⣿⣿⣿⣿⣦⣽⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⡀⠀⢀⣀⠀⠀⠀⢧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠑⠒⠒⠈⠁⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⡼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣄⣀⠀⠀⠀


⠀
												""")
time.sleep(3)

print(Fore.WHITE + "Get ready! your journey is about to begin...")
time.sleep(2)
loading()
os.system("clear")

print(Fore.WHITE + "Guard : Majesty! Our kingdom is under attack! We need to do something fast\n")
time.sleep(3)
print(Fore.YELLOW + "King : What! Where are our elite soilders\n")
time.sleep(3)
print(Fore.WHITE + "Guard : Sorry my lord, all of them are dead\n")
time.sleep(3)
print(Fore.YELLOW + f"King : And what happened to that warrior- The one with {hair_color} hair and {skin_color} skin?\n")
time.sleep(3)
print(Fore.WHITE + "Guard : Sir, he was sent to a mission by the ministers\n")
time.sleep(3)
print(Fore.YELLOW + f"King : WHAT KIND OF DAMNN MISSION IN THE MIDDLE OF THIS DISASTER? INFORM HIM TO COME FAST OR YOU ARE DEAD\n")
time.sleep(3)
print(Fore.WHITE + "Guard : Yes sir\n")
print("""



⣿⣿⣿⣿⣿⣿⣿⣿⣿⠙⣿⡇⠘⣿⠇⠘⣿⠏⢸⣿⠏⢸⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⠁⠀⠈⠀⠀⠈⠀⠈⠁⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣀⣀⣀⣀⣀⣀⣀⣀⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠓⠀⠀⠀⠀⠀⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣧⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⣿⣿⣿⣿⣿⣿
															""")
time.sleep(4)

loading()

os.system("clear")

print(Fore.RED + "*Sees a bird coming towards you with a message\nYou take that message and you are informed to come to the kingdom fast.\nYou fly to the kingdom*")
time.sleep(4)

print(Fore.YELLOW + "King : MADARA UCHIHA! You are finally here. I was waiting for you\n")
time.sleep(3)
print(Fore.RED + "You : Why did you call me anyway\n")
time.sleep(3)
print(Fore.YELLOW + "King : Our kingdom is attacked by aliens and most of our army is dead. We need you to fight them\n")
time.sleep(3)
print(Fore.RED + "You : Ahh Another Monday\n")
time.sleep(3)
print(Fore.WHITE + "*You rush to the battlefield and you see a massacre\nAn army of aliens is killing everyone\nSomeone tells you that killing the main boss will kill all these aliens too\n")
time.sleep(6)
loading()
os.system("clear")
print(Fore.RED + "You : HEY YOU OVER THERE. Where is your danm leader")
time.sleep(3)
print(Fore.BLUE + "Alien : HAHA you puny being. He is on our spaceship and you will never reach there HAHAHHA")
print(Fore.BLUE + """



.-""""-.        .-""""-.
  /        \      /        \
 /_        _\    /_        _\
// \      / \\  // \      / \\
|\__\    /__/|  |\__\    /__/|
 \    ||    /    \    ||    /
  \        /      \        /
   \  __  /        \  __  / 
    '.__.'          '.__.'
     |  |            |  |
jgs      |  |            |  |



	""")
time.sleep(5)

os.system("clear")

print(Fore.WHITE + "You need to reach the spaceship and you need to clear the battlefield for that\nAnswer this question to use FireBall Jutsu\n3x+5 = 9 (Find the value of x. If answer is not whole number then answer in fraction ex-2/3)\n")
time.sleep(8)

user_input = input("Write your answer:\n")

if user_input=="4/3":
	print(Fore.BLUE + "Correct answer! *Uses Fireball Jutsu*\n")
	print(Fore.RED + """




⠀⠀⠀⠀⠀⠀⢠⣤⡄⠀⠀⠀⠀⠀⠀⠀⠠⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣀⣀⣈⠉⠁⠀⣀⣀⡀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣿⠇⣿⣧⠀⢸⣿⣿⣧⠀⠀⠀⠀⠀⣿⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡀⠀⣠⣿⣿⣦⣈⣻⣿⠏⢰⣶⠀⠀⣰⡟⠉⠙⠻⢶⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠛⠛⠉⣾⠏⠉⠉⠁⠀⢀⣁⣤⡾⠋⠀⠀⠀⠀⠀⠻⣧⠀⠀⠀⠀⠀
⠀⡀⠀⠀⠀⣀⡼⢿⣄⠀⠀⠀⠀⠀⢹⣧⠀⣠⣶⣶⣦⣄⠀⠀⣿⠀⠀⠀⠀⠀
⠀⠛⠛⠛⠛⠋⠀⠀⢹⣆⠀⠈⠻⠾⠿⠋⠀⠻⣿⡿⠀⢻⡇⠀⣿⡀⠀⠀⠀⠀
⠀⣤⣄⠀⢰⣿⣿⣷⣸⡟⠀⣾⣦⣤⡀⠀⢠⣤⡀⠀⠀⣼⣧⡀⢻⡇⠀⠀⠀⠀
⠀⠀⠙⣷⡈⠻⠿⠿⠛⠁⢀⣿⠿⢿⣿⠀⠈⠉⠀⠐⣾⠋⠛⠃⠈⣿⡀⠀⠀⠀
⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⢸⡇⠀⠘⠋⠀⢠⣤⣤⣤⣿⣿⣷⣦⢀⣿⣿⣄⠀⠀
⠀⠀⠀⠀⠘⢷⣤⣀⠀⠀⠸⣇⠀⠀⠀⠀⠈⠉⠉⠻⣿⣿⣿⣧⣾⣿⣿⣿⡆⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠛⠻⣆⠀⠀⢀⣾⣿⣿⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠉⠁⠀⠀⠀
		""")
	time.sleep(3)

	os.system("clear")

	print(Fore.WHITE + "You used fireball jutsu and killed everyone in the battlefield\nYou see a huge spaceship\nAnswer this question to rush to it\nWhat is the value of PI in fraction?\n")
	time.sleep(3.5)
	user_input = input(Fore.WHITE + "Write your answer:\n")

	if user_input == "22/7":
		print(Fore.BLUE + "Correct answer! *Rushes to the spaceship*\n")
		time.sleep(3)

		os.system("clear")

		print(Fore.WHITE + "You rushed to the spaceship and you see two giant guards preventing you to go inside\nAnswer this question to launch a susanno\nPortable computers are called l_pt_p(Write the full spelling)\n")
		time.sleep(5)
		user_input = input("Write your answer:\n")
		if user_input == "laptop":
			print(Fore.BLUE + "Correct answer! *launches a susanno*")
			time.sleep(2)
			os.system("clear")
			print(Fore.WHITE + "You launched a susanno and killed both the guards\nYou enter the control room and find their leader there\n")
			time.sleep(3)

			print(Fore.YELLOW + "Leader : Who are you and what are you here for\n")
			time.sleep(3)
			print(Fore.RED + "You : I am Madara Uchiha and I am on a mission to destroy you bozo\n")
			time.sleep(3)
			print(Fore.YELLOW + "Leader : Oh! We will see about that\n")
			time.sleep(3)

			loading()
			os.system("clear")

			print(Fore.WHITE + "Leader launches a energy beam towards you\nAnswer this question to doge it\nStudents get depressed because of _ch__ls(Write the complete spelling)\n")
			time.sleep(3)
			user_input = input("Write your answer:\n")

			if user_input == "schools":
				print(Fore.BLUE + "Correct answer! *doges the beam*")

				time.sleep(3)
				os.system("clear")

				print(Fore.BLUE + "Its your turn to attack\nAnswer this question to unlock sharingan\n2+2/2")
				time.sleep(2)
				user_input = input("Write your answer:\n")

				if user_input == "3":
					print(Fore.BLUE + "Correct Answer! *unlocks sharingan*\nYou can now see the moves of your opponent before he performs it\n")
					print(Fore.RED + """
			⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣴⣶⣶⣶⣶⣦⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
			⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀
			⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⢶⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀
			⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⡿⠿⣿⠀⠀⠀⠀⣿⠿⢿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀
			⠀⢠⣾⣿⣿⣿⣿⣿⡿⠋⣠⣴⣿⣷⣤⣤⣾⣿⣦⣄⠙⢿⣿⣿⣿⣿⣿⣷⡄⠀
			⠀⣼⣿⣿⣿⣿⣿⡏⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⢹⣿⣿⣿⣿⣿⣧⠀
			⢰⣿⣿⣿⣿⣿⡿⠀⣾⣿⣿⣿⣿⠟⠉⠉⠻⣿⣿⣿⣿⣷⠀⢿⣿⣿⣿⣿⣿⡆
			⢸⣿⣿⣿⣿⣿⣇⣰⣿⣿⣿⣿⡇⠀⠀⠀⠀⢸⣿⣿⣿⣿⣆⣸⣿⣿⣿⣿⣿⡇
			⠸⣿⣿⣿⡿⣿⠟⠋⠙⠻⣿⣿⣿⣦⣀⣀⣴⣿⣿⣿⣿⠛⠙⠻⣿⣿⣿⣿⣿⠇
			⠀⢻⣿⣿⣧⠉⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠈⣿⣿⣿⡟⠀
			⠀⠘⢿⣿⣿⣷⣦⣤⣴⣾⠛⠻⢿⣿⣿⣿⣿⡿⠟⠋⣿⣦⣤⠀⣰⣿⣿⡿⠃⠀
			⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣄⣈⣁⣠⣤⣶⣾⣿⣿⣷⣾⣿⣿⡿⠁⠀⠀
			⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀
			⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀
			⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠻⠿⠿⠿⠿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
																				""")
					time.sleep(3)

					print(Fore.YELLOW + "Leader : So you are an Uchiha! You are gonna die by my hands!!\n")
					time.sleep(3)
					print(Fore.RED + "You : We will see about that\n")
					time.sleep(2.5)

					print(Fore.WHITE + "Leader is trying to attack you with an energy beam\nWith the help of sharingan you can see it\nAnswer this question to tie him with lava-rope\nHow many days are there in a leap year\n")
					user_input = input("Write your answer:\n")

					if user_input == "366":
						print(Fore.BLUE + "Correct Answer *Ties the leader with lava-rope*\n")
						time.sleep(3)
						os.system("clear")

						print(Fore.WHITE + "The leader is trying to do self-destruction\nAll the gates are closed and you need get out fast\nAnswer this question to do Teleportation Jutsu\nWhat is the child of a cow called __lf (Write the complete spelling)")
						time.sleep(3)
						user_input = input("Write your answer:\n")

						if user_input == "calf":
							print(Fore.BLUE + "Correct Answer! *Uses Teleportation Jutsu to get out*")
							time.sleep(3)
							loading()
							os.system("clear")

							print(Fore.YELLOW + "King : So you did it Madara?\n")
							time.sleep(3)
							print(Fore.RED + "You : Do you expect something else?\n")
							time.sleep(3)
							print(Fore.YELLOW + "King : Oh no Madara! Thank you for helping us\n")
							time.sleep(3)
							print(Fore.RED + "They don't call me The Mighty Ninja for nothing\n")
							time.sleep(3)

							loading()

							print("""
								THANK YOU FOR PLAYING THIS GAME
								 OTHER CHAPTERS ARE COMING SOON

								DIRECTOR AND PROGRAMMER : NOTSUPERSAIYAN

								""")
						


						else:
							print(Fore.RED + "Wrong Answer! The spaceship exploded and you died")
					else:
						print(Fore.RED + "Wrong answer! You died")
				else:
					print(Fore.RED + "Wrong answer! You died")
			else:
				print(Fore.RED + "Wrong answer! You died")
		else:
			print(Fore.RED + "Wrong Answer! You died")
	else:
		print(Fore.RED + "Wrong Answer! You died")
else:
	print(Fore.RED + "Wrong Answer! You died")

input()