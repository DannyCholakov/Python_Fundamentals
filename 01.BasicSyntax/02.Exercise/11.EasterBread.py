budget = float(input())
flourPrice = float(input())

packEggs = flourPrice * 0.75
priceMilk = (flourPrice * 1.25) * 0.25

priceOfBread = packEggs+priceMilk+flourPrice
remainingAmount = budget % priceOfBread

breadCount = int((budget-remainingAmount)/priceOfBread)

coloredEggs = 0
breadCounter = 0.0
for bread in range(breadCount):
    breadCounter += 1
    coloredEggs += 3
    if breadCounter % 3 == 0:
        coloredEggs -= breadCounter-2

print(f'You made {breadCount} loaves of Easter bread! Now you have {coloredEggs:.0f} eggs and {remainingAmount:.2f}BGN left.')