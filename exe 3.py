                                                        #Gusse The Number

#The Number I Have Selected Is - 47
d = 9
print("Guess The Right Number.")
print("You Have 9 Chances To Guess The Right Number.")
while (True):
    a = int(input("Guess The Number:\n"))
    d = d-1
    if a == 47:
        print("Congratulations!!! , You Won The Game.")
        print("You Took" , 9-d , "Tries To Win")
        break

    if d == 0:
       print("Game Over !!!!!")
       break

    elif 47 <a < 51:
        print("You Are So Close To The Number , The Number You Have Entered Is Bigger Than The Number , Try Again:")
        print("Number Of Guesses You Have Left -" , d)
        continue

    elif 43 < a < 47:
        print("You Are So Close To The Number , The Number You Have Entered Is Smaller Than The Number ,  Try Again:")
        print("Number Of Guesses You Have Left -", d)
        continue

    elif a < 47:
        print("The Number You Have Entered Is Smaller Than The Number , Try Again:")
        print("Number Of Guesses You Have Left -", d)
        continue

    elif a > 47:
        print("The Number You Have Entered Is Bigger Than The Number , Try Again:")
        print("Number Of Guesses You Have Left -", d)
        continue

