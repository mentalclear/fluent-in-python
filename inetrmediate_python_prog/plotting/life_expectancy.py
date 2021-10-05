from matplotlib import pyplot

data = open("inetrmediate_python_prog/plotting/life_expectancies_usa.txt", "r").readlines()

dates = []
male_life_expectancies = []
female_life_expectancies = []

for line in data:
    date, male, female = line.split(",")
    dates.append(date)
    male_life_expectancies.append(male)
    female_life_expectancies.append(female)


pyplot.plot(dates, male_life_expectancies, "bo-", label="Male")
pyplot.plot(dates, female_life_expectancies, "mo-", label="Female")

pyplot.legend(loc="upper left")
pyplot.ylabel("Age")
pyplot.xlabel("Year")
pyplot.title("US Life expectancy for men and women over time")

pyplot.show()