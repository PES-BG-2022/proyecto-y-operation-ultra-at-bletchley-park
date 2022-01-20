# Prueba 2
# Importamos los paquetes requeridos
import dash
import dash_html_components as html

# Creación de la app
app = dash.Dash(__name__)

# Elementos de diseños (graficos)
app.layout = html.Div([
html.H1('Hola Mundo')
])

# Correr la app
if __name__ == '__main__':
    app.run_server(debug=True)