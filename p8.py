day=input('Please type Day: ')
amount=int(input('Please type the Shopping amount: '))
if day.lower()=="sunday" and amount>5000:
    discount=(amount*10)/100
    amount=amount-discount
    print("After Discount 10% your Final Price:",amount)
else:
    print("Your Final Price is:",amount)
