# Write  a  program  that  asks  the  user  for  his  annual  income  and  displays  the
# corresponding tax rate.
rent = int(input())
tax = 0
if rent >= 60000:
    tax = rent * 0.45
elif 60000 > rent > 35000:
    tax = rent * 0.3
elif 35000 >= rent > 20000:
    tax = rent * 0.2
elif 20000 >= rent > 10000:
    tax = rent * 0.15
elif 10000 >= rent:
    tax = rent * 0.05
print(tax)