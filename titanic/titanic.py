# -----------------------------
# Analysis of Titanic data
# ----------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%pylab inline
# -------------------------------------------------------
# Create a dataframe out of the Titanic passenger data:
# -------------------------------------------------------
titanic_df = pd.read_csv('titanic_data.csv')
# print titanic_df.head(3)
# ---------------------------------
# Get some general data:
# ---------------------------------
no_of_passengers = titanic_df['PassengerId'].count()
print 'Total number of passengers = {}'.format(no_of_passengers)
no_of_females = (titanic_df[titanic_df['Sex'] == 'female'])['Sex'].count()
print 'Total number of females = {}'.format(no_of_females)
no_of_males = (titanic_df[titanic_df['Sex'] == 'male'])['Sex'].count()
print 'Total number of males = {}'.format(no_of_males)
# ---------------------------------------
# Plot some age-related information
# ---------------------------------------
male_data = titanic_df[titanic_df['Sex'] == 'male']
female_data = titanic_df[titanic_df['Sex'] == 'female']
# ------------------------------------------
# Plot a histogram for female passengers and male passengers
# ------------------------------------------
if False:
    female_data['Age'].plot(kind = 'hist', bins = 16)
    male_data['Age'].plot(kind = 'hist', bins = 16)
# ---------------------------------------------------------------------------
# Extract the information about surviving or dead passengers
# ----------------------------------------------------------------------------
survived_or_not = (titanic_df.groupby('Survived'))['PassengerId'].count()
# Number of surviving passengers
survived = survived_or_not.iloc[1]
# Number of dead passengers
not_survived = survived_or_not.iloc[0]
print 'Total no. of people survived = {}'.format(survived)
print 'Total no. of people died = {}'.format(not_survived)
# --------------------------------------------------------------------------
# Lets find out the distribution of surviving/dead passengers across genders
# --------------------------------------------------------------------------
gender_based_mortality_df = (titanic_df.groupby(['Survived', 'Sex']))['PassengerId'].count()
print gender_based_mortality_df
alive = pd.Series(gender_based_mortality_df.loc[1])
dead = pd.Series(gender_based_mortality_df.loc[0])
if False:
    print alive
    print dead
# Create a dataframe with informaton about alive and dead passengers
alive_or_dead = pd.DataFrame({'alive':alive, 'dead':dead})
if False:
    print alive_or_dead
# Express the alive_or_dead datafram in percentage
alive_or_dead_percent = (alive_or_dead/alive_or_dead.sum()) * 100
if False:
    print alive_or_dead_percent
# Now plot a stacked bar with the information about of female and male survival
female_rate = alive_or_dead_percent.loc['female']
male_rate = alive_or_dead_percent.loc['male']
if False:
    print female_rate
    print male_rate
category = ['Alive', 'Dead']
X = range(len(category))
plt.xticks([0.5, 1.5], category)
plt.title('Mortality Rate')
plt.xlabel('Category')
plt.ylabel('Percentage')
plt.bar(X, male_rate, color='b', label = 'Male')
plt.bar(X, female_rate, color='y', bottom = male_rate, label = 'Female')
plt.legend(loc = 'upper center')

