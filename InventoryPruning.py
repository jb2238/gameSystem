import database as DB
import feedbackManager as FM
import matplotlib.pyplot as plt
from datetime import datetime

'''
By: F322925
    
Contains the functions for sorting and returning 
the lowest performing games to be considered for pruning
'''

# -Take in rental history
#     -Create array with gameID and all dates taken out
#     -Work out game that havent been rented in a while
#     -Add to list
# -Take in game feedback
#     -Work out lowest average rating
#     -Add to list
# -Plot graph showing frequency of rentals for the games
# Done

RentalHistory = [["cod01"],["apxl01"],["prtl02"],["rktl01"],["hmff01"],["fifa01"],
                 ["ttfl02"],["hlkt01"],["amgs01"],["mcft01"],["lgsw02"],["tmrd01"],
                 ["yomi01"],["ror2"],["nms01"],["soth01"],["des201"],["drg01"],
                 ["slts01"],["lcmp01"]]

def getRentalHistory():
    '''
    Returns list of records with gameID and 
    every date the game has been rented -> [[gameID, date1, date2, ... ,dateN],[...],[...]]
    '''
    rentalData = DB.returnRentalHistory()
    i = 0
    for record in rentalData:
        for i in range(len(RentalHistory)):
            if(RentalHistory[i][0] == record[0]):
                RentalHistory[i].append(record[1])
    return RentalHistory

lowestGameDict = {}

def getLowest5Games(rentalHistory):
    '''
    Return list of least rented games and 
    the date they were last rented as -> [[gameID, date], [...], [...]]
    '''
    gameStack = [["","9999-9-9"],["","9999-9-9"],["","9999-9-9"],["","9999-9-9"],["","9999-9-9"]]
    top = 0
    for data in rentalHistory:
        if( (datetime.strptime(data[-1], '%Y-%m-%d').date() < datetime.strptime(gameStack[top][1], '%Y-%m-%d').date() ) and top < 5):
            gameStack[top][0] = data[0]
            gameStack[top][1] = data[-1]
            gameStack.sort(key=lambda sort:sort[1] ,reverse=False)
            top += 1
            if(top == 5):
                top = 4
    return gameStack



def getFeedbackHistory():
    '''
    Creates a list from feedback data and works out average
    rating for each of the games and returns them as -> [[gameID, average rating], [...], [...]]
    '''
    data = FM.load_feedback("Game_Feedback.txt")

    averages = []
    overallAverage = 0
    index = 0

    for i in range(len(data)):

        averages.append([data[i]["GameID"],data[i]["Rating"]])
        overallAverage += data[i]["Rating"]

    max = 1
    i = 0
    while i < max:
        j = 0
        max = len(averages)
        while j  < max:
            if ( (averages[i][0] == averages[j][0]) and (i != j) ):
                averages[i][1] = (averages[i][1] + averages[j][1])/2
                del(averages[j])
                max -= 1
            j+=1
        i+=1

    averages.sort(key=lambda sort:sort[1])

    averages.insert(0, ["Average\nRating", overallAverage/len(data)])

    return averages[0:6]

if __name__ == "__main__":
    print(getLowest5Games(getRentalHistory()))
    print(getFeedbackHistory())

