import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc 
import dash_html_components as html 

from pandas_datareader import data as web
from datetime import datetime as dt 

app = dash.Dash('Hello World')

app.layout = html.Div([
	dcc.Dropdown(
		id='my-dropdown',
		options=[
			{'label': 'First REITS', 'value': 'AW9U.SI'},
			{'label': 'Silverlake Axis Ltd', 'value': '5CP.SI'},
			{'label': 'Singtel', 'value': 'Z74.SI'},
			{'label': 'Mapletree Commercial Trust', 'value': 'N2IU.SI'},
			{'label': 'CapitaRetial China Trust', 'value': 'AU8U.SI'},
		],
		value='COKE'
	),
	dcc.Graph(id='my-graph')
	], style={'width': '500'})

@app.callback(Output('my-graph','figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
	df = web.DataReader(
			selected_dropdown_value,
			'yahoo',
			dt(2000,1,1),
			dt.now()
		)
	return {
		'data': [{
			'x': df.index,
			'y': df.Close
		}],
		'layout': {'margin': {'l':40, 'r':0, 't':20, 'b':30}}
	}

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == "__main__":
	app.run_server()