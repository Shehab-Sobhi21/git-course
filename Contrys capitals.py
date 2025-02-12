user_asking = input("Do You Wont To Play? (y, n) ").strip().lower()
trys = 5
score = 0
counter = 0
QnA = [
    ['What Is A Cabital Of Eygpt? ', 'Cairo'],
    ['What Is A Cabital Of KSA? ', 'Jeddah'],
    ['What Is A Cabital Of Qatar? ', 'Doha'],
    ['What Is A Cabital Of Kwait? ', 'Kwait'],
    ['What Is A Cabital Of Jordan? ', 'Amaan']]
if user_asking == "y":
    while trys > score:
        q1 = input(QnA[counter][0]).strip().capitalize()
        if q1 == QnA[counter][1]:
            print("Will Done You Answer Is True")
            score += 1
            counter += 1
        else:
            print("Oh Your Answer Is False")
            print("Try Again")
            trys -= 1
    if trys != 0:
        print("Congratolaitons You Won!!!")
        print("Your Score Is", score, "Points.")
    elif trys == 0:
        print("You Lose")
else:
    quit()
