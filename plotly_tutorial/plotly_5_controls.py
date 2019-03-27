
# Custom Buttons
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go
    from plotly.tools import FigureFactory as FF

    import cmocean
    import json
    import numpy as np
    import pandas as pd

    # Restyle Button
    if __name__ == '__main__':
        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/volcano.csv')

        data = [go.Surface(z=df.values.tolist(), colorscale='Viridis')]

        layout = go.Layout(
            width=800,
            height=900,
            autosize=False,
            margin=dict(t=0, b=0, l=0, r=0),
            scene=dict(
                xaxis=dict(
                    gridcolor='rgb(255, 255, 255)',
                    zerolinecolor='rgb(255, 255, 255)',
                    showbackground=True,
                    backgroundcolor='rgb(230, 230,230)'
                ),
                yaxis=dict(
                    gridcolor='rgb(255, 255, 255)',
                    zerolinecolor='rgb(255, 255, 255)',
                    showbackground=True,
                    backgroundcolor='rgb(230, 230, 230)'
                ),
                zaxis=dict(
                    gridcolor='rgb(255, 255, 255)',
                    zerolinecolor='rgb(255, 255, 255)',
                    showbackground=True,
                    backgroundcolor='rgb(230, 230,230)'
                ),
                aspectratio=dict(x=1, y=1, z=0.7),
                aspectmode='manual'
            )
        )

        updatemenus = list([
            dict(
                buttons=list([
                    dict(
                        args=['type', 'surface'],
                        label='3D Surface',
                        method='restyle'
                    ),
                    dict(
                        args=['type', 'heatmap'],
                        label='Heatmap',
                        method='restyle'
                    )
                ]),
                direction='left',
                pad={'r': 10, 't': 10},
                showactive=True,
                type='buttons',
                x=0.1,
                xanchor='left',
                y=1.1,
                yanchor='top'
            ),
        ])

        annotations = list([
            dict(text='Trace type:', x=0, y=1.085, yref='paper', align='left', showarrow=False)
        ])
        layout['updatemenus'] = updatemenus
        layout['annotations'] = annotations

        fig = dict(data=data, layout=layout)
        py.plot(fig, filename='tmp/control_tutorial.html', auto_play=True)

    # Update Several Data Attributes
    if __name__ == '__main__':
        def cmocean_to_plotly(cmap, pl_entries=100):
            h = 1.0 / (pl_entries - 1)
            pl_colorscale = []

            for k in range(pl_entries):
                C = map(np.uint8, np.array(cmap(k * h)[:3]) * 255)
                pl_colorscale.append([k * h, 'rgb' + str((C[0], C[1], C[2]))])

            return pl_colorscale


        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/volcano.csv')

        data = [go.Surface(z=df.values.tolist(), colorscale='Viridis')]

        button_layer_1_height = 1.12
        button_layer_2_height = 1.065

        layout = go.Layout(
            width=800,
            height=900,
            autosize=False,
            margin=dict(t=0, b=0, l=0, r=0),
            scene=dict(
                xaxis=dict(
                    gridcolor='rgb(255, 255, 255)',
                    zerolinecolor='rgb(255, 255, 255)',
                    showbackground=True,
                    backgroundcolor='rgb(230, 230,230)'
                ),
                yaxis=dict(
                    gridcolor='rgb(255, 255, 255)',
                    zerolinecolor='rgb(255, 255, 255)',
                    showbackground=True,
                    backgroundcolor='rgb(230, 230,230)'
                ),
                zaxis=dict(
                    gridcolor='rgb(255, 255, 255)',
                    zerolinecolor='rgb(255, 255, 255)',
                    showbackground=True,
                    backgroundcolor='rgb(230, 230,230)'
                ),
                aspectratio=dict(x=1, y=1, z=0.7),
                aspectmode='manual'
            )
        )

        updatemenus = list([
            dict(
                buttons=list([
                    dict(
                        args=['colorscale', json.dumps(cmocean_to_plotly(cmocean.cm.haline))],
                        label='Haline',
                        method='restyle'
                    ),
                    dict(
                        args=['colorscale', json.dumps(cmocean_to_plotly(cmocean.cm.turbid))],
                        label='Turbid',
                        method='restyle'
                    ),
                    dict(
                        args=['colorscale', json.dumps(cmocean_to_plotly(cmocean.cm.speed))],
                        label='Speed',
                        method='restyle'
                    ),
                    dict(
                        args=['colorscale', json.dumps(cmocean_to_plotly(cmocean.cm.haline))],
                        label='Tempo',
                        method='restyle'
                    ),
                    dict(
                        args=['colorscale', json.dumps(cmocean_to_plotly(cmocean.cm.gray))],
                        label='Gray',
                        method='restyle'
                    ),
                    dict(
                        args=['colorscale', json.dumps(cmocean_to_plotly(cmocean.cm.phase))],
                        label='Phase',
                        method='restyle'
                    ),
                    dict(
                        args=['colorscale', json.dumps(cmocean_to_plotly(cmocean.cm.balance))],
                        label='Balance',
                        method='restyle'
                    ),
                    dict(
                        args=['colorscale', json.dumps(cmocean_to_plotly(cmocean.cm.delta))],
                        label='Delta',
                        method='restyle'
                    ),
                    dict(
                        args=['colorscale', json.dumps(cmocean_to_plotly(cmocean.cm.curl))],
                        label='Curl',
                        method='restyle'
                    ),
                ]),
                direction='left',
                pad={'r': 10, 't': 10},
                showactive=True,
                type='buttons',
                x=0.1,
                xanchor='left',
                y=button_layer_1_height,
                yanchor='top'
            ),
            dict(
                buttons=list([
                    dict(
                        args=['reversescale', True],
                        label='Reverse',
                        method='restyle'
                    ),
                    dict(
                        args=['reversescale', False],
                        label='Undo',
                        method='restyle'
                    )
                ]),
                direction='left',
                pad={'r': 10, 't': 10},
                showactive=True,
                type='buttons',
                x=0.45,
                xanchor='left',
                y=button_layer_2_height,
                yanchor='top'
            ),
            dict(
                buttons=list([
                    dict(
                        args=[{'contours.showlines': False, 'type': 'contour'}],
                        label='Hide lines',
                        method='restyle'
                    ),
                    dict(
                        args=[{'contours.showlines': True, 'type': 'contour'}],
                        label='Show lines',
                        method='restyle'
                    ),
                ]),
                direction='left',
                pad={'r': 10, 't': 10},
                showactive=True,
                type='buttons',
                x=0.65,
                xanchor='left',
                y=button_layer_2_height,
                yanchor='top'
            ),
            dict(
                buttons=list([
                    dict(
                        args=['type', 'surface'],
                        label='3d Surface',
                        method='restyle'
                    ),
                    dict(
                        args=['type', 'heatmap'],
                        label='Heatmap',
                        method='restyle'
                    ),
                    dict(
                        args=['type', 'contour'],
                        label='Contour',
                        method='restyle'
                    )
                ]),
                direction='left',
                pad={'r': 10, 't': 10},
                showactive=True,
                type='buttons',
                x=0.1,
                xanchor='left',
                y=button_layer_2_height,
                yanchor='top'
            ),
        ])

        annotations = list([
            dict(text='cmocean<br>scale', x=0, y=1.11, yref='paper', align='left', showarrow=False),
            dict(text='Trace type', x=0, y=1.05, yref='paper', showarrow=False)
        ])
        layout['updatemenus'] = updatemenus
        layout['annotations'] = annotations

        fig = dict(data=data, layout=layout)
        py.plot(fig, filename='tmp/control_tutorial.html', auto_play=True)

    # Relayout Button
    if __name__ == '__main__':
        x0 = np.random.normal(2, 0.4, 400)
        y0 = np.random.normal(2, 0.4, 400)
        x1 = np.random.normal(3, 0.6, 600)
        y1 = np.random.normal(6, 0.4, 400)
        x2 = np.random.normal(4, 0.2, 200)
        y2 = np.random.normal(4, 0.4, 200)

        trace0 = go.Scatter(
            x=x0,
            y=y0,
            mode='markers',
            marker=dict(color='#835AF1')
        )
        trace1 = go.Scatter(
            x=x1,
            y=y1,
            mode='markers',
            marker=dict(color='#7FA6EE')
        )
        trace2 = go.Scatter(
            x=x2,
            y=y2,
            mode='markers',
            marker=dict(color='#B8F7D4')
        )
        data = [trace0, trace1, trace2]

        cluster0 = [dict(type='circle',
                         xref='x', yref='y',
                         x0=min(x0), y0=min(y0),
                         x1=max(x0), y1=max(y0),
                         opacity=.25,
                         line=dict(color='#835AF1'),
                         fillcolor='#835AF1')]
        cluster1 = [dict(type='circle',
                         xref='x', yref='y',
                         x0=min(x1), y0=min(y1),
                         x1=max(x1), y1=max(y1),
                         opacity=.25,
                         line=dict(color='#7FA6EE'),
                         fillcolor='#7FA6EE')]
        cluster2 = [dict(type='circle',
                         xref='x', yref='y',
                         x0=min(x2), y0=min(y2),
                         x1=max(x2), y1=max(y2),
                         opacity=.25,
                         line=dict(color='#B8F7D4'),
                         fillcolor='#B8F7D4')]

        updatemenus = list([
            dict(type="buttons",
                 buttons=list([
                     dict(label='None',
                          method='relayout',
                          args=['shapes', []]),
                     dict(label='Cluster 0',
                          method='relayout',
                          args=['shapes', cluster0]),
                     dict(label='Cluster 1',
                          method='relayout',
                          args=['shapes', cluster1]),
                     dict(label='Cluster 2',
                          method='relayout',
                          args=['shapes', cluster2]),
                     dict(label='All',
                          method='relayout',
                          args=['shapes', cluster0 + cluster1 + cluster2])
                 ]),
                 )
        ])

        layout = dict(title='Highlight Clusters', showlegend=False,
                      updatemenus=updatemenus)

        fig = dict(data=data, layout=layout)
        py.plot(fig, filename='tmp/control_tutorial.html', auto_play=True)

    # Update Button
    if __name__ == '__main__':
        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
        df.columns = [col.replace('AAPL.', '') for col in df.columns]

        trace_high = go.Scatter(x=list(df.index),
                                y=list(df.High),
                                name='High',
                                line=dict(color='#33CFA5'))

        trace_high_avg = go.Scatter(x=list(df.index),
                                    y=[df.High.mean()] * len(df.index),
                                    name='High Average',
                                    visible=False,
                                    line=dict(color='#33CFA5', dash='dash'))

        trace_low = go.Scatter(x=list(df.index),
                               y=list(df.Low),
                               name='Low',
                               line=dict(color='#F06A6A'))

        trace_low_avg = go.Scatter(x=list(df.index),
                                   y=[df.Low.mean()] * len(df.index),
                                   name='Low Average',
                                   visible=False,
                                   line=dict(color='#F06A6A', dash='dash'))

        data = [trace_high, trace_high_avg, trace_low, trace_low_avg]

        high_annotations = [dict(x='2016-03-01',
                                 y=df.High.mean(),
                                 xref='x', yref='y',
                                 text='High Average:<br>' + str(df.High.mean()),
                                 ax=0, ay=-40),
                            dict(x=df.High.idxmax(),
                                 y=df.High.max(),
                                 xref='x', yref='y',
                                 text='High Max:<br>' + str(df.High.max()),
                                 ax=0, ay=-40)]
        low_annotations = [dict(x='2015-05-01',
                                y=df.Low.mean(),
                                xref='x', yref='y',
                                text='Low Average:<br>' + str(df.Low.mean()),
                                ax=0, ay=40),
                           dict(x=df.High.idxmin(),
                                y=df.Low.min(),
                                xref='x', yref='y',
                                text='Low Min:<br>' + str(df.Low.min()),
                                ax=0, ay=40)]

        updatemenus = list([
            dict(type="buttons",
                 active=-1,
                 buttons=list([
                     dict(label='High',
                          method='update',
                          args=[{'visible': [True, True, False, False]},
                                {'title': 'Yahoo High',
                                 'annotations': high_annotations}]),
                     dict(label='Low',
                          method='update',
                          args=[{'visible': [False, False, True, True]},
                                {'title': 'Yahoo Low',
                                 'annotations': low_annotations}]),
                     dict(label='Both',
                          method='update',
                          args=[{'visible': [True, True, True, True]},
                                {'title': 'Yahoo',
                                 'annotations': high_annotations + low_annotations}]),
                     dict(label='Reset',
                          method='update',
                          args=[{'visible': [True, False, True, False]},
                                {'title': 'Yahoo',
                                 'annotations': []}])
                 ]),
                 )
        ])

        layout = dict(title='Yahoo', showlegend=False,
                      updatemenus=updatemenus)

        fig = dict(data=data, layout=layout)
        py.plot(fig, filename='tmp/control_tutorial.html', auto_play=True)

    # Style Buttons
    if __name__ == '__main__':
        df_wind = pd.read_csv('https://plot.ly/~datasets/2805.csv')

        df_known_capacity = df_wind[df_wind['total_cpcy'] != -99999.000]
        df_sum = df_known_capacity.groupby('manufac')['total_cpcy'].sum().sort_values(ascending=False).to_frame()

        df_farms = pd.read_csv('https://plot.ly/~jackp/17256.csv')
        df_farms.set_index('Wind Farm', inplace=True)

        wind_farms = list([
            dict(
                args=[{
                    'mapbox.center.lat': 38,
                    'mapbox.center.lon': -94,
                    'mapbox.zoom': 3,
                    'annotations[0].text': 'All US wind turbines (scroll to zoom)'
                }],
                label='USA',
                method='relayout'
            )
        ])

        for farm, row in df_farms.iterrows():
            desc = []
            for col in df_farms.columns:
                if col not in ['DegMinSec', 'Latitude', 'Longitude']:
                    if str(row[col]) not in ['None', 'nan', '']:
                        desc.append(col + ': ' + str(row[col]).strip("'"))
            desc.insert(0, farm)
            wind_farms.append(
                dict(
                    args=[{
                        'mapbox.center.lat': row['Latitude'],
                        'mapbox.center.lon': float(str(row['Longitude']).strip("'")),
                        'mapbox.zoom': 9,
                        'annotations[0].text': '<br>'.join(desc)
                    }],
                    label=' '.join(farm.split(' ')[0:2]),
                    method='relayout'
                )
            )

        data = []
        for mfr in list(df_sum.index):
            if mfr != 'unknown':
                trace = dict(
                    lat=df_wind[df_wind['manufac'] == mfr]['lat_DD'],
                    lon=df_wind[df_wind['manufac'] == mfr]['long_DD'],
                    name=mfr,
                    marker=dict(size=4),
                    type='scattermapbox'
                )
            data.append(trace)

        mapbox_access_token = 'pk.eyJ1IjoiY2hlbHNlYXBsb3RseSIsImEiOiJjaXFqeXVzdDkwMHFrZnRtOGtlMGtwcGs4In0.SLidkdBMEap9POJGIe1eGw'

        layout = dict(
            height=800,
            margin=dict(t=0, b=0, l=0, r=0),
            font=dict(color='#FFFFFF', size=11),
            paper_bgcolor='#000000',
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=0,
                center=dict(
                    lat=38,
                    lon=-94
                ),
                pitch=0,
                zoom=3,
                style='dark'
            ),
        )

        updatemenus = list([
            dict(
                buttons=wind_farms[0:6],
                direction='left',
                pad={'r': 0, 't': 10},
                type='buttons',
                x=0.1,
                xanchor='left',
                y=1.0,
                yanchor='top',
                bgcolor='#AAAAAA',
                active=99,
                bordercolor='#FFFFFF',
                font=dict(size=11, color='#000000')
            ),
            dict(
                buttons=wind_farms[6:10],
                direction='left',
                pad={'r': 0, 't': 10},
                type='buttons',
                x=0.1,
                xanchor='left',
                y=0.95,
                yanchor='top',
                bgcolor='#AAAAAA',
                active=99,
                bordercolor='#FFFFFF',
                font=dict(size=11, color='#000000')
            ),
            dict(
                buttons=list([
                    dict(
                        args=['mapbox.style', 'dark'],
                        label='Dark',
                        method='relayout'
                    ),
                    dict(
                        args=['mapbox.style', 'light'],
                        label='Light',
                        method='relayout'
                    ),
                    dict(
                        args=['mapbox.style', 'satellite'],
                        label='Satellite',
                        method='relayout'
                    ),
                    dict(
                        args=['mapbox.style', 'satellite-streets'],
                        label='Satellite with Streets',
                        method='relayout'
                    )
                ]),
                direction='up',
                x=0.75,
                xanchor='left',
                y=0.05,
                yanchor='bottom',
                bgcolor='#000000',
                bordercolor='#FFFFFF',
                font=dict(size=11)
            ),
        ])

        annotations = list([
            dict(text='All US wind turbines (scroll to zoom)', font=dict(color='magenta', size=14), borderpad=10,
                 x=0.05, y=0.05, xref='paper', yref='paper', align='left', showarrow=False, bgcolor='black'),
            dict(text='Wind<br>Farms', x=0.01, y=0.99, yref='paper', align='left', showarrow=False, font=dict(size=14))
        ])

        layout['updatemenus'] = updatemenus
        layout['annotations'] = annotations

        figure = dict(data=data, layout=layout)
        py.plot(fig, filename='tmp/control_tutorial.html', auto_play=True)


# Sliders
if __name__ == '__main__':
    import plotly.offline as py
    import numpy as np

    # Simple Slider Control
    if __name__ == '__main__':
        data = [dict(
            visible=False,
            line=dict(color='#00CED1', width=6),
            name='𝜈 = ' + str(step),
            x=np.arange(0, 10, 0.01),
            y=np.sin(step * np.arange(0, 10, 0.01))) for step in np.arange(0, 5, 0.1)]
        data[10]['visible'] = True
        steps = []
        for i in range(len(data)):
            step = dict(
                method='restyle',
                args=['visible', [False] * len(data)],
            )
            step['args'][1][i] = True  # Toggle i'th trace to "visible"
            steps.append(step)

        sliders = [dict(
            active=10,
            currentvalue={"prefix": "Frequency: "},
            pad={"t": 50},
            steps=steps
        )]

        layout = dict(sliders=sliders)

        fig = dict(data=data, layout=layout)
        py.plot(fig, filename='tmp/control_tutorial.html', auto_play=True)


# Dropdown Menus
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go
    from plotly.tools import FigureFactory as FF

    import json
    import numpy as np
    import pandas as pd
    # Restyle Dropdown
    if __name__ == '__main__':
        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/volcano.csv')

        data = [go.Surface(z=df.values.tolist(), colorscale='Viridis')]

        layout = go.Layout(
            width=800,
            height=900,
            autosize=False,
            margin=dict(t=0, b=0, l=0, r=0),
            scene=dict(
                xaxis=dict(
                    gridcolor='rgb(255, 255, 255)',
                    zerolinecolor='rgb(255, 255, 255)',
                    showbackground=True,
                    backgroundcolor='rgb(230, 230,230)'
                ),
                yaxis=dict(
                    gridcolor='rgb(255, 255, 255)',
                    zerolinecolor='rgb(255, 255, 255)',
                    showbackground=True,
                    backgroundcolor='rgb(230, 230, 230)'
                ),
                zaxis=dict(
                    gridcolor='rgb(255, 255, 255)',
                    zerolinecolor='rgb(255, 255, 255)',
                    showbackground=True,
                    backgroundcolor='rgb(230, 230,230)'
                ),
                aspectratio=dict(x=1, y=1, z=0.7),
                aspectmode='manual'
            )
        )

        updatemenus = list([
            dict(
                buttons=list([
                    dict(
                        args=['type', 'surface'],
                        label='3D Surface',
                        method='restyle'
                    ),
                    dict(
                        args=['type', 'heatmap'],
                        label='Heatmap',
                        method='restyle'
                    )
                ]),
                direction='down',
                pad={'r': 10, 't': 10},
                showactive=True,
                x=0.1,
                xanchor='left',
                y=1.1,
                yanchor='top'
            ),
        ])

        annotations = list([
            dict(text='Trace type:', x=0, y=1.085, yref='paper', align='left', showarrow=False)
        ])
        layout['updatemenus'] = updatemenus
        layout['annotations'] = annotations

        fig = dict(data=data, layout=layout)
        py.plot(fig, filename='tmp/control_tutorial.html', auto_play=True)

    # Relayout Dropdown
    if __name__ == '__main__':
        x0 = np.random.normal(2, 0.4, 400)
        y0 = np.random.normal(2, 0.4, 400)
        x1 = np.random.normal(3, 0.6, 600)
        y1 = np.random.normal(6, 0.4, 400)
        x2 = np.random.normal(4, 0.2, 200)
        y2 = np.random.normal(4, 0.4, 200)

        trace0 = go.Scatter(
            x=x0,
            y=y0,
            mode='markers',
            marker=dict(color='#835AF1')
        )
        trace1 = go.Scatter(
            x=x1,
            y=y1,
            mode='markers',
            marker=dict(color='#7FA6EE')
        )
        trace2 = go.Scatter(
            x=x2,
            y=y2,
            mode='markers',
            marker=dict(color='#B8F7D4')
        )
        data = [trace0, trace1, trace2]

        cluster0 = [dict(type='circle',
                         xref='x', yref='y',
                         x0=min(x0), y0=min(y0),
                         x1=max(x0), y1=max(y0),
                         opacity=.25,
                         line=dict(color='#835AF1'),
                         fillcolor='#835AF1')]
        cluster1 = [dict(type='circle',
                         xref='x', yref='y',
                         x0=min(x1), y0=min(y1),
                         x1=max(x1), y1=max(y1),
                         opacity=.25,
                         line=dict(color='#7FA6EE'),
                         fillcolor='#7FA6EE')]
        cluster2 = [dict(type='circle',
                         xref='x', yref='y',
                         x0=min(x2), y0=min(y2),
                         x1=max(x2), y1=max(y2),
                         opacity=.25,
                         line=dict(color='#B8F7D4'),
                         fillcolor='#B8F7D4')]

        updatemenus = list([
            dict(buttons=list([
                dict(label='None',
                     method='relayout',
                     args=['shapes', []]),
                dict(label='Cluster 0',
                     method='relayout',
                     args=['shapes', cluster0]),
                dict(label='Cluster 1',
                     method='relayout',
                     args=['shapes', cluster1]),
                dict(label='Cluster 2',
                     method='relayout',
                     args=['shapes', cluster2]),
                dict(label='All',
                     method='relayout',
                     args=['shapes', cluster0 + cluster1 + cluster2])
            ]),
            )
        ])

        layout = dict(title='Highlight Clusters', showlegend=False,
                      updatemenus=updatemenus)

        fig = dict(data=data, layout=layout)
        py.plot(fig, filename='tmp/control_tutorial.html', auto_play=True)

    # Update Dropdown
    if __name__ == '__main__':
        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
        df.columns = [col.replace('AAPL.', '') for col in df.columns]

        trace_high = go.Scatter(x=list(df.index),
                                y=list(df.High),
                                name='High',
                                line=dict(color='#33CFA5'))

        trace_high_avg = go.Scatter(x=list(df.index),
                                    y=[df.High.mean()] * len(df.index),
                                    name='High Average',
                                    visible=False,
                                    line=dict(color='#33CFA5', dash='dash'))

        trace_low = go.Scatter(x=list(df.index),
                               y=list(df.Low),
                               name='Low',
                               line=dict(color='#F06A6A'))

        trace_low_avg = go.Scatter(x=list(df.index),
                                   y=[df.Low.mean()] * len(df.index),
                                   name='Low Average',
                                   visible=False,
                                   line=dict(color='#F06A6A', dash='dash'))

        data = [trace_high, trace_high_avg, trace_low, trace_low_avg]

        high_annotations = [dict(x='2016-03-01',
                                 y=df.High.mean(),
                                 xref='x', yref='y',
                                 text='High Average:<br>' + str(df.High.mean()),
                                 ax=0, ay=-40),
                            dict(x=df.High.idxmax(),
                                 y=df.High.max(),
                                 xref='x', yref='y',
                                 text='High Max:<br>' + str(df.High.max()),
                                 ax=0, ay=-40)]
        low_annotations = [dict(x='2015-05-01',
                                y=df.Low.mean(),
                                xref='x', yref='y',
                                text='Low Average:<br>' + str(df.Low.mean()),
                                ax=0, ay=40),
                           dict(x=df.High.idxmin(),
                                y=df.Low.min(),
                                xref='x', yref='y',
                                text='Low Min:<br>' + str(df.Low.min()),
                                ax=0, ay=40)]

        updatemenus = list([
            dict(active=-1,
                 buttons=list([
                     dict(label='High',
                          method='update',
                          args=[{'visible': [True, True, False, False]},
                                {'title': 'Yahoo High',
                                 'annotations': high_annotations}]),
                     dict(label='Low',
                          method='update',
                          args=[{'visible': [False, False, True, True]},
                                {'title': 'Yahoo Low',
                                 'annotations': low_annotations}]),
                     dict(label='Both',
                          method='update',
                          args=[{'visible': [True, True, True, True]},
                                {'title': 'Yahoo',
                                 'annotations': high_annotations + low_annotations}]),
                     dict(label='Reset',
                          method='update',
                          args=[{'visible': [True, False, True, False]},
                                {'title': 'Yahoo',
                                 'annotations': []}])
                 ]),
                 )
        ])

        layout = dict(title='Yahoo', showlegend=False,
                      updatemenus=updatemenus)

        fig = dict(data=data, layout=layout)
        py.plot(fig, filename='tmp/control_tutorial.html', auto_play=True)


# Range Slider and Selector
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    from datetime import datetime
    import pandas as pd

    # Basic Range Slider and Range Selectors
    if __name__ == '__main__':
        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
        df.columns = [col.replace('AAPL.', '') for col in df.columns]

        trace = go.Scatter(x=list(df.Date),
                           y=list(df.High))

        data = [trace]
        layout = dict(
            title='Time series with range slider and selectors',
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
                        dict(count=1,
                             label='YTD',
                             step='year',
                             stepmode='todate'),
                        dict(count=1,
                             label='1y',
                             step='year',
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
        py.plot(fig, filename='tmp/control_tutorial.html', auto_play=True)

    # Range Slider with Vertically Stacked Subplots
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=["2013-01-15", "2013-01-29", "2013-02-26", "2013-04-19", "2013-07-02", "2013-08-27",
               "2013-10-22", "2014-01-20", "2014-05-05", "2014-07-01", "2015-02-09", "2015-04-13",
               "2015-05-13", "2015-06-08", "2015-08-05", "2016-02-25"],
            y=["8", "3", "2", "10", "5", "5", "6", "8", "3", "3", "7", "5", "10", "10", "9", "14"],
            name="var0",
            text=["8", "3", "2", "10", "5", "5", "6", "8", "3", "3", "7", "5", "10", "10", "9", "14"],
            yaxis="y",
        )

        trace2 = go.Scatter(
            x=["2015-04-13", "2015-05-13", "2015-06-08", "2015-08-05", "2016-02-25"],
            y=["53.0", "69.0", "89.0", "41.0", "41.0"],
            name="var1",
            text=["53.0", "69.0", "89.0", "41.0", "41.0"],
            yaxis="y2",
        )

        trace3 = go.Scatter(
            x=["2013-01-29", "2013-02-26", "2013-04-19", "2013-07-02", "2013-08-27", "2013-10-22",
               "2014-01-20", "2014-04-09", "2014-05-05", "2014-07-01", "2014-09-30", "2015-02-09",
               "2015-04-13", "2015-06-08", "2016-02-25"],
            y=["9.6", "4.6", "2.7", "8.3", "18", "7.3", "3", "7.5", "1.0", "0.5", "2.8", "9.2",
               "13", "5.8", "6.9"],
            name="var2",
            text=["9.6", "4.6", "2.7", "8.3", "18", "7.3", "3", "7.5", "1.0", "0.5", "2.8", "9.2",
                  "13", "5.8", "6.9"],
            yaxis="y3",
        )

        trace4 = go.Scatter(
            x=["2013-01-29", "2013-02-26", "2013-04-19", "2013-07-02", "2013-08-27", "2013-10-22",
               "2014-01-20", "2014-04-09", "2014-05-05", "2014-07-01", "2014-09-30", "2015-02-09",
               "2015-04-13", "2015-06-08", "2016-02-25"],
            y=["6.9", "7.5", "7.3", "7.3", "6.9", "7.1", "8", "7.8", "7.4", "7.9", "7.9", "7.6",
               "7.2", "7.2", "8.0"],
            name="var3",
            text=["6.9", "7.5", "7.3", "7.3", "6.9", "7.1", "8", "7.8", "7.4", "7.9", "7.9", "7.6",
                  "7.2", "7.2", "8.0"],
            yaxis="y4",
        )

        trace5 = go.Scatter(
            x=["2013-02-26", "2013-07-02", "2013-09-26", "2013-10-22", "2013-12-04", "2014-01-02",
               "2014-01-20", "2014-05-05", "2014-07-01", "2015-02-09", "2015-05-05"],
            y=["290", "1078", "263", "407", "660", "740", "33", "374", "95", "734", "3000"],
            name="var4",
            text=["290", "1078", "263", "407", "660", "740", "33", "374", "95", "734", "3000"],
            yaxis="y5",
        )

        data = [trace1, trace2, trace3, trace4, trace5]

        # style all the traces
        for k in range(len(data)):
            data[k].update(
                {
                    "hoverinfo": "name+x+text",
                    "line": {"width": 0.5},
                    "marker": {"size": 8},
                    "mode": "lines+markers",
                    "showlegend": False
                }
            )

        layout = {
            "annotations": [
                {
                    "x": "2013-06-01",
                    "y": 0,
                    "arrowcolor": "rgba(63, 81, 181, 0.2)",
                    "arrowsize": 0.3,
                    "ax": 0,
                    "ay": 30,
                    "text": "state1",
                    "xref": "x",
                    "yanchor": "bottom",
                    "yref": "y"
                },
                {
                    "x": "2014-09-13",
                    "y": 0,
                    "arrowcolor": "rgba(76, 175, 80, 0.1)",
                    "arrowsize": 0.3,
                    "ax": 0,
                    "ay": 30,
                    "text": "state2",
                    "xref": "x",
                    "yanchor": "bottom",
                    "yref": "y"
                }
            ],
            "dragmode": "zoom",
            "hovermode": "x",
            "legend": {"traceorder": "reversed"},
            "margin": {
                "t": 100,
                "b": 100
            },
            "shapes": [
                {
                    "fillcolor": "rgba(63, 81, 181, 0.2)",
                    "line": {"width": 0},
                    "type": "rect",
                    "x0": "2013-01-15",
                    "x1": "2013-10-17",
                    "xref": "x",
                    "y0": 0,
                    "y1": 0.95,
                    "yref": "paper"
                },
                {
                    "fillcolor": "rgba(76, 175, 80, 0.1)",
                    "line": {"width": 0},
                    "type": "rect",
                    "x0": "2013-10-22",
                    "x1": "2015-08-05",
                    "xref": "x",
                    "y0": 0,
                    "y1": 0.95,
                    "yref": "paper"
                }
            ],
            "xaxis": {
                "autorange": True,
                "range": ["2012-10-31 18:36:37.3129", "2016-05-10 05:23:22.6871"],
                "rangeslider": {
                    "autorange": True,
                    "range": ["2012-10-31 18:36:37.3129", "2016-05-10 05:23:22.6871"]
                },
                "type": "date"
            },
            "yaxis": {
                "anchor": "x",
                "autorange": True,
                "domain": [0, 0.2],
                "linecolor": "#673ab7",
                "mirror": True,
                "range": [-60.0858369099, 28.4406294707],
                "showline": True,
                "side": "right",
                "tickfont": {"color": "#673ab7"},
                "tickmode": "auto",
                "ticks": "",
                "titlefont": {"color": "#673ab7"},
                "type": "linear",
                "zeroline": False
            },
            "yaxis2": {
                "anchor": "x",
                "autorange": True,
                "domain": [0.2, 0.4],
                "linecolor": "#E91E63",
                "mirror": True,
                "range": [29.3787777032, 100.621222297],
                "showline": True,
                "side": "right",
                "tickfont": {"color": "#E91E63"},
                "tickmode": "auto",
                "ticks": "",
                "titlefont": {"color": "#E91E63"},
                "type": "linear",
                "zeroline": False
            },
            "yaxis3": {
                "anchor": "x",
                "autorange": True,
                "domain": [0.4, 0.6],
                "linecolor": "#795548",
                "mirror": True,
                "range": [-3.73690396239, 22.2369039624],
                "showline": True,
                "side": "right",
                "tickfont": {"color": "#795548"},
                "tickmode": "auto",
                "ticks": "",
                "title": "mg/L",
                "titlefont": {"color": "#795548"},
                "type": "linear",
                "zeroline": False
            },
            "yaxis4": {
                "anchor": "x",
                "autorange": True,
                "domain": [0.6, 0.8],
                "linecolor": "#607d8b",
                "mirror": True,
                "range": [6.63368032236, 8.26631967764],
                "showline": True,
                "side": "right",
                "tickfont": {"color": "#607d8b"},
                "tickmode": "auto",
                "ticks": "",
                "title": "mmol/L",
                "titlefont": {"color": "#607d8b"},
                "type": "linear",
                "zeroline": False
            },
            "yaxis5": {
                "anchor": "x",
                "autorange": True,
                "domain": [0.8, 1],
                "linecolor": "#2196F3",
                "mirror": True,
                "range": [-685.336803224, 3718.33680322],
                "showline": True,
                "side": "right",
                "tickfont": {"color": "#2196F3"},
                "tickmode": "auto",
                "ticks": "",
                "title": "mg/Kg",
                "titlefont": {"color": "#2196F3"},
                "type": "linear",
                "zeroline": False
            }
        }
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/control_tutorial.html', auto_play=True)

    #
    if __name__ == '__main__':
        py.plot(fig, filename='tmp/control_tutorial.html', auto_play=True)

    #
    if __name__ == '__main__':
        py.plot(fig, filename='tmp/control_tutorial.html', auto_play=True)
