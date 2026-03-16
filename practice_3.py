# EXERCISE 1 AT https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

from datetime import datetime
name = input('May i know your name please ? : ')
age = int(input('May i know your age please ? : '))
age_till_hundred = 100 - age
current_year = datetime.now().year
print(
    f'{name} will turn 100 years old the year {age_till_hundred + current_year}')
