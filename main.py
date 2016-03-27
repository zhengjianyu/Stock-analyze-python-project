#  Jianyu Zheng 33062456.  ICS 32 Lab sec 5.  Lab asst 3.

import signals
import indicators
import webwork
import date_determine as _D_

def main():
    '''main function'''
    while True:
        symbol = input('Please enter the ticker symbol of the stock you want to search: ')
        print()
        while True:
            start_date = input('Please enter the start date of the analysis in the following format:\nYYYY-MM-DD\n')
            if _D_.check_date(start_date) == True:
                if _D_.date_to_days(start_date) <= _D_.date_of_today():
                    break
                print("Error. The start date should be on or before today's date. Please try again.")
            print()
        print()
        while True:
            end_date = input('Please enter the end date:\nYYYY-MM-DD\n')
            if _D_.check_date(end_date) == True:
                if _D_.date_to_days(start_date) <= _D_.date_to_days(end_date):
                    if _D_.date_to_days(end_date) <= _D_.date_of_today():
                        break
                    else:
                        print("Error. The end date should be on or before today's date. Please try again.")
                else:
                    print('Error. The end date should be later than the start date. Please try again.')
        print()
        if webwork.data(symbol, start_date, end_date) != False:
            data_list = webwork.data(symbol, start_date, end_date)
            command = input(Menu)
            if command.upper() == 'A':
                N = int(input('Please enter the range of moving average: '))
                indicator = indicators.simple_moving_average(data_list, N)
                signal = signals.sm_signal(data_list, N, indicator.cal())
                print()
                print('SYMBOL: {}\nSTRATEGY: Simple moving average ({}-day)\n'.format(symbol, N))
                print_information_s(data_list, N, indicator.cal(), signal.cal())
                break
            elif command.upper() == 'B':
                N = int(input('Please enter the range of directional indicator: '))
                while True:
                    buy_threshold = int(input('Please enter the buy threshold: '))
                    sell_threshold = int(input('Please enter the sell threshold: '))
                    if buy_threshold > sell_threshold:
                        break
                    else:
                        print('Error. The buy threshold should be larger than the sell threshold. Please try again.\n')
                indicator = indicators.directional(data_list, N)
                signal = signals.dir_signal(indicator.cal(), buy_threshold, sell_threshold)
                print()
                print('SYMBOL: {}\nSTRATEGY: Directional ({}-day), buy above {}, sell below {}\n'.format(symbol, N, '%+d'%buy_threshold, sell_threshold))
                print_information_d(data_list, N, indicator.cal(), signal.cal())
                break
            else:
                invalid_command(command)
        print('Please try again.\n')
    


Menu = '''
Please choose the indicators to analyze:
A: Simple moving average.
B: Directional indicator.
'''


def invalid_command(response) -> None:  # string -> interaction
    ''' Print message for invalid menu command. '''
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.\n")

def print_information_d(data_list: list, N: int, indicator: list, signal: list) -> None:
    '''takes a list of data and prints the information'''
    print('DATE           CLOSE        INDICATOR       SIGNAL')
    for i in range(len(data_list)):
        print('{:15}{:13}{:16}{}'.format(data_list[i].split(',')[0],\
                data_list[i].split(',')[4], '%+d'%indicator[i], signal[i]))

def print_information_s(data_list: list, N: int, indicator: list, signal: list) -> None:
    '''takes a list of data and prints the information'''
    print('DATE           CLOSE        INDICATOR       SIGNAL')
    for i in range(len(data_list)):
        print('{:15}{:13}{:16}{}'.format(data_list[i].split(',')[0],\
                data_list[i].split(',')[4], str(indicator[i]), signal[i]))




if __name__ == '__main__':
    main()
### which price should I use: 'close' or 'close adj(adjust)'
