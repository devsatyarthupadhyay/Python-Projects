import random
computer = random.choice([1,0,-1])    # Function help us to choose a random outcome

print('''choose 
    s for snake 
    w for water
    g for gun\n''')

your_choice = input("Enter your choice :")
your_dict = {"s":1 , "w":0 ,"g":-1}

if(your_choice not in your_dict):
    print("please enter valid Input")
else:
    you = your_dict[your_choice]
    dict_reverse = {1:"Snake" , 0:"Water" ,-1:"Gun"}

    print(f'''\nYou choose {dict_reverse[you]}
computer choose {dict_reverse[computer]}\n''')

    if(computer == you):
        print("It's Draw !")
    else:
        if(computer == 1 and you == 0):
            print("You Lose !")
        elif(computer == 1 and you == -1):
            print("You win !")
        
        elif(computer == 0 and you == 1):
            print("You Win !")
        elif(computer == 0 and you == -1):
            print("You Lose !")
        
        elif(computer == -1 and you == 0):
            print("You Win !")
        elif(computer == -1 and you == 1):
            print("You Lose !")
    