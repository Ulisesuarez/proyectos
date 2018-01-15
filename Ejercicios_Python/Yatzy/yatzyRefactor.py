class Yatzy:

    def __init__(self,*dice):
        
        self.dice=[]
        for die in dice:
            
            self.dice.append(die)
        self.dice=tuple(self.dice)
    
    @staticmethod
    def chance(*dice):
        score=0
        #print(Dados)
        for die in dice[0]:
            #print(dado)
            score+=die
                   
        return score

    @staticmethod
    def yatzy(dice):
        
        if dice.count(dice[0]) == len(dice):
            return 50
        
        return 0
        
        counts = [0]*(len(dice)+1)
        for die in dice:
            counts[die-1] += 1
        for i in range(len(counts)):
            if counts[i] == 5:
                return 50
        return 0

if __name__=="__main__":

    tirada1=Yatzy(1,2,3,4,5)
    assert 15 == Yatzy.chance(tirada1.dice)
    tirada=[1,2,3,4,5]
    assert 15 == Yatzy.chance(tirada)
    tirada=[6,6,4,4,3]
    assert 23 == Yatzy.chance(tirada)
