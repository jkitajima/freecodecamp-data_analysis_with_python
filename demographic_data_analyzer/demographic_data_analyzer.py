"""
Demographic Data Analyzer
Extracted from the 1994 Census database.
"""


import numpy as np
import pandas as pd


def calculate_demographic_data(print_data: bool=True):
    demo = pd.read_csv('demographic_data_analyzer/adult.data.csv')
    
    race_count = demo['race']
    race_count.index = demo['race']
    race_count = race_count.value_counts()
    print(f'[Race count]\n{race_count}\n')
    
    average_age_men = round(demo['age'].loc[demo['sex'] == 'Male'].mean(), 1)
    print(f'[Average Age of Men]\n{average_age_men} years\n')
    
    demo['education'].index = demo['education']
    bach = demo['education'].loc['Bachelors'].count()
    everyone = len(demo)
    percentage_bachelors = round(bach*100 / everyone, 1)
    print("[Percentage of people who have a Bachelor's degree]")
    print(percentage_bachelors, end='%\n\n', sep='')
    
    educ = demo['education']
    salary = demo['salary']
    educ.index = range(educ.count())
    adv_educ = (educ == 'Bachelors') | (educ == 'Masters') | (educ == 'Doctorate')
    pcount = demo[(adv_educ) & (salary == '>50K')]
    higher_education_rich = round(len(pcount)*100 / len(demo[adv_educ]), 1)
    print(f'[Higher Education and Higher Salaries]\n{higher_education_rich}%\n')

    pcount = demo[(~(adv_educ)) & (salary == '>50K')]
    lower_education_rich = round(len(pcount)*100 / len(demo[~(adv_educ)]), 1)
    print(f'[Lower Education and Higher Salaries]\n{lower_education_rich}%\n')
    
    higher_education = educ[adv_educ].count()
    lower_education = educ[~(adv_educ)].count()
    
    hpw = demo['hours-per-week']
    min_work_hours = hpw.min()
    print(f'[Minimun work hours per week]\n{min_work_hours}\n')
    
    num_min_workers = len(demo[hpw == min_work_hours])
    rp = len(demo[(hpw == min_work_hours) & (salary == '>50K')])
    rich_percentage = round(rp*100 / num_min_workers, 1)
    rich_percentage = int(rich_percentage)
    print(f"[No work at all and get all the money]\n{rich_percentage}\n")
    
    country = demo['native-country']
    
    def get_country_percentage(country_name: str) -> float:
        population = country[country == country_name].count()
        population = population.item()
        
        rich_people_count = demo[(country == country_name) & (salary == '>50K')]
        rich_people_count = len(rich_people_count)
        
        percentage = round(rich_people_count*100 / population, 1)
        
        return percentage
    
    highest_earning_country = None
    highest_earning_country_percentage = None
    
    for e in country.value_counts().iteritems():
        p = get_country_percentage(e[0])
    
        if highest_earning_country_percentage is None or highest_earning_country_percentage < p:
            highest_earning_country_percentage = p
            highest_earning_country = e[0]
        
    print(f'[Highest Earning Country]\n{highest_earning_country} - {highest_earning_country_percentage}%\n')     
          
    top_IN_occupation = demo[(salary == '>50K') & (country == 'India')]
    top_IN_occupation = top_IN_occupation['occupation'].value_counts()
    top_IN_occupation = top_IN_occupation.first_valid_index()
    print(f'[Top Occupation of Richest People in India]\n{top_IN_occupation}')

calculate_demographic_data()
