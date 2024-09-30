#5b. Without loops

Years = (1980, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989)
Respondents = (17, 35, 26, 26, 25, 27, 35, 21, 19)

# Dictionary comprehension with zip to combine the lists
MyDict = {year: respondent for year, respondent in zip(Years, Respondents)}

print(MyDict)
