from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

# Set the ChromeDriver path
webdriver_path = "C:\Program Files (x86)\chromedriver.exe"

# Set Chrome options for headless mode
options = Options()
options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)

# Set up the Selenium driver
driver = webdriver.Chrome(webdriver_path, options=options)

# Define the time range
start_year = 1992
end_year = 2022

# Create an empty list to store the data rows
data_rows = []

# Iterate over the time range 
for year in range(start_year, end_year + 1):
    # Iterate over the months
    for month_index in range(1, 13):
        # Create the URL for each month
        url = f'https://www.timeanddate.com/sun/bangladesh/dhaka?month={month_index}'

        # Navigate to the website
        driver.get(url)

        # Find the table element
        table = driver.find_element(By.ID, 'as-monthsun')

        # Find the table header rows
        header_rows = table.find_elements(By.XPATH, './thead/tr')

        # Extract column headers from the first row of the header
        column_headers = [header.text for header in header_rows[0].find_elements(By.TAG_NAME, 'th')]

        # Extract column labels from the second row of the header
        #column_labels = ['Day/Date'] + [label.text for label in header_rows[1].find_elements(By.TAG_NAME, 'th')]

        # Extract column labels from the second row of the header
        column_labels = [label.text for label in header_rows[1].find_elements(By.TAG_NAME, 'th')]

        # Find the table body rows
        body_rows = table.find_elements(By.XPATH, './tbody/tr')

        # Iterate over the body rows and extract the data
        for row in body_rows:
            try:
                day_date = row.find_element(By.TAG_NAME, 'th').text
            except NoSuchElementException:
                day_date = ''

            # Extract the cells in each row
            cells = row.find_elements(By.TAG_NAME, 'td')

            # Create a list to store the data in each row, including the day/date
            row_data = [day_date] + [cell.text for cell in cells]

            # Adjust the row data if the number of columns differs from the number of column labels
            if len(row_data) != len(column_labels):
                # Discard extra columns in the data row
                if len(row_data) > len(column_labels):
                    row_data = row_data[:len(column_labels)]
                # Append empty values for missing columns in the data row
                else:
                    row_data += [''] * (len(column_labels) - len(row_data))

            # Append the row data to the list of data rows
            data_rows.append(row_data)

# Close the browser
driver.quit()

# Create a pandas DataFrame using the column labels and data rows
df = pd.DataFrame(data_rows, columns=column_labels)

# Save the DataFrame as a CSV file
output_file = 'suntable_output_30years.csv'
df.to_csv(output_file, index=True)

# Print the DataFrame
print(df)
print(f"\nData saved to '{output_file}'")

