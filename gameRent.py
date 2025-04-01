import subscriptionManager as SM
import gameSearch as GS
import database as DB

'''
By: F322925
    
Contains the functions needed inorder to undergo 
the rent process for the system
'''

def rentalTracker(custID):
    '''
    Updates rentalCounter -> [customer ID, number of games taken out]
    '''
    rentalCounter = []
    subInfo = SM.load_subscriptions("Subscription_Info.txt")
    for customer in subInfo:
        rentalCounter.append([customer,0])
    custIDsWRDate = DB.rentalCustIDs()

    for ID in custIDsWRDate:
        for i in range(len(rentalCounter)):
            if(ID[0] == rentalCounter[i][0] and ID[1] == ""):
                rentalCounter[i][1] += 1
    for i in range(len(rentalCounter)):
        if custID == rentalCounter[i][0]:
            return rentalCounter[i][1]

def availableToRentGame(gameID):
    '''
    Return true or false if a game can be rented
    ''' 
    if(DB.returnGameDict()[gameID]):
        return True
    else:
        return False
    
def verifyCustomer(custID):
    '''
    Verifies the entered customer ID and makes sure it is able to take out a game
    '''
    subInfo = SM.load_subscriptions("Subscription_Info.txt") #loads all subscriptions
    subscriptionType = subInfo[custID]["SubscriptionType"] #Premium/Basic
    rentalLimit = SM.get_rental_limit(subscriptionType) #max rentals
    checkSubscription = SM.check_subscription(custID, subInfo) #checks if subscription is active

    if(checkSubscription):
        #print(rentalTracker(custID))
        if(rentalTracker(custID) < rentalLimit):
            return True
        else:
            print("customar has max games already !")
    else:
        print("subscirptopn is nto valid")
    return False

def gameBeingRented(gameID, custID):
    '''
    Game has been rented, trigger new entry into Rental.txt 
    and update gamesAvailableDict()
    '''
    #checkCustID(custID)
    subInfo = SM.load_subscriptions("Subscription_Info.txt") #loads all subscriptions
    subscriptionType = subInfo[custID]["SubscriptionType"] #Premium/Basic
    rentalLimit = SM.get_rental_limit(subscriptionType) #max rentals
    checkSubscription = SM.check_subscription(custID, subInfo) #checks if subscription is active
    
    if(availableToRentGame(gameID)):
        if(checkSubscription):
            #print(rentalTracker(custID))
            if(rentalTracker(custID) < rentalLimit):
                DB.addNewRentalEntry(gameID, custID)
            else:
                print("customar has max games already !")
        else:
            print("subscirptopn is nto valid")
        #print(DB.returnGameDict())
    else:
        print("game not available")

if __name__ == "__main__":
    #rentGame("abcd", "ttfl02,apxl01,drg01")
    #gameBeingRented("yomi01","abcd")
    
    custID = "abcd"
    gameID = "rktl01"
    
    if(availableToRentGame(gameID)):
        gameBeingRented(gameID,custID)
    else:
        print("game nto available")

    pass