# Import the relevant libraries
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
import mpld3  # Import mpld3

# Read the video games sales data
video = pd.read_csv('./Data/Video_Games_Sales_as_at_22_Dec_2016.csv')
# Filter the data for 7th generation consoles (Wii, PS3, X360)
video7th = video[(video['Platform'] == 'Wii') | (video['Platform'] == 'PS3') | (video['Platform'] == 'X360')]

# Set the dark background style for the plot
plt.style.use('dark_background')

# Group the data by Rating and Platform, and sum the global sales
ratingSales = video7th.groupby(['Rating', 'Platform']).Global_Sales.sum()

# Create a stacked bar plot of sales per rating type for the 7th Gen Consoles
fig, ax = plt.subplots(figsize=(13, 11))
ratingSales.unstack().plot(kind='bar', stacked=True, colormap='Greens', grid=False, ax=ax)
plt.title('Stacked Barplot of Sales per Rating type of the 7th Gen Consoles')
plt.ylabel('Sales')

# Convert the plot to HTML using mpld3
html_output = mpld3.fig_to_html(fig)

# Save the HTML to a file
with open('plot_output.html', 'w') as f:
    f.write(html_output)


plt.style.use('dark_background')
genreSales = video7th.groupby(['Genre','Platform']).Global_Sales.sum()
genreSales.unstack().plot(kind='bar',stacked=True,  colormap= 'Reds', 
                          grid=False, figsize=(13,11))
plt.title('Stacked Barplot of Sales per Game Genre')
plt.ylabel('Sales')