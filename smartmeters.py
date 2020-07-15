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
        print("**Getting File Data For Day Data**")
        return self.file_data
    
    def dataByDay(self):
        """This Method creates a dictionary of the days and how many data points
           the days have
        """
        print("**Analyzing Individual Days**")
        sortedByDate = self.getData().sort_values(by='day')

        for (index, row) in sortedByDate.iterrows():
            if row["day"] in self.days:
                self.days[row["day"]] += 1
            else:
                self.days[row["day"]] = 1 
        print("**DONE**")
        print()

    def dataByYear(self):
        """Gets the Average amount of data points per day for each year"""
        print("**Getting Average Amount of Data Points Per Day For Each Year**")
        self.dataByDay()

        for key in self.days:
            self.years[key[:4]] += self.days[key]

        for year in self.years.items():
            self.years[year[0]] = self.years[year[0]] / 365

        print("**DONE**")
        print()

    def displayYear(self):
        """Bar Graph of the average amount of data points per day by year"""


        self.dataByYear()

        print("**Displaying Year Data Using Bar Graph**")

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
        """Displays the days average energy use from 2011-2014"""
        self.DataByDay()

        print("**Displaying Day Data Using Line Graph**")

        plt.plot(*zip(*sorted(self.days.items())),color="green")
        plt.title("Average Household Data From 2011-2014")
        plt.xlabel('Year')
        plt.ylabel('Households')
        plt.show()

    def bestYear(self):
        """This is the method that automatically gets our best year to evaluate seasonal energy data"""
        self.dataByYear()
        print("**Calculating Best Year To Use**")
        for year in self.years.items():

            if self.years[year[0]] > self.best_year[1]:
                self.best_year = year

        print("**DONE**")
        print()

        return self.best_year


class SeasonalEnergyUse:

    def __init__(self, best_year):
        """Initialize"""
        self.file_data = pd.read_csv("block_0.csv", usecols=["day", "energy_sum"])
        self.best_year = best_year
        self.avgDayDict = {}

    def getData(self):
        """Gets file data necessary for finding the seasonal energy use"""
        print("**Getting File Data For Seasonal Energy Use**")

        return self.file_data

    def printData(self):
        """Prints the data, if necessary"""
        print(self.file_data)

    def avgPerDay(self):
        """This method finds the average per day of the best year.

           ***This is the (backend) end goal of this project***
        """
        print("**Finding the Average Per Day of the Best Year")


        sortedDays = self.getData().sort_values(by='day')

        tempDayDict = {}

        for (index, row) in sortedDays.iterrows():
            if row["day"][:4] == self.best_year[0]:
                if row['day'] in tempDayDict:
                    tempDayDict[row['day']] = tempDayDict[row['day']][0]+row['energy_sum'], tempDayDict[row['day']][1]+1
                else:
                    tempDayDict[row['day']] = row['energy_sum'], 1

        for day in tempDayDict.items():
            self.avgDayDict[day[0]] = round(day[1][0]/day[1][1], 2)

        print("**DONE**")
        print()

    def displayBestYear(self):
        """This method displays a line graph of energy consumption over 2013"""
        self.avgPerDay()
        print("**Displaying the Average Energy Consumption Over the Best Year**")

        plt.plot(*zip(*sorted(self.avgDayDict.items())),color="green")
        plt.title("Average Energy Use in 2013")
        plt.xlabel('2013')
        plt.ylabel('Average Energy Use')
        x = ["Jan",'Feb',"March","April","May","June","July","Aug","Sept","Oct", "Nov","Dec"]
        x_pos = [i for i, _ in enumerate(x)]
        plt.xticks(x, x_pos)
        plt.show()





def driver():
    """Driver/Main"""

    most_data = MostData()

    # most_data.displayDay() # Use this to see data per day from 2011-2014

    #most_data.displayYear() # Use this to see a visual of the bar graph of the best year

    #print(most_data.bestYear())

    season_use = SeasonalEnergyUse(most_data.bestYear())

    #season_use.avgPerDay()

    season_use.displayBestYear()


driver()
