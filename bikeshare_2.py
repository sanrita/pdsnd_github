import time
import calendar
import pandas as pd


CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_city():
    """
    Return a string of the city that the user would like to retrieve data for.

    Args:
    None

    Returns:
    string of the city
    """
    while True:
        try:
            city = input('\nWould you like to see data for Chicago, New York City or Washington?\n').strip().lower()
            if city in CITY_DATA:
                break
        except:
            print('\nInvalid city value provided. Acceptable values are Chicago, New York City or Washington\n')
            continue
    return city

def get_month():
    """
    Return a string of the month that the user would like to retrieve data for.

    Args:
    None

    Returns:
    string of the month
    """
    while True:
        try:
            month = input('\nWhich month(January, February, March, April, May, June) would you like to see data for? If all, please type All\n').strip().lower()
            if month in MONTHS or month == 'all':
                break
        except:
            print('\nInvalid month provided. Acceptable values are January, February, March, April, May, June or All\n')
            continue
    return month

def get_dayofweek():
    """
    Return a string of the day of week that the user would like to retrieve data for.

    Args:
    None

    Returns:
    string of the day of the week
    """
    while True:
        try:
            dayofweek = input('\nWhich day of the week(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) would you like to see data for? If All, please type all\n').strip().lower()
            if dayofweek in DAYS or dayofweek == 'all':
                break
        except:
            print('\nInvalid day of the week provided. Acceptable values are Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All\n')
            continue
    return dayofweek

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = get_city()

    # get user input for month (all, january, february, ... , june)
    month = get_month()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_dayofweek()

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTHS.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most popular month of travel: {}\n'.format(calendar.month_name[common_month]))

    # display the most common day of week
    common_dayofweek = df['day_of_week'].mode()[0]
    print('Most popular day of week for travel: {}\n'.format(common_dayofweek))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_starthour = df['hour'].mode()[0]
    print('Most popular hour travelled: {}\n'.format(common_starthour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most popular start station used: {}\n'.format(start_station))

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most popular end station used: {}\n'.format(end_station))

    # display most frequent combination of start station and end station trip
    common_combinationstations = df.groupby(['Start Station', 'End Station']).count()
    print('Most frequent combination of start station and end station trip: {}'.format(common_combinationstations))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_traveltime = df['Trip Duration'].sum()
    print('Total travel time: {}\n'.format(total_traveltime))

    # display mean travel time
    mean_traveltime = df['Trip Duration'].mean()
    print('Average travel time: {}'.format(mean_traveltime))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """
    Displays statistics on bikeshare users.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Type of users:\n{}\n'.format(user_types))


    # Display counts of gender

    # Check if dataframe contains column gender
    if ('Gender' in df):
        gender = df['Gender'].value_counts()
        print('Types of users by gender:\n{}\n'.format(gender))
    else:
        print('No user gender information avaliable for your city')

    # Check if dataframe contains column Birth Year
    if ('Birth Year' in df):
        # Display earliest, most recent, and most common year of birth
        earliest_birthyear = int(df['Birth Year'].min())
        print('Oldest person to use our services was born in the year: {}\n'.format(earliest_birthyear))

        recent_birthyear = int(df['Birth Year'].max())
        print('Youngest person to use our services was born in the year: {}\n'.format(recent_birthyear))

        common_birthyear = int(df['Birth Year'].mode()[0])
        print('Most popular users that use our service is born in the year: {}'.format(common_birthyear))
    else:
        print('No user year of birth information avaliable for your city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def prompt_user(question):
    """
    Return a string of the users feedback when prompted to determine whether he/she would like to see the filtered data.

    Args:
    (str) question - question asked to the user

    Returns:
    string of the users feedback
    """
    while True:
        try:
            user_feedback = input('\n{} Type Yes or No\n'.format(question)).strip().lower()
            break
        except:
            print('\nInvalid feedback provided. Acceptable values are Yes or No\n')
            continue
    return user_feedback

def display_data(df):
    """
    Displays data from the filtered dataframe based on users request.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    show_rows = 5;
    start_row = 0
    end_row = show_rows

    # get user input for viewing of the filtered data
    user_feedback = prompt_user('Would you like to see the filtered data?')
    while True:
        if (user_feedback == 'yes'):
            print('Display data from rows {} to {}\n'.format(start_row + 1, end_row))
            print(df.iloc[start_row: end_row])

            start_row += show_rows
            end_row += show_rows

            user_feedback = prompt_user('Would you like to see data for rows {} to {}?'.format(start_row + 1, end_row))
            continue
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
