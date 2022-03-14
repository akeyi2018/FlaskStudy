import weakref


class prefecture:

    def __init__(self):
        pass

    def getPrefecture(self):
        da = {
            '千葉県': 1,
            '東京都': 2,
            '埼玉県': 3
        }
        return da

class Weather(prefecture):

    def __init__(self, pref):

        self.pre_list = self.getPrefecture()
        self.num = self.pre_list[pref]
        self.title = 'グラフサンプル'
        self.labels = [2017,2018,2019,2020,2021]
        self.data_01 = [30,25,28,21,20,12]
        self.data_02 = [10,15,20,10,12,18]
        self.data_03 = [3, 4, 2, 4, 2]

    def addInfo(self):
        weather = [self.labels, self.data_01, self.data_02]
        return weather
    
    def add2dInfo(self):
        w2d = []
        weather.append(self.data_01)
        weather.append(self.data_02)




if __name__ == "__main__":

    wk = Weather('東京都')
    print(wk.addInfo())

    # wp = prefecture()
    # pref = {}
    # for pre in wp.getPrefecture():
    #     print(pre)
    # print(pref)
