

# Filter 过滤器
if __name__ == '__main__':
    import plotly.offline as py

    # basic
    if __name__ == '__main__':
        subject = ['Moe', 'Larry', 'Curly', 'Moe', 'Larry', 'Curly', 'Moe', 'Larry', 'Curly', 'Moe', 'Larry', 'Curly']
        score = [1, 6, 2, 8, 2, 9, 4, 5, 1, 5, 2, 8]

        data = [dict(
            type='scatter',
            x=subject,
            y=score,
            mode='markers',
            transforms=[dict(
                type='filter',
                target='y',
                operation='>',
                value=4
            )]
        )]

        layout = dict(
            title='Scores > 4'
        )
        py.plot({'data': data, 'layout': layout}, filename='tmp/transforms_tutorial.html', auto_play=True, validate=False)

# Group By in Python
if __name__ == '__main__':
    import plotly.offline as py

    # basic
    if __name__ == '__main__':
        subject = ['Moe', 'Larry', 'Curly', 'Moe', 'Larry', 'Curly', 'Moe', 'Larry', 'Curly', 'Moe', 'Larry', 'Curly']
        score = [1, 6, 2, 8, 2, 9, 4, 5, 1, 5, 2, 8]

        data = [dict(
            type='scatter',
            x=subject,
            y=score,
            mode='markers',
            transforms=[dict(
                type='groupby',
                groups=subject,
                styles=[
                    dict(target='Moe', value=dict(marker=dict(color='blue'))),
                    dict(target='Larry', value=dict(marker=dict(color='red'))),
                    dict(target='Curly', value=dict(marker=dict(color='black')))
                ]
            )]
        )]
        py.plot({'data': data}, filename='tmp/transforms_tutorial.html', auto_play=True, validate=False)


# Aggregations in Python
if __name__ == '__main__':
    import plotly.offline as py

    # basic
    if __name__ == '__main__':
        subject = ['Moe', 'Larry', 'Curly', 'Moe', 'Larry', 'Curly', 'Moe', 'Larry', 'Curly', 'Moe', 'Larry', 'Curly']
        score = [1, 6, 2, 8, 2, 9, 4, 5, 1, 5, 2, 8]

        data = [dict(
            type='scatter',
            x=subject,
            y=score,
            mode='markers',
            transforms=[dict(
                type='aggregate',
                groups=subject,
                aggregations=[dict(
                    target='y', func='sum', enabled=True),
                ]
            )]
        )]
        py.plot({'data': data}, filename='tmp/transforms_tutorial.html', auto_play=True,  validate=False)


# Multiple Transforms in Python
if __name__ == '__main__':
    import plotly.offline as py
    import pandas as pd
    # Filter and Group By
    if __name__ == '__main__':
        df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")

        colors = ['blue', 'orange', 'green', 'red', 'purple']

        opt = []
        opts = []
        for i in range(0, len(colors)):
            opt = dict(
                target=df['continent'][[i]].unique(), value=dict(marker=dict(color=colors[i]))
            )
            opts.append(opt)

        data = [dict(
            type='scatter',
            mode='markers',
            x=df['lifeExp'],
            y=df['gdpPercap'],
            text=df['continent'],
            hoverinfo='text',
            opacity=0.8,
            marker=dict(
                size=df['pop'],
                sizemode='area',
                sizeref=200000
            ),
            transforms=[
                dict(
                    type='filter',
                    target=df['year'],
                    orientation='=',
                    value=2007
                ),
                dict(
                    type='groupby',
                    groups=df['continent'],
                    styles=opts
                )]
        )]

        layout = dict(
            yaxis=dict(
                type='log'
            )
        )
        py.plot({'data': data, 'layout':layout}, filename='tmp/transforms_tutorial.html', auto_play=True,  validate=False)

    # Filter and Aggregate
    if __name__ == '__main__':
        df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")

        data = [dict(
            type='scatter',
            mode='markers',
            x=df['lifeExp'],
            y=df['gdpPercap'],
            text=df['continent'],
            hoverinfo='text',
            opacity=0.8,
            marker=dict(
                size=df['pop'],
                sizemode='area',
                sizeref=200000
            ),
            transforms=[
                dict(
                    type='filter',
                    target=df['year'],
                    orientation='=',
                    value=2007
                ),
                dict(
                    type='aggregate',
                    groups=df['continent'],
                    aggregations=[
                        dict(target='x', func='avg'),
                        dict(target='y', func='avg'),
                        dict(target='marker.size', func='sum')
                    ]
                )]
        )]

        layout = dict(
            yaxis=dict(
                type='log'
            )
        )
        py.plot({'data': data, 'layout':layout}, filename='tmp/transforms_tutorial.html', auto_play=True,  validate=False)

    # All Transforms
    if __name__ == '__main__':
        df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")

        colors = ['blue', 'orange', 'green', 'red', 'purple']

        opt = []
        opts = []
        for i in range(0, len(colors)):
            opt = dict(
                target=df['continent'][[i]].unique(), value=dict(marker=dict(color=colors[i]))
            )
            opts.append(opt)

        data = [dict(
            type='scatter',
            mode='markers',
            x=df['lifeExp'],
            y=df['gdpPercap'],
            text=df['continent'],
            hoverinfo='text',
            opacity=0.8,
            marker=dict(
                size=df['pop'],
                sizemode='area',
                sizeref=200000
            ),
            transforms=[
                dict(
                    type='filter',
                    target=df['year'],
                    orientation='=',
                    value=2007
                ),
                dict(
                    type='groupby',
                    groups=df['continent'],
                    styles=opts
                ),
                dict(
                    type='aggregate',
                    groups=df['continent'],
                    aggregations=[
                        dict(target='x', func='avg'),
                        dict(target='y', func='avg'),
                        dict(target='marker.size', func='sum')
                    ]
                )]
        )]

        layout = dict(
            title='<b>Gapminder</b><br>2007 Average GDP Per Cap & Life Exp. by Continent',
            yaxis=dict(
                type='log'
            )
        )
        py.plot({'data': data, 'layout':layout}, filename='tmp/transforms_tutorial.html', auto_play=True,  validate=False)
