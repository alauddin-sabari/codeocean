import dash
from dash import html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load a sample dataset
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Grapes"],
    "Amount": [4, 1, 2, 5],
    "City": ["New York", "Montreal", "San Francisco", "Chicago"]
})

# Initialize the app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div(children=[
    html.H1(children="Plotly Dash Application"),
    dcc.Dropdown(
        id='city-dropdown',
        options=[{'label': city, 'value': city} for city in df['City'].unique()],
        value='New York'
    ),
    dcc.Graph(id='bar-chart'),
])

# Define callback to update graph
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('city-dropdown', 'value')]
)
def update_graph(selected_city):
    filtered_df = df[df['City'] == selected_city]
    fig = px.bar(filtered_df, x='Fruit', y='Amount', title=f'Fruit Count in {selected_city}')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8080)
