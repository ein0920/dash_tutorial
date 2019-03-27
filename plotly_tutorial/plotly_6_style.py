
# 1、Text and Annotations
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    # Adding Text to Data in Line and Scatter Plots
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[0, 1, 2],
            y=[1, 1, 1],
            mode='lines+markers+text',
            name='Lines, Markers and Text',
            text=['Text A', 'Text B', 'Text C'],
            textposition='top center'  # 显示text，不然就不显示
        )

        trace2 = go.Scatter(
            x=[0, 1, 2],
            y=[2, 2, 2],
            mode='markers+text',
            name='Markers and Text',
            text=['Text D', 'Text E', 'Text F'],
            textposition='bottom center'
        )

        trace3 = go.Scatter(
            x=[0, 1, 2],
            y=[3, 3, 3],
            mode='lines+text',
            name='Lines and Text',
            text=['Text G', 'Text H', 'Text I'],
            textposition='bottom center'
        )

        data = [trace1, trace2, trace3]

        layout = go.Layout(
            showlegend=False
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)

    # Adding Hover Text to Data in Line and Scatter Plots
    if __name__ == '__main__':
        data = [
            go.Scatter(
                x=[0, 1, 2],
                y=[1, 3, 2],
                mode='markers',
                text=['Text A', 'Text B', 'Text C']
            )
        ]

        layout = go.Layout(
            title='Hover over the points to see the text'
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)

    # Simple Annotation
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            y=[0, 1, 3, 2, 4, 3, 4, 6, 5]
        )

        trace2 = go.Scatter(
            x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            y=[0, 4, 5, 1, 2, 2, 3, 4, 2]
        )

        data = [trace1, trace2]

        layout = go.Layout(
            showlegend=False,
            annotations=[
                dict(
                    x=2,
                    y=5,
                    xref='x',
                    yref='y',
                    text='dict Text',
                    showarrow=True,
                    arrowhead=7,
                    ax=0,
                    ay=-40
                )
            ]
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)

    # Multiple Annotations
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            y=[0, 1, 3, 2, 4, 3, 4, 6, 5]
        )

        trace2 = go.Scatter(
            x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            y=[0, 4, 5, 1, 2, 2, 3, 4, 2]
        )

        data = [trace1, trace2]

        layout = go.Layout(
            showlegend=False,
            annotations=[
                dict(
                    x=2,
                    y=5,
                    xref='x',
                    yref='y',
                    text='dict Text',
                    showarrow=True,
                    arrowhead=7,
                    ax=0,
                    ay=-40
                ),
                dict(
                    x=4,
                    y=4,
                    xref='x',
                    yref='y',
                    text='dict Text 2',
                    showarrow=True,
                    arrowhead=7,
                    ax=0,
                    ay=-40
                )
            ]
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)

    # 3D Annotations
    if __name__ == '__main__':
        data = [go.Scatter3d(
            x=["2017-01-01", "2017-02-10", "2017-03-20"],
            y=["A", "B", "C"],
            z=[1, 1000, 100000],
            name="z",
        )]

        layout = go.Layout(
            scene=dict(
                aspectratio=dict(
                    x=1,
                    y=1,
                    z=1
                ),
                camera=dict(
                    center=dict(
                        x=0,
                        y=0,
                        z=0
                    ),
                    eye=dict(
                        x=1.96903462608,
                        y=-1.09022831971,
                        z=0.405345349304
                    ),
                    up=dict(
                        x=0,
                        y=0,
                        z=1
                    )
                ),
                dragmode="turntable",
                xaxis=dict(
                    title="",
                    type="date"
                ),
                yaxis=dict(
                    title="",
                    type="category"
                ),
                zaxis=dict(
                    title="",
                    type="log"
                ),
                annotations=[dict(
                    showarrow=False,
                    x="2017-01-01",
                    y="A",
                    z=0,
                    text="Point 1",
                    xanchor="left",
                    xshift=10,
                    opacity=0.7
                ), dict(
                    x="2017-02-10",
                    y="B",
                    z=4,
                    text="Point 2",
                    textangle=0,
                    ax=0,
                    ay=-75,
                    font=dict(
                        color="black",
                        size=12
                    ),
                    arrowcolor="black",
                    arrowsize=3,
                    arrowwidth=1,
                    arrowhead=1
                ), dict(
                    x="2017-03-20",
                    y="C",
                    z=5,
                    ax=50,
                    ay=0,
                    text="Point 3",
                    arrowhead=1,
                    xanchor="left",
                    yanchor="bottom"
                )]
            ),
            xaxis=dict(title="x"),
            yaxis=dict(title="y")
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)

    # Custom Text Color and Styling
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[0, 1, 2],
            y=[1, 1, 1],
            mode='lines+markers+text',
            name='Lines, Markers and Text',
            text=['Text A', 'Text B', 'Text C'],
            textposition='top right',
            textfont=dict(
                family='sans serif',
                size=18,
                color='#1f77b4'
            )
        )

        trace2 = go.Scatter(
            x=[0, 1, 2],
            y=[2, 2, 2],
            mode='lines+markers+text',
            name='Lines and Text',
            text=['Text G', 'Text H', 'Text I'],
            textposition='bottom center',
            textfont=dict(
                family='sans serif',
                size=18,
                color='#ff7f0e'
            )
        )

        data = [trace1, trace2]

        layout = go.Layout(
            showlegend=False
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)

    # Styling and Coloring Annotations
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            y=[0, 1, 3, 2, 4, 3, 4, 6, 5]
        )

        trace2 = go.Scatter(
            x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            y=[0, 4, 5, 1, 2, 2, 3, 4, 2]
        )

        data = [trace1, trace2]

        layout = go.Layout(
            showlegend=False,
            annotations=[
                dict(
                    x=2,
                    y=5,
                    xref='x',
                    yref='y',
                    text='max=5',
                    showarrow=True,
                    font=dict(
                        family='Courier New, monospace',
                        size=16,
                        color='#ffffff'
                    ),
                    align='center',
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=2,
                    arrowcolor='#636363',
                    ax=20,
                    ay=-30,
                    bordercolor='#c7c7c7',
                    borderwidth=2,
                    borderpad=4,
                    bgcolor='#ff7f0e',
                    opacity=0.8
                )
            ]
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)

    # Disabling Hover Text
    if __name__ == '__main__':
        trace = dict(
            x=[1, 2, 3, ],
            y=[10, 30, 15],
            type='scatter',
            name='first trace',
            hoverinfo='none'
        )
        py.plot([trace], filename='tmp/style_tutorial.html', auto_play=True)

    # Text Font as an Array - Styling Each Text Element
    if __name__ == '__main__':
        fig = go.Figure(
            data=[
                go.Scattergeo(
                    lat=[45.5, 43.4, 49.13, 51.1, 53.34, 45.24, 44.64, 48.25, 49.89, 50.45],
                    lon=[-73.57, -79.24, -123.06, -114.1, -113.28, -75.43, -63.57, -123.21, -97.13, -104.6],
                    marker={
                        "color": ["#bebada", "#fdb462", "#fb8072", "#d9d9d9", "#bc80bd", "#b3de69", "#8dd3c7",
                                  "#80b1d3", "#fccde5", "#ffffb3"],
                        "line": {
                            "width": 1
                        },
                        "size": 10
                    },
                    mode="markers+text",
                    name="",
                    text=["Montreal", "Toronto", "Vancouver", "Calgary", "Edmonton", "Ottawa", "Halifax", "Victoria",
                          "Winnepeg", "Regina"],
                    textfont={
                        "color": ["#bebada", "#fdb462", "#fb8072", "#d9d9d9", "#bc80bd", "#b3de69", "#8dd3c7",
                                  "#80b1d3", "#fccde5", "#ffffb3"],
                        "family": ["Arial, sans-serif", "Balto, sans-serif", "Courier New, monospace",
                                   "Droid Sans, sans-serif", "Droid Serif, serif", "Droid Sans Mono, sans-serif",
                                   "Gravitas One, cursive", "Old Standard TT, serif", "Open Sans, sans-serif",
                                   "PT Sans Narrow, sans-serif", "Raleway, sans-serif",
                                   "Times New Roman, Times, serif"],
                        "size": [22, 21, 20, 19, 18, 17, 16, 15, 14, 13]
                    },
                    textposition=["top center", "middle left", "top center", "bottom center", "top right",
                                  "middle left", "bottom right", "bottom left", "top right", "top right"]
                )
            ],
            layout={
                "title": "Canadian cities",
                "geo": {
                    "lataxis": {
                        "range": [40, 70]
                    },
                    "lonaxis": {
                        "range": [-130, -55]
                    },
                    "scope": "north america"
                }
            }
        )
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)

    # Adding Annotations with xref and yref as Paper
    if __name__ == '__main__':
        data = [
            go.Scatter(
                x=[1, 2, 3],
                y=[1, 2, 3],
                name='y',
            )
        ]

        layout = go.Layout(
            annotations=[
                dict(
                    x=0.5004254919715793,
                    y=-0.16191064079952971,
                    showarrow=False,
                    text='Custom x-axis title',
                    xref='paper',
                    yref='paper'
                ),
                dict(
                    x=-0.04944728761514841,
                    y=0.4714285714285711,
                    showarrow=False,
                    text='Custom y-axis title',
                    textangle=-90,
                    xref='paper',
                    yref='paper'
                )
            ],
            autosize=True,
            margin=dict(
                b=100
            ),
            title='Plot Title',
            xaxis=dict(
                autorange=False,
                range=[-0.05674507980728292, -0.0527310420933204],
                type='linear'
            ),
            yaxis=dict(
                autorange=False,
                range=[1.2876210047544652, 1.2977732997811402],
                type='linear'
            ),
            height=550,
            width=1137
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)


# 2、WebGL Text and Annotations in Python
if __name__ == '__main__':
    import numpy as np
    import plotly.offline as py
    import plotly.graph_objs as go
    from plotly.figure_factory import create_annotated_heatmap

    # Heatmap with Annotations
    if __name__ == '__main__':
        n = 250

        y = [[i] * n for i in range(12)]
        y = [item for sublist in y for item in sublist]

        trace = dict(type='heatmap', z=np.random.randint(1, 10, (12, n)), colorscale='Viridis')
        data = [trace]

        # Here's the key part - Scattergl text!

        data.append({'type': 'scattergl',
                     'mode': 'text',
                     'x': list(range(n)) * 12,
                     'y': y,
                     'text': np.random.choice(list('ATGC'), 12 * 250),
                     'textfont': {
                         'size': 20
                     }})

        steps = [{'args': ['xaxis', {'range': [-0.5 + e, 30.5 + e]}], 'method': 'relayout'} for e in range(n - 30)]

        sliders = [dict(
            active=0,
            steps=steps
        )]

        layout = dict(sliders=sliders)
        layout['xaxis'] = {'range': [-0.5, 30.5]}

        fig = dict(data=data, layout=layout)
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True, validate=False)


# 3、Text and Font Styling in Python
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    # Global Font Properties
    if __name__ == '__main__':
        data = [
            go.Scatter(
                x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
                y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
            )
        ]
        layout = go.Layout(
            title='Global Font',
            font=dict(family='Courier New, monospace', size=18, color='#7f7f7f')
        )
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)


# 4、Add a Background Image
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go
    import numpy as np

    # Add a Background Image
    if __name__ == '__main__':
        trace1 = go.Scatter(x=[0, 0.5, 1, 2, 2.2], y=[1.23, 2.5, 0.42, 3, 1])
        layout = go.Layout(images=[dict(
            source="https://images.plot.ly/language-icons/api-home/python-logo.png",
            xref="x",
            yref="y",
            x=0,
            y=3,
            sizex=2,
            sizey=2,
            sizing="stretch",
            opacity=0.5,
            layer="below")])
        fig = go.Figure(data=[trace1], layout=layout)
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)

    # Add a Logo
    if __name__ == '__main__':
        data = [
            go.Bar(
                x=['-35.3', '-15.9', '-15.8', '-15.6', '-11.1',
                   '-9.6', '-9.2', '-3.5', '-1.9', '-0.9',
                   '1.0', '1.4', '1.7', '2.0', '2.8', '6.2',
                   '8.1', '8.5', '8.5', '8.6', '11.4', '12.5',
                   '13.3', '13.7', '14.4', '17.5', '17.7',
                   '18.9', '25.1', '28.9', '41.4'],
                y=['Designers, musicians, artists, etc.',
                   'Secretaries and administrative assistants',
                   'Waiters and servers', 'Archivists, curators, and librarians',
                   'Sales and related', 'Childcare workers, home car workers, etc.',
                   'Food preparation occupations', 'Janitors, maids, etc.',
                   'Healthcare technicians, assistants. and aides',
                   'Counselors, social and religious workers',
                   'Physical, life and social scientists', 'Construction',
                   'Factory assembly workers', 'Machinists, repairmen, etc.',
                   'Media and communications workers', 'Teachers',
                   'Mechanics, repairmen, etc.', 'Financial analysts and advisers',
                   'Farming, fishing and forestry workers',
                   'Truck drivers, heavy equipment operator, etc.', 'Accountants and auditors',
                   'Human resources, management analysts, etc.', 'Managers',
                   'Lawyers and judges', 'Engineers, architects and surveyors',
                   'Nurses', 'Legal support workers',
                   'Computer programmers and system admin.', 'Police officers and firefighters',
                   'Chief executives', 'Doctors, dentists and surgeons'],
                marker=dict(
                    color='rgb(253, 240, 54)',
                    line=dict(color='rgb(0, 0, 0)',
                              width=2)
                ),
                orientation='h',
            )
        ]

        layout = go.Layout(
            images=[dict(
                source="https://raw.githubusercontent.com/cldougl/plot_images/add_r_img/vox.png",
                xref="paper", yref="paper",
                x=1, y=1.05,
                sizex=0.2, sizey=0.2,
                xanchor="right", yanchor="bottom"
            )],
            autosize=False, height=800, width=700,
            bargap=0.15, bargroupgap=0.1,
            barmode='stack', hovermode='x',
            margin=dict(r=20, l=300,
                        b=75, t=125),
            title='Moving Up, Moving Down<br><i>Percentile change in income between childhood and adulthood</i>',
            xaxis=dict(
                dtick=10, nticks=0,
                gridcolor='rgba(102, 102, 102, 0.4)',
                linecolor='#000', linewidth=1,
                mirror=True,
                showticklabels=True, tick0=0, tickwidth=1,
                title='<i>Change in percentile</i>',
            ),
            yaxis=dict(
                anchor='x',
                gridcolor='rgba(102, 102, 102, 0.4)', gridwidth=1,
                linecolor='#000', linewidth=1,
                mirror=True, showgrid=False,
                showline=True, zeroline=False,
                showticklabels=True, tick0=0,
                type='category',
            )
        )
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)

    # Label Spectroscopy Data by Adding Multiple Images
    if __name__ == '__main__':
        from scipy.signal import savgol_filter


        # simulate spectroscopy data
        def simulated_absorption(mu, sigma, intensity):
            data = [np.random.normal(mu[i], sigma[i], intensity[i]) for i in range(len(mu))]
            hists = [np.histogram(d, 1000, range=(200, 500), normed=True) for d in data]
            ys = [y for y, x in hists]
            s = savgol_filter(np.max(ys, axis=0), 41, 3)
            return hists[0][1], s


        mus = [[290, 240, 260], [330, 350]]
        sigmas = [[4, 6, 10], [5, 4]]
        intensities = [[100000, 300000, 700000], [40000, 20000]]

        simulated_absorptions = [simulated_absorption(m, s, i) for m, s, i in zip(mus, sigmas, intensities)]

        # create traces from data
        names = ['Benzene', 'Naphthalene']
        colors = ['red', 'maroon']
        traces = [go.Scatter(x=x, y=y, name=n, line=dict(color=c)) for (x, y), n, c in
                  zip(simulated_absorptions, names, colors)]

        # add pictures using layout-images and then connect the image to its trace using annotations
        layout = go.Layout(
            images=[dict(
                source="https://raw.githubusercontent.com/michaelbabyn/plot_data/master/benzene.png",
                xref="paper",
                yref="paper",
                x=0.75,
                y=0.65,
                sizex=0.3,
                sizey=0.3,
                xanchor="right",
                yanchor="bottom"
            ), dict(
                source="https://raw.githubusercontent.com/michaelbabyn/plot_data/master/naphthalene.png",
                xref="paper",
                yref="paper",
                x=0.9,
                y=0.3,
                sizex=0.3,
                sizey=0.3,

                xanchor="right",
                yanchor="bottom"
            )
            ],
            annotations=[
                dict(
                    x=93.0 / 300,
                    y=0.07 / 0.1,
                    xref='paper',
                    yref='paper',
                    showarrow=True,
                    arrowhead=0,
                    opacity=0.5,
                    ax=250,
                    ay=-40,
                ),
                dict(
                    x=156 / 300,
                    y=0.04 / 0.1,
                    xref='paper',
                    yref='paper',
                    showarrow=True,
                    arrowhead=0,
                    opacity=0.5,
                    ax=140,
                    ay=-10,
                )
            ],
            title='Absorption Frequencies of Benzene and Naphthalene',
            yaxis=dict(hoverformat='.3f', title='Absorption'),
            xaxis=dict(title='Wavelength'),
            showlegend=False,
            height=500,
            width=900

        )

        fig = go.Figure(data=traces, layout=layout)
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)

    # Zoom on Static Images
    if __name__ == '__main__':
        img_width = 1600
        img_height = 900
        scale_factor = 0.5

        layout = go.Layout(
            xaxis=go.layout.XAxis(
                visible=False,
                range=[0, img_width * scale_factor]),
            yaxis=go.layout.YAxis(
                visible=False,
                range=[0, img_height * scale_factor],
                # the scaleanchor attribute ensures that the aspect ratio stays constant
                scaleanchor='x'),
            width=img_width * scale_factor,
            height=img_height * scale_factor,
            margin={'l': 0, 'r': 0, 't': 0, 'b': 0},
            images=[go.layout.Image(
                x=0,
                sizex=img_width * scale_factor,
                y=img_height * scale_factor,
                sizey=img_height * scale_factor,
                xref="x",
                yref="y",
                opacity=1.0,
                layer="below",
                sizing="stretch",
                source='https://raw.githubusercontent.com/michaelbabyn/plot_data/master/bridge.jpg')]
        )
        # we add a scatter trace with data points in opposite corners to give the Autoscale feature a reference point
        fig = go.Figure(data=[{
            'x': [0, img_width * scale_factor],
            'y': [0, img_height * scale_factor],
            'mode': 'markers',
            'marker': {'opacity': 0}}], layout=layout)
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)


# 5、Shapes in Python
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    # Vertical and Horizontal Lines Positioned Relative to the Axes
    if __name__ == '__main__':
        trace0 = go.Scatter(
            x=[2, 3.5, 6],
            y=[1, 1.5, 1],
            text=['Vertical Line', 'Horizontal Dashed Line', 'Diagonal dotted Line'],
            mode='text',
        )
        data = [trace0]
        layout = {
            'xaxis': {
                'range': [0, 7]
            },
            'yaxis': {
                'range': [0, 2.5]
            },
            'shapes': [
                # Line Vertical
                {
                    'type': 'line',
                    'x0': 1,
                    'y0': 0,
                    'x1': 1,
                    'y1': 2,
                    'line': {
                        'color': 'rgb(55, 128, 191)',
                        'width': 3,
                    },
                },
                # Line Horizontal
                {
                    'type': 'line',
                    'x0': 2,
                    'y0': 2,
                    'x1': 5,
                    'y1': 2,
                    'line': {
                        'color': 'rgb(50, 171, 96)',
                        'width': 4,
                        'dash': 'dashdot',
                    },
                },
                # Line Diagonal
                {
                    'type': 'line',
                    'x0': 4,
                    'y0': 0,
                    'x1': 6,
                    'y1': 2,
                    'line': {
                        'color': 'rgb(128, 0, 128)',
                        'width': 4,
                        'dash': 'dot',
                    },
                },
            ]
        }

        fig = {
            'data': data,
            'layout': layout,
        }
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)

    # Lines Positioned Relative to the Plot & to the Axes
    if __name__ == '__main__':
        trace0 = go.Scatter(
            x=[2, 6],
            y=[1, 1],
            text=['Line positioned relative to the plot',
                  'Line positioned relative to the axes'],
            mode='text',
        )
        data = [trace0]
        layout = {
            'xaxis': {
                'range': [0, 8]
            },
            'yaxis': {
                'range': [0, 2]
            },
            'shapes': [
                # Line reference to the axes
                {
                    'type': 'line',
                    'xref': 'x',
                    'yref': 'y',
                    'x0': 4,
                    'y0': 0,
                    'x1': 8,
                    'y1': 1,
                    'line': {
                        'color': 'rgb(55, 128, 191)',
                        'width': 3,
                    },
                },
                # Line reference to the plot
                {
                    'type': 'line',
                    'xref': 'paper',
                    'yref': 'paper',
                    'x0': 0,
                    'y0': 0,
                    'x1': 0.5,
                    'y1': 0.5,
                    'line': {
                        'color': 'rgb(50, 171, 96)',
                        'width': 3,
                    },
                },
            ]
        }
        fig = {
            'data': data,
            'layout': layout,
        }
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)

    # Creating Tangent Lines with Shapes
    if __name__ == '__main__':
        import numpy as np

        x0 = np.linspace(1, 3, 200)
        y0 = x0 * np.sin(np.power(x0, 2)) + 1

        trace0 = go.Scatter(
            x=x0,
            y=y0,
        )
        data = [trace0]
        layout = {
            'title': "$f(x)=x\\sin(x^2)+1\\\\ f\'(x)=\\sin(x^2)+2x^2\\cos(x^2)$",
            'shapes': [
                {
                    'type': 'line',
                    'x0': 1,
                    'y0': 2.30756,
                    'x1': 1.75,
                    'y1': 2.30756,
                    'opacity': 0.7,
                    'line': {
                        'color': 'red',
                        'width': 2.5,
                    },
                },
                {
                    'type': 'line',
                    'x0': 2.5,
                    'y0': 3.80796,
                    'x1': 3.05,
                    'y1': 3.80796,
                    'opacity': 0.7,
                    'line': {
                        'color': 'red',
                        'width': 2.5,
                    },
                },
                {
                    'type': 'line',
                    'x0': 1.90,
                    'y0': -1.1827,
                    'x1': 2.50,
                    'y1': -1.1827,
                    'opacity': 0.7,
                    'line': {
                        'color': 'red',
                        'width': 2.5,
                    },
                },
            ]
        }
        fig = {
            'data': data,
            'layout': layout,
        }
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)

    # Rectangles Positioned Relative to the Axes
    if __name__ == '__main__':
        trace0 = go.Scatter(
            x=[1.5, 4.5],
            y=[0.75, 0.75],
            text=['Unfilled Rectangle', 'Filled Rectangle'],
            mode='text',
        )
        data = [trace0]
        layout = {
            'xaxis': {
                'range': [0, 7],
                'showgrid': False,
            },
            'yaxis': {
                'range': [0, 3.5]
            },
            'shapes': [
                # unfilled Rectangle
                {
                    'type': 'rect',
                    'x0': 1,
                    'y0': 1,
                    'x1': 2,
                    'y1': 3,
                    'line': {
                        'color': 'rgba(128, 0, 128, 1)',
                    },
                },
                # filled Rectangle
                {
                    'type': 'rect',
                    'x0': 3,
                    'y0': 1,
                    'x1': 6,
                    'y1': 2,
                    'line': {
                        'color': 'rgba(128, 0, 128, 1)',
                        'width': 2,
                    },
                    'fillcolor': 'rgba(128, 0, 128, 0.7)',
                },
            ]
        }
        fig = {
            'data': data,
            'layout': layout,
        }
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)

    # Rectangle Positioned Relative to the Plot & to the Axes
    if __name__ == '__main__':
        trace0 = go.Scatter(
            x=[1.5, 3],
            y=[2.5, 2.5],
            text=['Rectangle reference to the plot',
                  'Rectangle reference to the axes'],
            mode='text',
        )
        data = [trace0]
        layout = {
            'xaxis': {
                'range': [0, 4],
                'showgrid': False,
            },
            'yaxis': {
                'range': [0, 4]
            },
            'shapes': [
                # Rectangle reference to the axes
                {
                    'type': 'rect',
                    'xref': 'x',
                    'yref': 'y',
                    'x0': 2.5,
                    'y0': 0,
                    'x1': 3.5,
                    'y1': 2,
                    'line': {
                        'color': 'rgb(55, 128, 191)',
                        'width': 3,
                    },
                    'fillcolor': 'rgba(55, 128, 191, 0.6)',
                },
                # Rectangle reference to the plot
                {
                    'type': 'rect',
                    'xref': 'paper',
                    'yref': 'paper',
                    'x0': 0.25,
                    'y0': 0,
                    'x1': 0.5,
                    'y1': 0.5,
                    'line': {
                        'color': 'rgb(50, 171, 96)',
                        'width': 3,
                    },
                    'fillcolor': 'rgba(50, 171, 96, 0.6)',
                },
            ]
        }
        fig = {
            'data': data,
            'layout': layout,
        }
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)

    # Highlighting Time Series Regions with Rectangle Shapes
    if __name__ == '__main__':
        trace0 = go.Scatter(
            x=['2015-02-01', '2015-02-02', '2015-02-03', '2015-02-04', '2015-02-05',
               '2015-02-06', '2015-02-07', '2015-02-08', '2015-02-09', '2015-02-10',
               '2015-02-11', '2015-02-12', '2015-02-13', '2015-02-14', '2015-02-15',
               '2015-02-16', '2015-02-17', '2015-02-18', '2015-02-19', '2015-02-20',
               '2015-02-21', '2015-02-22', '2015-02-23', '2015-02-24', '2015-02-25',
               '2015-02-26', '2015-02-27', '2015-02-28'],
            y=[-14, -17, -8, -4, -7, -10, -12, -14, -12, -7, -11, -7, -18, -14, -14,
               -16, -13, -7, -8, -14, -8, -3, -9, -9, -4, -13, -9, -6],
            mode='lines',
            name='temperature'
        )
        data = [trace0]
        layout = {
            # to highlight the timestamp we use shapes and create a rectangular
            'shapes': [
                # 1st highlight during Feb 4 - Feb 6
                {
                    'type': 'rect',
                    # x-reference is assigned to the x-values
                    'xref': 'x',
                    # y-reference is assigned to the plot paper [0,1]
                    'yref': 'paper',
                    'x0': '2015-02-04',
                    'y0': 0,
                    'x1': '2015-02-06',
                    'y1': 1,
                    'fillcolor': '#d3d3d3',
                    'opacity': 0.2,
                    'line': {
                        'width': 0,
                    }
                },
                # 2nd highlight during Feb 20 - Feb 23
                {
                    'type': 'rect',
                    'xref': 'x',
                    'yref': 'paper',
                    'x0': '2015-02-20',
                    'y0': 0,
                    'x1': '2015-02-22',
                    'y1': 1,
                    'fillcolor': '#d3d3d3',
                    'opacity': 0.2,
                    'line': {
                        'width': 0,
                    }
                }
            ]
        }
        py.plot({'data': data, 'layout': layout}, filename='tmp/style_tutorial.html', auto_play=True)

    # Circles Positioned Relative to the Axes
    if __name__ == '__main__':
        trace0 = go.Scatter(
            x=[1.5, 3.5],
            y=[0.75, 2.5],
            text=['Unfilled Circle',
                  'Filled Circle'],
            mode='text',
        )
        data = [trace0]

        layout = {
            'xaxis': {
                'range': [0, 4.5],
                'zeroline': False,
            },
            'yaxis': {
                'range': [0, 4.5]
            },
            'width': 800,
            'height': 800,
            'shapes': [
                # unfilled circle
                {
                    'type': 'circle',
                    'xref': 'x',
                    'yref': 'y',
                    'x0': 1,
                    'y0': 1,
                    'x1': 3,
                    'y1': 3,
                    'line': {
                        'color': 'rgba(50, 171, 96, 1)',
                    },
                },
                # filled circle
                {
                    'type': 'circle',
                    'xref': 'x',
                    'yref': 'y',
                    'fillcolor': 'rgba(50, 171, 96, 0.7)',
                    'x0': 3,
                    'y0': 3,
                    'x1': 4,
                    'y1': 4,
                    'line': {
                        'color': 'rgba(50, 171, 96, 1)',
                    },
                },
            ]
        }
        fig = {
            'data': data,
            'layout': layout,
        }
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)

    # Highlighting Clusters of Scatter Points with Circle Shapes
    if __name__ == '__main__':
        import numpy as np

        x0 = np.random.normal(2, 0.45, 300)
        y0 = np.random.normal(2, 0.45, 300)

        x1 = np.random.normal(6, 0.4, 200)
        y1 = np.random.normal(6, 0.4, 200)

        x2 = np.random.normal(4, 0.3, 200)
        y2 = np.random.normal(4, 0.3, 200)

        trace0 = go.Scatter(
            x=x0,
            y=y0,
            mode='markers',
        )
        trace1 = go.Scatter(
            x=x1,
            y=y1,
            mode='markers'
        )
        trace2 = go.Scatter(
            x=x2,
            y=y2,
            mode='markers'
        )
        trace3 = go.Scatter(
            x=x1,
            y=y0,
            mode='markers'
        )
        layout = {
            'shapes': [
                {
                    'type': 'circle',
                    'xref': 'x',
                    'yref': 'y',
                    'x0': min(x0),
                    'y0': min(y0),
                    'x1': max(x0),
                    'y1': max(y0),
                    'opacity': 0.2,
                    'fillcolor': 'blue',
                    'line': {
                        'color': 'blue',
                    },
                },
                {
                    'type': 'circle',
                    'xref': 'x',
                    'yref': 'y',
                    'x0': min(x1),
                    'y0': min(y1),
                    'x1': max(x1),
                    'y1': max(y1),
                    'opacity': 0.2,
                    'fillcolor': 'orange',
                    'line': {
                        'color': 'orange',
                    },
                },
                {
                    'type': 'circle',
                    'xref': 'x',
                    'yref': 'y',
                    'x0': min(x2),
                    'y0': min(y2),
                    'x1': max(x2),
                    'y1': max(y2),
                    'opacity': 0.2,
                    'fillcolor': 'green',
                    'line': {
                        'color': 'green',
                    },
                },
                {
                    'type': 'circle',
                    'xref': 'x',
                    'yref': 'y',
                    'x0': min(x1),
                    'y0': min(y0),
                    'x1': max(x1),
                    'y1': max(y0),
                    'opacity': 0.2,
                    'fillcolor': 'red',
                    'line': {
                        'color': 'red',
                    },
                },
            ],
            'showlegend': False,
        }
        data = [trace0, trace1, trace2, trace3]
        fig = {
            'data': data,
            'layout': layout,
        }
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)

    # Venn Diagram with Circle Shapes
    if __name__ == '__main__':
        trace0 = go.Scatter(
            x=[1, 1.75, 2.5],
            y=[1, 1, 1],
            text=['$A$', '$A+B$', '$B$'],
            mode='text',
            textfont=dict(
                color='black',
                size=18,
                family='Arail',
            )
        )

        data = [trace0]

        layout = {
            'xaxis': {
                'showticklabels': False,
                'showgrid': False,
                'zeroline': False,
            },
            'yaxis': {
                'showticklabels': False,
                'showgrid': False,
                'zeroline': False,
            },
            'shapes': [
                {
                    'opacity': 0.3,
                    'xref': 'x',
                    'yref': 'y',
                    'fillcolor': 'blue',
                    'x0': 0,
                    'y0': 0,
                    'x1': 2,
                    'y1': 2,
                    'type': 'circle',
                    'line': {
                        'color': 'blue',
                    },
                },
                {
                    'opacity': 0.3,
                    'xref': 'x',
                    'yref': 'y',
                    'fillcolor': 'gray',
                    'x0': 1.5,
                    'y0': 0,
                    'x1': 3.5,
                    'y1': 2,
                    'type': 'circle',
                    'line': {
                        'color': 'gray',
                    },
                }
            ],
            'margin': {
                'l': 20,
                'r': 20,
                'b': 100
            },
            'height': 600,
            'width': 800,
        }
        fig = {
            'data': data,
            'layout': layout,
        }
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)

    # SVG Paths
    if __name__ == '__main__':
        trace0 = go.Scatter(
            x=[2, 1, 8, 8],
            y=[0.25, 9, 2, 6],
            text=['Filled Triangle',
                  'Filled Polygon',
                  'Quadratic Bezier Curves',
                  'Cubic Bezier Curves'],
            mode='text',
        )
        data = [trace0]
        layout = {

            'xaxis': {
                'range': [0, 9],
                'zeroline': False,
            },
            'yaxis': {
                'range': [0, 11],
                'showgrid': False,
            },
            'shapes': [
                # Quadratic Bezier Curves
                {
                    'type': 'path',
                    'path': 'M 4,4 Q 6,0 8,4',
                    'line': {
                        'color': 'rgb(93, 164, 214)',
                    },
                },
                # Cubic Bezier Curves
                {
                    'type': 'path',
                    'path': 'M 1,4 C 2,8 6,4 8,8',
                    'line': {
                        'color': 'rgb(207, 114, 255)',
                    },
                },
                # filled Triangle
                {
                    'type': 'path',
                    'path': ' M 1 1 L 1 3 L 4 1 Z',
                    'fillcolor': 'rgba(44, 160, 101, 0.5)',
                    'line': {
                        'color': 'rgb(44, 160, 101)',
                    },
                },
                # filled Polygon
                {
                    'type': 'path',
                    'path': ' M 3,7 L2,8 L2,9 L3,10, L4,10 L5,9 L5,8 L4,7 Z',
                    'fillcolor': 'rgba(255, 140, 184, 0.5)',
                    'line': {
                        'color': 'rgb(255, 140, 184)',
                    },
                },

            ]
        }
        fig = {
            'data': data,
            'layout': layout,
        }
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)


# 6、Logos
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    # Formatting and Positioning Images as Logos
    if __name__ == '__main__':
        data = [
            go.Bar(
                x=['-35.3', '-15.9', '-15.8', '-15.6', '-11.1',
                   '-9.6', '-9.2', '-3.5', '-1.9', '-0.9',
                   '1.0', '1.4', '1.7', '2.0', '2.8', '6.2',
                   '8.1', '8.5', '8.5', '8.6', '11.4', '12.5',
                   '13.3', '13.7', '14.4', '17.5', '17.7',
                   '18.9', '25.1', '28.9', '41.4'],
                y=['Designers, musicians, artists, etc.',
                   'Secretaries and administrative assistants',
                   'Waiters and servers', 'Archivists, curators, and librarians',
                   'Sales and related', 'Childcare workers, home car workers, etc.',
                   'Food preparation occupations', 'Janitors, maids, etc.',
                   'Healthcare technicians, assistants. and aides',
                   'Counselors, social and religious workers',
                   'Physical, life and social scientists', 'Construction',
                   'Factory assembly workers', 'Machinists, repairmen, etc.',
                   'Media and communications workers', 'Teachers',
                   'Mechanics, repairmen, etc.', 'Financial analysts and advisers',
                   'Farming, fishing and forestry workers',
                   'Truck drivers, heavy equipment operator, etc.', 'Accountants and auditors',
                   'Human resources, management analysts, etc.', 'Managers',
                   'Lawyers and judges', 'Engineers, architects and surveyors',
                   'Nurses', 'Legal support workers',
                   'Computer programmers and system admin.', 'Police officers and firefighters',
                   'Chief executives', 'Doctors, dentists and surgeons'],
                marker=dict(
                    color='rgb(253, 240, 54)',
                    line=dict(color='rgb(0, 0, 0)',
                              width=2)
                ),
                orientation='h',
            )
        ]

        layout = go.Layout(
            images=[dict(
                source="https://raw.githubusercontent.com/cldougl/plot_images/add_r_img/vox.png",
                xref="paper", yref="paper",
                x=1, y=1.05,
                sizex=0.2, sizey=0.2,
                xanchor="right", yanchor="bottom"
            )],
            autosize=False, height=800, width=700,
            bargap=0.15, bargroupgap=0.1,
            barmode='stack', hovermode='x',
            margin=dict(r=20, l=300,
                        b=75, t=125),
            title='Moving Up, Moving Down<br><i>Percentile change in income between childhood and adulthood</i>',
            xaxis=dict(
                dtick=10, nticks=0,
                gridcolor='rgba(102, 102, 102, 0.4)',
                linecolor='#000', linewidth=1,
                mirror=True,
                showticklabels=True, tick0=0, tickwidth=1,
                title='<i>Change in percentile</i>',
            ),
            yaxis=dict(
                anchor='x',
                gridcolor='rgba(102, 102, 102, 0.4)', gridwidth=1,
                linecolor='#000', linewidth=1,
                mirror=True, showgrid=False,
                showline=True, zeroline=False,
                showticklabels=True, tick0=0,
                type='category',
            )
        )
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)

# 7 3D Surface Coloring in Python
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    # Color by Variable
    if __name__ == '__main__':
        from plotly import tools

        import copy
        import json
        import math
        import urllib2

        # load ring cyclide data
        response = urllib2.urlopen('https://plot.ly/~empet/2381.json')
        data_file = response.read()
        fig = json.loads(data_file)

        data_original = fig['data'][0]  # trace0
        data = copy.deepcopy(fig['data'])[0]  # trace1

        lx = len(data['z'])
        ly = len(data['z'][0])
        out = []


        def dist_origin(x, y, z):
            return math.sqrt((1.0 * x) ** 2 + (1.0 * y) ** 2 + (1.0 * z) ** 2)


        for i in xrange(lx):
            temp = []
            for j in xrange(ly):
                temp.append(
                    dist_origin(data['x'][i][j], data['y'][i][j], data['z'][i][j]))
            out.append(temp)

        data['surfacecolor'] = out  # sets surface-color to distance from the origin

        scene = dict(
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
            cameraposition=[[0.2, 0.5, 0.5, 0.2], [0, 0, 0], 4.8]
        )

        fig = tools.make_subplots(rows=1, cols=2,
                                  specs=[[{'is_3d': True}, {'is_3d': True}]])

        # adding surfaces to subplots.
        data_original['scene'] = 'scene1'
        data_original['colorbar'] = dict(x=-0.07)

        data['scene'] = 'scene2'
        fig.append_trace(data_original, 1, 1)
        fig.append_trace(data, 1, 2)

        fig['layout'].update(title='Ring Cyclide',
                             height=800, width=950)
        fig['layout']['scene1'].update(scene)
        fig['layout']['scene2'].update(scene)
        fig['layout']['annotations'] = [
            dict(x=0.1859205, y=0.95,
                 xref='x', yref='y',
                 text='4th Dim Prop. to z',
                 showarrow=False),
            dict(x=0.858, y=0.95,
                 xref='x', yref='y',
                 text='4th Dim Prop. to Distance from Origin',
                 showarrow=False)
        ]
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)


# 8 Colorway in Python
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    # Set Default Trace Colors with colorway
    if __name__ == '__main__':
        import numpy as np


        def parabola_gen(a, b):
            return lambda x: a * x ** 2 + b


        parabolas = [parabola_gen(a, b) for a, b in zip(np.linspace(1, 3, 7), np.linspace(2, 14, 7))]
        x = np.linspace(-1, 3)
        data = [go.Scatter(x=x, y=p(x), mode='lines') for p in parabolas]

        colorway = ['#f3cec9', '#e7a4b6', '#cd7eaf', '#a262a9', '#6f4d96', '#3d3b72', '#182844']
        layout = go.Layout(colorway=colorway)
        py.plot(go.Figure(data=data, layout=layout), filename='tmp/style_tutorial.html', auto_play=True)


# 9 Matplotlib Colorscales in Python
if __name__ == '__main__':

    # Formatting the Colormap
    if __name__ == '__main__':
        import parula as par
        import matplotlib
        from matplotlib import cm
        import numpy as np

        magma_cmap = matplotlib.cm.get_cmap('magma')
        viridis_cmap = matplotlib.cm.get_cmap('viridis')
        parula_cmap = par.parula_map

        viridis_rgb = []
        magma_rgb = []
        parula_rgb = []
        norm = matplotlib.colors.Normalize(vmin=0, vmax=255)

        for i in range(0, 255):
            k = matplotlib.colors.colorConverter.to_rgb(magma_cmap(norm(i)))
            magma_rgb.append(k)

        for i in range(0, 255):
            k = matplotlib.colors.colorConverter.to_rgb(viridis_cmap(norm(i)))
            viridis_rgb.append(k)

        for i in range(0, 255):
            k = matplotlib.colors.colorConverter.to_rgb(parula_cmap(norm(i)))
            parula_rgb.append(k)


        def matplotlib_to_plotly(cmap, pl_entries):
            h = 1.0 / (pl_entries - 1)
            pl_colorscale = []

            for k in range(pl_entries):
                C = map(np.uint8, np.array(cmap(k * h)[:3]) * 255)
                pl_colorscale.append([k * h, 'rgb' + str((C[0], C[1], C[2]))])

            return pl_colorscale


        magma = matplotlib_to_plotly(magma_cmap, 255)
        viridis = matplotlib_to_plotly(viridis_cmap, 255)
        parula = matplotlib_to_plotly(parula_cmap, 255)
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)

    # Colorscales for Heatmaps
    if __name__ == '__main__':
        import plotly.plotly as py
        import numpy as np
        import os
        import plotly.graph_objs as go
        from plotly import tools


        def heatmap_plot(colorscale, title):
            example_dir = os.path.join(os.path.dirname('__file__'), "examples")

            hist2d = np.loadtxt(os.path.join(example_dir, "hist2d.txt"))
            trace1 = go.Heatmap(z=hist2d, colorscale=colorscale, showscale=False)

            st_helens = np.loadtxt(os.path.join(example_dir,
                                                "st-helens_before-modified.txt.gz")).T
            trace2 = go.Heatmap(z=st_helens, colorscale=colorscale, y0=-5, x0=-5)

            dx = dy = 0.05
            y, x = np.mgrid[-5: 5 + dy: dy, -5: 10 + dx: dx]
            z = np.sin(x) ** 10 + np.cos(10 + y * x) + np.cos(x) + 0.2 * y + 0.1 * x
            trace3 = go.Heatmap(z=z, colorscale=colorscale, showscale=False)

            fig = tools.make_subplots(rows=1, cols=3, print_grid=False)
            fig.append_trace(trace1, 1, 1)
            fig.append_trace(trace2, 1, 2)
            fig.append_trace(trace3, 1, 3)
            fig['layout'].update(title=title)
            fig['layout']['xaxis2'].update(range=[0, 450])
            fig['layout']['yaxis2'].update(range=[0, 270])

            return fig
        py.plot(heatmap_plot(colorscale=magma, title='MAGMA'), filename='tmp/style_tutorial.html', auto_play=True)


# 10 Styling Markers in Python
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    # Add Marker Border
    if __name__ == '__main__':
        import numpy as np

        x = np.random.uniform(low=3, high=6, size=(500,))
        y = np.random.uniform(low=3, high=6, size=(500,))

        data = [
            go.Scatter(
                mode='markers',
                x=x,
                y=y,
                marker=dict(
                    color='rgb(17, 157, 255)',
                    size=20,
                    line=dict(
                        color='rgb(231, 99, 250)',
                        width=2
                    )
                ),
                showlegend=False
            ),
            go.Scatter(
                mode='markers',
                x=[2],
                y=[4.5],
                marker=dict(
                    color='rgb(17, 157, 255)',
                    size=120,
                    line=dict(
                        color='rgb(231, 99, 250)',
                        width=12
                    )
                ),
                showlegend=False
            )]
        py.plot(data, filename='tmp/style_tutorial.html', auto_play=True)

    # Fully Opaque
    if __name__ == '__main__':
        import numpy as np

        x = np.random.uniform(low=3, high=6, size=(500,))
        y = np.random.uniform(low=3, high=6, size=(500,))

        data = [
            go.Scatter(
                mode='markers',
                x=x,
                y=y,
                marker=dict(
                    color='rgb(17, 157, 255)',
                    size=20,
                    line=dict(
                        color='rgb(231, 99, 250)',
                        width=2
                    )
                ),
                showlegend=False
            ),
            go.Scatter(
                mode='markers',
                x=[2, 2],
                y=[4.25, 4.75],
                marker=dict(
                    color='rgb(17, 157, 255)',
                    size=80,
                    line=dict(
                        color='rgb(231, 99, 250)',
                        width=8
                    )
                ),
                showlegend=False
            )]
        py.plot(data, filename='tmp/style_tutorial.html', auto_play=True)

    # Opacity
    if __name__ == '__main__':
        import numpy as np

        x = np.random.uniform(low=3, high=6, size=(500,))
        y = np.random.uniform(low=3, high=4.5, size=(500,))
        x2 = np.random.uniform(low=3, high=6, size=(500,))
        y2 = np.random.uniform(low=4.5, high=6, size=(500,))

        data = [
            go.Scatter(
                mode='markers',
                x=x,
                y=y,
                opacity=0.5,
                marker=dict(
                    color='rgb(17, 157, 255)',
                    size=20,
                    line=dict(
                        color='rgb(231, 99, 250)',
                        width=2
                    )
                ),
                name='Opacity 0.5'
            ),
            go.Scatter(
                mode='markers',
                x=x2,
                y=y2,
                marker=dict(
                    color='rgb(17, 157, 255)',
                    size=20,
                    line=dict(
                        color='rgb(231, 99, 250)',
                        width=2
                    )
                ),
                name='Opacity 1.0'
            ),
            go.Scatter(
                mode='markers',
                x=[2, 2],
                y=[4.25, 4.75],
                opacity=0.5,
                marker=dict(
                    color='rgb(17, 157, 255)',
                    size=80,
                    line=dict(
                        color='rgb(231, 99, 250)',
                        width=8
                    )
                ),
                showlegend=False
            )]

        py.plot(data, filename='tmp/style_tutorial.html', auto_play=True)

    # Marker Opacity
    if __name__ == '__main__':
        import numpy as np

        x = np.random.uniform(low=3, high=6, size=(500,))
        y = np.random.uniform(low=3, high=6, size=(500,))

        data = [
            go.Scatter(
                mode='markers',
                x=x,
                y=y,
                marker=dict(
                    color='rgb(17, 157, 255)',
                    size=20,
                    opacity=0.5,
                    line=dict(
                        color='rgb(231, 99, 250)',
                        width=2
                    )
                ),
                showlegend=False
            ),
            go.Scatter(
                mode='markers',
                x=[2, 2],
                y=[4.25, 4.75],
                marker=dict(
                    color='rgb(17, 157, 255)',
                    size=80,
                    opacity=0.5,
                    line=dict(
                        color='rgb(231, 99, 250)',
                        width=8
                    )
                ),
                showlegend=False
            )]
        py.plot(data, filename='tmp/style_tutorial.html', auto_play=True)

    # Color Opacity
    if __name__ == '__main__':
        import numpy as np

        x = np.random.uniform(low=3, high=6, size=(500,))
        y = np.random.uniform(low=3, high=6, size=(500,))

        data = [
            go.Scatter(
                mode='markers',
                x=x,
                y=y,
                marker=dict(
                    color='rgba(17, 157, 255, 0.5)',
                    size=20,
                    line=dict(
                        color='rgb(231, 99, 250)',
                        width=2
                    )
                ),
                showlegend=False
            ),
            go.Scatter(
                mode='markers',
                x=[2, 2],
                y=[4.25, 4.75],
                marker=dict(
                    color='rgba(17, 157, 255, 0.5)',
                    size=80,
                    line=dict(
                        color='rgb(231, 99, 250)',
                        width=8
                    )
                ),
                showlegend=False
            )]
        py.plot(data, filename='tmp/style_tutorial.html', auto_play=True)


# 11 Colorscales in Python
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    # Custom Discretized Heatmap Colorscale
    if __name__ == '__main__':
        py.plot([{
            'z': [
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            ],
            'type': 'heatmap',
            'colorscale': [
                # Let first 10% (0.1) of the values have color rgb(0, 0, 0)
                [0, 'rgb(0, 0, 0)'],
                [0.1, 'rgb(0, 0, 0)'],

                # Let values between 10-20% of the min and max of z
                # have color rgb(20, 20, 20)
                [0.1, 'rgb(20, 20, 20)'],
                [0.2, 'rgb(20, 20, 20)'],

                # Values between 20-30% of the min and max of z
                # have color rgb(40, 40, 40)
                [0.2, 'rgb(40, 40, 40)'],
                [0.3, 'rgb(40, 40, 40)'],

                [0.3, 'rgb(60, 60, 60)'],
                [0.4, 'rgb(60, 60, 60)'],

                [0.4, 'rgb(80, 80, 80)'],
                [0.5, 'rgb(80, 80, 80)'],

                [0.5, 'rgb(100, 100, 100)'],
                [0.6, 'rgb(100, 100, 100)'],

                [0.6, 'rgb(120, 120, 120)'],
                [0.7, 'rgb(120, 120, 120)'],

                [0.7, 'rgb(140, 140, 140)'],
                [0.8, 'rgb(140, 140, 140)'],

                [0.8, 'rgb(160, 160, 160)'],
                [0.9, 'rgb(160, 160, 160)'],

                [0.9, 'rgb(180, 180, 180)'],
                [1.0, 'rgb(180, 180, 180)']
            ],
            'colorbar': {
                'tick0': 0,
                'dtick': 1
            }
        }], filename='tmp/style_tutorial.html', auto_play=True)

    # Colorscale for Scatter Plots
    if __name__ == '__main__':
        data = [
            go.Scatter(
                y=[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                   5, 5, 5, 5, 5, 5],
                marker=dict(
                    size=16,
                    cmax=39,
                    cmin=0,
                    color=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                           26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
                    colorbar=dict(
                        title='Colorbar'
                    ),
                    colorscale='Viridis'
                ),
                mode='markers')
        ]

        fig = go.Figure(data=data)
        py.plot(fig, filename='tmp/style_tutorial.html', auto_play=True)

    # Colorscale for Contour Plot
    if __name__ == '__main__':
        data = [
            go.Contour(
                z=[[10, 10.625, 12.5, 15.625, 20],
                   [5.625, 6.25, 8.125, 11.25, 15.625],
                   [2.5, 3.125, 5., 8.125, 12.5],
                   [0.625, 1.25, 3.125, 6.25, 10.625],
                   [0, 0.625, 2.5, 5.625, 10]],
                colorscale='Jet',
            )
        ]
        py.plot(data, filename='tmp/style_tutorial.html', auto_play=True)

    # Custom Heatmap Colorscale
    if __name__ == '__main__':
        import six.moves.urllib
        import json

        response = six.moves.urllib.request.urlopen(
            'https://raw.githubusercontent.com/plotly/datasets/master/custom_heatmap_colorscale.json')
        dataset = json.load(response)

        data = [
            go.Heatmap(
                z=dataset['z'],
                colorscale=[[0.0, 'rgb(165,0,38)'], [0.1111111111111111, 'rgb(215,48,39)'],
                            [0.2222222222222222, 'rgb(244,109,67)'], [0.3333333333333333, 'rgb(253,174,97)'],
                            [0.4444444444444444, 'rgb(254,224,144)'], [0.5555555555555556, 'rgb(224,243,248)'],
                            [0.6666666666666666, 'rgb(171,217,233)'], [0.7777777777777778, 'rgb(116,173,209)'],
                            [0.8888888888888888, 'rgb(69,117,180)'], [1.0, 'rgb(49,54,149)']]
            )
        ]
        py.plot(data, filename='tmp/style_tutorial.html', auto_play=True)

    # Custom Contour Plot Colorscale
    if __name__ == '__main__':
        data = [
            go.Contour(
                z=[[10, 10.625, 12.5, 15.625, 20],
                   [5.625, 6.25, 8.125, 11.25, 15.625],
                   [2.5, 3.125, 5., 8.125, 12.5],
                   [0.625, 1.25, 3.125, 6.25, 10.625],
                   [0, 0.625, 2.5, 5.625, 10]],
                colorscale=[[0, 'rgb(166,206,227)'], [0.25, 'rgb(31,120,180)'], [0.45, 'rgb(178,223,138)'],
                            [0.65, 'rgb(51,160,44)'], [0.85, 'rgb(251,154,153)'], [1, 'rgb(227,26,28)']],
            )
        ]

        py.plot(data, filename='tmp/style_tutorial.html', auto_play=True)

    # Custom Colorbar
    if __name__ == '__main__':
        import six.moves.urllib
        import json

        response = six.moves.urllib.request.urlopen(
            'https://raw.githubusercontent.com/plotly/datasets/master/custom_heatmap_colorscale.json')
        dataset = json.load(response)

        data = [
            go.Heatmap(
                z=dataset['z'],
                colorscale=[[0.0, 'rgb(165,0,38)'], [0.1111111111111111, 'rgb(215,48,39)'],
                            [0.2222222222222222, 'rgb(244,109,67)'],
                            [0.3333333333333333, 'rgb(253,174,97)'], [0.4444444444444444, 'rgb(254,224,144)'],
                            [0.5555555555555556, 'rgb(224,243,248)'],
                            [0.6666666666666666, 'rgb(171,217,233)'], [0.7777777777777778, 'rgb(116,173,209)'],
                            [0.8888888888888888, 'rgb(69,117,180)'],
                            [1.0, 'rgb(49,54,149)']],
                colorbar=dict(
                    title='Surface Heat',
                    titleside='top',
                    tickmode='array',
                    tickvals=[2, 50, 100],
                    ticktext=['Hot', 'Mild', 'Cool'],
                    ticks='outside'
                )
            )
        ]
        py.plot(data, filename='tmp/style_tutorial.html', auto_play=True)


# 12 Cmocean Colorscales in Python
if __name__ == '__main__':
    pass
