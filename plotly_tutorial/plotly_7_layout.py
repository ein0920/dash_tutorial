
# 1 Formatting Ticks in Python
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    # Tickmode - Linear
    if __name__ == '__main__':
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        y = [28.8, 28.5, 37, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]

        trace0 = go.Scatter(
            x=x,
            y=y
        )

        data = [trace0]

        layout = go.Layout(
            xaxis=go.layout.XAxis(
                tickmode='linear',
                tick0=0.5,
                dtick=0.75
            )
        )

        fig = go.Figure(
            data=data,
            layout=layout
        )
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Tickmode - Array
    if __name__ == '__main__':
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        y = [28.8, 28.5, 37, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]

        trace0 = go.Scatter(
            x=x,
            y=y
        )

        data = [trace0]

        layout = go.Layout(
            xaxis=go.layout.XAxis(
                tickmode='array',
                tickvals=[1, 3, 5, 7, 9, 11],
                ticktext=['One', 'Three', 'Five', 'Seven', 'Nine', 'Eleven']
            )
        )

        fig = go.Figure(
            data=data,
            layout=layout
        )
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Using Tickformat Attribute
    if __name__ == '__main__':
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        y = [0.18, 0.38, 0.56, 0.46, 0.59, 0.4, 0.78, 0.77, 0.74, 0.42, 0.45, 0.39]

        trace0 = go.Scatter(
            x=x,
            y=y
        )

        data = [trace0]

        layout = go.Layout(
            yaxis=go.layout.YAxis(
                tickformat='%'
            )
        )

        fig = go.Figure(
            data=data,
            layout=layout
        )
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Using Tickformat Atttribute - Date/Time
    if __name__ == '__main__':
        import pandas as pd

        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

        trace0 = go.Scatter(
            mode='lines',
            name='AAPL High',
            x=df['Date'],
            y=df['AAPL.High'],
            line=go.scatter.Line(
                color='#17BECF'
            )
        )

        trace1 = go.Scatter(
            mode='lines',
            name='AAPL Low',
            x=df['Date'],
            y=df['AAPL.Low'],
            line=go.scatter.Line(
                color='#7F7F7F'
            )
        )

        data = [trace0, trace1]

        layout = go.Layout(
            title='Time Series with Custom Date-Time Format',
            xaxis=go.layout.XAxis(
                tickformat='%d %B (%a)<br>%Y'
            )
        )

        fig = go.Figure(
            data=data,
            layout=layout
        )
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Using Exponentformat Attribute
    if __name__ == '__main__':
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        y = [68000, 52000, 60000, 20000, 95000, 40000, 60000, 79000, 74000, 42000, 20000, 90000]

        trace0 = go.Scatter(
            x=x,
            y=y
        )

        data = [trace0]

        layout = go.Layout(
            yaxis=go.layout.YAxis(
                showexponent='all',
                exponentformat='e'
            )
        )

        fig = go.Figure(
            data=data,
            layout=layout
        )
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Tickformatstops to customize for different zoom levels
    if __name__ == '__main__':
        import pandas as pd

        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

        trace0 = go.Scatter(
            x=df['Date'],
            y=df['mavg']
        )

        data = [trace0]

        layout = go.Layout(
            xaxis=go.layout.XAxis(
                tickformatstops=[
                    go.layout.xaxis.Tickformatstop(
                        dtickrange=[None, 1000],
                        value="%H:%M:%S.%L ms"
                    ),
                    go.layout.xaxis.Tickformatstop(
                        dtickrange=[1000, 60000],
                        value="%H:%M:%S s"
                    ),
                    go.layout.xaxis.Tickformatstop(
                        dtickrange=[60000, 3600000],
                        value="%H:%M m"
                    ),
                    go.layout.xaxis.Tickformatstop(
                        dtickrange=[3600000, 86400000],
                        value="%H:%M h"
                    ),
                    go.layout.xaxis.Tickformatstop(
                        dtickrange=[86400000, 604800000],
                        value="%e. %b d"
                    ),
                    go.layout.xaxis.Tickformatstop(
                        dtickrange=[604800000, "M1"],
                        value="%e. %b w"
                    ),
                    go.layout.xaxis.Tickformatstop(
                        dtickrange=["M1", "M12"],
                        value="%b '%y M"
                    ),
                    go.layout.xaxis.Tickformatstop(
                        dtickrange=["M12", None],
                        value="%Y Y"
                    )
                ]
            )
        )

        fig = go.Figure(
            data=data,
            layout=layout
        )

        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)


# 2 Setting Graph Size in Python
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    # Adjusting Height, Width, & Margins
    if __name__ == '__main__':
        data = [
            go.Scatter(
                x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
                y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
            )
        ]
        layout = go.Layout(
            autosize=False,
            width=500,
            height=500,
            margin=go.layout.Margin(
                l=50,
                r=50,
                b=100,
                t=100,
                pad=4
            ),
            paper_bgcolor='#7f7f7f',
            plot_bgcolor='#c7c7c7'
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Automatically Adjust Margins
    if __name__ == '__main__':
        data = [
            go.Bar(
                x=['Apples', 'Oranges', 'Watermelon', 'Pears'],
                y=[3, 2, 1, 4]
            )
        ]
        layout = go.Layout(
            autosize=False,
            width=500,
            height=500,
            yaxis=go.layout.YAxis(
                title='Y-axis Title',
                ticktext=['Very long label', 'long label', '3', 'label'],
                tickvals=[1, 2, 3, 4],
                tickmode='array',
                automargin=True,
                titlefont=dict(size=30),
            ),
            paper_bgcolor='#7f7f7f',
            plot_bgcolor='#c7c7c7'
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)


# 3 Setting the Title, Legend Entries, and Axis Titles in Python
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    # Styling Axes Labels
    if __name__ == '__main__':
        import plotly.plotly as py
        import plotly.graph_objs as go

        trace1 = go.Scatter(
            x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            y=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            name='Name of Trace 1'
        )
        trace2 = go.Scatter(
            x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            y=[1, 0, 3, 2, 5, 4, 7, 6, 8],
            name='Name of Trace 2'
        )
        data = [trace1, trace2]
        layout = go.Layout(
            title='Plot Title',
            xaxis=dict(
                title='x Axis',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            ),
            yaxis=dict(
                title='y Axis',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )
        )
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)


# 4 3D Axes in Python
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    # Range of axes
    if __name__ == '__main__':
        import numpy as np
        N = 70
        trace1 = go.Mesh3d(x=(70 * np.random.randn(N)),
                           y=(55 * np.random.randn(N)),
                           z=(40 * np.random.randn(N)),
                           opacity=0.5,
                           color='rgba(244,22,100,0.6)'
                           )

        layout = go.Layout(
            scene=dict(
                xaxis=dict(
                    nticks=4, range=[-100, 100], ),
                yaxis=dict(
                    nticks=4, range=[-50, 100], ),
                zaxis=dict(
                    nticks=4, range=[-100, 100], ), ),
            width=700,
            margin=dict(
                r=20, l=10,
                b=10, t=10)
        )
        fig = go.Figure(data=[trace1], layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Fixed Ratio Axes
    if __name__ == '__main__':
        import plotly.tools as tls
        import numpy as np

        N = 50

        fig = tls.make_subplots(
            rows=2, cols=2,
            specs=[
                [{'is_3d': True}, {'is_3d': True}],
                [{'is_3d': True}, {'is_3d': True}]
            ],
            print_grid=False
        )
        for i in [1, 2]:
            for j in [1, 2]:
                fig.append_trace(
                    go.Mesh3d(
                        x=(60 * np.random.randn(N)),
                        y=(25 * np.random.randn(N)),
                        z=(40 * np.random.randn(N)),
                        opacity=0.5,
                    ),
                    row=i, col=j)

        fig['layout'].update(go.Layout(
            width=700,
            margin=dict(
                r=10, l=10,
                b=10, t=10)
        ))

        # fix the ratio in the top left subplot to be a cube
        fig['layout']['scene'].update(go.layout.Scene(aspectmode='cube'))

        # manually force the z-axis to appear twice as big as the other two
        fig['layout']['scene2'].update(go.layout.Scene(
            aspectmode='manual',
            aspectratio=go.layout.scene.Aspectratio(
                x=1, y=1, z=2
            )
        ))

        # draw axes in proportion to the proportion of their ranges
        fig['layout']['scene3'].update(go.layout.Scene(aspectmode='data'))

        # automatically produce something that is well proportioned using 'data' as the default
        fig['layout']['scene4'].update(go.layout.Scene(aspectmode='auto'))
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Set Axes Title
    if __name__ == '__main__':
        N = 50
        trace1 = go.Mesh3d(x=(60 * np.random.randn(N)),
                           y=(25 * np.random.randn(N)),
                           z=(40 * np.random.randn(N)),
                           opacity=0.5,
                           color='yellow'
                           )
        trace2 = go.Mesh3d(x=(70 * np.random.randn(N)),
                           y=(55 * np.random.randn(N)),
                           z=(30 * np.random.randn(N)),
                           opacity=0.5,
                           color='pink'
                           )
        layout = go.Layout(
            scene=dict(
                xaxis=dict(
                    title='X AXIS TITLE'),
                yaxis=dict(
                    title='Y AXIS TITLE'),
                zaxis=dict(
                    title='Z AXIS TITLE'), ),
            width=700,
            margin=dict(
                r=20, b=10,
                l=10, t=10)
        )
        fig = go.Figure(data=[trace1, trace2], layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Ticks Formatting
    if __name__ == '__main__':
        N = 50
        trace1 = go.Mesh3d(x=(60 * np.random.randn(N)),
                           y=(25 * np.random.randn(N)),
                           z=(40 * np.random.randn(N)),
                           opacity=0.5,
                           color='rgba(100,22,200,0.5)'
                           )

        layout = go.Layout(
            scene=dict(
                xaxis=dict(
                    ticktext=['TICKS', 'MESH', 'PLOTLY', 'PYTHON'],
                    tickvals=[0, 50, 75, -50]),
                yaxis=dict(
                    nticks=5, tickfont=dict(
                        color='green',
                        size=12,
                        family='Old Standard TT, serif', ),
                    ticksuffix='#'),
                zaxis=dict(
                    nticks=4, ticks='outside',
                    tick0=0, tickwidth=4), ),
            width=700,
            margin=dict(
                r=10, l=10,
                b=10, t=10)
        )
        fig = go.Figure(data=[trace1], layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Background and Grid Color
    if __name__ == '__main__':
        import numpy as np

        N = 50
        trace1 = go.Mesh3d(x=(30 * np.random.randn(N)),
                           y=(25 * np.random.randn(N)),
                           z=(30 * np.random.randn(N)),
                           opacity=0.5, )

        layout = go.Layout(
            scene=dict(
                xaxis=dict(
                    backgroundcolor="rgb(200, 200, 230)",
                    gridcolor="rgb(255, 255, 255)",
                    showbackground=True,
                    zerolinecolor="rgb(255, 255, 255)", ),
                yaxis=dict(
                    backgroundcolor="rgb(230, 200,230)",
                    gridcolor="rgb(255, 255, 255)",
                    showbackground=True,
                    zerolinecolor="rgb(255, 255, 255)"),
                zaxis=dict(
                    backgroundcolor="rgb(230, 230,200)",
                    gridcolor="rgb(255, 255, 255)",
                    showbackground=True,
                    zerolinecolor="rgb(255, 255, 255)", ), ),
            width=700,
            margin=dict(
                r=10, l=10,
                b=10, t=10)
        )
        fig = go.Figure(data=[trace1], layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)


# 5 Axes in Python
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    # Toggling Axes Lines, Ticks, Labels, and Autorange
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            y=[8, 7, 6, 5, 4, 3, 2, 1, 0]
        )
        trace2 = go.Scatter(
            x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
        )
        data = [trace1, trace2]
        layout = go.Layout(
            xaxis=dict(
                autorange=True,
                showgrid=False,
                zeroline=False,
                showline=False,
                ticks='',
                showticklabels=False
            ),
            yaxis=dict(
                autorange=True,
                showgrid=False,
                zeroline=False,
                showline=False,
                ticks='',
                showticklabels=False
            )
        )
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Tick Placement, Color, and Style
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            y=[8, 7, 6, 5, 4, 3, 2, 1, 0]
        )
        trace2 = go.Scatter(
            x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
        )
        data = [trace1, trace2]
        layout = go.Layout(
            xaxis=dict(
                tickmode='linear',
                ticks='outside',
                tick0=0,
                dtick=0.25,
                ticklen=8,
                tickwidth=4,
                tickcolor='#000'
            ),
            yaxis=dict(
                tickmode='linear',
                ticks='outside',
                tick0=0,
                dtick=0.25,
                ticklen=8,
                tickwidth=4,
                tickcolor='#000'
            )
        )
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Set and Style Axes Title Labels and Ticks
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            y=[8, 7, 6, 5, 4, 3, 2, 1, 0]
        )
        trace2 = go.Scatter(
            x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
        )
        data = [trace1, trace2]
        layout = go.Layout(
            xaxis=dict(
                title='AXIS TITLE',
                titlefont=dict(
                    family='Arial, sans-serif',
                    size=18,
                    color='lightgrey'
                ),
                showticklabels=True,
                tickangle=45,
                tickfont=dict(
                    family='Old Standard TT, serif',
                    size=14,
                    color='black'
                ),
                exponentformat='e',
                showexponent='all'
            ),
            yaxis=dict(
                title='AXIS TITLE',
                titlefont=dict(
                    family='Arial, sans-serif',
                    size=18,
                    color='lightgrey'
                ),
                showticklabels=True,
                tickangle=45,
                tickfont=dict(
                    family='Old Standard TT, serif',
                    size=14,
                    color='black'
                ),
                exponentformat='e',
                showexponent='all'
            )
        )
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Styling and Coloring Axes and the Zero-Line
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            y=[8, 7, 6, 5, 4, 3, 2, 1, 0]
        )
        trace2 = go.Scatter(
            x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
        )
        data = [trace1, trace2]
        layout = go.Layout(
            xaxis=dict(
                showgrid=True,
                zeroline=True,
                showline=True,
                mirror='ticks',
                gridcolor='#bdbdbd',
                gridwidth=2,
                zerolinecolor='#969696',
                zerolinewidth=4,
                linecolor='#636363',
                linewidth=6
            ),
            yaxis=dict(
                showgrid=True,
                zeroline=True,
                showline=True,
                mirror='ticks',
                gridcolor='#bdbdbd',
                gridwidth=2,
                zerolinecolor='#969696',
                zerolinewidth=4,
                linecolor='#636363',
                linewidth=6
            )
        )
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Setting the Range of Axes Manually
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            y=[8, 7, 6, 5, 4, 3, 2, 1, 0]
        )
        trace2 = go.Scatter(
            x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
        )
        data = [trace1, trace2]
        layout = go.Layout(
            xaxis=dict(
                range=[2, 5]
            ),
            yaxis=dict(
                range=[2, 5]
            )
        )
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Subcategory Axes
    if __name__ == '__main__':
        trace1 = go.Box(
            x=[2, 3, 1, 5],
            y=["A", "A", "A", "A"],
            line=dict(color='gray'),
            name="A",
            orientation="h"
        )

        trace2 = go.Box(
            x=[8, 3, 6, 5],
            y=["B", "B", "B", "B"],
            line=dict(color='gray'),
            name="B",
            orientation="h"
        )

        trace3 = go.Box(
            x=[2, 3, 2, 5],
            y=["C", "C", "C", "C"],
            line=dict(color='gray'),
            name="C",
            orientation="h"
        )

        trace4 = go.Box(
            x=[7.5, 3, 6, 4],
            y=["D", "D", "D", "D"],
            line=dict(color='gray'),
            name="D",
            orientation="h"
        )

        data = [trace1, trace2, trace3, trace4]

        layout = go.Layout(
            annotations=[
                dict(
                    x=-0.0951769406393,
                    y=1.06972670892,
                    showarrow=False,
                    text="Subgroup",
                    xref="paper",
                    yref="paper"
                ),
                dict(
                    x=-0.235516552511,
                    y=1.07060587474,
                    showarrow=False,
                    text="Group",
                    xref="paper",
                    yref="paper"
                ),
                dict(
                    x=-0.235516552511,
                    y=0.922906017856,
                    showarrow=False,
                    text="One",
                    xref="paper",
                    yref="paper"
                ),
                dict(
                    x=-0.235516552511,
                    y=0.375,
                    showarrow=False,
                    text="Two",
                    xref="paper",
                    yref="paper"
                )
            ],
            height=400,
            hovermode="closest",
            legend=dict(
                x=0.986145833333,
                y=0.936263886049
            ),
            margin=dict(
                r=10,
                t=25,
                b=40,
                l=110
            ),
            shapes=[
                dict(
                    line=dict(
                        color="rgba(68, 68, 68, 0.5)",
                        width=1
                    ),
                    type="line",
                    x0=-0.3,
                    x1=1.2,
                    xref="paper",
                    y0=0.5,
                    y1=0.5,
                    yref="paper"
                ),
                dict(
                    line=dict(
                        color="rgba(68, 68, 68, 0.63)",
                        width=1
                    ),
                    type="line",
                    x0=-0.3,
                    x1=1.2,
                    xref="paper",
                    y0=1,
                    y1=1,
                    yref="paper"
                )
            ],
            showlegend=True,
            title="",
            width=600,
            xaxis=dict(
                domain=[0, 1]
            ),
            yaxis=dict(
                autorange=True,
                categoryorder="category descending",
                domain=[0, 1],
                range=[-0.5, 3.5],
                showline=True,
                title="",
                type="category"
            )
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Logarithmic Axes
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            y=[8, 7, 6, 5, 4, 3, 2, 1, 0]
        )
        trace2 = go.Scatter(
            x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
        )
        data = [trace1, trace2]
        layout = go.Layout(
            xaxis=dict(
                type='log',
                autorange=True
            ),
            yaxis=dict(
                type='log',
                autorange=True
            )
        )
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Fixed Ratio Axes
    if __name__ == '__main__':
        trace0 = go.Scatter(
            x=[0, 1, 1, 0, 0, 1, 1, 2, 2, 3, 3, 2, 2, 3],
            y=[0, 0, 1, 1, 3, 3, 2, 2, 3, 3, 1, 1, 0, 0]
        )

        trace1 = go.Scatter(
            x=[0, 1, 2, 3],
            y=[1, 2, 4, 8],
            yaxis="y2"
        )

        trace2 = go.Scatter(
            x=[1, 10, 100, 10, 1],
            y=[0, 1, 2, 3, 4],
            xaxis="x2",
            yaxis="y3",
        )

        trace3 = go.Scatter(
            x=[1, 100, 30, 80, 1],
            y=[1, 1.5, 2, 2.5, 3],
            xaxis="x2",
            yaxis="y4"
        )

        data = [trace0, trace1, trace2, trace3]

        layout = go.Layout(
            width=800,
            height=500,
            title="fixed-ratio axes",
            xaxis=dict(
                nticks=10,
                domain=[0, 0.45],
                title="shared X axis"
            ),
            yaxis=dict(
                scaleanchor="x",
                domain=[0, 0.45],
                title="1:1"
            ),
            yaxis2=dict(
                scaleanchor="x",
                scaleratio=0.2,
                domain=[0.55, 1],
                title="1:5"
            ),
            xaxis2=dict(
                type="log",
                domain=[0.55, 1],
                anchor="y3",
                title="unconstrained log X"
            ),
            yaxis3=dict(
                domain=[0, 0.45],
                anchor="x2",
                title="Scale matches ->"
            ),
            yaxis4=dict(
                scaleanchor="y3",
                domain=[0.55, 1],
                anchor="x2",
                title="Scale matches <-"
            ),
            showlegend=False
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Reversed Axes
    if __name__ == '__main__':
        data = [
            go.Scatter(
                x=[1, 2],
                y=[1, 2]
            )
        ]
        layout = go.Layout(
            xaxis=dict(
                autorange='reversed'
            )
        )
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Reversed Axes with Range ( Min/Max ) Specified
    if __name__ == '__main__':
        import numpy as np

        x = np.linspace(0, 10, 100)
        y = np.random.randint(1, 100, 100)

        trace = go.Scatter(x=x, y=y, mode='markers')
        data = [trace]
        layout = go.Layout(title='Reversed Axis with Min/Max', xaxis=dict(range=[10, 0]))

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # nonnegative, tozero, and normal Rangemode
    if __name__ == '__main__':
        data = [
            go.Scatter(
                x=[2, 4, 6],
                y=[-3, 0, 3]
            )
        ]
        layout = go.Layout(
            showlegend=False,
            xaxis=dict(
                rangemode='tozero',
                autorange=True
            ),
            yaxis=dict(
                rangemode='nonnegative',
                autorange=True
            )
        )
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Enumerated Ticks with Tickvals and Ticktext
    if __name__ == '__main__':
        import pandas as pd

        # get and filter apple data
        apple_df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
        apple_df_2016 = apple_df[apple_df.Date < '2017'][apple_df.Date > '2016']

        # get clean and filter tesla data
        tesla_df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/tesla-stock-price.csv')
        tesla_df.date = pd.to_datetime(tesla_df.date)
        tesla_df_2016 = tesla_df[tesla_df.date < '2017'][tesla_df.date > '2016']

        # set x-axis labels and their corresponding data values
        labels = ['End of Q1', 'End of Q2', 'End of Q3', 'End of Q4']
        tickvals = ['2016-04-01', '2016-07-01', '2016-10-01', apple_df_2016.Date.max()]

        data = [
            go.Scatter(
                x=apple_df_2016.Date,
                y=apple_df_2016['AAPL.High'],
                name='Apple',
                marker=dict(color='#851e52'),
            ),
            go.Scatter(
                x=tesla_df_2016.date,
                y=tesla_df_2016.high,
                name='Tesla',
                yaxis='y2',
                marker=dict(color='#d3560e'),
            ),
        ]

        layout = go.Layout(
            title='2016 Quarterly Stock Trends',
            xaxis=go.layout.XAxis(
                ticktext=labels,
                tickvals=tickvals
            ),
            yaxis2=dict(
                overlaying='y',
                side='right',
                showgrid=False,
            )
        )
        fig = go.Figure(data, layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)


# 6 Horizontal Legends in Python
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    # Horizontal Legend
    if __name__ == '__main__':
        import numpy as np

        trace1 = go.Scatter(
            x=np.random.randn(75),
            mode='markers',
            name="Plot1",
            marker=dict(
                size=16,
                color='rgba(152, 0, 0, .8)'
            ))
        trace2 = go.Scatter(
            x=np.random.randn(75),
            mode='markers',
            name="Plot2",
            marker=dict(
                size=16,
                color='rgba(0, 152, 0, .8)'
            ))
        trace3 = go.Scatter(
            x=np.random.randn(75),
            mode='markers',
            name="Plot3",
            marker=dict(
                size=16,
                color='rgba(0, 0, 152, .8)'
            ))

        data = [trace1, trace2, trace3]
        layout = go.Layout(
            legend=dict(
                orientation="h")
        )
        figure = go.Figure(data=data, layout=layout)
        py.plot(figure, filename='tmp/layout_tutorial.html', auto_play=True)


# 7 Legends in Python
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    # Show Legend
    if __name__ == '__main__':
        trace0 = go.Scatter(
            x=[1, 2, 3, 4, 5],
            y=[1, 2, 3, 4, 5],
        )

        trace1 = go.Scatter(
            x=[1, 2, 3, 4, 5],
            y=[5, 4, 3, 2, 1],
        )

        data = [trace0, trace1]
        fig = go.Figure(data=data)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    #
    if __name__ == '__main__':
        trace0 = go.Scatter(
            x=[1, 2, 3, 4, 5],
            y=[1, 2, 3, 4, 5],
        )

        data = [trace0]
        layout = go.Layout(showlegend=True)
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Hide Legend
    if __name__ == '__main__':
        trace0 = go.Scatter(
            x=[1, 2, 3, 4, 5],
            y=[1, 2, 3, 4, 5],
        )

        trace1 = go.Scatter(
            x=[1, 2, 3, 4, 5],
            y=[5, 4, 3, 2, 1],
        )

        data = [trace0, trace1]
        layout = go.Layout(showlegend=False)
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Hide Legend Entries
    if __name__ == '__main__':
        trace0 = go.Scatter(
            x=[1, 2, 3, 4, 5],
            y=[1, 2, 3, 4, 5],
            showlegend=False
        )

        trace1 = go.Scatter(
            x=[1, 2, 3, 4, 5],
            y=[5, 4, 3, 2, 1],
        )

        data = [trace0, trace1]
        fig = go.Figure(data=data)

        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Legend Names
    if __name__ == '__main__':
        trace0 = go.Scatter(
            x=[1, 2, 3, 4, 5],
            y=[1, 2, 3, 4, 5],
            name='Positive'
        )

        trace1 = go.Scatter(
            x=[1, 2, 3, 4, 5],
            y=[5, 4, 3, 2, 1],
            name='Negative'
        )

        data = [trace0, trace1]
        fig = go.Figure(data=data)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Horizontal Legend
    if __name__ == '__main__':
        trace0 = go.Scatter(
            x=[1, 2, 3, 4, 5],
            y=[1, 2, 3, 4, 5],
        )

        trace1 = go.Scatter(
            x=[1, 2, 3, 4, 5],
            y=[5, 4, 3, 2, 1],
        )

        data = [trace0, trace1]
        layout = go.Layout(
            legend=dict(orientation="h")
        )
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Legend Position
    if __name__ == '__main__':
        trace0 = go.Scatter(
            x=[1, 2, 3, 4, 5],
            y=[1, 2, 3, 4, 5],
        )

        trace1 = go.Scatter(
            x=[1, 2, 3, 4, 5],
            y=[5, 4, 3, 2, 1],
        )

        data = [trace0, trace1]
        layout = go.Layout(
            legend=dict(x=-.1, y=1.2)
        )
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Style Legend
    if __name__ == '__main__':
        trace0 = go.Scatter(
            x=[1, 2, 3, 4, 5],
            y=[1, 2, 3, 4, 5],
        )

        trace1 = go.Scatter(
            x=[1, 2, 3, 4, 5],
            y=[5, 4, 3, 2, 1],
        )
        data = [trace0, trace1]

        layout = go.Layout(
            legend=dict(
                x=0,
                y=1,
                traceorder='normal',
                font=dict(
                    family='sans-serif',
                    size=12,
                    color='#000'
                ),
                bgcolor='#E2E2E2',
                bordercolor='#FFFFFF',
                borderwidth=2
            )
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    # Grouped Legend
    if __name__ == '__main__':
        data = [
            {
                'x': [1, 2, 3],
                'y': [2, 1, 3],
                'legendgroup': 'group',  # this can be any string, not just "group"
                'name': 'first legend group',
                'mode': 'markers',
                'marker': {
                    'color': 'rgb(164, 194, 244)'
                }
            },
            {
                'x': [1, 2, 3],
                'y': [2, 2, 2],
                'legendgroup': 'group',
                'name': 'first legend group - average',
                'mode': 'lines',
                'line': {
                    'color': 'rgb(164, 194, 244)'
                }
            },
            {
                'x': [1, 2, 3],
                'y': [4, 9, 2],
                'legendgroup': 'group2',
                'name': 'second legend group',
                'mode': 'markers',
                'marker': {
                    'color': 'rgb(142, 124, 195)'
                }
            },
            {
                'x': [1, 2, 3],
                'y': [5, 5, 5],
                'legendgroup': 'group2',
                'name': 'second legend group - average',
                'mode': 'lines',
                'line': {
                    'color': 'rgb(142, 124, 195)'
                }
            }
        ]
        py.plot(data, filename='tmp/layout_tutorial.html', auto_play=True)

    # You can also hide entries in grouped legends:
    if __name__ == '__main__':
        data = [
            {
                'x': [1, 2, 3],
                'y': [2, 1, 3],
                'legendgroup': 'group',
                'name': 'first legend group',
                'mode': 'markers',
                'marker': {
                    'color': 'rgb(164, 194, 244)'
                }
            },
            {
                'x': [1, 2, 3],
                'y': [2, 2, 2],
                'legendgroup': 'group',
                'name': 'first legend group - average',
                'mode': 'lines',
                'line': {
                    'color': 'rgb(164, 194, 244)'
                },
                'showlegend': False
            },
            {
                'x': [1, 2, 3],
                'y': [4, 9, 2],
                'legendgroup': 'group2',
                'name': 'second legend group',
                'mode': 'markers',
                'marker': {
                    'color': 'rgb(142, 124, 195)'
                }
            },
            {
                'x': [1, 2, 3],
                'y': [5, 5, 5],
                'legendgroup': 'group2',
                'name': 'second legend group - average',
                'mode': 'lines',
                'line': {
                    'color': 'rgb(142, 124, 195)'
                },
                'showlegend': False
            }
        ]
        py.plot(data, filename='tmp/layout_tutorial.html', auto_play=True)


# 8 3D Surface Lighting in Python
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    # Lighting effects on 3D Surface Plot
    if __name__ == '__main__':
        import plotly.tools as tls
        import numpy as np

        x = np.linspace(-np.pi, np.pi, 100)
        y = np.linspace(-np.pi, np.pi, 100)

        Y, X = np.meshgrid(x, y)
        Z1 = np.cos(X) * np.sin(Y)
        Z2 = 2 + np.cos(X) * np.sin(Y)
        trace1 = go.Surface(z=Z1, colorscale='Viridis')
        py.plot([trace1], filename='tmp/layout_tutorial.html', auto_play=True)


# 10 Hover Text and Formatting in Python
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    # Add Hover Text
    if __name__ == '__main__':
        data = [
            go.Scatter(
                x=[1, 2, 3, 4, 5],
                y=[2, 1, 6, 4, 4],
                text=["Text A", "Text B", "Text C", "Text D", "Text E"],
                hoverinfo='text',
                marker=dict(
                    color='green'
                ),
                showlegend=False
            )
        ]
        py.plot(data, filename='tmp/layout_tutorial.html', auto_play=True)

    # Format Hover Text
    if __name__ == '__main__':
        data = [
            go.Scatter(
                x=[1, 2, 3, 4, 5],
                y=[2.02825, 1.63728, 6.83839, 4.8485, 4.73463],
                hoverinfo='y',
                marker=dict(
                    color='green'
                ),
                showlegend=False
            )
        ]

        layout = go.Layout(
            title="Set hover text formatting<br><a href= https://github.com/d3/d3-time-format/blob/master/README.md#locale_format>https://github.com/d3/d3-time-format/blob/master/README.md#locale_format</a>",
            titlefont=dict(
                size=10
            ),
            xaxis=dict(
                zeroline=False
            ),
            yaxis=dict(
                hoverformat='.2f'
            )
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    #
    if __name__ == '__main__':
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

    #
    if __name__ == '__main__':
        py.plot(fig, filename='tmp/layout_tutorial.html', auto_play=True)

