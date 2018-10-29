import dash
import dash_core_components as dcc 
import dash_html_components as html 
import pandas as pd 


df = pd.read_csv(
				'https://gist.githubusercontent.com/chriddyp/'
				'c78bf172206ce24f77d6363a2d754b59/raw/'
    			'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    			'usa-agricultural-exports-2011.csv')

# print(df)
def generate_table(dataframe, max_rows=10):

		# Header
	table = ([html.Tr([html.Th(col) for col in dataframe.columns])] +

		# Body
		[html.Tr([
			html.Td(dataframe.iloc[i][col] for col in dataframe.columns)
			]) for i in range(min(len(dataframe), max_rows))])
	print(table)
	return html.Table(
			[html.Tr( [html.Th("name"), html.Th("address"), html.Th("email")] )] +
    		[
    			html.Tr( [html.Td("walter"), html.Td("rudin"), html.Td("wr@analysis.com")] ),
    			html.Tr( [html.Td("gilbert"), html.Td("strang"), html.Td("gb@algebra.com")] )
    		]
		)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(children=[
		html.H4(children='US Agriculture Exports (2011)'),
		generate_table(df)
	])


if __name__ == '__main__':
	app.run_server(debug=True)