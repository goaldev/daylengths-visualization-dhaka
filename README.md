# Visualizing Daylengths and Solar Noon Times in Dhaka, Bangladesh 

Welcome to the Visualizing Daylengths and Solar Noon Times repository for Dhaka, Bangladesh! 🌞📊

Unleash the power of data visualization as we embark on a journey to explore the daylengths and solar noon times in the vibrant city of Dhaka. By visualizing this valuable information, we gain a clear vision of the abundance of daylight available in this bustling metropolis.

Why is this important, you ask? Well, the length of the day directly impacts various aspects of our lives. Imagine harnessing the longest daylengths to collect sunlight, which serves as the lifeblood of solar panel systems. With this knowledge, we can pave the way for innovative solutions to address the pressing issue of load shedding in Dhaka, Bangladesh.

Join us on this illuminating journey and empower yourself with knowledge about daylengths and solar noon times in Dhaka, Bangladesh!

# Website and [Tableau Dashboards](https://public.tableau.com/app/profile/nasrin.akter) 
We scrape data from a reliable [source](https://www.timeanddate.com/sun/bangladesh/dhaka) and leverage Tableau to create captivating visualizations. 

Dive into our interactive [dashboards](https://public.tableau.com/app/profile/nasrin.akter) and witness the patterns and dynamics of Dhaka's daylight.

# Findings

There is a relation between solar noon time and the number of days. Solar noon refers to the time of day when the sun is at its highest point in the sky. It is the moment when the sun crosses the observer's meridian.

The position of the sun at solar noon varies throughout the year due to the tilt of the Earth's axis and its elliptical orbit around the sun. As a result, the solar noon time changes slightly each day.

The relationship between solar noon time and the number of days is as follows: 

1. As the number of days increases, the solar noon time gradually shifts. This shift can be observed over long periods, such as weeks, months, or seasons.
The specific shift in solar noon time depends on factors such as the observer's location on Earth and the time of year. However, on average, the solar noon time tends to move forward by a few minutes each day.

Therefore, if you track the solar noon time for consecutive days, you will notice a gradual change in the time as the number of days increases.

2. We also see that there is a general correlation between the solar noon time and the daylengths. As the solar noon time progresses, the daylengths also increase gradually. 

3. Based on the past 30 years (from 1992 to 2022) of data analysis, it is evident that Dhaka consistently experiences a significant number of days with daylengths exceeding 13 hours. This finding strongly suggests that Dhaka is an ideal location for the implementation of solar panels, offering a promising solution to combat the prevalent issue of load shedding.

# Build from Sources and Run the Selenium Scraper

1. Clone the repository
```bash
git clone https://github.com/NasrinRipa/mastercourse_scraping_test.git
```
2. Intialize and activate virtual environment
```bash
virtualenv --no-site-packages  venv
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Download Chrome WebDrive from https://chromedriver.chromium.org/downloads
5. Run scraper_suntable.py for scraping data table from the website and for cleaning/rearranging the table, use cleaned_suntable.py 
6. The folder "selenium_scraper" contains 2 Python files for data scraping and data cleaning/rearranging, and all the csv files are in the "csv_files" folder.
