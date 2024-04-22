# closure is nested function 
# closure is a function having access to the scope of parent

def parent_function(person):
    coins = 3

    def play_games():
        nonlocal coins
        #fungsi nonlocal mengubah isi variabel coins di parent (dan tidak termasuk local variable)
        coins -= 1 

        if coins :
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1 :
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins")

        
    return play_games



tommy = parent_function("Tommy")
jenny = parent_function("Jenny")


tommy()
tommy()
tommy()

jenny()