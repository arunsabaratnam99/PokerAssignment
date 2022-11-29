import random
import copy

#Arun Sabaratnam 300297854

class Player:
  def __init__(self):
    self.hand = []
    
  def print(self):
    print(self.hand)
  
class Game(Player):
  def __init__(self, deck, players, n = 2):
    self.playersnum = n
    self.players = players
    self.tablecards = []
    self.deck = deck
    
    
  def print(self):
    print(self.playersnum)
    print(self.tablecards)
    
    for i in self.players:
      print(i.hand)
      
    print(self.deck)
    
  
  def add_card(self,index):
    self.players[index].hand.append(self.deck[0])
    self.deck.pop(0)
    
     
  def add_to_table(self):
    self.tablecards.append(self.deck[0])
    self.deck.pop(0)
    
  
  def isStraightFlush(self,values, cards):    
    firstvalues = [x[0] for x in cards]
    secondvalues = [x[1] for x in cards]
        
    if secondvalues.count(secondvalues[0]) != len(secondvalues):
      return False 
    
    else:
      valuesofhand = []
      for i in firstvalues:
        valuesofhand.append(values[i])
        valuesofhand = sorted(valuesofhand)
        
      for i in range(len(valuesofhand)):
        try:
          if valuesofhand[i+1] - valuesofhand[i] != 1:
            return False
          
        except:
          break
        
    return True 
         
  
  def isFourOfAKind(self, cards):
    firstvalues = [x[0] for x in cards]
    copyoffirstvalues = copy.deepcopy(firstvalues)
    
    firstvalues = list(set(firstvalues))
    
    if len(firstvalues) != 2:
      return False 
    
    for i in firstvalues:
      if copyoffirstvalues.count(i) == 4:
        return True 
    
    return False 

  
  def isFullHouse(self,cards):
    firstvalues = [x[0] for x in cards]
    copyoffirstvalues = copy.deepcopy(firstvalues)
    
    firstvalues = list(set(firstvalues))
        
    if len(firstvalues) != 2:
      return False 
    
    if copyoffirstvalues.count(firstvalues[0]) == 3 and copyoffirstvalues.count(firstvalues[1]) == 2 or copyoffirstvalues.count(firstvalues[0]) == 2 and copyoffirstvalues.count(firstvalues[1]) == 3:
      return True 
    
    return False 
      
  
  def isFlush(self,cards):
    secondvalues = [x[1] for x in cards]
    
    if secondvalues.count(secondvalues[0]) != len(secondvalues):
      return False 
    
    return True    
      
  def isStraight(self,values, cards):
    firstvalues = [x[0] for x in cards]

    valuesofhand = []
    for i in firstvalues:
      valuesofhand.append(values[i])
      valuesofhand = sorted(valuesofhand)
      
    for i in range(len(valuesofhand)):
      try:
        if valuesofhand[i+1] - valuesofhand[i] != 1:
          return False
        
      except:
        break
        
    return True 
  
  def isThreeOfAKind(self,cards):
    firstvalues = [x[0] for x in cards]
    copyoffirstvalues = copy.deepcopy(firstvalues)
    
    firstvalues = list(set(firstvalues))
    
    for i in firstvalues:
      if copyoffirstvalues.count(i) == 3:
        return True 
    
    return False   
  
  def isTwoPairs(self, cards):
    firstvalues = [x[0] for x in cards]
    copyoffirstvalues = copy.deepcopy(firstvalues)
    
    firstvalues = list(set(firstvalues))
    
    if len(firstvalues) != 3:
      return False 
    
    paircheck = []
    for i in range(len(firstvalues)):
      paircheck.append(copyoffirstvalues.count(firstvalues[i]))
      paircheck = sorted(paircheck)
      
    
    if paircheck == [1,2,2]:
      return True
    return False 
      
      
  def isOnePair(self,cards):
    firstvalues = [x[0] for x in cards]
    copyoffirstvalues = copy.deepcopy(firstvalues)
    
    firstvalues = list(set(firstvalues))
    
    paircheck = []
    for i in range(len(firstvalues)):
      paircheck.append(copyoffirstvalues.count(firstvalues[i]))
      paircheck = sorted(paircheck)
      
    
    if 2 in paircheck:
      return True
    return False 


deck = []
cards = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']

values = {}

for i in range(1, len(cards) + 1):
  values[cards[i-1]] = i

print(values)

suit = ['D','C','S','H']  

n = int(input('Please input the amount of players that are playing the game\n'))
players = [Player() for i in range(n)]

for i in cards:
  for j in suit:
    temp = ''
    temp = temp + i + j 
    deck.append(temp)
    
random.shuffle(deck)


game = Game(deck,players,n)

for i in range(game.playersnum):
  for j in range(5):
    game.add_card(i)
    
print(game.isStraightFlush(values,['5S', 'AS', '3S', '2S', '4S']))
print(game.isFourOfAKind(['5S','5D','5D','3D','5D']))
print(game.isFullHouse(['5S','3S','5D','3D','3S']))
print(game.isStraight(values,['TD', 'JD', 'KH', 'QS', '8S']))
print(game.isThreeOfAKind(['TD', 'JD', 'JH', 'JS', '8S']))
print(game.isTwoPairs(['TH', '6S', 'AS', 'TC', '6D'] ))
print(game.isOnePair(['TH', '6S', 'AS', 'KC', '3D']))






