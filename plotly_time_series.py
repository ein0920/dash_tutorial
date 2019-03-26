
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

# candle
