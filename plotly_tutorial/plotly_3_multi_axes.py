
# 1、multi axes
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    # two y-axes
    if __name__ == '__main__':

        trace1 = go.Scatter(
            x=[1, 2, 3],
            y=[40, 50, 60],
            name='yaxis data'
        )
        trace2 = go.Scatter(
            x=[2, 3, 4],
            y=[4, 5, 6],
            name='yaxis2 data',
            yaxis='y2'
        )
        data = [trace1, trace2]
        layout = go.Layout(
            title='Double Y Axis Example',
            yaxis=dict(
                title='yaxis title'
            ),
            yaxis2=dict(
                title='yaxis2 title',
                titlefont=dict(
                    color='rgb(148, 103, 189)'
                ),
                tickfont=dict(
                    color='rgb(148, 103, 189)'
                ),
                overlaying='y',
                side='right'
            )
        )
        fig = go.Figure(data=data, layout=layout)
        plot_url = py.plot(fig, filename='tmp/multi_tutorial.html', auto_play=True)


    # multi Y-Axes
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[1, 2, 3],
            y=[4, 5, 6],
            name='yaxis1 data'
        )
        trace2 = go.Scatter(
            x=[2, 3, 4],
            y=[40, 50, 60],
            name='yaxis2 data',
            yaxis='y2'
        )
        trace3 = go.Scatter(
            x=[4, 5, 6],
            y=[40000, 50000, 60000],
            name='yaxis3 data',
            yaxis='y3'
        )
        trace4 = go.Scatter(
            x=[5, 6, 7],
            y=[400000, 500000, 600000],
            name='yaxis4 data',
            yaxis='y4'
        )
        data = [trace1, trace2, trace3, trace4]
        layout = go.Layout(
            title='multiple y-axes example',
            width=800,
            xaxis=dict(
                domain=[0.3, 0.7]
            ),
            yaxis=dict(
                title='yaxis title',
                titlefont=dict(
                    color='#1f77b4'
                ),
                tickfont=dict(
                    color='#1f77b4'
                )
            ),
            yaxis2=dict(
                title='yaxis2 title',
                titlefont=dict(
                    color='#ff7f0e'
                ),
                tickfont=dict(
                    color='#ff7f0e'
                ),
                anchor='free',
                overlaying='y',
                side='left',
                position=0.15
            ),
            yaxis3=dict(
                title='yaxis4 title',
                titlefont=dict(
                    color='#d62728'
                ),
                tickfont=dict(
                    color='#d62728'
                ),
                anchor='x',
                overlaying='y',
                side='right'
            ),
            yaxis4=dict(
                title='yaxis5 title',
                titlefont=dict(
                    color='#9467bd'
                ),
                tickfont=dict(
                    color='#9467bd'
                ),
                anchor='free',
                overlaying='y',
                side='right',
                position=0.85
            )
        )
        fig = go.Figure(data=data, layout=layout)
        plot_url = py.plot(fig, filename='tmp/multi_tutorial.html', auto_play=True)


# Subplots
if __name__ == '__main__':
    from plotly import tools
    import plotly.offline as py
    import plotly.graph_objs as go

    # Simple Subplot
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[1, 2, 3],
            y=[4, 5, 6],
            mode='markers+text',
            text=['Text A', 'Text B', 'Text C'],
            textposition='bottom center'
        )
        trace2 = go.Scatter(
            x=[20, 30, 40],
            y=[50, 60, 70],
            mode='markers+text',
            text=['Text D', 'Text E', 'Text F'],
            textposition='bottom center'
        )

        fig = tools.make_subplots(rows=1, cols=2)

        fig.append_trace(trace1, 1, 1)
        fig.append_trace(trace2, 1, 2)

        fig['layout'].update(height=600, width=800, title='i <3 annotations and subplots')
        py.iplot(fig, filename='simple-subplot-with-annotations')
        '''
        This is the format of your plot grid:
        [ (1,1) x1,y1 ]  [ (1,2) x2,y2 ]
        '''
        plot_url = py.plot(fig, filename='tmp/multi_tutorial.html', auto_play=True)

    # Multiple Subplots，不用subplot
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[1, 2, 3],
            y=[4, 5, 6]
        )
        trace2 = go.Scatter(
            x=[20, 30, 40],
            y=[50, 60, 70],
            xaxis='x2',
            yaxis='y2'
        )
        trace3 = go.Scatter(
            x=[300, 400, 500],
            y=[600, 700, 800],
            xaxis='x3',
            yaxis='y3'
        )
        trace4 = go.Scatter(
            x=[4000, 5000, 6000],
            y=[7000, 8000, 9000],
            xaxis='x4',
            yaxis='y4'
        )
        data = [trace1, trace2, trace3, trace4]
        layout = go.Layout(
            xaxis=dict(
                domain=[0, 0.45]
            ),
            yaxis=dict(
                domain=[0, 0.45]
            ),
            xaxis2=dict(
                domain=[0.55, 1]
            ),
            xaxis3=dict(
                domain=[0, 0.45],
                anchor='y3'
            ),
            xaxis4=dict(
                domain=[0.55, 1],
                anchor='y4'
            ),
            yaxis2=dict(
                domain=[0, 0.45],
                anchor='x2'
            ),
            yaxis3=dict(
                domain=[0.55, 1]
            ),
            yaxis4=dict(
                domain=[0.55, 1],
                anchor='x4'
            )
        )
        fig = go.Figure(data=data, layout=layout)
        plot_url = py.plot(fig, filename='tmp/multi_tutorial.html', auto_play=True)

    # Multiple Subplots with Titles，用subplot
    if __name__ == '__main__':
        trace1 = go.Scatter(x=[1, 2, 3], y=[4, 5, 6])
        trace2 = go.Scatter(x=[20, 30, 40], y=[50, 60, 70])
        trace3 = go.Scatter(x=[300, 400, 500], y=[600, 700, 800])
        trace4 = go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000])

        fig = tools.make_subplots(rows=2, cols=2, subplot_titles=('Plot 1', 'Plot 2',
                                                                  'Plot 3', 'Plot 4'))

        fig.append_trace(trace1, 1, 1)
        fig.append_trace(trace2, 1, 2)
        fig.append_trace(trace3, 2, 1)
        fig.append_trace(trace4, 2, 2)

        fig['layout'].update(height=600, width=600, title='Multiple Subplots' +
                                                          ' with Titles')
        plot_url = py.plot(fig, filename='tmp/multi_tutorial.html', auto_play=True)

    # Simple Subplot with Annotations
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[1, 2, 3],
            y=[4, 5, 6],
            mode='markers+text',
            text=['Text A', 'Text B', 'Text C'],
            textposition='bottom'
        )
        trace2 = go.Scatter(
            x=[20, 30, 40],
            y=[50, 60, 70],
            mode='markers+text',
            text=['Text D', 'Text E', 'Text F'],
            textposition='bottom'
        )

        fig = tools.make_subplots(rows=1, cols=2)

        fig.append_trace(trace1, 1, 1)
        fig.append_trace(trace2, 1, 2)

        fig['layout'].update(height=600, width=800, title='i <3 annotations and subplots')
        plot_url = py.plot(fig, filename='tmp/multi_tutorial.html', auto_play=True)

    # Side by Side Subplot，不均衡的subplot
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[1, 2, 3],
            y=[4, 5, 6]
        )
        trace2 = go.Scatter(
            x=[20, 30, 40],
            y=[50, 60, 70],
            xaxis='x2',
            yaxis='y2'
        )
        data = [trace1, trace2]
        layout = go.Layout(
            xaxis=dict(
                domain=[0, 0.7]
            ),
            xaxis2=dict(
                domain=[0.8, 1]
            ),
            yaxis2=dict(
                anchor='x2'
            )
        )
        fig = go.Figure(data=data, layout=layout)
        plot_url = py.plot(fig, filename='tmp/multi_tutorial.html', auto_play=True)

    # Customizing Subplot Axes
    if __name__ == '__main__':
        trace1 = go.Scatter(x=[1, 2, 3], y=[4, 5, 6])
        trace2 = go.Scatter(x=[20, 30, 40], y=[50, 60, 70])
        trace3 = go.Scatter(x=[300, 400, 500], y=[600, 700, 800])
        trace4 = go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000])

        fig = tools.make_subplots(rows=2, cols=2, subplot_titles=('Plot 1', 'Plot 2',
                                                                  'Plot 3', 'Plot 4'))
        fig.append_trace(trace1, 1, 1)
        fig.append_trace(trace2, 1, 2)
        fig.append_trace(trace3, 2, 1)
        fig.append_trace(trace4, 2, 2)

        fig['layout']['xaxis1'].update(title='xaxis 1 title')
        fig['layout']['xaxis2'].update(title='xaxis 2 title', range=[10, 50])
        fig['layout']['xaxis3'].update(title='xaxis 3 title', showgrid=False)
        fig['layout']['xaxis4'].update(title='xaxis 4 title', type='log')

        fig['layout']['yaxis1'].update(title='yaxis 1 title')
        fig['layout']['yaxis2'].update(title='yaxis 2 title', range=[40, 80])
        fig['layout']['yaxis3'].update(title='yaxis 3 title', showgrid=False)
        fig['layout']['yaxis4'].update(title='yaxis 4 title')

        fig['layout'].update(title='Customizing Subplot Axes')
        plot_url = py.plot(fig, filename='tmp/multi_tutorial.html', auto_play=True)

    # Subplots with Shared X-Axes
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[0, 1, 2],
            y=[10, 11, 12]
        )
        trace2 = go.Scatter(
            x=[2, 3, 4],
            y=[100, 110, 120],
        )
        trace3 = go.Scatter(
            x=[3, 4, 5],
            y=[1000, 1100, 1200],
        )
        fig = tools.make_subplots(rows=3, cols=1, specs=[[{}], [{}], [{}]],
                                  shared_xaxes=True, shared_yaxes=True,
                                  vertical_spacing=0.001)
        fig.append_trace(trace1, 3, 1)
        fig.append_trace(trace2, 2, 1)
        fig.append_trace(trace3, 1, 1)

        fig['layout'].update(height=600, width=600, title='Stacked Subplots with Shared X-Axes')
        plot_url = py.plot(fig, filename='tmp/multi_tutorial.html', auto_play=True)

    # Subplots with Shared Y-Axes
    if __name__ == '__main__':
        trace0 = go.Scatter(
            x=[1, 2, 3],
            y=[2, 3, 4]
        )
        trace1 = go.Scatter(
            x=[20, 30, 40],
            y=[5, 5, 5],
        )
        trace2 = go.Scatter(
            x=[2, 3, 4],
            y=[600, 700, 800],
        )
        trace3 = go.Scatter(
            x=[4000, 5000, 6000],
            y=[7000, 8000, 9000],
        )

        fig = tools.make_subplots(rows=2, cols=2, shared_yaxes=True)

        fig.append_trace(trace0, 1, 1)
        fig.append_trace(trace1, 1, 2)
        fig.append_trace(trace2, 2, 1)
        fig.append_trace(trace3, 2, 2)

        fig['layout'].update(height=600, width=600,
                             title='Multiple Subplots with Shared Y-Axes')
        plot_url = py.plot(fig, filename='tmp/multi_tutorial.html', auto_play=True)

    # Subplots with Shared Axes
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[1, 2, 3],
            y=[2, 3, 4]
        )
        trace2 = go.Scatter(
            x=[20, 30, 40],
            y=[5, 5, 5],
            xaxis='x2',
            yaxis='y'
        )
        trace3 = go.Scatter(
            x=[2, 3, 4],
            y=[600, 700, 800],
            xaxis='x',
            yaxis='y3'
        )
        trace4 = go.Scatter(
            x=[4000, 5000, 6000],
            y=[7000, 8000, 9000],
            xaxis='x4',
            yaxis='y4'
        )
        data = [trace1, trace2, trace3, trace4]
        layout = go.Layout(
            xaxis=dict(
                domain=[0, 0.45]
            ),
            yaxis=dict(
                domain=[0, 0.45]
            ),
            xaxis2=dict(
                domain=[0.55, 1]
            ),
            xaxis4=dict(
                domain=[0.55, 1],
                anchor='y4'
            ),
            yaxis3=dict(
                domain=[0.55, 1]
            ),
            yaxis4=dict(
                domain=[0.55, 1],
                anchor='x4'
            )
        )
        fig = go.Figure(data=data, layout=layout)
        plot_url = py.plot(fig, filename='tmp/multi_tutorial.html', auto_play=True)

    # Stacked Subplots
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[0, 1, 2],
            y=[10, 11, 12]
        )
        trace2 = go.Scatter(
            x=[2, 3, 4],
            y=[100, 110, 120],
        )
        trace3 = go.Scatter(
            x=[3, 4, 5],
            y=[1000, 1100, 1200],
        )

        fig = tools.make_subplots(rows=3, cols=1)

        fig.append_trace(trace3, 1, 1)
        fig.append_trace(trace2, 2, 1)
        fig.append_trace(trace1, 3, 1)

        fig['layout'].update(height=600, width=600, title='Stacked subplots')
        plot_url = py.plot(fig, filename='tmp/multi_tutorial.html', auto_play=True)

    # Stacked Subplots with a Shared X-Axis
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[0, 1, 2],
            y=[10, 11, 12]
        )
        trace2 = go.Scatter(
            x=[2, 3, 4],
            y=[100, 110, 120],
            yaxis='y2'
        )
        trace3 = go.Scatter(
            x=[3, 4, 5],
            y=[1000, 1100, 1200],
            yaxis='y3'
        )
        data = [trace1, trace2, trace3]
        layout = go.Layout(
            yaxis=dict(
                domain=[0, 0.33]
            ),
            legend=dict(
                traceorder='reversed'
            ),
            yaxis2=dict(
                domain=[0.33, 0.66]
            ),
            yaxis3=dict(
                domain=[0.66, 1]
            )
        )
        fig = go.Figure(data=data, layout=layout)
        plot_url = py.plot(fig, filename='tmp/multi_tutorial.html', auto_play=True)

    # Custom Sized Subplot with Subplot Titles
    if __name__ == '__main__':
        trace0 = go.Scatter(
            x=[1, 2],
            y=[1, 2]
        )
        trace1 = go.Scatter(
            x=[1, 2],
            y=[1, 2]
        )
        trace2 = go.Scatter(
            x=[1, 2, 3],
            y=[2, 1, 2]
        )
        fig = tools.make_subplots(rows=2, cols=2, specs=[[{}, {}], [{'colspan': 2}, None]],
                                  subplot_titles=('First Subplot', 'Second Subplot', 'Third Subplot'))

        fig.append_trace(trace0, 1, 1)
        fig.append_trace(trace1, 1, 2)
        fig.append_trace(trace2, 2, 1)

        fig['layout'].update(showlegend=False, title='Specs with Subplot Title')
        plot_url = py.plot(fig, filename='tmp/multi_tutorial.html', auto_play=True)

    # Multiple Custom Sized Subplots
    if __name__ == '__main__':
        trace1 = go.Scatter(x=[1, 2], y=[1, 2], name='(1,1)')
        trace2 = go.Scatter(x=[1, 2], y=[1, 2], name='(1,2)')
        trace3 = go.Scatter(x=[1, 2], y=[1, 2], name='(2,1)')
        trace4 = go.Scatter(x=[1, 2], y=[1, 2], name='(3,1)')
        trace5 = go.Scatter(x=[1, 2], y=[1, 2], name='(5,1)')
        trace6 = go.Scatter(x=[1, 2], y=[1, 2], name='(5,2)')

        fig = tools.make_subplots(rows=5, cols=2,
                                  specs=[[{}, {'rowspan': 2}],
                                         [{}, None],
                                         [{'rowspan': 2, 'colspan': 2}, None],
                                         [None, None],
                                         [{}, {}]],
                                  print_grid=True)

        fig.append_trace(trace1, 1, 1)
        fig.append_trace(trace2, 1, 2)
        fig.append_trace(trace3, 2, 1)
        fig.append_trace(trace4, 3, 1)
        fig.append_trace(trace5, 5, 1)
        fig.append_trace(trace6, 5, 2)

        fig['layout'].update(height=600, width=600, title='specs examples')
        plot_url = py.plot(fig, filename='tmp/multi_tutorial.html', auto_play=True)


# Inset Plots in Python
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go


    # Simple Inset Graph
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[1, 2, 3],
            y=[4, 3, 2]
        )
        trace2 = go.Scatter(
            x=[20, 30, 40],
            y=[30, 40, 50],
            xaxis='x2',
            yaxis='y2'
        )
        data = [trace1, trace2]
        layout = go.Layout(
            xaxis2=dict(
                domain=[0.6, 0.95],
                anchor='y2'
            ),
            yaxis2=dict(
                domain=[0.6, 0.95],
                anchor='x2'
            )
        )
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/multi_tutorial.html', auto_play=True)


# Mixed Subplot
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    import pandas as pd

    # read in volcano database data
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/volcano_db.csv', encoding='latin-1')

    # frequency of Country
    freq = df
    freq = freq.Country.value_counts().reset_index().rename(columns={'index': 'x'})

    # plot(1) top 10 countries by total volcanoes
    locations = go.Bar(x=freq['x'][0:10], y=freq['Country'][0:10], marker=dict(color='#CF1020'))

    # read in 3d volcano surface data
    df_v = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/volcano.csv')

    # plot(2) 3d surface of volcano
    threed = go.Surface(z=df_v.values.tolist(), colorscale='Reds', showscale=False)

    # plot(3)  scattergeo map of volcano locations
    trace3 = {
        "geo": "geo3",
        "lon": df['Longitude'],
        "lat": df['Latitude'],
        "hoverinfo": 'text',
        "marker": {
            "size": 4,
            "opacity": 0.8,
            "color": '#CF1020',
            "colorscale": 'Viridis'
        },
        "mode": "markers",
        "type": "scattergeo"
    }

    data = [locations, threed, trace3]

    # control the subplot below using domain in 'geo', 'scene', and 'axis'
    layout = {
        "plot_bgcolor": 'black',
        "paper_bgcolor": 'black',
        "titlefont": {
            "size": 20,
            "family": "Raleway"
        },
        "font": {
            "color": 'white'
        },
        "dragmode": "zoom",
        "geo3": {
            "domain": {
                "x": [0, 0.55],
                "y": [0, 0.9]
            },
            "lakecolor": "rgba(127,205,255,1)",
            "oceancolor": "rgb(6,66,115)",
            "landcolor": 'white',
            "projection": {"type": "orthographic"},
            "scope": "world",
            "showlakes": True,
            "showocean": True,
            "showland": True,
            "bgcolor": 'black'
        },
        "margin": {
            "r": 10,
            "t": 25,
            "b": 40,
            "l": 60
        },
        "scene": {"domain": {
            "x": [0.5, 1],
            "y": [0, 0.55]
        },
            "xaxis": {"gridcolor": 'white'},
            "yaxis": {"gridcolor": 'white'},
            "zaxis": {"gridcolor": 'white'}
        },
        "showlegend": False,
        "title": "<br>Volcano Database",
        "xaxis": {
            "anchor": "y",
            "domain": [0.6, 0.95]
        },
        "yaxis": {
            "anchor": "x",
            "domain": [0.65, 0.95],
            "showgrid": False
        }
    }

    annotations = {"text": "Source: NOAA",
                   "showarrow": False,
                   "xref": "paper",
                   "yref": "paper",
                   "x": 0,
                   "y": 0}

    layout['annotations'] = [annotations]

    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='tmp/multi_tutorial.html', auto_play=True)


# figure factory
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go
    import plotly.figure_factory as ff

    # Horizontal Table and Chart
    if __name__ == '__main__':
        table_data = [['Team', 'Wins', 'Losses', 'Ties'],
                      ['Montréal<br>Canadiens', 18, 4, 0],
                      ['Dallas Stars', 18, 5, 0],
                      ['NY Rangers', 16, 5, 0],
                      ['Boston<br>Bruins', 13, 8, 0],
                      ['Chicago<br>Blackhawks', 13, 8, 0],
                      ['LA Kings', 13, 8, 0],
                      ['Ottawa<br>Senators', 12, 5, 0]]

        figure = ff.create_table(table_data, height_constant=60)

        teams = ['Montréal Canadiens', 'Dallas Stars', 'NY Rangers',
                 'Boston Bruins', 'Chicago Blackhawks', 'LA Kings', 'Ottawa Senators']
        GFPG = [3.54, 3.48, 3.0, 3.27, 2.83, 2.45, 3.18]
        GAPG = [2.17, 2.57, 2.0, 2.91, 2.57, 2.14, 2.77]

        trace1 = go.Scatter(x=teams, y=GFPG,
                            marker=dict(color='#0099ff'),
                            name='Goals For<br>Per Game',
                            xaxis='x2', yaxis='y2')
        trace2 = go.Scatter(x=teams, y=GAPG,
                            marker=dict(color='#404040'),
                            name='Goals Against<br>Per Game',
                            xaxis='x2', yaxis='y2')

        figure.add_traces([trace1, trace2])

        # initialize xaxis2 and yaxis2
        figure['layout']['xaxis2'] = {}
        figure['layout']['yaxis2'] = {}

        # Edit layout for subplots
        figure.layout.xaxis.update({'domain': [0, .5]})
        figure.layout.xaxis2.update({'domain': [0.6, 1.]})

        # The graph's yaxis MUST BE anchored to the graph's xaxis
        figure.layout.yaxis2.update({'anchor': 'x2'})
        figure.layout.yaxis2.update({'title': 'Goals'})

        # Update the margins to add a title and see graph x-labels.
        figure.layout.margin.update({'t': 50, 'b': 100})
        figure.layout.update({'title': '2016 Hockey Stats'})
        py.plot(figure, filename='tmp/multi_tutorial.html', auto_play=True)

    # Vertical Table and Chart
    if __name__ == '__main__':
        # Add table data
        table_data = [['Team', 'Wins', 'Losses', 'Ties'],
                      ['Montréal<br>Canadiens', 18, 4, 0],
                      ['Dallas Stars', 18, 5, 0],
                      ['NY Rangers', 16, 5, 0],
                      ['Boston<br>Bruins', 13, 8, 0],
                      ['Chicago<br>Blackhawks', 13, 8, 0],
                      ['Ottawa<br>Senators', 12, 5, 0]]

        # Initialize a figure with ff.create_table(table_data)
        figure = ff.create_table(table_data, height_constant=60)

        # Add graph data
        teams = ['Montréal Canadiens', 'Dallas Stars', 'NY Rangers',
                 'Boston Bruins', 'Chicago Blackhawks', 'Ottawa Senators']
        GFPG = [3.54, 3.48, 3.0, 3.27, 2.83, 3.18]
        GAPG = [2.17, 2.57, 2.0, 2.91, 2.57, 2.77]

        # Make traces for graph
        trace1 = go.Bar(x=teams, y=GFPG, xaxis='x2', yaxis='y2',
                        marker=dict(color='#0099ff'),
                        name='Goals For<br>Per Game')
        trace2 = go.Bar(x=teams, y=GAPG, xaxis='x2', yaxis='y2',
                        marker=dict(color='#404040'),
                        name='Goals Against<br>Per Game')

        # Add trace data to figure
        figure.add_traces([trace1, trace2])

        # initialize xaxis2 and yaxis2
        figure['layout']['xaxis2'] = {}
        figure['layout']['yaxis2'] = {}

        # Edit layout for subplots
        figure.layout.yaxis.update({'domain': [0, .45]})
        figure.layout.yaxis2.update({'domain': [.6, 1]})

        # The graph's yaxis2 MUST BE anchored to the graph's xaxis2 and vice versa
        figure.layout.yaxis2.update({'anchor': 'x2'})
        figure.layout.xaxis2.update({'anchor': 'y2'})
        figure.layout.yaxis2.update({'title': 'Goals'})

        # Update the margins to add a title and see graph x-labels.
        figure.layout.margin.update({'t': 75, 'l': 50})
        figure.layout.update({'title': '2016 Hockey Stats'})

        # Update the height because adding a graph vertically will interact with
        # the plot height calculated for the table
        figure.layout.update({'height': 800})
        py.plot(figure, filename='tmp/multi_tutorial.html', auto_play=True)


# Table and Chart Subplots
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    import pandas as pd
    import re

    # Import CSV Data
    if __name__ == '__main__':
        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Mining-BTC-180.csv')

        # remove min:sec:millisec from dates
        for i, row in enumerate(df['Date']):
            p = re.compile(' 00:00:00')
            datetime = p.split(df['Date'][i])[0]
            df.iloc[i, 1] = datetime

        table = go.Table(
            columnwidth=[0.4, 0.47, 0.48, 0.4, 0.4, 0.45, 0.5, 0.6],
            header=dict(
                # values=list(df.columns[1:]),
                values=['Date', 'Number<br>Transactions', 'Output<br>Volume (BTC)',
                        'Market<br>Price', 'Hash<br>Rate', 'Cost per<br>trans-USD',
                        'Mining<br>Revenue-USD', 'Trasaction<br>fees-BTC'],
                font=dict(size=10),
                line=dict(color='rgb(50, 50, 50)'),
                align='left',
                fill=dict(color='#d562be'),
            ),
            cells=dict(
                values=[df[k].tolist() for k in df.columns[1:]],
                line=dict(color='rgb(50, 50, 50)'),
                align='left',
                fill=dict(color='#f5f5fa')
            )
        )
        py.plot([table], filename='tmp/multi_tutorial.html', auto_play=True)

    # Table and Right Aligned Plots
    if __name__ == '__main__':
        table_trace1 = go.Table(
            domain=dict(x=[0, 0.5],
                        y=[0, 1.0]),
            columnwidth=[30] + [33, 35, 33],
            columnorder=[0, 1, 2, 3, 4],
            header=dict(height=50,
                        values=[['<b>Date</b>'], ['<b>Number<br>transactions</b>'],
                                ['<b>Output<br>volume(BTC)</b>'], ['<b>Market<br>Price</b>']],
                        line=dict(color='rgb(50, 50, 50)'),
                        align=['left'] * 5,
                        font=dict(color=['rgb(45, 45, 45)'] * 5, size=14),
                        fill=dict(color='#d562be')),
            cells=dict(values=[df[k].tolist() for k in
                               ['Date', 'Number-transactions', 'Output-volume(BTC)', 'Market-price']],
                       line=dict(color='#506784'),
                       align=['left'] * 5,
                       font=dict(color=['rgb(40, 40, 40)'] * 5, size=12),
                       format=[None] + [", .2f"] * 2 + [',.4f'],
                       prefix=[None] * 2 + ['$', u'\u20BF'],
                       suffix=[None] * 4,
                       height=27,
                       fill=dict(color=['rgb(235, 193, 238)', 'rgba(228, 222, 249, 0.65)']))
        )

        trace1 = go.Scatter(
            x=df['Date'],
            y=df['Hash-rate'],
            xaxis='x1',
            yaxis='y1',
            mode='lines',
            line=dict(width=2, color='#9748a1'),
            name='hash-rate-TH/s'
        )

        trace2 = go.Scatter(
            x=df['Date'],
            y=df['Mining-revenue-USD'],
            xaxis='x2',
            yaxis='y2',
            mode='lines',
            line=dict(width=2, color='#b04553'),
            name='mining revenue'
        )

        trace3 = go.Scatter(
            x=df['Date'],
            y=df['Transaction-fees-BTC'],
            xaxis='x3',
            yaxis='y3',
            mode='lines',
            line=dict(width=2, color='#af7bbd'),
            name='transact-fee'
        )

        axis = dict(
            showline=True,
            zeroline=False,
            showgrid=True,
            mirror=True,
            ticklen=4,
            gridcolor='#ffffff',
            tickfont=dict(size=10)
        )

        layout1 = dict(
            width=950,
            height=800,
            autosize=False,
            title='Bitcoin mining stats for 180 days',
            margin=dict(t=100),
            showlegend=False,
            xaxis1=dict(axis, **dict(domain=[0.55, 1], anchor='y1', showticklabels=False)),
            xaxis2=dict(axis, **dict(domain=[0.55, 1], anchor='y2', showticklabels=False)),
            xaxis3=dict(axis, **dict(domain=[0.55, 1], anchor='y3')),
            yaxis1=dict(axis, **dict(domain=[0.66, 1.0], anchor='x1', hoverformat='.2f')),
            yaxis2=dict(axis, **dict(domain=[0.3 + 0.03, 0.63], anchor='x2', tickprefix='$', hoverformat='.2f')),
            yaxis3=dict(axis, **dict(domain=[0.0, 0.3], anchor='x3', tickprefix=u'\u20BF', hoverformat='.2f')),
            plot_bgcolor='rgba(228, 222, 249, 0.65)'
        )

        fig1 = dict(data=[table_trace1, trace1, trace2, trace3], layout=layout1)
        py.plot(fig1, filename='tmp/multi_tutorial.html', auto_play=True)



