#  Jianyu Zheng 33062456.  ICS 32 Lab sec 5.  Lab asst 3.

import urllib.request


def data(symbol, start_date, end_date) -> list:
    '''takes the symbol and two dates and returns the information of the stock'''
    try:
        start = split_date(start_date)
        end = split_date(end_date)
        response = urllib.request.urlopen(url_format(symbol, minus_one(start[1]),\
                    start[2], start[0], minus_one(end[1]), end[2], end[0]))
##        print('response', response)
        data = response.read()
##        print('data', data)
        string_data = data.decode(encoding = 'utf-8')
##        print('string_data', string_data)
        response.close()
        data_list = string_data.splitlines()[1:]
##        print('data_list', data_list)
        data_list.reverse()
##        print(string_data)
        return data_list
    except urllib.error.HTTPError:
        print('Sorry, the stock is not found.')
        return False
    except:
        print('Error. Cannot connect to the server.')
        return False
##    except socket.gaierror:
##        print('Sorry, cannot connect to the online.')
##    except urllib.error.URLError:
##        print('Connection error')
##    except NameError:
##        print('NameError')


def minus_one(string: str) -> str:
    '''takes a string, turns it into a number and then minus one, returns a string'''
    result = str(int(string) - 1)
    return result

def split_date(date: str) -> list:
    '''takes the string of date and split them into a list'''
    L = date.split('-')
    return L

def url_format(symbol: str, start_month: str, start_day: str, start_year: str,\
               end_month: str, end_day:str, end_year: str) -> str:
    '''takes these elements and returns a url format'''
    return 'http://ichart.yahoo.com/table.csv?s={}&a={}&b={}&c={}&d={}&e={}&f={}&g=d'\
           .format(symbol, start_month, start_day, start_year, end_month, end_day, end_year)
