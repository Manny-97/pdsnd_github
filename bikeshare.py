# Importing necessary libraries
import time
import pandas as pd     # for data manipulation
import numpy as np      # for fast mathematical computation
import matplotlib.pyplot as plt     # for data visualization
import seaborn as sns

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('input any of the following to choose a city: chicago, new york city, washington')
    value = input('Input your desired city: ')
    value = value.lower()
    while len(value) != 0:
        if value in ['chicago', 'new york city', 'washington']:
            city = value
            break
        else:
            value = input('Input any of the listed options: ')



    # TO DO: get user input for month (all, january, february, ... , june)
    print('input any of the following to choose month option: all, january, february, march, april, may, june')
    value1 = input('Input your desired month: ')
    value1 = value1.lower()
    while len(value1) != 0:
        if value1 in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            month = value1
            break
        else:
            value1 = input('Input any of the listed months options: ')



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('input any of the following to choose a day of the week option: all, monday, tuesday, wednessday, thursday, friday, saturday, sunday')
    value2 = input('Input your desired day of the week: ')
    value2 = value2.lower()
    while len(value2) != 0:
        if value2 in ['all', 'monday', 'tuesday', 'wednessday', 'thursday', 'friday', 'saturday', 'sunday']:
            day = value2
            break
        else:
            value2 = input('Input any of the listed days options: ')



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june'] #'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    elif month == 'all':
        df = df[df['month'] == months]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        
        df = df[df['day_of_week']==day.title()]
    elif day == 'all':
        df = df




    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    month_dict = {1:'january', 2:'february', 3:'march', 4:'april', 5:'may', 6:'june'} #, 6:'july', 7:'august',
                  #8:'september', 9:'october', 10:'november', 11:'december'}
    val = df['Start Time'].dt.month.mode().iat[0]
    print('Most Frequent Start Month: ' + month_dict[val])

    # TO DO: display the most common day of week
    print('Most Frequent Start Day of Week:',df['Start Time'].dt.day_name().mode())

    # TO DO: display the most common start hour
    # find the most common hour (from 0 to 23)
    print('Most Frequent Start Hour:',df['Start Time'].dt.hour.mode())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    if ('Start Station' in df.columns) and ('End Station' in df.columns):
        print('Most Commonly used Start Station:',df['Start Station'].mode())

    # TO DO: display most commonly used end station
        print('Most Commonly used End Station:',df['End Station'].mode())

    # TO DO: display most frequent combination of start station and end station trip
        df['mix'] = 'Start: ' + df['Start Station'] + ' End: ' + df['End Station']
        print('The most Frequent Combination of Start and End Station: ', 
              df['mix'].value_counts().index[0], 'With count value: ', df['mix'].value_counts()[0])
    else:
        print('Trip stats cannot be calculated because Trip does not appear in the dataframe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    if 'Trip Duration' in df.columns:
        print('Total travel time: ',df['Trip Duration'].sum())

    # TO DO: display mean travel time
        print('Mean travel time:',df['Trip Duration'].mean())
    else:
        print('Trip stats cannot be calculated because Trip Duration does not appear in the dataframe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        print('Count of User Types: \n',df['User Type'].value_counts())
    else:
        print('User Type stats cannot be calculated because User Type does not appear in the dataframe')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('Count of Gender: \n',df['Gender'].value_counts())
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Earliest Year of Birth: ', df['Birth Year'].min())
        print('Most Recent Year of Birth: ', df['Birth Year'].max())
        print('Most Common Year of Birth: ', df['Birth Year'].mode())
    else:
        print('Birth year stats cannot be calculated because Birth Year does not appear in the dataframe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no? ")
    start_loc = 0
    while view_data.lower() !='':
        if view_data == 'yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_data = input("Do you wish to continue viewing the 5 rows? Enter yes or no ").lower()
        elif view_data == 'no':
            break

def missing_col(df):
    plt.figure(figsize=(10,6))
    sns.heatmap(df.isna().T, cmap='viridis', cbar_kws={'label': 'Missing Data'})
    sns.displot(df.isna().melt(value_name='missing'), y='variable', hue='missing', 
                       multiple='fill', aspect=1.25)
    plt.show()
    
def main():
    """Combines all functions together to give meaningful output"""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        missing_col(df)
        display_data(df)
        restart = input('\nWould you like to restart the program? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
