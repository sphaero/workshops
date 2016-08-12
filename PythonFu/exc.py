
cupcakes = 9

def yo_mama():
    global cupcakes
    cupcakes -= 1
    if cupcakes:
        return cupcakes
    # implicit return None
    
def yo_mama2():
    global cupcakes
    cupcakes -= 1
    if cupcakes < 3:
        return cupcakes, "We need moa"
    elif cupcakes:
        return cupcakes
    # implicit return None

for x in range(9):
    print(yo_mama())
    
cupcakes = 9
for x in range(9):
    print(yo_mama2())


class OutOfCupCakesError(Exception):
    pass

def yo_mama3():
    global cupcakes
    cupcakes -= 1
    if cupcakes < 3:
        raise OutOfCupCakesError
    elif cupcakes:
        return cupcakes
    # implicit return None

cupcakes = 9
for x in range(9):
    try:
        print(yo_mama3())
    except OutOfCupCakesError:
        print("we need moa")

