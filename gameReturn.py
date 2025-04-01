import database as DB
import gameRent as GR
import subscriptionManager as SM
import feedbackManager as FM

'''
By: F322925
    
Contains the functions needed inorder to return a game
after it has been rented out to a customer
'''

# -/Take in customer ID
# -/If customer has >0 games then continue
#     -/Else no games can be returned, stop.
# -/Get list of games customer has currently
# -/Enter gameID of to be returned game
# -/If in list then provide option to leave review and a rating then
#     -/Save this into gameFeedback using FM
# -/Add return date and reduce number of games in possession by 1

def custIDCheck(custID):
    '''
    Check if a customer has any games taken out already
    returns True or False
    '''
    numberOfGames = GR.rentalTracker(custID)

    if(numberOfGames > 0):
        return True
        
    else:
        return False
        

def returnListFromCustID(custID):
    '''
    Return all game IDs that have been rented by a specific customer
    '''
    gameList = DB.getRentedGamesByCustID(custID)
    return gameList

def verifyGameInList(custID, gameID, gameList):
    '''
    Return true if gameID is in the list of games by that customer
    '''
    for game in gameList:
        if(game[0] == gameID and game[2] == ""):
            return True
        
def getFeedback(custID, gameID, rating, comment):
    '''
    Add customer feedback to Game_Feedback.txt
    '''
    FM.add_feedback(gameID, rating, comment, "Game_Feedback.txt")

def returnGame(custID, gameID):
    '''
    Call function to return a game in the rental.txt file
    then update the rental tracker to reflect the returned game
    '''
    DB.returnGame(custID, gameID)
    GR.rentalTracker(custID)

    
if __name__ == "__main__":
    custID = "abcd"
    gameID = "drg01"
    if(custIDCheck(custID)):
        if(verifyGameInList(custID, gameID, returnListFromCustID(custID))):
            getFeedback(custID, gameID, 5, "Very cool and silly game!! ROCK AND STONE!!")
            returnGame(custID, gameID)
    pass
