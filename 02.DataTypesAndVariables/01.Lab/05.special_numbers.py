n = int(input())

for number in range(1,n + 1):
   sum_of_digits = 0
   digit = number

   while digit > 0:
       sum_of_digits += digit % 10
       digit = int(digit / 10)

   if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
       print(f'{number} -> True')
   else:
       print(f'{number} -> False')