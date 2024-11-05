# What to do
# Create valid data
# Specification
# Each person born in Romania receives a unique identification number.
# # The number has 13 digits, e.g. 1234567890123
# # What the digits represent:
# # First digit – the gender: male or female
# 1 or 2 – born between 1 January 1900 and 31 December 1999
# 3 or 4 - born between 1 January 1800 and 31 December 1899
# 5 or 6 - born between 1 January 2000 and 31 December 2099
# 7 or 8 – Foreign residents in Romania.
# 9 - For non-residents
# Next 2 digits – last 2 digits of the year of birth (e.g. born in 1980 then it will 80 )
# Next 2 digits – month of birth (01 to 12)
# Next 2 digits - date of birth (01 to 31 depending on the month of birth)
# Next 2 digits – area code (valid codes are 01 to 52)
# Next 3 digits – order number
# Last digit control number is created by:
# Take the first 12 numbers of the CNP: 123456789012 and multiply each number with the corresponding position number from this string: 279146358279 like: 1 * 2 + 2 * 7 + 3 * 9 + 4 * 1+…..+ 12 * 9= X
# You divide X by 11 the rest obtained if it is 10 then the last digit is 1 otherwise it equals the rest obtained

import random
import datetime

def random_date(start, end):
  return start + datetime.timedelta(
      seconds=random.randint(0, int((end - start).total_seconds())))

def date_generator(x):
    x = int(x[0])
    if x == 1 or x == 2:
        start = datetime.date(1900, 1, 1)
        end = datetime.date(1999, 12, 31)
        return random_date(start, end)
    elif x == 3 or x == 4:
        start = datetime.date(1800, 1, 1)
        end = datetime.date(1899, 12, 31)
        return random_date(start, end)
    elif x == 5 or x == 6:
        start = datetime.date(2000, 1, 1)
        end = datetime.date.now()
        return random_date(start, end)
    else:
        start = datetime.date(1800, 1, 1)
        end = datetime.date.now()
        return random_date(start, end)

def last_digit(x):
    d = 0
    x = [int(i) for i in "".join(s)]
    for i, j in zip(x, "279146358279"):
        d += i * int(j)
    if d % 11 < 10:
        return d % 11
    else:
        return 1

s=[str(random.randint(1, 9))]
birthday = date_generator(s)
s.append(str(birthday.year)[-2:])
s.append(("0"+str(birthday.month))[-2:])
s.append(("0"+str(birthday.day))[-2:])
s.append(("0"+str(random.randint(1, 52)))[-2:])
s.append(("00"+str(random.randint(1, 999)))[-3:])
s.append(str(last_digit(s)))
print(''.join(s))