import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv("datos2.csv")

app = dash.Dash(__name__)

app.layout = html.Div([html.H1("Relación del PIB y Mortalidad infaltil"),
    html.Div(children='''
        Una relación a lo largo del tiempo
    '''),
    dcc.Graph(id="grafica-con-slider"),
    dcc.Slider(
        id="año-slider",
        min=df["year"].min(),
        max=df["year"].max(),
        value=df["year"].min(),
        marks={str(year): str(year) for year in df["year"].unique()},
        step=None
    )
])


@app.callback(
    Output("grafica-con-slider", "figure"),
    Input("año-slider", "value"))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="NY.GDP.PCAP.KD", y="SH.DYN.NMRT",
                     size="SP.POP.TOTL", color = "Region" ,hover_name="country",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)