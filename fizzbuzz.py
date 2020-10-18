# https://codegolf.stackexchange.com/questions/58615/1-2-fizz-4-buzz
limit = 100
fizz_variable = 3
buzz_variable = 5

for i in range(1, limit + 1) :
    fizz = (i % fizz_variable) == 0
    buzz = (i % buzz_variable) == 0

    print fizz * "Fizz" + buzz * "Buzz" + (not fizz and not buzz) * str(i)
