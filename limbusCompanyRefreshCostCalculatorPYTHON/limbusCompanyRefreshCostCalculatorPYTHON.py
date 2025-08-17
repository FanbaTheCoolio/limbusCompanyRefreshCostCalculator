costMultiplier = 15
keywordlessCost = 15
keywordCost = 120
refreshRequired = 50

def main():
    isActive = True

    while isActive:
        print("""
        glory to project moon
        (1) Calculate Refresh Cost
        (2) Calculate Amount Of Refreshes Possible
        (3) Calculate Average Floor Refresh Goal
        (4) Exit
        """)
        userChoice = input()

        if userChoice == "1":
            calculateRefreshCostRequired()
        elif userChoice == "2":
            calculatePossibleRefreshAmount()
        elif userChoice == "3":
            calculateAverageRefreshGoal()
        elif userChoice == "4":
            print("may your sinclairs be many and your heathcliffs few")
            isActive = False
        else:
            print("dude you put the wrong choice in; dont it again")
def calculateAverageRefreshGoal():
    print("This is based of using the base refresh")

    print("Number of floors intended to be cleared")
    numberOfFloors = int(input())

    refreshesRequiredPerFloor = int(refreshRequired / numberOfFloors)
    costPerFloor = 0
    for currentRefreshCount in range(refreshesRequiredPerFloor):
        currentCost = (costMultiplier * currentRefreshCount) + keywordlessCost
        costPerFloor += currentCost
 
    print(f"Average refreshes required per floor: {refreshesRequiredPerFloor}")
    print(f"Average cost per floor: {costPerFloor}")
        
def calculatePossibleRefreshAmount():
    moneyAvailable = 0
    isAffordable = True
    baseCost = 0
    refreshCounter = 0

    try:
        print("Enter amount of money")
        moneyAvailable = int(input())

        print("Enter the type of refresh (B)ase, (K)eyword)")
        refreshType = input().upper()
    except:
        print("dude you did it wrong")
        return

    if refreshType == "B":
        baseCost = keywordlessCost
    elif refreshType == "K":
        baseCost = keywordCost

    while isAffordable:
        currentCost = (costMultiplier * refreshCounter) + baseCost
        moneyAvailable -= currentCost
        if moneyAvailable < 0:
            isAffordable = False
            print(f"You can afford {refreshCounter} refreshes")
        else:
            refreshCounter += 1

def calculateRefreshCostRequired():
    baseCost = 0
    totalCost = 0

    try:
        print("(B)ase refresh or (K)eyword refresh")
        refreshType = input().upper()

        print("Enter the number of refreshes:")
        amountOfRefreshes = int(input())
    except:
        print("Input mismatch; kys just use my program properly")
        return

    if refreshType == "B":
        baseCost = keywordlessCost
    elif refreshType == "K":
        baseCost = keywordCost

    for currentRefreshCount in range(amountOfRefreshes):
        currentCost = (costMultiplier * currentRefreshCount) + baseCost
        totalCost += currentCost

    print(f"Total Cost : {totalCost}")

main()