fruits = ['apple', 'banana', 'cherry', 'grape', 'orange', 'pear']

def pickFruit():
    while True:
        try:
            checkFruit = int(input('Which fruit do you want to see? Choose from 0-5'))
            print(fruits[checkFruit])
        except IndexError:
            print('I said 0-5...try again!')

pickFruit()

