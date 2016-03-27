#  Jianyu Zheng 33062456.  ICS 32 Lab sec 5.  Lab asst 3.

import datetime



def check_date(date: str) -> bool:
    '''takes the string of date and returns the right date or the error message'''
    try:
        if date[4] == date[7] == '-':
            if 0 < int(date[5:7]) <= 12:
                if 0 < int(date[8:]) <= 31:
                    if 1940 < int(date[0:4]):
                        return True
                    else:
                        print('The specified year is too old.')
                        return False
                else:
                    print('Invalid day.')
                    return False
            else:
                print('Invalid month.')
                return False
        else:
            print('Error. The date is entered in an incorrect format.')
            return False
    except ValueError:
        print('Error. The date should be numbers.')
    except IndexError:
        print('Error. The length of date is not in an correct format.\n')

def date_to_days(date: str) -> int:
    '''takes the string of date and turns the date into days'''
    L = split_date(date)
    days = int(L[0])*365 + int(L[1])*30 + int(L[2])
    return days

def date_of_today() -> int:
    '''returns today's date and turns it into days'''
    cur = datetime.datetime.now()
    days = cur.year*365 + cur.month*30 + cur.day
    return days

def split_date(date: str) -> list:
    '''takes the string of date and split them into a list'''
    L = date.split('-')
    return L
