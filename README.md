# London Smart Meters

This project is a simple OOP written in python to analyze over 230,000 data
points collected during the trial phase of the SmartMeter project that the
UK Power Networks conducted. They had smart meters in households collecting
data from November of 2011 to February 2014. The data set used in this project
starts in October 2012, until February 2014.

The full data set released by UK Power Networks contains 10GB of data, and
has 167 million rows. (Estimation of almost a billion data points)

The end goal of this project is to analyze the seasonal consumption of energy
for a given year. We do this in the following steps

First we need to figure out which year has the most data points for us to use.
The MostData class of this project automatically calculates the best year to
use for analyzing seasonal change. Within this class we can also produce a bar
graph containing each years average amount of daily data points.

Using the information found by the MostData class, we can use the 
SeasonalEnergyUse class to calculate the average energy consumption for over 50
households for each day of the year. We can also produce a line graph to visually
see the results.

All the graphs produced are located in the graphs folder in .png form.

AmountHouseholdData.png is a line graph displaying the amount of households 
participating in the study from 2011-2014. The actual graph produced by python 
code is interactive, showing the dates as you move the cursor. You can see a drastic 
increase right before 2013, which is something we were looking for, and hoping the data 
would reveal.

EnergyUseYear.png is a very simple bar graph that shows the amount of households
participating in the study per year.

AverageEnergy2013.png was our final product, to look for seasonal change in energy use.
It looks at the calendar year of the year produced by the MostData class. It traces the
average energy consumption in KwH for all of the houses in the study. We can see a clear
dip in energy use during the warmer months. This graph is interactive when produced
with python code.

While this project only used block_0 of the released data, this project is applicable to
any block provided by UK Power Networks. The file is hardcoded, so you must change it
within the code, or use pythons stdin to pass in the file name as an argument.

Using the run.sh file automatically pushes changes to GitHub,  and runs the program.
If you cannot execute run.sh, you have to change its file permissions with the command line
command $ chmod 777 run.sh

CONCLUSION: 
There is a clear trend in seasonal energy consumption. Trivially, we can attribute this
to using energy for heating purposes.


Author: William Sprouse
Email: wilsprouse@gmail.com
LinkedIn: https://www.linkedin.com/in/williamsprouse/


