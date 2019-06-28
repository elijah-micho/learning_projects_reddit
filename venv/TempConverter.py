def converterBot():

    def celToFar():
        temp_celsius = int(input('Enter a temperature in celsius: '))
        return temp_celsius * (9 / 5) + 32

    def farToCel():
        temp_farenheit = float(input('Enter a temperature in Farenheit: '))
        return (temp_farenheit - 32) * 5 / 9

    user_answer = int(input('Do you want to convert F to C or C to F? Enter 1 or 2 '))

    if user_answer == 1:
        print(farToCel())
    else:
        print(celToFar())

while True:
    converterBot()

    restart = input('Convert again? (Type Y for Yes and N for No) ')
    if restart == 'Y':
        converterBot()
    else:
        break
