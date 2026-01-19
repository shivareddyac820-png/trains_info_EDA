import pandas as pd

# 1 DATA EXPLORATION AND BASIC OPERATIONS

# reading the data and displaying top 10 rows

df = pd.read_csv("C:/Users/shiva/Documents/Power BI Desktop/Railway_info.csv")
print(df.head(10))

#to know about data and datatypes
print(df.describe())
print(df.info())

#count of unique trains and source station and destination station

print(df['Train_No'].nunique())
print(df['Source_Station_Name'].nunique())
print(df['Destination_Station_Name'].nunique())

#most common source station

most_source = df['Source_Station_Name'].value_counts().idxmax()
print(df['Source_Station_Name'].value_counts().head(1))

#most  common destiantion station

most_Destination = df['Destination_Station_Name'].value_counts().idxmax()
print(df['Destination_Station_Name'].value_counts().head(1))

#finding and handling missing values

print(df.isnull().sum())
df = df.dropna()


# standardize the name of source and destinatiopn station name in the dataset

cols =['Source_Station_Name','Destination_Station_Name']

df[cols]= df[cols].apply(lambda x :x.str.upper())

print(df[cols].head(5))

# 2 DATA TRANSFORMATION AND AGGREGATION

# filtering trains based weekday

sat_trains = df['days'].str.contains('Saturday',case=False,na=False)

sat_trains1 = df[df['days'] == 'Saturday']

print(sat_trains1)


# created a new dataframe for the station name with JABALPUR source or start station

new_df = df[df['Source_Station_Name'] == 'JABALPUR']

print(new_df)


# counting trains staring from each station of source station name

train_count_source = df.groupby('Source_Station_Name')['Train_No'].count().reset_index(name='Train_Count_Source')

print(train_count_source)

#avg no of trains from each source station



# mapping the weekdays with numbering to easily find out the weekday


weekday_map = {
    'Sunday': 1,
    'Monday': 2,
    'Tuesday': 3,
    'Wednesday': 4,
    'Thursday': 5,
    'Friday': 6,
    'Saturday': 7
}

df['weekday_number'] = df['days'].map(weekday_map)

print(df.head())

# finding traind per day with group by and count

df['days'] = df['days'].str.strip().str.replace('d$','',regex=True).str.title()

trains_per_day = df.groupby(['Source_Station_Name','days'])['Train_No'].count().reset_index(name='train_count')

print(trains_per_day['train_count'])                                                                                           


# finding avg number of trains per each day of siource station

avg_train_station = trains_per_day.groupby('Source_Station_Name')['train_count'].mean().reset_index(name='avg_per_station')

print(avg_train_station)

print(df.head(5))


# mapping days into weekdays and weekend based on days in dataset to split the days into 2 type weekday adn weekend 

weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
weekends = ['Saturday','Sunday']


df['day_type'] = df['days'].apply(lambda x : 'weekday' if x in weekdays else 'weekend')


print(df)


# finding number of trains on weekday and weekday fot each source station name

trains_day_type = df.groupby(['Source_Station_Name','day_type'])['Train_No'].count().reset_index(name='Train_count')


print(trains_day_type)


#3 ADVANCED DATA ANALYSIS

# counting again no of train per day for distribution of train journeys throughout the week

order =['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']


per_day = df['days'].value_counts().reindex(order).reset_index()

per_day.columns = ['days','train_count']

print(per_day)


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(6,5))
sns.barplot(x='days', y='train_count', data=per_day, palette='Blues_d')
plt.title('Train journeys Throughout the Week')
plt.xlabel('Weekday')
plt.ylabel('Number of Train Journeys')
plt.show()



# count jorneys based on source station

source_count = df.groupby('Source_Station_Name').size().reset_index(name='trains_count').sort_values(by='trains_count',ascending = False)

print(source_count)


plt.figure(figsize=(6,5))
sns.barplot(x='Source_Station_Name',y='trains_count',data=source_count,palette ='Blues_d')
plt.title('train journeys throughtout the week based on source')
plt.xlabel('source station')
plt.ylabel('number of trains from source station')
plt.show()


destination_count = df.groupby('Destination_Station_Name').size().reset_index(name = 'trains_count').sort_values(by='trains_count',ascending = False)

print(destination_count)

plt.figure(figsize=(6,5))
sns.barplot(x='Destination_Station_Name',y='trains_count',data = destination_count,palette = 'Blues_d')
plt.title('train journeys throughout the week based on destination')
plt.xlabel('destination station')
plt.ylabel('number of trains from destination')
plt.show()

#finding correlation bw trains and week

counts_day = df.groupby(['days','weekday_number']).size().reset_index(name='train_count').sort_values('weekday_number')

print(counts_day)


corr = counts_day['weekday_number'].corr(counts_day['train_count'])
print("correlation bw day of week and number of trains:",corr)



plt.figure(figsize=(6,5))
sns.lineplot(x='weekday_number',y='train_count',data=counts_day,marker='o')
plt.xticks(counts_day['weekday_number'],counts_day['days'])
plt.title('trends of train over week')
plt.xlabel('weekday')
plt.ylabel('number of trains')
plt.show()

# 4 DATA VISUALIZATION AND REPORTING

# visulaization is already done above with bar and line chart like number of train over a week
#number of stations for source and destination stations

#reporting 



