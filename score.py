def score():
    sScore = input("Enter score: ")
    fScore = float(sScore)
    if (fScore >= 1.0 or fScore <= 0.0):
        print('Bad score')
    elif (fScore >= 0.9):
        print('A')
    elif ( (fScore >= 0.8) and (fScore < 0.9) ):
        print('B')
    elif ( (fScore >= 0.7) and (fScore < 0.8) ):
        print('C')
    elif ( (fScore >= 0.6) and (fScore < 0.7) ):
        print('D')
    else:
        print('F')

#score()