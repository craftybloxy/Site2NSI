import pandas as pd
import plotly.express as px

# Load the CSV data into a DataFrame
df = pd.read_csv("./Data/Video_Games_Sales_as_at_22_Dec_2016.csv")

# Display the first few rows of the DataFrame
print("First few rows of the dataset:")
print(df.head())
print()

# Aggregate global sales for each platform by year
platform_sales_by_year = df.groupby(['Year_of_Release', 'Platform'])['Global_Sales'].sum().reset_index()

# Aggregate total global sales for all platforms by year
total_sales_by_year = df.groupby('Year_of_Release')['Global_Sales'].sum().reset_index()
total_sales_by_year['Platform'] = 'Total'

# Concatenate platform sales and total sales
combined_sales = pd.concat([platform_sales_by_year, total_sales_by_year])

# Sort the combined data by year
combined_sales = combined_sales.sort_values(by='Year_of_Release')

# Display pivot table for better understanding
print("Pivot table of combined sales data:")
pivot_table = combined_sales.pivot_table(index='Year_of_Release', columns='Platform', values='Global_Sales', fill_value=0)
print(pivot_table)
print()

# Display summary statistics of global sales by platform
print("Summary statistics of global sales by platform:")
summary_statistics = combined_sales.groupby('Platform')['Global_Sales'].describe()
print(summary_statistics)
print()

# Plot premier
fig = px.line(combined_sales, x='Year_of_Release', y='Global_Sales', color='Platform',
              title="Graphique des ventes par consoles")
fig.update_xaxes(type='category')  # Use categorical x-axis
fig.update_layout(xaxis_title='Year of Release', yaxis_title='Global Sales')
fig.write_html("./html/global_sales_comparison.html")


# Aggregate global sales for each game
game_sales = df.groupby('Name')['Global_Sales'].sum().reset_index()

# Sort the data by sales in descending order and take the top 10
top_games = game_sales.sort_values(by='Global_Sales', ascending=False).head(20)

# Plot second
fig = px.bar(top_games, x='Name', y='Global_Sales', 
             title="Les 20 jeux les plus vendu SUR 16000 JEUX", 
             labels={'Global_Sales': 'Global Sales', 'Name': 'Game Name'})
fig.write_html("./html/global_sales_game.html")


# Fill NaN values in the 'Name' column with an empty string
df['Name'] = df['Name'].fillna('')

zelda_games = df[df['Name'].str.contains('Zelda')]

fig = px.bar(zelda_games, x='Name', y='Global_Sales', 
             title='Comparaison des ventes de jeux zelda')
fig.write_html("./html/global_zelda_game.html")
