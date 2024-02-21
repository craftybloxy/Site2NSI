import pandas as pd
laptop = pd.read_csv('./Data/Cleaned_Laptop_data.csv', encoding = 'utf-8')

import plotly.graph_objs as go
from plotly.offline import plot
print(laptop)
sorted_laptop = laptop.sort_values(by=['old_price'], ascending = True)
x_data = sorted_laptop['old_price']
y_data = sorted_laptop['latest_price']

# Create a trace
trace = go.Scatter(
    x=x_data,
    y=y_data,
    mode='lines+markers',
    name='Example Graph'
)

# Create layout
layout = go.Layout(
    title='Example Graph',
    xaxis=dict(title='X-axis Label'),
    yaxis=dict(title='Y-axis Label')
)

# Create figure object
fig = go.Figure(data=[trace], layout=layout)

# Generate HTML file
plot(fig, filename='graph.html')



print(laptop['Price_euros'])

