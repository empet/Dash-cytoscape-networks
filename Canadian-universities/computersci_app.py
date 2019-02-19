"""The network  of ten Canadian  universities
"""
import json

import dash
import dash_html_components as html

import dash_cytoscape as cyto

app = dash.Dash(__name__)
server = app.server

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

# Load Data
with open('computersci-data.json', 'r') as f:
    elements = json.loads(f.read())

# Load stylesheet
with open('computersci-style.json', 'r') as f:
    stylesheet = json.loads(f.read())
# App
app.layout = html.Div([
    cyto.Cytoscape(
        id = 'cytoscape',
        elements = elements,
        layout={'name': 'preset'},

        stylesheet = stylesheet,
        style={
            'width': '80%',
            'height': '750px',
            'position': 'absolute',
            #'background-color': '#0A0A0A',
            'left': 0,
            'top': 0,
            'z-index': 999
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
