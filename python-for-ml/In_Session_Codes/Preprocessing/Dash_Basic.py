import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

df = pd.read_excel(r"C:\Users\NOTEBOOK\Downloads\Amit Repository\Amit\python-for-ml\Preprocessing\Dash.xlsx")

app = Dash()
app.title = "Interactive Dash App"
num_cols = df.select_dtypes(include='number').columns
app.layout = html.Div([html.H1("Interactive Dashboard with pie plot"),
                       html.Label("Select a value to show in the pie chart"),
                       dcc.Dropdown(id='column-dropdown',
                       options=[{'label': col, 'value': col} for col in num_cols],
                       value = num_cols[0]),
                       dcc.Graph(id='pie-chart')
])

@app.callback(Output('pie-chart', 'figure'),
             [Input('column-dropdown', 'value')])
def update_pie(selected_column):
    grouped = df.groupby('Area')[selected_column].sum().reset_index()
    fig = px.pie(grouped, values=selected_column, names='Area',
                title=f'Pie Chart of {selected_column} by Area', hole=0.4,
                color_discrete_sequence=px.colors.qualitative.Pastel)
    return fig

if __name__ == '__main__':
    app.run(debug=True)