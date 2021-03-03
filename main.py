import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
pd.set_option('max_rows',20)
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"

df = pd.read_csv("data.csv")

def fig_world_trend(month='Jan'):

    fig = px.bar(df, y=df['Revenue'], x=df["Date"], title="Monthly Generated Revenue",height=600,color_discrete_sequence =['maroon'])
    fig.update_layout(title_x=0.5,plot_bgcolor='#FFF',paper_bgcolor='#FFF',xaxis_title="Month",yaxis_title="Revenue")
    return fig

def pie_chart():
    fig = px.pie(values=list(df['Revenue']), names=list(df['Date']))
    return fig

def line_chart():
    fig = px.line(df, x=df['Date'], y=df['Revenue'], title='Month vise Revenue')
    return fig

external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Data_factory Dashboard'


#Page header
colors = {
    'background': '#111111',
    'bodyColor':'#FFFFFF',
    'text': '#7FDBFF'
}
def get_page_heading_style():
    return {'backgroundColor': colors['background']}


def get_page_heading_title():
    return html.H1(children='Data_Factory Dashboard',
                                        style={
                                        'textAlign': 'center',
                                        'color': colors['text']
                                    })

def get_page_heading_subtitle():
    return html.Div(children='Visualize financial data.',
                                         style={
                                             'textAlign':'center',
                                             'color':colors['text']
                                         })

def generate_page_header():
    main_header =  dbc.Row(
                            [
                                dbc.Col(get_page_heading_title(),md=12)
                            ],

                            align="center",
                            style=get_page_heading_style()
                        )
    subtitle_header = dbc.Row(
                            [
                                dbc.Col(get_page_heading_subtitle(),md=12)
                            ],
                            align="center",
                            style=get_page_heading_style()
                        )
    header = (main_header,subtitle_header)
    return header


# Graph container for Dash
def graph1():
    return dcc.Graph(id='graph1',figure=fig_world_trend('Jan'))

def graph2():
    return dcc.Graph(id='graph2',figure=pie_chart())

def graph3():
    return dcc.Graph(id='graph3',figure=line_chart())


divBorderStyle = {
    'backgroundColor' : '#393939',
    'borderRadius': '12px',
    'lineHeight': 0.9,
}
colors = {
    'background': '#2D2D2D',
    'text': '#E1E2E5',
    'figure_text': '#ffffff',
    'confirmed_text': '#3CA4FF',
    'deaths_text': '#f44336',
    'recovered_text': '#5A9E6F',
    'highest_case_bg': '#393939',

}

# def get_cards():
#     cards = html.Div([
#         html.Div([
#             html.H4(children='Total Cases: ',
#                     style={
#                         'textAlign': 'center',
#                         'color': colors['confirmed_text'],
#                     }
#                     ),
#             # html.P(f"{'df_confirmed_total[-1]'}",
#             #        style={
#             #            'textAlign': 'center',
#             #            'color': colors['confirmed_text'],
#             #            'fontSize': 30,
#             #        }
#             #        ),
#             # html.P('Past 24hrs increase: +'"{'df_confirmed_total[-1]'}"
#             #        + ' (' ,
#             #        style={
#             #            'textAlign': 'center',
#             #            'color': colors['confirmed_text'],
#             #        }
#             #        ),
#         ],
#             style=divBorderStyle,
#             className='four columns',
#         ),
#         # html.Div([
#         #     html.H4(children='Total Deceased: ',
#         #             style={
#         #                 'textAlign': 'center',
#         #                 'color': colors['deaths_text'],
#         #             }
#         #             ),
#         #     html.P(f"{df_deaths_total[-1]:,d}",
#         #            style={
#         #                'textAlign': 'center',
#         #                'color': colors['deaths_text'],
#         #                'fontSize': 30,
#         #            }
#         #            ),
#         #     html.P('Mortality Rate: ' + str(round(df_deaths_total[-1] / df_confirmed_total[-1] * 100, 3)) + '%',
#         #            style={
#         #                'textAlign': 'center',
#         #                'color': colors['deaths_text'],
#         #            }
#         #            ),
#         # ],
#         #     style=divBorderStyle,
#         #     className='four columns'),
#         # html.Div([
#         #     html.H4(children='Total Recovered: ',
#         #             style={
#         #                 'textAlign': 'center',
#         #                 'color': colors['recovered_text'],
#         #             }
#         #             ),
#         #     html.P(f"{df_recovered_total[-1]:,d}",
#         #            style={
#         #                'textAlign': 'center',
#         #                'color': colors['recovered_text'],
#         #                'fontSize': 30,
#         #            }
#         #            ),
#         #     html.P('Recovery Rate: ' + str(round(df_recovered_total[-1] / df_confirmed_total[-1] * 100, 3)) + '%',
#         #            style={
#         #                'textAlign': 'center',
#         #                'color': colors['recovered_text'],
#         #            }
#         #            ),
#         # ],
#         #     style=divBorderStyle,
#         #     className='four columns'),
#     ], className='row'),
#
#     return cards

def get_cards():
    cards = html.Div([
                html.H3('Available Cash'),
                html.Div([
                    html.P('$555555'),
                ])
            ],style={'backgroundColor': colors['background'],
                                        'textAlign': 'center',
                                        'color': colors['text']
                                    })

    return cards
def generate_layout():
    page_header = generate_page_header()
    cards = get_cards()
    layout = dbc.Container(
        [
            page_header[0],
            page_header[1],
            html.Hr(),
            cards,
            html.Hr(),

            dbc.Row(
                [

                    dbc.Col(graph1(), md=dict(size=6, offset=3)),
                    dbc.Col(graph2(), md=dict(size=6, offset=3)),
                    dbc.Col(graph3(), md=dict(size=6, offset=3))

                ],

                align="center",

            ),
            # dbc.Row(
            #     [
            #
            #
            #
            #     ],
            #
            #     align="center",
            #
            # ),


        ], fluid=True, style={'backgroundColor': '#FFF'}
    )
    return layout

app.layout = generate_layout()



if __name__ == '__main__':
    app.run_server(debug=True)