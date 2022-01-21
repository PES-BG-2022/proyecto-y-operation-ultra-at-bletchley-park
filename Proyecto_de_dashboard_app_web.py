# Importamos los módulos a utilizar

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

# Cargando los datos a utilizar
df = pd.read_csv("datos_final.csv")

# Creando la app
app = dash.Dash(__name__)

# Creación de los elementos gráficos a visualizar
app.layout = html.Div([html.H1("Relación del PIB per cápita y mortalidad infaltil"),
    html.H2("Una relación a lo largo del tiempo"),
    dcc.Graph(id="grafica-con-slider"),
    dcc.Slider(
        id="año-slider",
        min=df["Año"].min(),
        max=df["Año"].max(),
        value=df["Año"].min(),
        marks={str(year): str(year) for year in df["Año"].unique()},
        step=None
    ),
    html.Div(children='''
        El diametro de cada gráfica representa la población del país
    '''),
        html.Div(children='''
        El color de cada gráfica representa la región del país
    '''),
            html.Div(children='''
        Orenos y Morales (2022)
    ''')
])

# Creación del callback para hacer la interacción entre datos y elementos gráficos

@app.callback(
    Output("grafica-con-slider", "figure"),
    Input("año-slider", "value"))
def update_figure(selected_year):
    filtered_df = df[df.Año == selected_year]

    fig = px.scatter(filtered_df, x="PIB per cápita", y="Moratalidad Infantil",
                     size="Población", color = "Región" ,hover_name="country",
                     size_max=55)

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)