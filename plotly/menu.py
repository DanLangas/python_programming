import plotly
import plotly.graph_objs as go 
from datetime import datetime
import pandas_datareader as web

df = web.DataReader("aapl", 'google',
                    datetime(2015, 1, 1),
                    datetime(2016, 7, 1))

trace_high = go.Bar(    x=df.index,
                        y=df.High,
                        name='High')

trace_low = go.Scatter(x=df.index,
                       y=df.Low,
                       name='Low',
                       line=dict(color='#F06A6A'))

data = [trace_high, trace_low]


updatemenus = list([
    dict(active=-1,
         buttons=list([   
            dict(label = 'High',
                 method = 'update',
                 args = [{'visible': [True, False]},
                         {'title': 'Yahoo High'}]),

            dict(label = 'Low',
                 method = 'update',
                 args = [{'visible': [False, True]},
                         {'title': 'Yahoo Low'}])
        ]),
    )
])

layout = dict(title='Yahoo', showlegend=False,
              updatemenus=updatemenus)

fig = dict(data=data, layout=layout)

plotly.offline.plot(fig, auto_open=False, show_link=False)
