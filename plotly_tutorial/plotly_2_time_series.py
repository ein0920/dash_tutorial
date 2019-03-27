
# timeseries
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    import pandas as pd

    # basic
    if __name__ == '__main__':

        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

        data = [go.Scatter(x=df.Date, y=df['AAPL.High'])]  # 字符串格式的日期

        py.plot(data, filename='tmp/timeseries_tutorial.html',auto_play=True)

    # Time Series Plot with Custom Date Range
    if __name__ == '__main__':
        import datetime


        def to_unix_time(dt):
            epoch = datetime.datetime.utcfromtimestamp(0)
            return (dt - epoch).total_seconds() * 1000


        x = [datetime.datetime(year=2013, month=10, day=4),
             datetime.datetime(year=2013, month=11, day=5),
             datetime.datetime(year=2013, month=12, day=6)]
        data = [go.Scatter(
            x=x,
            y=[1, 3, 6])]

        layout = go.Layout(xaxis=dict(
            range=[to_unix_time(datetime.datetime(2013, 10, 17)),
                   to_unix_time(datetime.datetime(2013, 11, 20))]
        ))

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/timeseries_tutorial.html',auto_play=True)

    # Manually Set Range
    if __name__ == '__main__':
        df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

        trace_high = go.Scatter(
            x=df.Date,
            y=df['AAPL.High'],
            name="AAPL High",
            line=dict(color='#17BECF'),
            opacity=0.8)

        trace_low = go.Scatter(
            x=df.Date,
            y=df['AAPL.Low'],
            name="AAPL Low",
            line=dict(color='#7F7F7F'),
            opacity=0.8)

        data = [trace_high, trace_low]

        layout = dict(
            title="Manually Set Date Range",
            xaxis=dict(
                range=['2016-07-01', '2016-12-31'])
        )

        fig = dict(data=data, layout=layout)
        py.plot(fig, filename='tmp/timeseries_tutorial.html',auto_play=True)


    # Time Series With Rangeslider，不会自动跳y的范围
    if __name__ == '__main__':
        df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

        trace_high = go.Scatter(
            x=df.Date,
            y=df['AAPL.High'],
            name="AAPL High",
            line=dict(color='#17BECF'),
            opacity=0.8)

        trace_low = go.Scatter(
            x=df.Date,
            y=df['AAPL.Low'],
            name="AAPL Low",
            line=dict(color='#7F7F7F'),
            opacity=0.8)

        data = [trace_high, trace_low]

        layout = dict(
            title='Time Series with Rangeslider',
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=1,
                             label='1m',
                             step='month',
                             stepmode='backward'),
                        dict(count=6,
                             label='6m',
                             step='month',
                             stepmode='backward'),
                        dict(step='all')
                    ])
                ),
                rangeslider=dict(
                    visible=True
                ),
                type='date'
            )
        )

        fig = dict(data=data, layout=layout)

        py.plot(fig, filename='tmp/timeseries_tutorial.html',auto_play=True)

# candlestick，ohlc换一下就可以了
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    import pandas as pd
    from datetime import datetime

    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

    # Simple Candlestick with Pandas，自动打开rangeslider
    if __name__ == '__main__':

        trace = go.Candlestick(x=df['Date'],
                        open=df['AAPL.Open'],
                        high=df['AAPL.High'],
                        low=df['AAPL.Low'],
                        close=df['AAPL.Close'])
        data = [trace]
        py.plot(data, filename='tmp/timeseries_tutorial.html', auto_play=True)

    # Candlestick without Rangeslider
    if __name__ == '__main__':

        trace = go.Candlestick(x=df['Date'],
                        open=df['AAPL.Open'],
                        high=df['AAPL.High'],
                        low=df['AAPL.Low'],
                        close=df['AAPL.Close'])

        layout = go.Layout(
            xaxis=dict(
                rangeslider=dict(
                    visible=False
                )
            )
        )

        data = [trace]

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/timeseries_tutorial.html', auto_play=True)

    # Adding Customized Text and Annotations
    if __name__ == '__main__':
        trace = go.Candlestick(x=df['Date'],
                        open=df['AAPL.Open'],
                        high=df['AAPL.High'],
                        low=df['AAPL.Low'],
                        close=df['AAPL.Close'])
        data = [trace]
        layout = {
            'title': 'The Great Recession',
            'yaxis': {'title': 'AAPL Stock'},
            'shapes': [{
                'x0': '2016-12-09', 'x1': '2016-12-09',
                'y0': 0, 'y1': 1, 'xref': 'x', 'yref': 'paper',
                'line': {'color': 'rgb(30,30,30)', 'width': 1}
            }],
            'annotations': [{
                'x': '2016-12-09', 'y': 0.05, 'xref': 'x', 'yref': 'paper',
                'showarrow': False, 'xanchor': 'left',
                'text': 'Increase Period Begins'
            }]
        }
        fig = dict(data=data, layout=layout)
        py.plot(fig, filename='tmp/timeseries_tutorial.html', auto_play=True)


    # Custom Candlestick Colors
    if __name__ == '__main__':
        trace = go.Candlestick(x=df['Date'],
                        open=df['AAPL.Open'],
                        high=df['AAPL.High'],
                        low=df['AAPL.Low'],
                        close=df['AAPL.Close'],
                        increasing=dict(line=dict(color='red')),
                        decreasing=dict(line=dict(color='green')))
        data = [trace]
        py.plot(data, filename='tmp/timeseries_tutorial.html', auto_play=True)


    # Simple Example with datetime Objects
    if __name__ == '__main__':
        open_data = [33.0, 33.3, 33.5, 33.0, 34.1]
        high_data = [33.1, 33.3, 33.6, 33.2, 34.8]
        low_data = [32.7, 32.7, 32.8, 32.6, 32.8]
        close_data = [33.0, 32.9, 33.3, 33.1, 33.1]
        dates = [datetime(year=2013, month=10, day=10),
                 datetime(year=2013, month=11, day=10),
                 datetime(year=2013, month=12, day=10),
                 datetime(year=2014, month=1, day=10),
                 datetime(year=2014, month=2, day=10)]

        trace = go.Candlestick(x=dates,
                               open=open_data,
                               high=high_data,
                               low=low_data,
                               close=close_data)
        data = [trace]
        py.plot(data, filename='tmp/timeseries_tutorial.html', auto_play=True)

