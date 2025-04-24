import pandas as pd
from google_play_scraper import app

# List of package names seperated using a comma ,
package_names = ["ai.chat.gpt.bot","ai.chat.gpt.bot"]

# List to store results
results = []

# Fetch category for each app using the google play store categorisation
for package_name in package_names:
    try:
        app_info = app(package_name)
        category = app_info.get('genre', 'No category found')
        results.append({'Package Name': package_name, 'Category': category})
    except Exception as e:
        results.append({'Package Name': package_name, 'Category': f"Error: {str(e)}"})

# Create a DataFrame
df = pd.DataFrame(results)

# save as csv
df.to_csv('app_categories.csv', index=False, encoding='utf-8')

# save as txt
#with open('app_categories.txt', 'w', encoding='utf-8') as f:
 #   f.write(df.to_string(index=False))


# Print the table
#print(df)

# Save the table to an Excel file
# df.to_excel('app_categories.xlsx', index=False)
