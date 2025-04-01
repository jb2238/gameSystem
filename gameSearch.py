import database as db

def searchForGame(searchTerm):
    '''
    By: F322925
    
    Given a search term will search through game_info.txt for all 
    games with this search term in either platform, genre, title or ID.

    Returns a list containing the game info for all found games.
    '''
    resultList = []
    games = db.returnGameInfoList()

    for game in games:
        for i in range(0,4):
            if game[i].lower() == searchTerm.lower() :
                resultList.append(game)
    return resultList



if __name__ == "__main__":
    print(searchForGame(input()))