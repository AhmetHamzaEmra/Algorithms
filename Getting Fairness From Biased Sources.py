import random
def BiasedCoin():
    number = random.randint(1,4)
    if number == 3:
        return "tails"
    else:
        return "heads"

def fair():
    toss1=BiasedCoin()
    toss2=BiasedCoin()
    print (toss1)
    print (toss2)
    if (toss1!=toss2):
        if(toss1=="heads"):
            print (toss1)
        else:
            print (toss1)
    else:
        fair()
fair()
