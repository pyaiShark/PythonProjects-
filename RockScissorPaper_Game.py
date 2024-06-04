# 1.rock vs scissor = rock
# 2.scissor vs paper = scissor
# 3.paper vs rock = paper


import random

g_list = ["rock", "scissor", "paper"]
Computer_result = 0
User_result = 0
print("The Game play in 5 round. ")
while True:
    try:
        user_input = int(input(''' 
        Game start..
                  1.Play |Yes
                  2.NO |exit
                  
        '''))

        if user_input == 1:
            for _ in range(1, 6):
                user_value = int(input('''
                    Enter choice.
                           1.rock
                           2.scissor
                           3.paper
                           
                    '''))
                if user_value == 1:
                    User_choice = 'rock'
                elif user_value == 2:
                    User_choice = 'scissor'
                elif user_value == 3:
                    User_choice = 'paper'
                elif user_value > 3:
                    print("Invalid...")
                    continue
                Computer_choice = random.choice(g_list)
                if Computer_choice == User_choice:
                    print("User choice", User_choice)
                    print("Computer choice", Computer_choice)
                    print(''' 
                    Game draw..
                    ''')
                    Computer_result = Computer_result + 1
                    User_result = User_result + 1
                    print("Computer Score:-", Computer_result, "\n", "user Score:-", User_result)
                elif User_choice == 'rock' and Computer_choice == 'scissor' or User_choice == 'paper' and Computer_choice == 'rock' or User_choice == 'scissor' and Computer_choice == 'paper':
                    print("User choice", User_choice)
                    print("Computer choice", Computer_choice)
                    print('''                                                                    
                     User win..                                                                  
                     ''')
                    User_result = User_result + 1
                    print("Computer Score:-", Computer_result, "\n", "user Score:-", User_result)
                else:
                    print("User choice", User_choice)
                    print("Computer choice", Computer_choice)
                    print('''                                                                     
                     Computer win..                                                                   
                     ''')
                    Computer_result = Computer_result + 1
                    print("Computer Score:-", Computer_result, "\n", \
                        "user Score:-", User_result)
            if User_result > Computer_result:
                print("\n \n \n \n Final result : \n \t \a User Win..1", \
                    "\n User Total score :-", User_result, \
                    "\n Computer total score :- ", Computer_result)
            elif User_result < Computer_result:
                print("\n \n \n \n Final Result : \n \t \a Computer Win..", \
                    "\n Computer Total score :-", \
                    Computer_result, "\n User Total Score :- ", User_result)
            else:
                print("\n \n \n Final Result : \n \t \a Game Draw..", \
                    "\n Computer Total Score :-", Computer_result, "\n User Total Score :-", User_result)
        elif user_input == 2:
            break
        else:
            print("Plz. \n Enter a valid choice : ")
            continue
    except ValueError:
        print("Enter a valid number to continue game : ")







