#Black and White pebble game

import random                   #Imports the python random library

WHITEPEBBLE = 0                 #definition used to improve code readability
BLACKPEBBLE = 1                 #definition used to improve code readability
white = random.randint(1,100)   #start with a random number of white pebbles 
black = random.randint(1,100)   #start with a random number of black pebbles 

def SelectPebbles(white, black):
    '''This function randomly selects two pebbles at a time from a collection of white and black pebbles. It then returns the colours of the
       chosen pebbles and the number of remaining white and black pebbles'''
    selectedpebbles = []
    for pebblecount in range(0,2):
                                #in the specified range (start, end) - end
                                #exclusive, which, in this case, would be [0,1]
        selectedpebbles=random.randint(1,white+black)
        if selectedpebble <= white: #white pebble is selected
            white -=1
            selectedpebbles.append(WHITEPEBBLE)
        else:                       #If black pebble is selected
            black -=1
            selectedpebbles.append(BLACKPEBBLE)
    return selectedpebbles, white, black

if __name__ == "__main__":
    '''Each time this main function loops, it takes two pebbles from a collection of black and white pebbles. In the event two pebbles
       of the same colour are removed, a black pebble is returned to the collection. Otherwise, a white pebble is returned. Game continues 
       until only one pebble is left''' 
    
    print("start:")
    print("White:{white}, Black: {black}".format(white=white,black=black))

    while black + white >= 2:
        selectedpebbles, white, black = SelectPebbles(white, black)
        if selectedpebbles[0] == selectedpebbles[1]:
            black +=1
        else:
            white +=1

    print("End:")
    print("White:{white}, Black: {black}".format(white=white,black=black))