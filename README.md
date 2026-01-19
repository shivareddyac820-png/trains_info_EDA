📌 Project Objective
To analyze train frequency across the week and identify patterns that can help in schedule optimization and demand planning.

🗂️ Dataset Overview

Dataset: Trains_info.csv
Contains information about:
Train journeys
Source & destination stations
Days of travel

🧹 Data Cleaning & Preparation

To ensure accurate analysis, I performed the following steps:
Identified unique values to understand the dataset
Converted days into week numbers
Standardized station names to uppercase
Identified and handled missing values
Removed incomplete records for consistency

🔍 Exploratory Data Analysis (EDA)

Key analysis steps included:
Filtering trains by weekday vs weekend
Creating station-specific dataframes (e.g., JABALPUR as source)
Counting trains by source and destination
Calculating average number of trains per day
Mapping days into weekdays and weekends
Analyzing daily train distribution
Studying station-wise train journeys
Finding correlation between days of the week and train frequency

📈 Visual Insights
From the visualizations:

Friday has the highest number of train journeys
CST–MUMBAI is the busiest:
513 trains as a source station
514 trains as a destination station
Train journeys increase toward the end of the week
Correlation = 0.33 between day of week and number of trains, indicating higher activity later in the week
💡 Key Insights
✔ Train journeys are significantly higher on weekdays, especially Friday
✔ CST–MUMBAI acts as a major railway hub
✔ Weekend train journeys are lower compared to weekdays

✅ Conclusion

This analysis shows higher demand for train journeys on weekdays, particularly toward the end of the week.
👉 Railway authorities can optimize schedules by increasing weekday services and adjusting weekend operations to improve efficiency and customer satisfaction.
