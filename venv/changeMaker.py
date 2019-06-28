def changeMaker():
    try:
        change_amount = float(input('Enter your dollar amount here: '))
        print('$'+ str(change_amount))
    except ValueError:
        print('Not a valid value!')

    change_amount = change_amount*100

    quarters = int(change_amount/25)
    remainder1 = change_amount % 25

    dimes = (remainder1/10)
    remainder2 = (dimes*10)%10

    nickels = remainder2/5
    remainder3 = (nickels*5)%5

    pennies = remainder3

    print(str(quarters) + ' quarters')
    print(str(int(dimes)) + ' dimes')

    print(str(int(nickels)) + ' nickels')

    print(str(int(pennies)) + ' pennies')

changeMaker()

