
import statistics as stats

from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        
        averages = []
        for row in self.data:
            y = []
            data_row = row[1:]
            for x in data_row:
                try:
                    y.append(float(x))
                except: ValueError
                
                continue
            
            averages.append(round(stats.mean(y),3))
        return averages

    def median02(self):

        median = []
        for row in self.data:
            y = []
            data_row = row[1:]
            for x in data_row:
                try:
                    y.append(float(x))
                except: ValueError
                
                continue
            
            self.data_sorted = sorted(self.data)
            
            median.append(round(stats.median(y)))
        return median
    print(StockData)

    def stddev03(self):
        """pt3
        """
        ...
