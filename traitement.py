import pandas as pd
import plotly.express as px

df = pd.read_csv("./Data/Video_Games_Sales_as_at_22_Dec_2016.csv")

print("Premières lignes du jeu de données :")
print(df.head())
print()

platform_sales_by_year = df.groupby(['Year_of_Release', 'Platform'])['Global_Sales'].sum().reset_index()

total_sales_by_year = df.groupby('Year_of_Release')['Global_Sales'].sum().reset_index()
total_sales_by_year['Platform'] = 'Total'

combined_sales = pd.concat([platform_sales_by_year, total_sales_by_year])
combined_sales = combined_sales.sort_values(by='Year_of_Release')

pivot_table = combined_sales.pivot_table(index='Year_of_Release', columns='Platform', values='Global_Sales', fill_value=0)
print(pivot_table)
print()

summary_statistics = combined_sales.groupby('Platform')['Global_Sales'].describe()
print(summary_statistics)
print()

fig = px.line(combined_sales, x='Year_of_Release', y='Global_Sales', color='Platform',
              title="Graphique des ventes par consoles")
fig.update_xaxes(type='category')
fig.update_layout(xaxis_title='Année de sortie', yaxis_title='Ventes mondiales')
fig.write_html("./html/global_sales_comparison.html")

game_sales = df.groupby('Name')['Global_Sales'].sum().reset_index()

top_games = game_sales.sort_values(by='Global_Sales', ascending=False).head(20)

fig = px.bar(top_games, x='Name', y='Global_Sales', 
             title="Les 20 jeux les plus vendus SUR 16000 JEUX", 
             labels={'Global_Sales': 'Ventes mondiales', 'Name': 'Nom du jeu'})
fig.write_html("./html/global_sales_game.html")

df['Name'] = df['Name'].fillna('')

zelda_games = df[df['Name'].str.contains('Zelda')]

fig = px.bar(zelda_games, x='Name', y='Global_Sales', 
             title='Comparaison des ventes de jeux Zelda')
fig.write_html("./html/global_zelda_game.html")
