
import pandas as pd
import time
import numpy as np


CITY_DATA = {"chicago" : "chicago.csv",
"new york": "new_york_city.csv",
"washington": "washington.csv" } 

months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
options = ['none', 'day', 'month', 'both']

def get_filters():

    '''This function helps to get filters regarding the city and time (day or month or both) that the user wants to analyze

        Returns:
        city - name of the city to analyze
        month - name of the month to filter by, or "all" to apply no month filter
        day - name of the day of week to filter by, or "all" to apply no day filter
   
    '''
    
    print('Hello! Let\'s explore some US bikeshare data! \n')
    
    city = input('Please type the city name that you would like to see. Chicago, New York, or Washington? \n').lower()
    
    cont_loop_c = False
    while cont_loop_c== False:
        if city in CITY_DATA.keys():
            #print('You have chosen {} as city'.format(city.title()))
            break
        else:
            city = input('There is something wrong. Please make sure that you type correctly one of the following cities: Chicago, New York, or Washington? \n').lower()
        cont_loop_c = False

    option = input("Would you like to filter data by month, day, both or not at all. Type 'none' for no time filter \n").lower()
    cont_loop_o = False
    while cont_loop_o== False:
        if option == 'month':
            month = input('Please type one of the following month that you would like to see. January, February, March, April, May, June. \n').lower()
            cont_loop_m = False
            while cont_loop_m== False:
                if month in months:
                    day ='all'
                #print('You have chosen {} as month'.format(month.title()))
                    break
                else:
                    month = input('There is something wrong. Please make sure that you type correctly \n').lower()
                cont_loop_m = False
            break
        elif option == 'day':
            day = input('Please type the day that you would like to see. \n').lower()
            cont_loop_d = False
            while cont_loop_d== False:
                if day in days:
                    month = 'all'
                #print('You have chosen {} as month'.format(month.title()))
                    break
                else:
                    day = input('There is something wrong. Please make sure that you type correctly \n').lower()
                cont_loop_d = False
            break
        elif option == 'both':
            month = input('Please type the month that you would like to see. \n').lower()
            cont_loop_mm = False
            while cont_loop_mm== False:
                if month in months:
                #print('You have chosen {} as month'.format(month.title()))
                    break
                else:
                    month = input('There is something wrong. Please make sure that you type correctly \n').lower()
                cont_loop_mm = False
            day = input('Please type the day that you would like to see. \n').lower()
            cont_loop_dd = False
            while cont_loop_dd== False:
                if day in days:
                #print('You have chosen {} as month'.format(month.title()))
                    break
                else:
                    day = input('There is something wrong. Please make sure that you type correctly \n').lower()
                cont_loop_dd = False
            break
        elif option =='none':
            month='all'
            day='all'
            break
        else:
            option = input('There is something wrong. Please make sure that you type correctly \n').lower()
               
    cont_loop_o = False
 
    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    '''This function loads data according to the filters chisen by the user
       
        Args:
        city - name of the city to analyze
        month - name of the month to filter by, or "all" to apply no month filter
        day - name of the day of week to filter by, or "all" to apply no day filter

        Returns:
        df: dataframe of bikeshare data
   
    '''
    
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month_i = months.index(month)
        df = df[df['month'] == month_i]

    if day != 'all':
        days_i = days.index(day)-1
        df = df[df['day_of_week'] == days_i]
        
    
    return df


def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    pop_month = df['month'].mode()[0]
    print("The most common month is " + str(pop_month))

    pop_day = df['day_of_week'].mode()[0]
    print("The most common day is " + str(pop_day))
   
    pop_hour =df['hour'].mode()[0]
    print("The most common hour is " + str(pop_hour))



    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    '''This function calculates the statistics regarding the stations
       
        Args:
        df: dataframe of bikeshare data

        Returns:

        the most common starting station according to the filter
        the most common end station according to the filter
        the most frequent combination of start station and end station trip according to the filter
   
    '''
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    pop_start_station = df['Start Station'].mode()[0]
    print("The most common Start Station is " + str(pop_start_station))

    pop_end_station = df['End Station'].mode()[0]
    print("The most common End Station is " + str(pop_end_station))

    combined_station = 'Start station: ' + df['Start Station'] + 'and end station: ' + df['End Station']
    print("The most frequent combination of start station and end station trip is " + combined_station.mode()[0])



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    tot_duration = df['Trip Duration'].sum()
    print("Total travel time: " + str(tot_duration))

    avg_duration = round(df['Trip Duration'].mean(),2)
    print("Average travel time: " + str(avg_duration))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_type = df['User Type'].value_counts().to_frame()
    print(user_type)

    if city != 'washington':
        gender_type = df['Gender'].value_counts().to_frame()
        earliest= df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print(gender_type)
        print("The earliest birth year of users is: " + str(earliest))
        print("The most recent birth year of users is: " + str(most_recent))
        print("The most common birth year of users is: " + str(most_common))
    else:
        print("The information regarding users gender and birth date are not available for Washington")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    
    while True:
        see_raw_data = input('\n Would you like to see the raw_data? Please type yes or no. \n')
        if see_raw_data.lower() == 'yes':
            number_rows =  len(df.index)
            i = 0
            while see_raw_data == 'yes':
                print(df.iloc[i:i+5, :])
                i+=5
                if i >= number_rows:
                    print('The end of data set is reached.\n')
                    break
                see_raw_data = input(' Please type "yes" to see the next 5 rows, otherwise please type "no" \n').lower()
            if see_raw_data.lower() == 'no':
                break
     
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? Please type yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
