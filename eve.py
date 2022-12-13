# !pip install dash==2.0.0
# !pip install jupyter-dash

import os
import openai
import time

openai.api_key = "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"

from jupyter_dash import JupyterDash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# Presets: Define Open AI Requirements here
def run_preset(query):
  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=query,
    temperature=0.7,
    max_tokens=800,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    #stop=["#", ";"]
  )

  return response.choices[0].text

# Build App
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = JupyterDash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H5("F5 AI driven - Product Configuraton Playground"),
    dcc.Dropdown(
        id='dropdown-preset',
        options=[
            {'label': 'Generate an NGINX Configuraton', 'value': '01'},
            {'label': 'Generate a BIG-IP Configuration', 'value': '02'},
            {'label': 'Create a Web Application Firewall Policy', 'value': '03'},
            {'label': 'Create a BIG-IP iRule', 'value': '04'},
            {'label': 'Create a unique password', 'value': '05'},
            {'label': 'Build a Terraform Operator', 'value': '06'},
            {'label': 'Build a Helm Chart', 'value': '07'},
            {'label': 'Build a Kubernetes Configuration', 'value': '08'},
            {'label': 'Build your Open Telemetry code', 'value': '09'},
            {'label': 'List F5 Products', 'value': '10'}
        ],
        placeholder="Load a preset configuration"
    ),
    dcc.Textarea(
          id='textarea-query',
          value='',
          placeholder="Type a query in natural language or select a preset above",
          style={'width': '100%', 'height': 200},
    ),
    html.Div(id='textarea-query-output', style={'whiteSpace': 'pre-line', 'padding-top': '10px'}),
    html.Button('Generate', id='button-generate',n_clicks=0),
    html.Div(id='div-output-results', style={'padding-top': '10px'}),
    html.Pre(
        id='div-output-results2',
        style={
          'height': 400,
          'overflow': 'auto',
          'font-family': 'courier new',
          'font-weight': 'bold',
          'color': 'white',
          'background-color': 'LightSlateGrey',
          'padding': '10px',
          'font-size': '100%',
          'border': 'solid 1px #A2B1C6'
          }
        ),
], style={
        'border': 'solid 1px #A2B1C6',
        'border-radius': '5px',
        'padding': '20px',
        'margin-top': '10px'
    })
##
## Called when Preset dropdown is selected
##
@app.callback(
    Output(component_id='textarea-query', component_property='value'),
    Input(component_id='dropdown-preset', component_property='value'),
)
def update_output(dropdown):
    ##return 'You have selected query "{}"'.format(get_query_from_preset(dropdown))
    return get_query_from_preset(dropdown)

def get_query_from_preset(preset):
  query = ''
  if preset == '01':
        query = "Write an nginx config to do:"
  elif preset == '02':
        query = ""
  elif preset == '03':
        query = "Write a BIG-IP web application firewall config to do the following:"
  elif preset == '04':
        query = "Write a BIG-IP iRule for the following:"
  elif preset == '05':
        query = ""
  elif preset == '06':
        query = ""
  elif preset == '07':
        query = ""
  elif preset == '08':
        query = ""
  elif preset == '09':
        query = ""
  elif preset == '10':
        query = ""
  return query

##
## Called when the Button 'Generate' is pushed
##
@app.callback(
    Output(component_id='div-output-results2', component_property='children'),
    State(component_id='textarea-query', component_property='value'),
    State(component_id='dropdown-preset', component_property='value'),
    Input('button-generate', 'n_clicks')

)
def update_output2(textarea, preset, n_clicks):

    if n_clicks is None or n_clicks == 0:
        return '(nothing generated yet)'
    else:
        ## Execute dynamically the 'run_preset_nn' function (where 'nn' is the preset number)
        #results = globals()['run_preset_%s' % preset](textarea)
        results = globals()['run_preset'](textarea)
        return results

# Run app and display result inline in the notebook
app.run_server(port=8118, debug=False)
