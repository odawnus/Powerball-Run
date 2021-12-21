import requests
from bs4 import BeautifulSoup
import re
import random

'''
    POWERBALL RUN

    Program increases your chance of winning the Powerball Jackpot.
    Through testing and math, the probability of the same winning combination
    of white balls appearing in a draw again will not happen during your lifetime,
    your kids lifetime,or their kids lifetime. We exclude the Powerball(6th ball)
    due to the fact it adds even more complexity and the likely hood of 5 white balls
    and the Powerball appearing are almost impossible. So by simply by eliminating
    those white ball combinations increases your chances of winning because if by chance
    you quick picked one of the previous winning combinations it is almost
    certainly a losing ticket.

'''




#set for white balls so duplicates will be tossed out since you cannot have duplicate keys
megamillion = set()
#mega ball doesn't need to be set but doesn't matter since it is only one number
megaball = set()
counter = 0

# each request gets a year worth of powerball winning numbers
r = requests.get('https://powerball.com/api/v1/numbers/powerball?_format=json&min=2018-12-31%2000:00:00&max=2019-12-31%2023:59:59')
e = requests.get('https://powerball.com/api/v1/numbers/powerball?_format=json&min=2019-12-31%2000:00:00&max=2020-12-31%2023:59:59')
s = requests.get('https://powerball.com/api/v1/numbers/powerball?_format=json&min=2020-12-31%2000:00:00&max=2021-12-31%2023:59:59')


plays = input('Enter How Many Draws: ')
plays = int(plays)

def powerball(*args):
        #this set the length of the dictionary for the while balls once it hits 5 it rolls the mega ball number
        while len(megamillion) < 5:
            key = random.randint(1,69)
            number = random.randint(1,69)
            number_str = str(number)
            megamillion.add(number_str.zfill(2))
            
        else:
            megakey = 1
            number = random.randint(1,26)
            megaball.add(number)
        return
            

            


def creation():
    #joined 3 list, that gives 3 years of numbers
    res_joined = r.text + e.text + s.text

    #find all strings that contain 5 commas
    plist = [i for i in re.findall(r'[0-9]+(?:\,[0-9]+){5}',res_joined)]
    mlist = list(sorted(megamillion))

    # removes spaces, removes quotes, and removes brackets from strings that are randomly generated so text is similar to plist.
    tlist = str(mlist).replace(" ","").replace("'","").replace("[","").replace("]","")
    # iterates over plist and compares to tlist. Counts the number of times the loop is ran before finding a previous winner
    for i in plist:
        
        if i[0:-3] == tlist:
            print(tlist)
            print("This is how many times: ", counter)
            print('we have a previous winner')
            break
        else:
            None
        



def main( *args):
    count = True
    global megamillion
    global megaball
    global counter
    #finallist makes a list of all the final printouts
    finallist = []        
    while count:
        #this loop specifies the number of draws/loops
        if counter < plays:
            counter = counter + 1
            count = False
            
            for x in range(0,11):
                if x != 1:
                    powerball()
                    creation()
                    #Content that is printed out at the end of the main loop.
                    phrase = str("Your numbers are {0} and Powerball {1}".format(sorted(megamillion),megaball))
                    finallist.append(phrase[:])                    
                    continue
                    
                else:
                    count = True     
                    #when the lotto() reaches 5 times, the below variables erase their contents and wait to build the next list
                    megamillion.clear()
                    megaball.clear()
                    break
        else:
            print("\n".join(finallist))
            return
    
    return


main()


