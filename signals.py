#  Jianyu Zheng 33062456.  ICS 32 Lab sec 5.  Lab asst 3.


class sm_signal:
    '''contain the function of simple moving average singal stratigies'''

    def __init__(self, data_list: list, N: int, indicator: list):
        '''takes a list of data and a number, returns three parameters'''
        self._data = data_list
        self._range = N
        self._indicator = indicator
    
    def cal(self) -> list:
        '''takes a list of data and a number, returns a list of singals'''
        result = []
        for a in range(self._range):
            result.append('')
        for i in range(self._range, len(self._data)):
            if self._data[i].split(',')[4] < self._indicator[i] and self._data[i-1].split(',')[4] > self._indicator[i-1]:
                result.append('SELL')
            elif self._data[i].split(',')[4] > self._indicator[i] and self._data[i-1].split(',')[4] < self._indicator[i-1]:
                result.append('BUY')
            else:
                result.append('')
        return result



class dir_signal:
    '''contain the function of directional singal stratigies'''

    def __init__(self, data_list: list, buy_threshold: int, sell_threshold: int):
        '''takes a list of data and two numbers, returns a list of price change'''
        self._change = data_list
        self._buy = buy_threshold
        self._sell = sell_threshold

    def cal(self):
        '''takes a list of directional and two numbers, returns a list of singal'''
        result = ['']
        for i in range(1, len(self._change)):
            if self._change[i] > self._buy and self._change[i-1] <= self._buy:
                result.append('BUY')
            elif self._change[i] < self._sell and self._change[i-1] >= self._sell:
                result.append('SELL')
            else:
                result.append('')
        if self._sell > 0:
            result[0] = 'SELL'
        if self._buy < 0:
            result[0] = 'BUY'
        return result




