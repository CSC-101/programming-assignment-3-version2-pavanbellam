import data



#task 1
def population_total(lst:list[data.CountyDemographics])->int: #It just uses a for loop to take in each county's population and adds it to our counter
    pop = 0
    for a in lst:
        pop+=a.population['2014 Population']
    return pop
#task 2 we iterate through a lst and check the abreviations are the same and then appends it if it is true
def filter_by_state(lst:list[data.CountyDemographics],abr:str)->list[data.CountyDemographics]: #Uses an empty list and a for loop to go through each object and check if the abreviation is right and then will append the object to the list at the end returning said list
    cdlst = []
    for a in lst:
        if abr==a.state:
            cdlst.append(a)
    return cdlst
#task 3 it is the same piece of code just with different goals in each we do a for loop through the list and check what type of key it is and then add up the population in 2014
def population_by_education(lst:list[data.CountyDemographics], wrd:str) -> float:
    pop = 0
    for eth in lst:
        if wrd in eth.education:
                pop +=eth.population['2014 Population'] *(eth.education[wrd]/100)
    return pop
def population_by_ethnicities(lst:list[data.CountyDemographics], wrd:str) -> float:
    pop = 0
    for eth in lst:
            if wrd in eth.ethnicities:
                pop +=eth.population['2014 Population']*(eth.ethnicities[wrd]/100)
    return pop
def population_below_poverty_level(lst:list[data.CountyDemographics]) -> float:
    pop = 0
    for pov in lst:
                pop +=pov.population['2014 Population']*(pov.income['Persons Below Poverty Level']/100)
    return pop
#task 4 does the same thing as the previous task, but we use sub percentages which we have done by dividing with a ratio and multiplying by a hundred and we do that ethinicty, education, and income
def percent_by_education(counties: list[data.CountyDemographics], education_key: str) -> float:
    total_population = population_total(counties)
    total_with_education = population_by_education(counties, education_key)

    if total_population == 0:
        return 0.0

    return (total_with_education / total_population)*100

def percent_by_ethnicities(counties: list[data.CountyDemographics], eth_key: str) -> float:
    total_population = population_total(counties)
    total_with_eth = population_by_ethnicities(counties, eth_key)

    if total_population == 0:
        return 0.0

    return (total_with_eth / total_population)*100

def percent_below_poverty(counties: list[data.CountyDemographics]) -> float:
    total_population = population_total(counties)
    total_with_eth = population_below_poverty_level(counties)

    if total_population == 0:
        return 0.0

    return (total_with_eth / total_population)*100
#task 5 Basically similar to the first task we have an empty array and we iterate through objects in the list and if it passes our condition we append it and return the list
def education_greater_than(lst: list[data.CountyDemographics], wrd: str, threshold: float) -> list[data.CountyDemographics]:
    cdlst = []
    for county in lst:
        if wrd in county.education and county.education[wrd] > threshold:
            cdlst.append(county)
    return cdlst

def education_less_than(lst: list[data.CountyDemographics], wrd: str, threshold: float) -> list[data.CountyDemographics]:
    cdlst = []
    for county in lst:
        if wrd in county.education and county.education[wrd] < threshold:
            cdlst.append(county)
    return cdlst

def ethnicity_greater_than(lst: list[data.CountyDemographics], wrd: str, threshold: float) -> list[data.CountyDemographics]:
    cdlst = []
    for county in lst:
        if wrd in county.ethnicities and county.ethnicities[wrd] > threshold:
            cdlst.append(county)
    return cdlst

def ethnicity_less_than(lst: list[data.CountyDemographics], wrd: str, threshold: float) -> list[data.CountyDemographics]:
    cdlst = []
    for county in lst:
        if wrd in county.ethnicities and county.ethnicities[wrd] < threshold:
            cdlst.append(county)
    return cdlst

def below_poverty_level_greater_than(lst: list[data.CountyDemographics], threshold: float) -> list[data.CountyDemographics]:
    cdlst = []
    for county in lst:
        if "Persons Below Poverty Level" in county.income and county.income["Persons Below Poverty Level"] > threshold:
            cdlst.append(county)
    return cdlst

def below_poverty_level_less_than(lst: list[data.CountyDemographics], threshold: float) -> list[data.CountyDemographics]:
    cdlst = []
    for county in lst:
        if "Persons Below Poverty Level" in county.income and county.income["Persons Below Poverty Level"] < threshold:
            cdlst.append(county)
    return cdlst
