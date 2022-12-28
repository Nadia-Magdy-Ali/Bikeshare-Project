import pandas as pd
import numpy as np
import time
CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    city=input('We have US bikeshare data for Chicago, New York, and Washington.\n\n\
Kindly enter the name of the city you want to explore\n').title()
    cities=('Washington','New York','Chicago')
    while city not in cities :
        print('\nOps!This is not a valid answer, please try again\n')
        city=input('We have US bikeshare data for Chicago, New York, and Washington.\n\n\
Kindly enter the name of the city you want to explore\n').title()

    # get user input for month (all, january, february, ... , june)

    month =input('\nIf you wish to filter your data by month please type in the month you wish to filter by\n\
January, February, March, April, May, June or you can type all if you don\'t want to filter\n').title()
    all_months=('January','February','March','April','May','June','All')

    while month not in all_months:
        print('\nOps!This is not a valid answer, please try again\n')
        month =input('\nIf you wish to filter your data by month please type in the month you wish to filter by\n\
January, February, March, April, May, June or you can type all if you don\'t want to filter\n').title()
    # get user input for day of week (all, monday, tuesday, ... sunday)

    day=input('\nIf you wish to filter your data by day please please type the day you wish to filter by\n\
Saturday , Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or you can type all if you don\'t wish to filter\n').title()
    all_days=('Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','All')

    while day not in all_days:
        print('\nOps!This is not a valid answer, please try again\n')
        day=input('\nIf you wish to filter your data by day please please type the day you wish to filter by\n\
Saturday , Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or you can type all if you don\'t wish to filter\n').title()

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
    CITY_DATA = { 'Chicago': 'chicago.csv',
                  'New York': 'new_york_city.csv',
                  'Washington': 'washington.csv' }

    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month_name()
    df['day_of_week']=df['Start Time'].dt.day_name()

    if month != 'All':
        df= df[df['month']== month]
    if day != 'All':
        df=df[df['day_of_week'].str.startswith(day.title())]

    return df


def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    while month == 'All':
        popular_month= df['month'].mode()[0]
        print('The most popular month is: {}'.format(popular_month))
        break
    # display the most common day of week
    while day =='All':
        popular_day= df['day_of_week'].mode()[0]
        print('The most popular day is: {}'.format(popular_day))
        break
    # display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular hour is: {}'.format(popular_hour))
    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print('The commonly used start station is: {}'.format(popular_start_station))
    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The commonly used end station is: {}'.format(popular_end_station))
    # display most frequent combination of start station and end station trip
    df['route']=df['Start Station']+' '+ df['End Station']
    pop_end_start=df['route'].mode()[0]
    print('The commonly used combination of start station and end station is: {}'.format(pop_end_start))
    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: {} seconds'.format(total_travel_time))
    # display mean travel time
    aveg_time=df['Trip Duration'].mean()
    print('The average travel time is: {} seconds'.format(aveg_time))

    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_typs=df['User Type'].value_counts()
    print('User types count:\n{}'.format(user_typs))
    # Display counts of gender
    if city != 'Washington':
        gen_count=df['Gender'].value_counts()
        print('\nUser gender count:\n{}'.format(gen_count))

    # Display earliest, most recent, and most common year of birth
        early_year=int(df['Birth Year'].min())
        print('The earliest year of birth is: {}'.format(early_year))
        recen_year=int(df['Birth Year'].max())
        print('The most recent year of birth is: {}'.format(recen_year))
        comm_year=int(df['Birth Year'].mode())
        print('The most common year of birth is: {}'.format(comm_year))

    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*40)

def raw_data(city):
    """
     purpose: checkinking if user would like to view raw data
     returns: if yes was entered it will return 5 rows of raw data
     the function will keep asking the user if he wants to see more untill the user says no or we reach the end

     """
    choice=input('Would you like to see 5 rows of raw data ? yes/no\n').lower()
    while choice not in ('yes','no'):
        print('\nOps!Invalid input please try again\n')
        choice=input('Would you like to see 5 lines of raw data ? yes/no\n').lower()
    while choice == 'yes':
        try:
            for rows in pd.read_csv(CITY_DATA[city],chunksize=5):
                pd.set_option('display.max_columns', 200)
                print(rows)

                choice =input('Would you like to see another 5 rows? yes/no\n').lower()
                while choice not in ('yes','no'):
                    print('\nOps!Invalid input please try again\n')
                    choice=input('Would you like to see another 5 rows? yes/no\n').lower()
                    
                if choice != 'yes':
                    break
            break
        except KeyboardInterrupt:
            print('Thank you')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        while restart not in ('yes', 'no'):
            print('\nOps!Invalid input please try again\n')
            restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':

            break


if __name__ == "__main__":
	main()
