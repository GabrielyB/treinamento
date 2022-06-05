def fizzbuzz(x):
    if x == 3:
        volta = "Fizz"
    elif x == 5:
        volta = "Buzz"
    elif x%3 == 0 and x>3:
        x = x
        if x%5 == 0 and x>5:
            volta = ("FizzBuzz")
        else:
            volta = ("Fizz")

    elif x%3 > 0 and x>3:
        x = x
        if x%5 == 0 and x>5:
            volta = ("Buzz")
        else:
            volta = x
    else:
        volta = x
    return volta
    
def test_fizzbuzz0():
    assert fizzbuzz(5) == "Buzz"
def test_fizzbuzz1():
    assert fizzbuzz(3) == "Fizz"
def test_fizzbuzz2():
    assert fizzbuzz(20) == "Buzz"
def test_fizzbuzz3():
    assert fizzbuzz(230) == "Buzz"