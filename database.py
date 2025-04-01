import datetime

'''
By: F322925
    
Contains all of the necessary functions required for accessing 
the data stored in the txt files for different purposes
'''

gamesAvailableDict = {
"cod01":True,
"apxl01":True,
"prtl02":True,
"rktl01":True,
"hmff01":True,
"fifa01":True,
"ttfl02":True,
"hlkt01":True,
"amgs01":True,
"mcft01":True,
"lgsw02":True,
"tmrd01":True,
"yomi01":True,
"ror2":True,
"nms01":True,
"soth01":True,
"des201":True,
"drg01":True,
"slts01":True,
"lcmp01":True
}

#// Game Search 

def returnGameInfoList():
    '''
    Returns the contents of the Game_Info.txt file as a 2D list
    '''

    games = []

    try:
        f = open("Game_Info.txt", "r")
        for game in f:
            gameInfo = game.strip().split(",")
            games.append(gameInfo)
        f.close()
        return games
    except FileNotFoundError:
        print("Error -- File not found. [returnGameInfoList - database.py]")
    except Exception as e:
        print(e)

def returnGameDict():
    '''
    Returns a dictionary of the games that are available and not available to 
    rent.
    '''
    try:
        f = open("Rental.txt", "r")
        for record in f:
            recordInfo = record.strip().split(",")
            if(recordInfo[2] == ""):
                gamesAvailableDict[recordInfo[0]] = False
            else:
                gamesAvailableDict[recordInfo[0]] = True
        f.close()
        return gamesAvailableDict
    except FileNotFoundError:
        print("Error - File not found. [checkIfAvailableToRent - database.py]")
    except Exception as e:
        print(e)

#// Game Rent

def addNewRentalEntry(gameID, custID):
    '''
    Adds new record to rental.txt
    '''
    f = open("Rental.txt", "a")
    f.write("\n" + str(gameID) + "," + 
            str(datetime.date.today()) + "," + "," + str(custID))
    f.close()

def rentalCustIDs():
    '''
    Returns list of all customer IDs in the Rental.txt file
    '''
    custIDs = []
    f = open("Rental.txt", "r")
    for line in f:
        line = line.strip().split(",")
        if(line[3] == "RentedCustomerID"):
            continue
        if(line[2] == ""):
            custIDs.append([line[3],line[2]])
    f.close()
    return custIDs

def getRentedGamesByCustID(custID):
    '''
    Returns list of all games associated with a specific customer ID
    '''
    rentedGameList = []
    f = open("Rental.txt", "r")
    for line in f:
        line = line.strip().split(",")
        if(line[3] == custID):
            rentedGameList.append(line)
    f.close()
    return rentedGameList

#// Game Return

def returnGame(custID, gameID):
    '''
    Edits the Rental.txt record by adding the return date to the record
    '''
    custID = str(custID)
    gameID = str(gameID)
    oldRecord = []

    gameList = getRentedGamesByCustID(custID)
    for game in gameList:
        if(game[0] == gameID):
            oldRecord = game
    oldRecordStr = oldRecord[0]+","+oldRecord[1]+","+oldRecord[2]+","+oldRecord[3]

    f = open("Rental.txt", "r")
    data = f.read().replace(oldRecordStr,gameID+","+oldRecord[1]+","+
                            str(datetime.date.today())+","+custID)
    f.close()
    f = open("Rental.txt", "w")
    f.write(data)
    f.close()

#// Inventory Pruning

def returnRentalHistory():
    '''
    Returns list of every entry in Rental.txt -> [GameID,RentalDate,ReturnDate]
    '''
    data = []
    f = open("Rental.txt", "r")
    for line in f:
        line = line.strip().split(",")
        if(line[0] == "GameID"):
            continue
        data.append([line[0], line[1], line[2]])
    f.close()
    return data
    


if __name__ == "__main__":
    #print(returnGameInfoList())
    #print(checkIfAvailableToRent(["ttfl02","apxl01","drg01"]))
    #print(returnGameDict())
    #addNewRentalEntry("game", "CUSTID")
    #rentalCustIDs()
    #getRentedGamesByCustID("abcd")
    #returnGame("ijkl", "apxl01")
    returnRentalHistory()
    pass