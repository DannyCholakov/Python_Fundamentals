journey_cost = float(input())
number_of_months = int(input())
saved_money = 0

for month in range(1, number_of_months+1):
    if month % 4 == 0:
        saved_money += saved_money * 0.25

    if month % 2 != 0 and month != 1:
        saved_money -= saved_money * 0.16

    saved_money += journey_cost * 0.25

if journey_cost > saved_money:
    needed_money = journey_cost - saved_money
    print(f"Sorry. You need {needed_money:.2f}lv. more.")
else:
    money = saved_money - journey_cost
    print(f"Bravo! You can go to Disneyland and you will have {money:.2f}lv. for souvenirs.")
