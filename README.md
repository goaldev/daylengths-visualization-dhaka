Welcome to our repository and let's explore Dhaka's daylengths and solar noon times with captivating visualizations! 🌞📊

Embark on an insightful journey as we unlock the power of data visualization to explore daylengths and solar noon times in the vibrant city of Dhaka. Through captivating visual representations, we gain a clear understanding of the abundance of daylight that graces this bustling metropolis.

But why is this information so important, you may wonder? Well, the length of the day directly impacts various aspects of our lives. Imagine harnessing the knowledge of longest daylengths to maximize sunlight collection, providing a potential solution to address the critical issue of load shedding in Dhaka, Bangladesh.

Join us in this illuminating quest and empower yourself with valuable knowledge about daylengths and solar noon times in Dhaka, Bangladesh!

# Website and Interactive Tableau Dashboards
To ensure accuracy, we gather data from a reliable [source](https://www.timeanddate.com/sun/bangladesh/dhaka) and employ Tableau's powerful visualization capabilities to create interactive and captivating dashboards.

Dive into our mesmerizing dashboards through the links below, and witness the intriguing patterns and dynamics of Dhaka's daylight:

📊 [Dashboard 1](https://public.tableau.com/views/solarnoontimein30years/Daylengths30years?:language=en-US&:display_count=n&:origin=viz_share_link) - Explore daylengths across the past 30 years.

📊 [Dashboard 2](https://public.tableau.com/views/Daylengthsandsolarnoonin2022Dhaka/daylengthSolarnoon2022?:language=en-US&:display_count=n&:origin=viz_share_link) - Delve into the daylengths and solar noon times of the year 2022.

📊 [Dashboard 3](https://public.tableau.com/views/daylengthsandsolarnoontimefromJantoMay2023inDhaka/DaylengthsSolarnoon2023?:language=en-US&:display_count=n&:origin=viz_share_link) - Witness daylengths and solar noon times from January to May 2023.

📊 [Dashboard 4](https://public.tableau.com/views/DaylengthsinJan2023Dhaka/DaylengthSolarnoonJan2023?:language=en-US&:display_count=n&:origin=viz_share_link) - Specific focus on daylengths in January 2023.


## Findings

There is a relation between solar noon time and the number of days. Solar noon refers to the time of day when the sun is at its highest point in the sky. It is the moment when the sun crosses the observer's meridian.

The position of the sun at solar noon varies throughout the year due to the tilt of the Earth's axis and its elliptical orbit around the sun. As a result, the solar noon time changes slightly each day.

The relationship between solar noon time and the number of days is as follows: 

1. As the number of days increases, the solar noon time gradually shifts. This shift can be observed over long periods, such as weeks, months, or seasons.
The specific shift in solar noon time depends on factors such as the observer's location on Earth and the time of year. However, on average, the solar noon time tends to move forward by a few minutes each day.

Therefore, if you track the solar noon time for consecutive days, you will notice a gradual change in the time as the number of days increases.

2. We also see that there is a general correlation between the solar noon time and the daylengths. As the solar noon time progresses, the daylengths also increase gradually. 

3. Based on the past 30 years (from 1992 to 2022) of data analysis, it is evident that Dhaka consistently experiences a significant number of days with daylengths exceeding 13 hours. This finding strongly suggests that Dhaka is an ideal location for the implementation of solar panels, offering a promising solution to combat the prevalent issue of load shedding.

### Build from Sources and Run the Selenium Scraper

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


### Acknowledgments

I would like to express my heartfelt gratitude to Mohammad Sabik Irbaz, MasterCourse Bangladesh, who played a pivotal role in the success of this project. Their expertise, guidance, and unwavering support were instrumental in shaping my skills and enabling me to complete this repository. I am truly grateful for their mentorship and valuable insights throughout this journey.
