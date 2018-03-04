class Yatzy:

    def __init__(self,*dice):

        self.dice = []
        for die in dice:
            
            self.dice.append(die)
        self.dice=tuple(self.dice)

    @staticmethod
    def chance(*dice):
        
        if isinstance(dice[0], tuple):
            dice=dice[0]
        
        return sum(dice)
        

    @staticmethod
    def yatzy(*dice):
        if isinstance(dice[0], tuple):
            dice=dice[0]
        
        if dice.count(dice[0]) == len(dice):
                return 50
        return 0

    @staticmethod
    def ones(*dice):
        if isinstance(dice[0], tuple):
           dice=dice[0]
        
        return dice.count(1)
    @staticmethod
    def twos(*dice):
        if isinstance(dice[0], tuple):
            dice=dice[0]
        return dice.count(2)*2
    @staticmethod
    def threes(*dice):
        if isinstance(dice[0], tuple):
            dice=dice[0]
        return dice.count(3)*3
    @staticmethod
    def fours(*dice):
        if isinstance(dice[0], tuple):
            dice=dice[0]
        return dice.count(4)*4
    @staticmethod
    def fives(*dice):
        if isinstance(dice[0], tuple):
            dice=dice[0]
        return dice.count(5)*5
    @staticmethod
    def sixes(*dice):
        if isinstance(dice[0], tuple):
            dice=dice[0]
        return dice.count(6)*6
    @staticmethod
    def score_pair(*dice):
        if isinstance(dice[0], tuple):
            dice=dice[0]
        
        dice=tuple(reversed(sorted(dice)))
        for die in dice :
            if dice.count(die)==2:
                return die*2
        return 0
    @staticmethod
    def two_pair(*dice):
        if isinstance(dice[0], tuple):
            dice=dice[0]
        score=0
        pairs=0
        for die in dice :
            if dice.count(die)==2:
                score=score+die
                pairs+=0.5
        if pairs==2:
            return score
        else:
            return 0
    @staticmethod
    def four_of_a_kind(*dice):
        
        if isinstance(dice[0], tuple):
            dice=dice[0]
            
        for die in dice :
            if dice.count(die)==4:
                return die*4
        return 0

    @staticmethod
    def three_of_a_kind(*dice):
        
        if isinstance(dice[0], tuple):
            dice=dice[0]
            
        for die in dice :
            if dice.count(die)==3:
                return die*3
        return 0

    @staticmethod
    def smallStraight(*dice):
        if isinstance(dice[0], tuple):
                dice=dice[0]
        expectedDice=(1,2,3,4,5)
        for die in expectedDice:
            if dice.count(die)<1:
                return 0
        return 15
    @staticmethod
    def largeStraight(*dice):
        if isinstance(dice[0], tuple):
                dice=dice[0]
        expectedDice=(2,3,4,5,6)
        for die in expectedDice:
            if dice.count(die)<1:
                return 0
        return 20

    @staticmethod
    def fullHouse(*dice):
        if isinstance(dice[0], tuple):
                dice=dice[0]
        pair,three=False,False
        score=0
        for die in dice:
            if dice.count(die)==2:
                pair=True
                score=score+die
            if dice.count(die)==3:
                three=True
                score=score+die
        if pair and three:
            return score
        return 0
        

                
        
                
        

if __name__=="__main__":

    tirada1=Yatzy(1,2,3,4,5)
    assert 15 == Yatzy.chance(tirada1.dice)
    assert 15 == Yatzy.smallStraight(tirada1.dice)
    tirada=(1,2,3,4,5)
    assert 15 == Yatzy.chance(tirada)
    tirada=(6,6,4,4,3)
    assert 23 == Yatzy.chance(tirada) 
    assert 0 == Yatzy.yatzy(tirada)
    assert 50 == Yatzy.yatzy(6,6,6,6,6)
    assert 25 == Yatzy.fives(5,5,5,5,5)
    assert 12 == Yatzy.score_pair(2,2,5,6,6)
    tirada1=Yatzy(1,5,3,4,5)
    assert 10 == Yatzy.score_pair(tirada1.dice)
    assert 0 == Yatzy.two_pair(2,1,1,3,4)
    assert 18 == Yatzy.two_pair(2,4,4,5,5)
    assert 24 == Yatzy.four_of_a_kind(6,5,6,6,6)
    tirada1=Yatzy(1,5,5,5,5)
    assert 20 == Yatzy.four_of_a_kind(tirada1.dice)
    assert 20 == Yatzy.largeStraight(2,3,4,5,6)
    assert 0 == Yatzy.largeStraight(2,3,4,5,1)
    assert 13 == Yatzy.fullHouse(2,3,2,3,3)
    assert 0 == Yatzy.fullHouse(1,1,2,2,3)