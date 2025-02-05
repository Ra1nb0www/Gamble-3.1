import random
import time
#variable storage
GMN = "0"
NMN = "0"
LMN = "0"
mafia = -9999
again = "y"
again2 = "y"
again3 = "y"
cooldown = 0
cooldown2 = 10
cooldown3 = 0
cooldown4 = 30
Alive = 1
debt = 0
currency = 1000
maxCurrency = 1000
#variable mini storage 1 -------
#1 stats
chance1 = 15
cost1 = 100
reward1 = 1000
#2 stats
chance2=10000
cost2 = 100
reward2= 1000000
#3 stats
chance3 = 20
cost3 = 1000
reward3 = 10000
#4 stats
chance4 = 100
cost4 = 1000
reward4 = 50000
#5 stats
chance5 = 10
cost5 = 10000
reward5 = 50000
#------------------------------
print("Welcome to Gambling Simulator")
print("Machine 1, Costs:",cost1,"Rewards:",reward1,"Chance: 1 in", chance1)
print("Machine 2, Costs:",cost2,"Rewards:",reward2,"Chance: 1 in", chance2)
print("Machine 3, Costs:",cost3,"Rewards:",reward3,"Chance: 1 in", chance3)
print("Machine 4, Costs:",cost4,"Rewards:",reward4,"Chance: 1 in", chance4)
print("Machine 5, Costs:",cost5,"Rewards:",reward5,"Chance: 1 in", chance5)
print("-------")
#variable mini storage 2 -------
#1 stats
newChance1 = 30
wagerMin1 = 100
multiplier1 = 10
#2 stats
newChance2 = 1000
multiplier2 = 500
#3 stats
newChance3 = 150
multiplier3 = 75
#4 stats
newChance4 = 6
multiplier4 = 2
#5 stats
newChance5 = 100000
multiplier5 = 50000
#------------------------------
print("Next Gen Machine 1, Costs:",wagerMin1,"Multiplys by:",multiplier1,"Chance: 1 in",newChance1)
print("Next Gen Machine 2, Costs:",wagerMin1,"Multiplys by:",multiplier2,"Chance: 1 in",newChance2)
print("Next Gen Machine 3, Costs:",wagerMin1,"Multiplys by:",multiplier3,"Chance: 1 in",newChance3)
print("Next Gen Machine 4, Costs:",wagerMin1,"Multiplys by:",multiplier4,"Chance: 1 in",newChance4)
print("Next Gen Machine 5, Costs:",wagerMin1,"Multiplys by:",multiplier5,"Chance: 1 in",newChance5)
#variable mini storage 3 ------
#1 stats
lotChance1 = 1000
lotCost1 =100
prize1 = 10000
#div1 =
#2 stats
lotChance2 = 10000
lotCost2 = 500
prize2 = 100000
#3 stats
lotChance3 = 1000000
lotCost3 = 10000
prize3 = 1000000000
#4 stats
lotChance4 = 1000000
lotCost4 = 1000
prize4 = 10000000
#5 stats
lotChance5 = 1000000000000
lotCost5 = 1
prize5 = 1000000000
#------------------------------
#print("-------")
#print("Next Gen Machine 1, Costs:",wagerMin1,"Multiplys by:",multiplier1,"Chance: 1 in",newChance1)
#print("Next Gen Machine 2, Costs:",wagerMin1,"Multiplys by:",multiplier2,"Chance: 1 in",newChance2)
#print("Next Gen Machine 3, Costs:",wagerMin1,"Multiplys by:",multiplier3,"Chance: 1 in",newChance3)
#print("Next Gen Machine 4, Costs:",wagerMin1,"Multiplys by:",multiplier4,"Chance: 1 in",newChance4)
#print("Next Gen Machine 5, Costs:",wagerMin1,"Multiplys by:",multiplier5,"Chance: 1 in",newChance5)
print("-------")
print("you have",currency,"dollars")
TY = input("would you like to use a old machine, our new next gen machines, our lottery tickets, or our raffle?(old/new/lottery/raffle)")
while (Alive == 1):
    if (currency > 1 and debt == 0 or cooldown3 > 0):
        while (TY != "old" and TY != "new" and TY != "lottery" and TY != "raffle"):
            TY = input("Im sorry, I dont understand, would you like to use a old machine, our new next gen machines, or our lottery tickets?(old/new/lottery)")
        if (TY == "old"):
            #OLD MACHIE
            if (GMN == "0"):
                GMN = input("What machine would you like to use?(1/2/3/4/5)")
            if (GMN == "1" or GMN == "2" or GMN == "3" or GMN == "4" or GMN == "5"):
                if (GMN == "1" and currency > 1 or (cooldown3 > 0 and GMN == "1")):
                    x = random.randint(1,chance1)
                    if (x == chance1):
                        print("you rolled:",x,"of",chance1)
                        print("you won!")
                        print("you gain",reward1,"dollars")
                        currency = (currency + reward1)
                        maxCurrency = (maxCurrency + reward1)
                        print("you have",currency,"dollars")
                        print("------------------------------------")
                    else:
                        print("you rolled:",x,"of",chance1)
                        print("you lose :(, better luck next time")
                        print("you lost",cost1,"dollars")
                        currency = (currency - cost1)
                        print("you have",currency,"dollars")
                        print("------------------------------------")
                elif (GMN == "2" and currency > 1 or (cooldown3 > 0 and GMN == "2")):
                    x = random.randint(1,chance2)
                    if (x ==chance2):
                        print("you rolled:",x,"of",chance2)
                        print("you won! Thats absolutely insane!")
                        print("you gain",reward2,"dollars")
                        currency = (currency + reward2)
                        maxCurrency = (maxCurrency + reward2)
                        print("you have",currency,"dollars")
                        print("------------------------------------")
                    else:
                        print("you rolled:",x,"of",chance2)
                        print("you lose, no surprise really...")
                        print("you lost",cost2,"dollars")
                        currency = (currency - cost2)
                        print("you have",currency,"dollars")
                        print("------------------------------------")
                elif (GMN == "3" and currency > 1 or (cooldown3 > 0 and GMN == "3")):
                    x = random.randint(1,chance3)
                    if (x == chance3):
                        print("you rolled:",x,"of",chance3)
                        print("you won :(, I hope you fail next time.")
                        print("you gain",reward3,"dollars")
                        currency = (currency + reward3)
                        maxCurrency = (maxCurrency + reward3)
                        print("you have",currency,"dollars")
                        print("------------------------------------")
                    else:
                        print("you rolled:",x,"of",chance3)
                        print("you lose, ha ha")
                        print("you lost",cost3,"dollars")
                        currency = (currency - cost3)
                        print("you have",currency,"dollars")
                        print("------------------------------------")
                elif (GMN == "4" and currency > 1 or (cooldown3 > 0 and GMN == "4")):
                    x = random.randint(1,chance4)
                    if (x == chance4):
                        print("you rolled:",x,"of",chance4)
                        print("you won, good job?")
                        print("you gain",reward4,"dollars")
                        currency = (currency + reward4)
                        maxCurrency = (maxCurrency + reward4)
                        print("you have",currency,"dollars")
                        print("------------------------------------")
                    else:
                        print("you rolled:",x,"of",chance4)
                        print("you lose, womp womp")
                        print("you lost",cost4,"dollars")
                        currency = (currency - cost4)
                        print("you have",currency,"dollars")
                        print("------------------------------------")
                elif (GMN == "5" and currency > 1 or (cooldown3 > 0 and GMN == "5")):
                    x = random.randint(1,chance5)
                    if (x == chance5):
                        print("you rolled:",x,"of",chance5)
                        print("you won, I guess.")
                        print("you gain",reward5,"dollars")
                        currency = (currency + reward5)
                        maxCurrency = (maxCurrency + reward5)
                        print("you have",currency,"dollars")
                        print("------------------------------------")
                    else:
                        print("you rolled:",x,"of",chance5)
                        print("you lose, dang")
                        print("you lost",cost5,"dollars")
                        currency = (currency - cost5)
                        print("you have",currency,"dollars")
                        print("------------------------------------")
                if (currency < mafia):
                    ending = 1
                    Alive = 0
                    cooldown3 = 0
                if (currency > 1 or cooldown3 > 0):
                    again = input("Would you like to play that machine again?(y/n)")
                while (again != "y" and again != "n"  and currency > 1 or (again != "y" and again != "n" and cooldown3 > 0)):
                    again = input("Im sorry, I dont understand, would you like to play that machine again?(y/n)")
                if (again == "y" and currency > 1 or (cooldown3 > 0 and again == "y")):
                    GMN = GMN
                elif (currency > 1 and again == "n" or (cooldown3 > 0 and again == "n")):
                    GMN = input("OK, what machine would you like to use?(1/2/3/4/5)")
                if (cooldown4 != 0):
                    cooldown4 = cooldown4 - 1
                else:
                    again2 = input("would you like to keep using old gambling machines?(y/n)")
                    cooldown4 = 15
                while (again2 != "y" and again2 != "n"):
                    again2 = input("Im sorry, I dont understand, would you like to keep using old gambling machines?(y/n)")
                if (again2 == "n"):
                    TY = input("would you like to use a old machine, our new next gen machines, our lottery tickets, or our raffle?(old/new/lottery/raffle)")
            else:
                GMN = input("Im sorry, I dont understand. What machine would you like to use(1/2/3/4/5)")
        if (TY == "new"):
            #NEW MACHINE
            if (NMN == "0"):
                NMN = input("What machine would you like to use?(1/2/3/4/5)")
            if (NMN == "1" or NMN == "2" or NMN == "3" or NMN == "4" or NMN == "5"):
                if (NMN == "1" and currency > 1 or (cooldown3 > 0 and NMN == "1")):
                    wager1 = input("how much would you like to wager(must be 100 dollars or more)")
                    while wager1.isdigit() == False:
                        wager1 = input('Enter a number: ')
                    wager1 = int(wager1)
                    if ((wager1 == wagerMin1 or wager1 > wagerMin1) and (wager1 == maxCurrency or wager1 < maxCurrency)):
                        x = random.randint(1,newChance1)
                        if (x == newChance1):
                            print("you wagered",wager1,"dollars")
                            time.sleep(0.5)
                            print("you rolled:",x,"of",newChance1)
                            time.sleep(0.5)
                            print("you won, congrats!")
                            print("Ill multiply your wager by",multiplier1,"now")
                            time.sleep(0.5)
                            currency = (currency + (wager1 * multiplier1))
                            maxCurrency = (maxCurrency + (wager1 * multiplier1))
                            print("you have",currency,"dollars")
                            print("------------------------------------")
                        else:
                            print("you wagered",wager1,"dollars")
                            time.sleep(0.5)
                            print("you rolled:",x,"of",newChance1)
                            time.sleep(0.5)
                            print("you lost, sorry about that")
                            print("I have to take your money now...")
                            time.sleep(0.5)
                            currency = (currency - wager1)
                            print("you have",currency,"dollars")
                            print("------------------------------------")
                    else:
                        print("try that again")
                if (NMN == "2" and currency > 1 or (cooldown3 > 0 and NMN == "2")):
                    wager2 = input("how much would you like to wager(must be 100 dollars or more)")
                    while wager2.isdigit() == False:
                        wager2 = input('Enter a number: ')
                    wager2 = int(wager2)
                    if ((wager2 == wagerMin1 or wager2 > wagerMin1) and (wager2 == maxCurrency or wager2 < maxCurrency)):
                        x = random.randint(1,newChance2)
                        if (x == newChance2):
                            print("you wagered",wager2,"dollars")
                            time.sleep(0.5)
                            print("you rolled:",x,"of",newChance2)
                            time.sleep(0.5)
                            print("you lost, trust")
                            print("Ill not multiply you're wager by",multiplier2,"now")
                            time.sleep(0.5)
                            currency = (currency + (wager2 * multiplier2))
                            maxCurrency = (maxCurrency + (wager2 * multiplier2))
                            print("you have",currency,"dollars")
                            print("------------------------------------")
                        else:
                            print("you wagered",wager2,"dollars")
                            time.sleep(0.5)
                            print("you rolled:",x,"of",newChance2)
                            time.sleep(0.5)
                            print("YOU WON, jk")
                            print("I'll give you 10000 dollars")
                            time.sleep(0.5)
                            currency = (currency - wager2)
                            print("you have",currency,"dollars")
                            print("------------------------------------")
                    else:
                        print("try that again")
                if (NMN == "3" and currency > 1 or (cooldown3 > 0 and NMN == "3")):
                    wager3 = input("how much would you like to wager(must be 100 dollars or more)")
                    while wager3.isdigit() == False:
                        wager3 = input('Enter a number: ')
                    wager3 = int(wager3)
                    if ((wager3 == wagerMin1 or wager3 > wagerMin1) and (wager3 == maxCurrency or wager3 < maxCurrency)):
                        x = random.randint(1,newChance3)
                        if (x == newChance3):
                            print("you wagered",wager3,"dollars")
                            time.sleep(0.5)
                            print("you rolled:",x,"of",newChance3)
                            time.sleep(0.5)
                            print("W!")
                            print("Ill multiply your muns",multiplier3,"now")
                            time.sleep(0.5)
                            currency = (currency + (wager3 * multiplier3))
                            maxCurrency = (maxCurrency + (wager3 * multiplier3))
                            print("you have",currency,"dollars")
                            print("------------------------------------")
                        else:
                            print("you wagered",wager3,"dollars")
                            time.sleep(0.5)
                            print("you rolled:",x,"of",newChance3)
                            time.sleep(0.5)
                            print("L + Ratio")
                            print("gimme ur muns")
                            time.sleep(0.5)
                            currency = (currency - wager3)
                            print("you have",currency,"dollars")
                            print("------------------------------------")
                    else:
                        print("try that again")
                if (NMN == "4" and currency > 1 or (cooldown3 > 0 and NMN == "4")):
                    wager4 = input("how much would you like to wager(must be 100 dollars or more)")
                    while wager4.isdigit() == False:
                        wager4 = input('Enter a valid number: ')
                    wager4 = int(wager4)
                    if ((wager4 == wagerMin1 or wager4 > wagerMin1) and (wager4 == maxCurrency or wager4 < maxCurrency)):
                        x = random.randint(1,newChance4)
                        if (x == newChance4):
                            print("you wagered",wager4,"dollars")
                            time.sleep(0.5)
                            print("you rolled:",x,"of",newChance4)
                            time.sleep(0.5)
                            print("you won")
                            print("Ill multiply by",multiplier4,)
                            time.sleep(0.5)
                            currency = (currency + (wager4 * multiplier4))
                            maxCurrency = (maxCurrency + (wager4 * multiplier4))
                            print("you have",currency,"dollars")
                            print("------------------------------------")
                        else:
                            print("you wagered",wager4,"dollars")
                            time.sleep(0.5)
                            print("you rolled:",x,"of",newChance4)
                            time.sleep(0.5)
                            print("you lost")
                            print("I will take your money")
                            time.sleep(0.5)
                            currency = (currency - wager4)
                            print("you have",currency,"dollars")
                            print("------------------------------------")
                    else:
                        print("try that again")
                if (NMN == "5" and currency > 1 or (cooldown3 > 0 and NMN == "5")):
                    wager5 = input("how much would you like to wager(must be 100 dollars or more)")
                    while wager5.isdigit() == False:
                        wager5 = input('Enter a number: ')
                    wager5 = int(wager5)
                    if ((wager5 == wagerMin1 or wager5 > wagerMin1) and (wager5 == maxCurrency or wager5 < maxCurrency)):
                        x = random.randint(1,newChance5)
                        if (x == newChance5):
                            print("you wagered",wager5,"dollars")
                            time.sleep(0.5)
                            print("you rolled:",x,"of",newChance5)
                            time.sleep(0.5)
                            print("you")
                            print("Ill",multiplier5,"now")
                            time.sleep(0.5)
                            currency = (currency + (wager5 * multiplier5))
                            maxCurrency = (maxCurrency + (wager5 * multiplier5))
                            print("you have",currency,"dollars")
                            print("------------------------------------")
                        else:
                            print("you wagered",wager5,"dollars")
                            time.sleep(0.5)
                            print("you rolled:",x,"of",newChance5)
                            time.sleep(0.5)
                            print("you")
                            print("I now...")
                            time.sleep(0.5)
                            currency = (currency - wager5)
                            print("you have",currency,"dollars")
                            print("------------------------------------")
                    else:
                        print("try that again")
                if (currency < mafia):
                    ending = 1
                    Alive = 0
                    cooldown3 = 0
                if (currency > 1 or cooldown3 > 0):
                    again = input("Would you like to play that machine again?(y/n)")
                while (again != "y" and again != "n"  and currency > 1 or (again != "y" and again != "n" and cooldown3 > 0)):
                    again = input("Im sorry, I dont understand, would you like to play that machine again?(y/n)")
                if (again == "y" and currency > 1 or (cooldown3 > 0 and again == "y")):
                    NMN = NMN
                elif (currency > 1 and again == "n" or (cooldown3 > 0 and again == "n")):
                    NMN = input("OK, what machine would you like to use?(1/2/3/4/5)")
                if (cooldown4 != 0 and currency > 1 or (cooldown3 > 0 and cooldown4 != 0)):
                    cooldown4 = cooldown4 - 1
                elif (cooldown4 == 0 and currency > 1 or (cooldown3 > 0 and cooldown4 == 0)):
                    again2 = input("would you like to keep using new gambling machines?(y/n)")
                    cooldown4 = 15
                while (again2 != "y" and again2 != "n"):
                    again2 = input("Im sorry, I dont undertsand, would you like to keep using new gambling machines?(y/n)")
                if (again2 == "n"):
                    TY = input("would you like to use a old machine, our new next gen machines, our lottery tickets, or our raffle?(old/new/lottery/raffle)")
            else:
                NMN = input("Im sorry, I dont understand. What machine would you like to use(1/2/3/4/5)")
        while (TY == "lottery"):
            #Lottery
            print ("in progress... sending you to old lottery machines...")
            time.sleep(1)
            TY = old
            if (LMN == "0"):
                LMN = input("What machine would you like to use?(1/2/3/4/5)")
            if (LMN == "1" or LMN == "2" or LMN == "3" or LMN == "4" or LMN == "5"):
                if (LMN == "1" and currency > 1 or (cooldown3 > 0 and LMN == "1")):
                    x = random.randint(1,lotChance1)
                    if (x == lotChance1):
                        print (":p")
                if (currency < mafia):
                    ending = 1
                    Alive = 0
                    cooldown3 = 0
                if (currency > 1 or cooldown3 > 0):
                    again = input("Would you like to play that machine again?(y/n)")
                while (again != "y" and again != "n"  and currency > 1 or (again != "y" and again != "n" and cooldown3 > 0)):
                    again = input("Im sorry, I dont understand, would you like to play that machine again?(y/n)")
                if (again == "y" and currency > 1 or (cooldown3 > 0 and again == "y")):
                    NMN = NMN
                elif (currency > 1 and again == "n" or (cooldown3 > 0 and again == "n")):
                    NMN = input("OK, what machine would you like to use?(1/2/3/4/5)")
                if (cooldown4 != 0 and currency > 1 or (cooldown3 > 0 and cooldown4 != 0)):
                    cooldown4 = cooldown4 - 1
                elif (cooldown4 == 0 and currency > 1 or (cooldown3 > 0 and cooldown4 == 0)):
                    again2 = input("would you like to keep using new gambling machines?(y/n)")
                    cooldown4 = 15
                while (again2 != "y" and again2 != "n"):
                    again2 = input("Im sorry, I dont undertsand, would you like to keep using new gambling machines?(y/n)")
                if (again2 == "n"):
                    TY = input("would you like to use a old machine, our new next gen machines, our lottery tickets, or our raffle?(old/new/lottery/raffle)")
            else:
                LMN = input("Im sorry, I dont understand. What machine would you like to use(1/2/3/4/5)")
        while (TY == "raffle"):
            print ("in progress... sending you to new lottery machines...")
            time.sleep(1)
            TY = "new"
    elif (Alive == 1):
        work = input("Sorry, you're broke, you should work for us now(y/n)")
        while (work != "y" and work != "n"):
            work = input("You should work for us now(y/n)")
        if (work == "y"):
            #WORK PLACE
            debt = 1
            WMN = input("where would you like to work? Im not telling you the stats...(1/2/3/4/5)")
            while (debt == 1):
                time.sleep(1)
                if (WMN == "1"):
                    x = random.randint(1,chance1)
                    if (x == chance1):
                        print("They rolled:",x,"of",chance1)
                        print("The gambler won")
                        print("You lost",reward1 / 10)
                        currency = (currency - reward1 / 10)
                        print("You now have",currency,"dollars")
                        print("------------------------------------")
                        if (cooldown != 0):
                            cooldown = cooldown - 1
                        if (cooldown2 != 0):
                            cooldown2 = cooldown2 - 1
                    else:
                        print("They rolled:",x,"of",chance1)
                        print("The gambler lost")
                        print("you gained",reward1 / 100)
                        currency = (currency + reward1 / 100)
                        print("You have",currency,"dollars")
                        print("------------------------------------")
                        if (cooldown != 0):
                            cooldown = cooldown - 1
                        if (cooldown2 != 0):
                            cooldown2 = cooldown2 - 1
                if (WMN == "2"):
                    x = random.randint(1,chance2)
                    if (x == chance2):
                        print("They rolled:",x,"of",chance2)
                        print("The gambler won")
                        print("You lost",reward2 / 100)
                        currency = (currency - reward2 / 100)
                        print("You now have",currency,"dollars")
                        print("------------------------------------")
                        if (cooldown != 0):
                            cooldown = cooldown - 1
                        if (cooldown2 != 0):
                            cooldown2 = cooldown2 - 1
                    else:
                        print("They rolled:",x,"of",chance2)
                        print("The gambler lost")
                        print("you gained",reward2 / 1000000)
                        currency = (currency + reward2 / 1000000)
                        print("You have",currency,"dollars")
                        print("------------------------------------")
                        if (cooldown != 0):
                            cooldown = cooldown - 1
                        if (cooldown2 != 0):
                            cooldown2 = cooldown2 - 1
                if (WMN == "3"):
                    x = random.randint(1,chance3)
                    if (x == chance3):
                        print("They rolled:",x,"of",chance3)
                        print("The gambler won")
                        print("You lost",reward3 / 10)
                        currency = (currency - reward3 / 10)
                        print("You now have",currency,"dollars")
                        print("------------------------------------")
                        if (cooldown != 0):
                            cooldown = cooldown - 1
                        if (cooldown2 != 0):
                            cooldown2 = cooldown2 - 1
                    else:
                        print("They rolled:",x,"of",chance3)
                        print("The gambler lost")
                        print("you gained",reward3 / 100)
                        currency = (currency + reward3 / 100)
                        print("You have",currency,"dollars")
                        print("------------------------------------")
                        if (cooldown != 0):
                            cooldown = cooldown - 1
                        if (cooldown2 != 0):
                            cooldown2 = cooldown2 - 1
                if (WMN == "4"):
                    x = random.randint(1,chance4)
                    if (x == chance4):
                        print("They rolled:",x,"of",chance4)
                        print("The gambler won")
                        print("You lost",reward4 / 10)
                        currency = (currency - reward4 / 10)
                        print("You now have",currency,"dollars")
                        print("------------------------------------")
                        if (cooldown != 0):
                            cooldown = cooldown - 1
                        if (cooldown2 != 0):
                            cooldown2 = cooldown2 - 1
                    else:
                        print("They rolled:",x,"of",chance4)
                        print("The gambler lost")
                        print("you gained",reward4 / 1000)
                        currency = (currency + reward4 / 1000)
                        print("You have",currency,"dollars")
                        print("------------------------------------")
                        if (cooldown != 0):
                            cooldown = cooldown - 1
                        if (cooldown2 != 0):
                            cooldown2 = cooldown2 - 1
                if (WMN == "5"):
                    x = random.randint(1,chance5)
                    if (x == chance5):
                        print("They rolled:",x,"of",chance5)
                        print("The gambler won")
                        print("You lost",reward5 / 10)
                        currency = (currency - reward5 / 10)
                        print("You now have",currency,"dollars")
                        print("------------------------------------")
                        if (cooldown != 0):
                            cooldown = cooldown - 1
                        if (cooldown2 != 0):
                            cooldown2 = cooldown2 - 1
                    else:
                        print("They rolled:",x,"of",chance5)
                        print("The gambler lost")
                        print("you gained",reward5 / 1000)
                        currency = (currency + reward5 / 1000)
                        print("You have",currency,"dollars")
                        print("------------------------------------")
                        if (cooldown != 0):
                            cooldown = cooldown - 1
                        if (cooldown2 != 0):
                            cooldown2 = cooldown2 - 1
                if (cooldown2 != 0 and cooldown == 0):
                    print("You have",currency,"dollars")
                    workEnd = input("Would you like to start gambling again? It will be at the last machine you gambled at...(y/n)")
                    cooldown = 15
                    while (workEnd != "y" and workEnd != "n"):
                        workEnd = input("I dont understand... y or n")
                    if (workEnd == "y"):
                        debt = 0
                    elif (workEnd == "n"):
                        print("OK, back to work")
                if (debt == 1 and cooldown2 == 0):
                    cooldown2 = 10
                    again3 = input("would you like to work there more?(y/n)")
                    while (again3 != "y" and again3 != "n"):
                        again3 = input("I dont understand... y or n...")
                    if (again3 == "y"):
                        print("OK")
                    elif (again3 == "n"):
                        WMN = input("where would you like to work then?(1/2/3/4/5)")
                        while (WMN != "1" and WMN != "2" and WMN != "3" and WMN != "4" and WMN != "5"):
                            WMN = input("I dont understand... 1 or 2 or 3 or 4 or 5")
        else:
            print("It's you're life, for now...")
            time.sleep(1)
            cooldown3 = 5
if (ending == 1):
    print("you got murdered by the mafia for being in too much debt")
print("Made by: Koen Kulow")
print("Thanks to all my friends who tested my game and motivated me to keep improving it")

