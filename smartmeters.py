import pandas as pd
import matplotlib.pyplot as plt


class MostData:
    """This Class is used to produce a year that has the most data points
       since we only want to evaluate a single year's worth of data. We can use
       this class to produce a visual, and to have our program automatically
       suggest what year to use.
    """

    def __init__(self):
        """Initialize, we only need LCLid and the days in which data was collected"""
        self.file_data = pd.read_csv("block_0.csv", usecols=["LCLid", "day"])
        self.days = {}
        self.years = {"2011": 0, "2012": 0, "2013": 0, "2014": 0 }
        self.best_year = 'year', 0

    def getData(self):
        """Returns the file data in column x row form"""
        return self.file_data
    
    def dataByDay(self):
        """This Method creates a dictionary of the days and how many data points
           the days have
        """

        sortedByDate = self.getData().sort_values(by='day')

        for (index, row) in sortedByDate.iterrows():
            if row["day"] in self.days:
                self.days[row["day"]] += 1
            else:
                self.days[row["day"]] = 1 
        #print(days)

    def dataByYear(self):
        """Gets the Average amount of data points per day for each year"""

        self.dataByDay()

        for key in self.days:
            self.years[key[:4]] += self.days[key]

        for year in self.years.items():
            self.years[year[0]] = self.years[year[0]] / 365

    def displayYear(self):
        """Bar Graph of the average amount of data points per day by year"""

        self.dataByYear()
        xAxis = ['2011', '2012', '2013', '2014']
        energyUseAverage = [self.years['2011'], self.years['2012'], self.years['2013'], self.years['2014']]


        x_pos = [i for i, _ in enumerate(xAxis)]

        plt.bar(x_pos, energyUseAverage, color='green')

        plt.xlabel("Year")
        plt.ylabel("Average Data Points Per Day")
        plt.title("Energy Usage Data Points by Year from 2011-2014")

        plt.xticks(x_pos, xAxis)

        plt.show()


    def displayDay(self):
        self.DataByDay()
        plt.plot(*zip(*sorted(self.days.items())),color="green")
        plt.title("Average Household Data From 2011-2014")
        plt.xlabel('Year')
        plt.ylabel('Households')
        plt.show()

    def bestYear(self):
        """This is the method that automatically gets our best year to evaluate seasonal energy data"""
        self.dataByYear()
        print("passed")
        for year in self.years.items():

            if self.years[year[0]] > self.best_year[1]:
                self.best_year = year

        return self.best_year


class SeasonalEnergyUse:

    def __init__(self):
        self.file_data = pd.read_csv("block_0.csv", usecols=["LCLid", "day", "energy_sum"])

    def getData(self):
        return self.file_data

    def printData(self):
        print(self.file_data)

    def avgPerDay(self):
        sortedDays = self.getData().sort_values(by='day')
        print(sortedDays)


def driver():

    most_data = MostData()

    # most_data.displayDay() # Use this to see data per day from 2011-2014

    #most_data.displayYear() # Use this to see a visual of the bar graph of the best year

    #print(most_data.bestYear())

    season_use = SeasonalEnergyUse()

    season_use.avgPerDay()


driver()
