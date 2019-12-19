print ("Hello Homestead customer, please input your positive account number")

account_number = int(input("account_number\n"))
while account_number > -1:
    print (account_number)
    print()
    first_name = input("first_name\n")
    middle_name = input("middle_name\n")
    last_name = input("last_name\n")
    print()
    print (first_name)
    print (middle_name)
    print (last_name)
    print()
    purchase_price = int(input("cost of purchase"))
    monthly_payment = purchase_price / 12
    print (monthly_payment)

    print ("Hello Homestead customer, please input your positive account number")
    account_number = int(input("account_number"))
    
