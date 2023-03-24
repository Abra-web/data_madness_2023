#imports
from os.path import abspath,join,dirname,normpath,basename
from os import makedirs,rename,rmdir
import requests,zipfile,io
import shutil
import pandas as pd
#Setup data
data_folder=join(dirname(abspath('')),'data')
makedirs(data_folder,exist_ok=True)



#Read all data
data_2011 = pd.read_csv(join(data_folder,'2011 Stack Overflow Survey Results.csv'),encoding='windows-1252')
# country - What Country or Region do you live in?
# age - How old are you?
# Industry - How would you best describe the industry you work in?
# size of company - Which best describes the size of your company?
# occupation - Which of the following best describes your occupation?
# Fair amount of questions of knowledge of languages here!
# Operating system - What operating system do you use the most?
# StackOverflow usage - Which of our sites do you frequent most?

# how much they like the job - Please rate your job/career satisfaction
# money annually - Including bonus, what is your annual compensation in USD?
data_2012 = pd.read_csv(join(data_folder,'2012 Stack Overflow Survey Results.csv'))
# country - What Country or Region do you live in?
# age - How old are you?
# Industry - How would you best describe the industry you work in?
# size of company - Which best describes the size of your company?
# occupation - Which of the following best describes your occupation?
# Fair amount of questions of knowledge of languages here!
# Operating system - What desktop operating system do you use the most?
# StackOverflow usage - Which of our sites do you frequent most?
# IM ONTO SOMETHING INTERESTING
# how much they like their jobs - What best describes your career / job satisfaction?
# How much they earn annually - Including bonus, what is your annual compensation in USD?
data_2013 = pd.read_csv(join(data_folder,'2013 Stack Overflow Survey Responses.csv'))
# country - What Country or Region do you live in?
# age - How old are you?
# Industry - How would you best describe the industry you work in?
# size of company - How many people work for your company?
# occupation - Which of the following best describes your occupation?
# Fair amount of questions of knowledge of languages here!
# Also technologies excited about
# Operating system - What desktop operating system do you use the most?

# how much they like their jobs - What best describes your career / job satisfaction?
# How much they earn annually - Including bonus, what is your annual compensation in USD?

# a lot of columns with no names ffs
data_2014 = pd.read_csv(join(data_folder,'2014 Stack Overflow Survey Responses.csv'))
# country - What Country or Region do you live in?
# age - How old are you?
# GENDER  - What is your gender?
# occupation - Which of the following best describes your occupation?
# How much they earn annually - Including bonus, what is your annual compensation in USD?
# Industry - How would you best describe the industry you work in?
# Remote work - Do you work remotely?
# Remote work satisfaction - Do you enjoy working remotely?
# Fair amount of questions of knowledge of languages here!
# Also technologies excited about
# Operating system - What desktop operating system do you use the most?
#   - How do you use Stack Overflow?
data_2015 = pd.read_csv(join(data_folder,'2015 Stack Overflow Developer Survey Responses.csv'))
# NEED TO REMOVE FIRST ROW - bugged csv
# Country - Country
# Age - Age
# Gender - Gender
# Years of experience - Years IT / Programming Experience
# Occupation - Occupation
# OS - Desktop Operating System
# HUGE amount of questions of knowledge of languages here!
# HUGE technologies excited about
# Compensation - Compensation ( or Compensation: midpoint)
# Industry - Industry
# Job satisfaction - Job Satisfaction
# Remote work? - Remote Status
# a bunch of nameless columns
data_2016 = pd.read_csv(join(data_folder,'2016 Stack Overflow Survey Responses.csv'))
# Country - country
# age - age_range
# gender - gender
# occupation - occupation
# experience - experience_range
# salary - salary_range ( also salary_midpoint)
# used technologies - tech_do
# wanted - tech_want
# industry - industry
# company size - company_size_range
# remote? - remote
# job satisfaction - job_satisfaction
# why stack overflow - why_stack_overflow
data_2017 = pd.read_csv(join(data_folder,'survey_results_public2017.csv'))
#country - Country
# occupation - Professional
# remote? - HomeRemote
# company size - CompanySize
# used - HaveWorkedLanguage
# want - WantWorkLanguage
# also we have framework, database, platform, IDE
# agile etc - Methodology
# Random columns about SO, but dont know what they mean really
data_2018 = pd.read_csv(join(data_folder,'survey_results_public2018.csv'))
#Country - Country
# company size - CompanySize
# experience - YearsCoding & YearsCodingProf
# job satisfaction - JobSatisfaction
# career satisfaction - CareerSatisfaction
# salary - Salary ( also currency in Currency) - converted into ConvertedSalary
# used - LanguageWorkedWith
# want - LanguageDesireNextYear # also Database, Platform, Framework ,
# IDE
# OperatingSystem
# Visiting Stack Overflow - StackOverflowVisit
# has account - Stack OverflowHasAccount
# considering membershit - StackOverflowConsiderMember
# age - Age

data_2019 = pd.read_csv(join(data_folder,'survey_results_public2019.csv'))
# country - Country
# company size - OrgSize
# type of developer - DevType
# years coding - YearsCode and YearsCodePro
# job satisfaction - JobSat / CareerSat
# total payout - ConvertedComp
# remote work ? - WorkRemote
# used - LanguageWorkedWith
# want - LanguageDesireNextYear / Database / Platform / WebFrame / MiscTech
# system - OpSys
# SOVisitTo
# SOVisitFreq
# SOFindAnswer
# SOTimeSaved
# age - Age
# gender - Gender
data_2020 = pd.read_csv(join(data_folder,'survey_results_public2020.csv'))
# age - Age
# compensation total converted - ConvertedComp
# country - Country
# DatabaseWorkedWith / DatabaseDesireNextYear ALSO Language/ Platform/ MiscTech NEWCollabTools
# opsys - OpSys
# company size - OrgSize
# employment type - Employment
# gender - Gender
# satisfaction - JobSat\
# SOPartFreq
# SOComm
# SOAccount
# SOVisitFreq
# YearsCode
# YearsCodePro
data_2021 = pd.read_csv(join(data_folder,'survey_results_public2021.csv'))
# Country - Country
# YearsCode
# YearsCodePro
# company size -OrgSize
# LanguageHaveWorkedWith - LanguageWantToWorkWith / Database / Platform / Webframe / MiscTech / Tools
# OpSys
# SOVisitFreq
# SOPartFreq
# Age
# Gender
# ConvertedCompYearly
data_2022 = pd.read_csv(join(data_folder,'survey_results_public2022.csv'))
# remote? - RemoteWork
# YearsCode
# YearsCodePro
# size of company - OrgSize
# Country - Country
# LanguageHaveWorkedWith / LanguageWantToWorkWith ALSO Database/ Platform/ Webframe/ MiscTech/ Tools
# SOVisitFreq
# SOAccount
# SOPartFreq
# age - Age
# Gender - Gender
# ConvertedCompYearly
b=2





