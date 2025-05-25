import plotly.graph_objects as go

# Sample data for the chart
x = ['A', 'B', 'C', 'D']
y1 = [0.1, 0.3, 0.5, 0.0]
y2 = [0.2, 0.4, 0.3, 0.5]

# External data: additional information for each category
extra_info = {
    'A': 'Extra info for category A',
    'B': 'Extra info for category B',
    'C': 'Extra info for category C',
    'D': 'Extra info for category D'
}

# Create a grouped bar chart
fig = go.Figure()

# Adding the first trace
fig.add_trace(go.Bar(
    x=x,
    y=y1,
    name='Group 1',
    hovertemplate = '<b>%{x}</b><br>Group 1: %{y}<br>Extra Info: %{customdata}<extra></extra>',
    customdata=[extra_info[x_] for x_ in x]  # Use the external dictionary to populate the hover info
))

# Adding the second trace
fig.add_trace(go.Bar(
    x=x,
    y=y2,
    name='Group 2',
    hovertemplate = '<b>%{x}</b><br>Group 2: %{y}<br>Extra Info: %{customdata}<extra></extra>',
    customdata=[extra_info[x_] for x_ in x]  # Same logic here for the second trace
))

# Update layout
fig.update_layout(
    barmode='group',
    title='Grouped Bar Chart with External Data in Hover',
    xaxis_title='Category',
    yaxis_title='Values'
)

# Show the plot
fig.show()
