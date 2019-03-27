
'''
官方教程
https://plot.ly/python/
全部的参数解析 https://plot.ly/python/reference/#scatter
'''


# 1、一个综合的例子-bar
if __name__ == '__main__1':
    import plotly.offline as py
    import plotly.graph_objs as go

    figure = go.Figure(
        # 两个数据放到同一个chart中
        data=[
            # 不能像matplotlib那样两个y放在一起
            go.Bar(
                x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                   2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                   350, 430, 474, 526, 488, 537, 500, 439],
                name='Rest of world',
                marker=go.bar.Marker(
                    color='rgb(55, 83, 109)'
                )
            ),
            go.Bar(
                x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                   2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                   299, 340, 403, 549, 499],
                name='China',
                marker=go.bar.Marker(
                    color='rgb(26, 118, 255)'
                )
            )
        ],
        # 这个chart的样子
        layout=go.Layout(
            title='US Export of Plastic Scrap',
            showlegend=True,
            legend=go.layout.Legend(
                x=0,
                y=1.0
            ),
            margin=go.layout.Margin(l=100, r=10, t=100, b=20)  # chart本身到边框的距离，单位px
        )
    )

    py.plot(figure, filename='tmp/temp-plot.html', auto_open=True, )

    '''
    一、长代码的经验：
        1、多括号的处理，
        2、多参数的处理，不同参数处于同一缩进，参数单开一行
        3、不同块空一行
    '''


# 2、plotly的基础
if __name__ == '__main__2':
    import plotly.offline as py
    import plotly.graph_objs as go
    import numpy as np

    N = 100
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    sz = np.random.rand(N) * 30

    fig = go.Figure(data=None, layout=None, frames=None, skip_invalid=False)  # 有四个参数，没有size的参数
    # 添加chart，就是data参数的内容
    fig.add_scatter(x=x,
                    y=y,
                    mode='markers',  # 'markers'是显示点
                    marker={'size': sz,
                            'color': colors,
                            'opacity': 0.6,
                            'colorscale': 'Viridis'
                            })

    # 1、图像发布成html
    url = py.plot(fig, filename='tmp/temp-plot.html', auto_open=True, )

    # 2、输出到静态图像orca，其中orca是一个服务器，能够发布图像
    import plotly.io as pio
    pio.write_image(fig, r'D:\py36 projects\dash_tutorial\tmp\fig1.png')

    pio.orca.config  # 输出的一些config
    pio.orca.status

    pio.orca.shutdown_server()

    # 3、privacy
    # 这个很多是在存到plotly的服务器的那里

    # 4、Sending Data to Charts in Python
    if __name__ == '__main__':
        # import plotly.plotly as py  # 这个是放到plotly的服务器上的，
        import plotly.offline as py  # 这个是发布到离线的本地文件的
        import plotly.graph_objs as go

        data = [go.Scatter(x=[1, 2], y=[3, 4])]

        plot_url = py.plot(data, filename='tmp/my_plot.html',auto_open=True,)

        # 更新数据？
        new_data = [go.Scatter(x=[3, 4], y=[3, 2])]

        plot_url = py.plot(data, filename='tmp/my_plot.html', fileopt='append')  # 本地没办法这样更新


# 3、Scatter
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    import numpy as np
    import pandas as pd

    # mode参数：marker, lines+markers, lines
    # 附带visible,showlegend,legendgroup
    # opacity, name
    if __name__ == '__main__':

        N = 100
        random_x = np.linspace(0, 1, N)
        random_y0 = np.random.randn(N) + 5
        random_y1 = np.random.randn(N)
        random_y2 = np.random.randn(N) - 5

        # Create traces
        trace0 = go.Scatter(
            x=random_x,
            y=random_y0,
            mode='markers',
            name='markers',
            # visible = False,
            # showlegend=False,
            # legendgroup='test legendgroup',  # 不知道是干嘛的
        )
        trace1 = go.Scatter(
            x=random_x,
            y=random_y1,
            mode='lines+markers',
            name='lines+markers',
            # legendgroup='test legendgroup',  # 不知道是干嘛的
        )
        trace2 = go.Scatter(
            x=random_x,
            y=random_y2,
            mode='lines',
            name='lines'
        )

        data = [trace0, trace1, trace2]
        url = py.plot(data, filename='tmp/scatter_tutorial.html', auto_open=True, )


    # markers参数，
    if __name__ == '__main__':
        N = 500

        trace0 = go.Scatter(
            x=np.random.randn(N),
            y=np.random.randn(N) + 2,
            name='Above',
            mode='markers',
            marker=dict(
                size=10,
                color='rgba(152, 0, 0, .8)',
                line=dict(
                    width=2,
                    color='rgb(0, 0, 0)'
                )
            ),
        )

        trace1 = go.Scatter(
            x=np.random.randn(N),
            y=np.random.randn(N) - 2,
            name='Below',
            mode='markers',
            marker=dict(
                size=10,
                color='rgba(255, 182, 193, .9)',
                line=dict(
                    width=2,
                )
            )
        )

        data = [trace0, trace1]

        # layout是整个chart，title也是大标题
        layout = dict(title='Styled Scatter',
                      yaxis=dict(zeroline=False),  # 不显示x轴
                      xaxis=dict(zeroline=False)
                      )

        fig = dict(data=data, layout=layout)
        url = py.plot(fig, filename='tmp/scatter_tutorial.html', auto_open=True, )

    # Data Labels on Hover
    # 默认的hover是以x为主的，同时读取对应的y，x的标签在轴下，y标签在点的边上，如果一个x对应多个y则有多个标签
    # hovermode = 'closet'就只放到一个标签中，并且根据点来去，不是根据x来取
    # text的y的标签下显示对应的x标签，做一个和x轴的数字的对应
    if __name__ == '__main__':
        l = []
        y = []
        data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv")
        # Setting colors for plot.
        N = 53
        c = ['hsl(' + str(h) + ',50%' + ',50%)' for h in np.linspace(0, 360, N)]

        for i in range(int(N)):
            y.append((2000 + i))
            trace0 = go.Scatter(
                x=data['Rank'],
                y=data['Population'] + (i * 1000000),
                mode='markers',
                marker=dict(size=14,
                            line=dict(width=1),
                            color=c[i],
                            opacity=0.3
                            ), name=y[i],
                text=data['State'] # The hover text goes here...
            )
            l.append(trace0)

        layout = go.Layout(
            title='Stats of USA States',
            hovermode='closest',
            xaxis=dict(
                title='Rank',
                ticklen=5,
                zeroline=False,
                gridwidth=2,
            ),
            yaxis=dict(
                title='Population',
                ticklen=5,
                gridwidth=2,
            ),
            showlegend=False
        )
        fig = go.Figure(data=l, layout=layout)
        url = py.plot(fig, filename='tmp/scatter_tutorial.html', auto_open=True, )

    # 颜色深浅作为第三维
    if __name__ == '__main__':
        trace1 = go.Scatter(
            y=np.random.randn(500),
            mode='markers',
            marker=dict(
                size=16,
                color=np.random.randn(500),  # set color equal to a variable
                colorscale='Viridis',
                showscale=True
            )
        )
        data = [trace1]
        url = py.plot(data, filename='tmp/scatter_tutorial.html', auto_open=True, )


    # 大数据模式，Scattergl
    if __name__ == '__main__':
        N = 100000
        trace = go.Scattergl(
            x=np.random.randn(N),
            y=np.random.randn(N),
            mode='markers',
            marker=dict(
                color='#FFBAD2',
                line=dict(width=1)
            )
        )
        data = [trace]
        url = py.plot(data, filename='tmp/scatter_tutorial.html', auto_open=True, )


    # hover相关，line相关，fill
    if __name__ == '__main__':
        N = 100
        random_x = np.linspace(0, 1, N)
        random_y0 = np.random.randn(N) + 5
        random_y1 = np.random.randn(N)
        random_y2 = np.random.randn(N) - 5

        # Create traces
        trace0 = go.Scatter(
            x=random_x,
            y=random_y0,
            mode='markers',
            name='markers',
            # hoverinfo='skip'  # Any combination of "x", "y", "z", "text", "name" joined with a "+"
            # hoverlabel=dict(
            #     bgcolor='yellow',  # 默认是点的颜色
            #     bordercolor='black',
            #     font=dict(
            #         family='',  # 字体
            #         size='',  #
            #         color='',  # 颜色
            #     ),
            #     namelength = -1, # -1：trace的全称，0-3：显示的字符数
            # ),
            # hoveron='points',
            # hovertemplate='Price: %{y:$.2f}'  # 自定义hoverbox的显示模板，会覆盖hoverinfo
        )
        trace1 = go.Scatter(
            x=random_x,
            y=random_y1,
            mode='lines+markers',
            name='lines+markers',
            fill='tonextx',  # tozeroy从x轴往上下，toself是线性拟合线为基准，tonextx不知道@todo
            fillcolor='green',

        )
        trace2 = go.Scatter(
            x=random_x,
            y=random_y2,
            mode='lines',
            name='lines',
            # line=dict(
            #     color='red',
            #     width=5,
            #     shape='spline',  # 平滑方式vh是方波图，spline是平滑
            #     smoothing=1.3,  # 平滑度0-1.3
            #     dash='15px', # 样式，实行，空心，点状，或者是5px
            #     simplify=True  # 是否去掉共线性的点
            # )
        )

        data = [trace0, trace1, trace2]
        url = py.plot(data, filename='tmp/scatter_tutorial.html', auto_open=True, )


    # marker
    if __name__ == '__main__':
        N = 100
        random_x = np.linspace(0, 1, N)
        random_y0 = np.random.randn(N) + 5


        # Create traces
        trace0 = go.Scatter(
            x=random_x,
            y=random_y0,
            mode='markers',
            name='markers',
            marker=dict(
                # symbol='star',
                opacity=0.5,
                size=12,
                # maxdisplayed=10, # 最大显示数
                line=dict(  # marker的边线
                    color='red',
                    width=3,
                    cauto=True, # 是否自动设置
                gradient='radial', # 渐进模式
                ),
            )
        )

        data = [trace0]
        url = py.plot(data, filename='tmp/scatter_tutorial.html', auto_open=True, )


    # stack


    # error_x和error_y


    # xcalendar和ycalendar


    # textfont和textposition


    # selected和unselected，拖动选择框来select
    if __name__ == '__main__':
        N = 100
        random_x = np.linspace(0, 1, N)
        random_y0 = np.random.randn(N) + 5


        # Create traces
        trace0 = go.Scatter(
            x=random_x,
            y=random_y0,
            mode='markers',
            name='markers',
            selected=dict(
                marker=dict(
                    color='red'
                )
            )
        )

        data = [trace0]
        url = py.plot(data, filename='tmp/scatter_tutorial.html', auto_open=True, )

    # color,cauto,cmin,cmax,cmid,colorscale, autocolorscale, reversescale,showscale


# 4、line，还是用scatter的
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    import numpy as np

    # mode参数，其实就跟scatter一样，这里就不写了

    # line style,line的dash参数，同scatter
    if __name__ == '__main__':

        # Add data
        month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                 'August', 'September', 'October', 'November', 'December']
        high_2000 = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]
        low_2000 = [13.8, 22.3, 32.5, 37.2, 49.9, 56.1, 57.7, 58.3, 51.2, 42.8, 31.6, 15.9]
        high_2007 = [36.5, 26.6, 43.6, 52.3, 71.5, 81.4, 80.5, 82.2, 76.0, 67.3, 46.1, 35.0]
        low_2007 = [23.6, 14.0, 27.0, 36.8, 47.6, 57.7, 58.9, 61.2, 53.3, 48.5, 31.0, 23.6]
        high_2014 = [28.8, 28.5, 37.0, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]
        low_2014 = [12.7, 14.3, 18.6, 35.5, 49.9, 58.0, 60.0, 58.6, 51.7, 45.2, 32.2, 29.1]

        # Create and style traces
        trace0 = go.Scatter(
            x=month,
            y=high_2014,
            name='High 2014',
            line=dict(
                color=('rgb(205, 12, 24)'),
                width=4)
        )
        trace1 = go.Scatter(
            x=month,
            y=low_2014,
            name='Low 2014',
            line=dict(
                color=('rgb(22, 96, 167)'),
                width=4, )
        )
        trace2 = go.Scatter(
            x=month,
            y=high_2007,
            name='High 2007',
            line=dict(
                color=('rgb(205, 12, 24)'),
                width=4,
                dash='dash')  # dash options include 'dash', 'dot', and 'dashdot'
        )
        trace3 = go.Scatter(
            x=month,
            y=low_2007,
            name='Low 2007',
            line=dict(
                color=('rgb(22, 96, 167)'),
                width=4,
                dash='dash')
        )
        trace4 = go.Scatter(
            x=month,
            y=high_2000,
            name='High 2000',
            line=dict(
                color=('rgb(205, 12, 24)'),
                width=4,
                dash='dot')
        )
        trace5 = go.Scatter(
            x=month,
            y=low_2000,
            name='Low 2000',
            line=dict(
                color=('rgb(22, 96, 167)'),
                width=4,
                dash='dot')
        )
        data = [trace0, trace1, trace2, trace3, trace4, trace5]

        # Edit the layout
        layout = dict(title='Average High and Low Temperatures in New York',
                      xaxis=dict(title='Month'),
                      yaxis=dict(title='Temperature (degrees F)'),
                      )

        fig = dict(data=data, layout=layout)

        py.plot(fig, filename='tmp/line_tutorial.html', auto_play=True)


    # Connect Data Gaps，x有空值connectgaps参数
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[1, 2, 3, 4, 5,
               6, 7, 8, 9, 10,
               11, 12, 13, 14, 15],
            y=[10, 20, None, 15, 10,
               5, 15, None, 20, 10,
               10, 15, 25, 20, 10],
            name='<b>No</b> Gaps',  # Style name/legend entry with html tags
            connectgaps=True
        )
        trace2 = go.Scatter(
            x=[1, 2, 3, 4, 5,
               6, 7, 8, 9, 10,
               11, 12, 13, 14, 15],
            y=[5, 15, None, 10, 5,
               0, 10, None, 15, 5,
               5, 10, 20, 15, 5],
            name='Gaps',
        )

        data = [trace1, trace2]

        fig = dict(data=data)
        py.plot(fig, filename='tmp/line_tutorial.html', auto_play=True)


    # interpolation hv,vh的关系
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[1, 2, 3, 4, 5],
            y=[1, 3, 2, 3, 1],
            mode='lines+markers',
            name="'linear'",
            hoverinfo='name',
            line=dict(
                shape='linear'
            )
        )
        trace2 = go.Scatter(
            x=[1, 2, 3, 4, 5],
            y=[6, 8, 7, 8, 6],
            mode='lines+markers',
            name="'spline'",
            text=["tweak line smoothness<br>with 'smoothing' in line object"],
            hoverinfo='text+name',
            line=dict(
                shape='spline'
            )
        )
        trace3 = go.Scatter(
            x=[1, 2, 3, 4, 5],
            y=[11, 13, 12, 13, 11],
            mode='lines+markers',
            name="'vhv'",
            hoverinfo='name',
            line=dict(
                shape='vhv'
            )
        )
        trace4 = go.Scatter(
            x=[1, 2, 3, 4, 5],
            y=[16, 18, 17, 18, 16],
            mode='lines+markers',
            name="'hvh'",
            hoverinfo='name',
            line=dict(
                shape='hvh'
            )
        )
        trace5 = go.Scatter(
            x=[1, 2, 3, 4, 5],
            y=[21, 23, 22, 23, 21],
            mode='lines+markers',
            name="'vh'",
            hoverinfo='name',
            line=dict(
                shape='vh'
            )
        )
        trace6 = go.Scatter(
            x=[1, 2, 3, 4, 5],
            y=[26, 28, 27, 28, 26],
            mode='lines+markers',
            name="'hv'",
            hoverinfo='name',
            line=dict(
                shape='hv'
            )
        )
        data = [trace1, trace2, trace3, trace4, trace5, trace6]
        layout = dict(
            legend=dict(
                y=0.5,
                traceorder='reversed',
                font=dict(
                    size=16
                )
            )
        )
        fig = dict(data=data, layout=layout)
        py.plot(fig, filename='tmp/line_tutorial.html', auto_play=True)


    # Label Lines with Annotations:annotations是在layout里面的
    if __name__ == '__main__':
        title = 'Main Source for News'

        labels = ['Television', 'Newspaper', 'Internet', 'Radio']

        colors = ['rgb(67,67,67)', 'rgb(115,115,115)', 'rgb(49,130,189)', 'rgb(189,189,189)']

        mode_size = [8, 8, 12, 8]

        line_size = [2, 2, 4, 2]

        x_data = [
            [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2013],
            [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2013],
            [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2013],
            [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2013],
        ]

        y_data = [
            [74, 82, 80, 74, 73, 72, 74, 70, 70, 66, 66, 69],
            [45, 42, 50, 46, 36, 36, 34, 35, 32, 31, 31, 28],
            [13, 14, 20, 24, 20, 24, 24, 40, 35, 41, 43, 50],
            [18, 21, 18, 21, 16, 14, 13, 18, 17, 16, 19, 23],
        ]

        traces = []

        for i in range(0, 4):
            traces.append(go.Scatter(
                x=x_data[i],
                y=y_data[i],
                mode='lines',
                line=dict(color=colors[i], width=line_size[i]),
                connectgaps=True,
            ))

            traces.append(go.Scatter(
                x=[x_data[i][0], x_data[i][11]],
                y=[y_data[i][0], y_data[i][11]],
                mode='markers',
                marker=dict(color=colors[i], size=mode_size[i])
            ))

        layout = go.Layout(
            xaxis=dict(
                showline=True,
                showgrid=False,
                showticklabels=True,
                linecolor='rgb(204, 204, 204)',
                linewidth=2,
                ticks='outside',
                tickcolor='rgb(204, 204, 204)',
                tickwidth=2,
                ticklen=5,
                tickfont=dict(
                    family='Arial',
                    size=12,
                    color='rgb(82, 82, 82)',
                ),
            ),
            yaxis=dict(
                showgrid=False,
                zeroline=False,
                showline=False,
                showticklabels=False,
            ),
            autosize=False,
            margin=dict(
                autoexpand=False,
                l=100,
                r=20,
                t=110,
            ),
            showlegend=False
        )

        annotations = []

        # Adding labels
        for y_trace, label, color in zip(y_data, labels, colors):
            # labeling the left_side of the plot
            annotations.append(dict(xref='paper', x=0.05, y=y_trace[0],  # paper是相对于画图区域的比例，y就是在chart中坐标的位置了
                                    xanchor='right', yanchor='middle',
                                    text=label + ' {}%'.format(y_trace[0]),
                                    font=dict(family='Arial',
                                              size=16),
                                    showarrow=False))
            # labeling the right_side of the plot
            annotations.append(dict(xref='paper', x=0.95, y=y_trace[11],
                                    xanchor='left', yanchor='middle',
                                    text='{}%'.format(y_trace[11]),
                                    font=dict(family='Arial',
                                              size=16),
                                    showarrow=False))
        # Title
        annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                                xanchor='left', yanchor='bottom',
                                text='Main Source for News',
                                font=dict(family='Arial',
                                          size=30,
                                          color='rgb(37,37,37)'),
                                showarrow=False))
        # Source
        annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                                xanchor='center', yanchor='top',
                                text='Source: PewResearch Center & ' +
                                     'Storytelling with data',
                                font=dict(family='Arial',
                                          size=12,
                                          color='rgb(150,150,150)'),
                                showarrow=False))

        layout['annotations'] = annotations

        fig = go.Figure(data=traces, layout=layout)
        py.plot(fig, filename='tmp/line_tutorial.html', auto_play=True)


    # Filled Lines
    if __name__ == '__main__':
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x_rev = x[::-1]

        # Line 1
        y1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y1_upper = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        y1_lower = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        y1_lower = y1_lower[::-1]

        # Line 2
        y2 = [5, 2.5, 5, 7.5, 5, 2.5, 7.5, 4.5, 5.5, 5]
        y2_upper = [5.5, 3, 5.5, 8, 6, 3, 8, 5, 6, 5.5]
        y2_lower = [4.5, 2, 4.4, 7, 4, 2, 7, 4, 5, 4.75]
        y2_lower = y2_lower[::-1]

        # Line 3
        y3 = [10, 8, 6, 4, 2, 0, 2, 4, 2, 0]
        y3_upper = [11, 9, 7, 5, 3, 1, 3, 5, 3, 1]
        y3_lower = [9, 7, 5, 3, 1, -.5, 1, 3, 1, -1]
        y3_lower = y3_lower[::-1]

        trace1 = go.Scatter(
            x=x + x_rev,
            y=y1_upper + y1_lower,
            fill='tozerox',
            fillcolor='rgba(0,100,80,0.2)',
            line=dict(color='rgba(255,255,255,0)'),
            showlegend=False,
            name='Fair',
        )
        trace2 = go.Scatter(
            x=x + x_rev,
            y=y2_upper + y2_lower,
            fill='tozerox',
            fillcolor='rgba(0,176,246,0.2)',
            line=dict(color='rgba(255,255,255,0)'),
            name='Premium',
            showlegend=False,
        )
        trace3 = go.Scatter(
            x=x + x_rev,
            y=y3_upper + y3_lower,
            fill='tozerox',
            fillcolor='rgba(231,107,243,0.2)',
            line=dict(color='rgba(255,255,255,0)'),
            showlegend=False,
            name='Fair',
        )
        trace4 = go.Scatter(
            x=x,
            y=y1,
            line=dict(color='rgb(0,100,80)'),
            mode='lines',
            name='Fair',
        )
        trace5 = go.Scatter(
            x=x,
            y=y2,
            line=dict(color='rgb(0,176,246)'),
            mode='lines',
            name='Premium',
        )
        trace6 = go.Scatter(
            x=x,
            y=y3,
            line=dict(color='rgb(231,107,243)'),
            mode='lines',
            name='Ideal',
        )

        data = [trace1, trace2, trace3, trace4, trace5, trace6]

        layout = go.Layout(
            paper_bgcolor='rgb(255,255,255)',
            plot_bgcolor='rgb(229,229,229)',
            xaxis=dict(
                gridcolor='rgb(255,255,255)',
                range=[1, 10],  # 显示范围了
                showgrid=True,
                showline=False,  # 边线
                showticklabels=True,
                tickcolor='rgb(127,127,127)',
                ticks='outside',
                zeroline=False
            ),
            yaxis=dict(
                gridcolor='rgb(255,255,255)',
                showgrid=True,
                showline=False,
                showticklabels=True,
                tickcolor='rgb(127,127,127)',
                ticks='outside',
                zeroline=False
            ),
        )
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/line_tutorial.html', auto_play=True)


# 5、bar
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    import numpy as np

    # Grouped Bar Chart，layout的barmode='group'
    if __name__ == '__main__':
        trace1 = go.Bar(
            x=['giraffes', 'orangutans', 'monkeys'],
            y=[20, 14, 23],
            name='SF Zoo'
        )
        trace2 = go.Bar(
            x=['giraffes', 'orangutans', 'monkeys'],
            y=[12, 18, 29],
            name='LA Zoo'
        )

        data = [trace1, trace2]
        layout = go.Layout(
            barmode='group'
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/line_tutorial.html', auto_play=True)


    # Stacked Bar Chart，layout的barmode='stack'
    if __name__ == '__main__':
        trace1 = go.Bar(
            x=['giraffes', 'orangutans', 'monkeys'],
            y=[20, 14, 23],
            name='SF Zoo'
        )
        trace2 = go.Bar(
            x=['giraffes', 'orangutans', 'monkeys'],
            y=[12, 18, 29],
            name='LA Zoo'
        )

        data = [trace1, trace2]
        layout = go.Layout(
            barmode='stack'
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/line_tutorial.html', auto_play=True)


    # Bar Chart with Hover Text
    if __name__ == '__main__':
        trace0 = go.Bar(
            x=['Product A', 'Product B', 'Product C'],
            y=[20, 14, 23],
            text=['27% market share', '24% market share', '19% market share'],
            marker=dict(
                color='rgb(158,202,225)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5,
                )
            ),
            opacity=0.6
        )

        data = [trace0]
        layout = go.Layout(
            title='January 2013 Sales Report',
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/line_tutorial.html', auto_play=True)


    # Bar Chart with Direct Labels，textposition='auto'
    if __name__ == '__main__':
        x = ['Product A', 'Product B', 'Product C']
        y = [20, 14, 23]

        data = [go.Bar(
            x=x,
            y=y,
            text=y,
            textposition='auto',
            marker=dict(
                color='rgb(158,202,225)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5),
            ),
            opacity=0.6
        )]
        py.plot(data, filename='tmp/line_tutorial.html', auto_play=True)

    # Grouped Bar Chart with Direct Labels
    if __name__ == '__main__':
        x = ['Product A', 'Product B', 'Product C']
        y = [20, 14, 23]
        y2 = [16, 12, 27]

        trace1 = go.Bar(
            x=x,
            y=y,
            text=y,
            textposition='auto',
            marker=dict(
                color='rgb(158,202,225)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5),
            ),
            opacity=0.6
        )

        trace2 = go.Bar(
            x=x,
            y=y2,
            text=y2,
            textposition='auto',
            marker=dict(
                color='rgb(58,200,225)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5),
            ),
            opacity=0.6
        )

        data = [trace1, trace2]
        py.plot(data, filename='tmp/line_tutorial.html', auto_play=True)


    # Rotated Bar Chart Labels，layout的xaxis=dict(tickangle=-45)
    if __name__ == '__main__':
        trace0 = go.Bar(
            x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            y=[20, 14, 25, 16, 18, 22, 19, 15, 12, 16, 14, 17],
            name='Primary Product',
            marker=dict(
                color='rgb(49,130,189)'
            )
        )
        trace1 = go.Bar(
            x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            y=[19, 14, 22, 14, 16, 19, 15, 14, 10, 12, 12, 16],
            name='Secondary Product',
            marker=dict(
                color='rgb(204,204,204)',
            )
        )

        data = [trace0, trace1]
        layout = go.Layout(
            xaxis=dict(tickangle=-45),
            barmode='group',
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/line_tutorial.html', auto_play=True)


    # Customizing Individual Bar Colors
    if __name__ == '__main__':
        trace0 = go.Bar(
            x=['Feature A', 'Feature B', 'Feature C',
               'Feature D', 'Feature E'],
            y=[20, 14, 23, 25, 22],
            marker=dict(
                color=['rgba(204,204,204,1)', 'rgba(222,45,38,0.8)',
                       'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
                       'rgba(204,204,204,1)']),
        )

        data = [trace0]
        layout = go.Layout(
            title='Least Used Feature',
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/line_tutorial.html', auto_play=True)

    # Customizing Individual Bar Widths
    if __name__ == '__main__':
        trace0 = go.Bar(
            x=[1, 2, 3, 5.5, 10],
            y=[10, 8, 6, 4, 2],
            width=[0.8, 0.8, 0.8, 3.5, 4]
        )

        data = [trace0]

        fig = go.Figure(data=data)
        py.plot(fig, filename='tmp/line_tutorial.html', auto_play=True)

    # Customizing Individual Bar Base，base=[-500, -600, -700]
    if __name__ == '__main__':
        data = [
            go.Bar(
                x=['2016', '2017', '2018'],
                y=[500, 600, 700],
                base=[-500, -600, -700],
                marker=dict(
                    color='red'
                ),
                name='expenses'
            ),
            go.Bar(
                x=['2016', '2017', '2018'],
                y=[300, 400, 700],
                base=0,
                marker=dict(
                    color='blue'
                ),
                name='revenue'
            )
        ]

        fig = go.Figure(data=data)
        py.plot(fig, filename='tmp/line_tutorial.html', auto_play=True)


    # Colored and Styled Bar Chart
    if __name__ == '__main__':
        trace1 = go.Bar(
            x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
               2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
            y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
               350, 430, 474, 526, 488, 537, 500, 439],
            name='Rest of world',
            marker=dict(
                color='rgb(55, 83, 109)'
            )
        )
        trace2 = go.Bar(
            x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
               2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
            y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
               299, 340, 403, 549, 499],
            name='China',
            marker=dict(
                color='rgb(26, 118, 255)'
            )
        )
        data = [trace1, trace2]
        layout = go.Layout(
            title='US Export of Plastic Scrap',
            xaxis=dict(
                tickfont=dict(
                    size=14,
                    color='rgb(107, 107, 107)'
                )
            ),
            yaxis=dict(
                title='USD (millions)',
                titlefont=dict(
                    size=16,
                    color='rgb(107, 107, 107)'
                ),
                tickfont=dict(
                    size=14,
                    color='rgb(107, 107, 107)'
                )
            ),
            legend=dict(
                x=0,
                y=1.0,
                bgcolor='rgba(255, 255, 255, 0)',
                bordercolor='rgba(255, 255, 255, 0)'
            ),
            barmode='group',
            bargap=0.15,
            bargroupgap=0
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/line_tutorial.html', auto_play=True)


    # Waterfall Bar Chart
    if __name__ == '__main__':
        x_data = ['Product<br>Revenue', 'Services<br>Revenue',
                  'Total<br>Revenue', 'Fixed<br>Costs',
                  'Variable<br>Costs', 'Total<br>Costs', 'Total']
        y_data = [400, 660, 660, 590, 400, 400, 340]
        text = ['$430K', '$260K', '$690K', '$-120K', '$-200K', '$-320K', '$370K']

        # Base
        trace0 = go.Bar(
            x=x_data,
            y=[0, 430, 0, 570, 370, 370, 0],
            marker=dict(
                color='rgba(1,1,1, 0.0)',
            )
        )
        # Revenue
        trace1 = go.Bar(
            x=x_data,
            y=[430, 260, 690, 0, 0, 0, 0],
            marker=dict(
                color='rgba(55, 128, 191, 0.7)',
                line=dict(
                    color='rgba(55, 128, 191, 1.0)',
                    width=2,
                )
            )
        )
        # Costs
        trace2 = go.Bar(
            x=x_data,
            y=[0, 0, 0, 120, 200, 320, 0],
            marker=dict(
                color='rgba(219, 64, 82, 0.7)',
                line=dict(
                    color='rgba(219, 64, 82, 1.0)',
                    width=2,
                )
            )
        )
        # Profit
        trace3 = go.Bar(
            x=x_data,
            y=[0, 0, 0, 0, 0, 0, 370],
            marker=dict(
                color='rgba(50, 171, 96, 0.7)',
                line=dict(
                    color='rgba(50, 171, 96, 1.0)',
                    width=2,
                )
            )
        )
        data = [trace0, trace1, trace2, trace3]
        layout = go.Layout(
            title='Annual Profit- 2015',
            barmode='stack',
            paper_bgcolor='rgba(245, 246, 249, 1)',
            plot_bgcolor='rgba(245, 246, 249, 1)',
            showlegend=False
        )

        annotations = []

        for i in range(0, 7):
            annotations.append(dict(x=x_data[i], y=y_data[i], text=text[i],
                                    font=dict(family='Arial', size=14,
                                              color='rgba(245, 246, 249, 1)'),
                                    showarrow=False, ))
            layout['annotations'] = annotations

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/line_tutorial.html', auto_play=True)


    # Bar Chart with Relative Barmode
    if __name__ == '__main__':
        x = [1, 2, 3, 4]

        trace1 = {
            'x': x,
            'y': [1, 4, 9, 16],
            'name': 'Trace1',
            'type': 'bar'
        }
        trace2 = {
            'x': x,
            'y': [6, -8, -4.5, 8],
            'name': 'Trace2',
            'type': 'bar'
        }
        trace3 = {
            'x': x,
            'y': [-15, -3, 4.5, -8],
            'name': 'Trace3',
            'type': 'bar'
        }

        trace4 = {
            'x': x,
            'y': [-1, 3, -3, -4],
            'name': 'Trace4',
            'type': 'bar'
        }

        data = [trace1, trace2, trace3, trace4]
        layout = {
            'xaxis': {'title': 'X axis'},
            'yaxis': {'title': 'Y axis'},
            'barmode': 'relative',
            'title': 'Relative Barmode'
        }
        py.plot({'data': data, 'layout': layout}, filename='tmp/line_tutorial.html', auto_play=True)


# 6 pie
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    # Styled Pie Chart
    if __name__ == '__main__':
        labels = ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen']
        values = [4500, 2500, 1053, 500]
        colors = ['#FEBFB3', '#E1396C', '#96D38C', '#D0F9B1']

        trace = go.Pie(labels=labels, values=values,
                       hoverinfo='label+percent', textinfo='value',
                       textfont=dict(size=20),
                       marker=dict(colors=colors,
                                   line=dict(color='#000000', width=2)),

                )

        py.plot([trace], filename='tmp/piechart_tutorial.html', auto_play=True)

    # Donut Chart
    if __name__ == '__main__':
        fig = {
            "data": [
                {
                    "values": [16, 15, 12, 6, 5, 4, 42],
                    "labels": [
                        "US",
                        "China",
                        "European Union",
                        "Russian Federation",
                        "Brazil",
                        "India",
                        "Rest of World"
                    ],
                    "domain": {"x": [0, .48]},
                    "name": "GHG Emissions",
                    "hoverinfo": "label+percent+name",
                    "hole": .4,
                    "type": "pie"
                },
                {
                    "values": [27, 11, 25, 8, 1, 3, 25],
                    "labels": [
                        "US",
                        "China",
                        "European Union",
                        "Russian Federation",
                        "Brazil",
                        "India",
                        "Rest of World"
                    ],
                    "text": ["CO2"],
                    "textposition": "inside",
                    "domain": {"x": [.52, 1]},
                    "name": "CO2 Emissions",
                    "hoverinfo": "label+percent+name",
                    "hole": .4,
                    "type": "pie"
                }],
            "layout": {
                "title": "Global Emissions 1990-2011",
                "annotations": [
                    {
                        "font": {
                            "size": 20
                        },
                        "showarrow": False,
                        "text": "GHG",
                        "x": 0.20,
                        "y": 0.5
                    },
                    {
                        "font": {
                            "size": 20
                        },
                        "showarrow": False,
                        "text": "CO2",
                        "x": 0.8,
                        "y": 0.5
                    }
                ]
            }
        }
        py.plot(fig, filename='tmp/piechart_tutorial.html', auto_play=True)

    # Pie Chart Subplots
    if __name__ == '__main__':
        fig = {
            'data': [
                {
                    'labels': ['1st', '2nd', '3rd', '4th', '5th'],
                    'values': [38, 27, 18, 10, 7],
                    'type': 'pie',
                    'name': 'Starry Night',
                    'marker': {'colors': ['rgb(56, 75, 126)',
                                          'rgb(18, 36, 37)',
                                          'rgb(34, 53, 101)',
                                          'rgb(36, 55, 57)',
                                          'rgb(6, 4, 4)']},
                    'domain': {'x': [0, .48],
                               'y': [0, .49]},
                    'hoverinfo': 'label+percent+name',
                    'textinfo': 'none'
                },
                {
                    'labels': ['1st', '2nd', '3rd', '4th', '5th'],
                    'values': [28, 26, 21, 15, 10],
                    'marker': {'colors': ['rgb(177, 127, 38)',
                                          'rgb(205, 152, 36)',
                                          'rgb(99, 79, 37)',
                                          'rgb(129, 180, 179)',
                                          'rgb(124, 103, 37)']},
                    'type': 'pie',
                    'name': 'Sunflowers',
                    'domain': {'x': [.52, 1],
                               'y': [0, .49]},
                    'hoverinfo': 'label+percent+name',
                    'textinfo': 'none'

                },
                {
                    'labels': ['1st', '2nd', '3rd', '4th', '5th'],
                    'values': [38, 19, 16, 14, 13],
                    'marker': {'colors': ['rgb(33, 75, 99)',
                                          'rgb(79, 129, 102)',
                                          'rgb(151, 179, 100)',
                                          'rgb(175, 49, 35)',
                                          'rgb(36, 73, 147)']},
                    'type': 'pie',
                    'name': 'Irises',
                    'domain': {'x': [0, .48],
                               'y': [.51, 1]},
                    'hoverinfo': 'label+percent+name',
                    'textinfo': 'none'
                },
                {
                    'labels': ['1st', '2nd', '3rd', '4th', '5th'],
                    'values': [31, 24, 19, 18, 8],
                    'marker': {'colors': ['rgb(146, 123, 21)',
                                          'rgb(177, 180, 34)',
                                          'rgb(206, 206, 40)',
                                          'rgb(175, 51, 21)',
                                          'rgb(35, 36, 21)']},
                    'type': 'pie',
                    'name': 'The Night Café',
                    'domain': {'x': [.52, 1],
                               'y': [.51, 1]},
                    'hoverinfo': 'label+percent+name',
                    'textinfo': 'none'
                }
            ],
            'layout': {'title': 'Van Gogh: 5 Most Prominent Colors Shown Proportionally',
                       'showlegend': False}
        }

        py.plot(fig, filename='tmp/piechart_tutorial.html', auto_play=True)


# 7、Filled Area Plots in Python
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    # Basic Overlaid Area Chart
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[1, 2, 3, 4],
            y=[0, 2, 3, 5],
            fill='tozeroy'
        )
        trace2 = go.Scatter(
            x=[1, 2, 3, 4],
            y=[3, 5, 1, 7],
            fill='tonexty'
        )

        data = [trace1, trace2]
        py.plot(data, filename='tmp/fill_tutorial.html', auto_play=True)

    # Overlaid Area Chart Without Boundary Lines，tonexty就是邻近的y
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[1, 2, 3, 4],
            y=[0, 2, 3, 5],
            fill='tozeroy',
            mode='none'
        )
        trace2 = go.Scatter(
            x=[1, 2, 3, 4],
            y=[3, 5, 1, 7],
            fill='tonexty',
            mode='none'
        )

        data = [trace1, trace2]
        py.plot(data, filename='tmp/fill_tutorial.html', auto_play=True)

    # Interior Filling for Area Chart
    if __name__ == '__main__':
        trace0 = go.Scatter(
            x=[1, 2, 3, 4],
            y=[3, 4, 8, 3],
            fill=None,
            mode='lines',
            line=dict(
                color='rgb(143, 19, 131)',
            )
        )
        trace1 = go.Scatter(
            x=[1, 2, 3, 4],
            y=[1, 6, 2, 6],
            fill='tonexty',
            mode='lines',
            line=dict(
                color='rgb(143, 19, 131)',
            )
        )

        data = [trace0, trace1]
        py.plot(data, filename='tmp/fill_tutorial.html', auto_play=True)

    # Stacked Area Chart
    if __name__ == '__main__':
        # Add original data
        x = ['Winter', 'Spring', 'Summer', 'Fall']

        trace0 = dict(
            x=x,
            y=[40, 60, 40, 10],
            hoverinfo='x+y',
            mode='lines',
            line=dict(width=0.5,
                      color='rgb(131, 90, 241)'),
            stackgroup='one'
        )
        trace1 = dict(
            x=x,
            y=[20, 10, 10, 60],
            hoverinfo='x+y',
            mode='lines',
            line=dict(width=0.5,
                      color='rgb(111, 231, 219)'),
            stackgroup='one'
        )
        trace2 = dict(
            x=x,
            y=[40, 30, 50, 30],
            hoverinfo='x+y',
            mode='lines',
            line=dict(width=0.5,
                      color='rgb(184, 247, 212)'),
            stackgroup='one'
        )
        data = [trace0, trace1, trace2]

        fig = dict(data=data)
        py.plot(fig, filename='tmp/fill_tutorial.html', auto_play=True)


    # Stacked Area Chart with Normalized Values，stackgroup he groupnorm
    if __name__ == '__main__':
        trace0 = dict(
            x=['Winter', 'Spring', 'Summer', 'Fall'],
            y=['40', '20', '30', '40'],
            mode='lines',
            line=dict(width=0.5,
                      color='rgb(184, 247, 212)'),
            stackgroup='one',
            groupnorm='percent'
        )
        trace1 = dict(
            x=['Winter', 'Spring', 'Summer', 'Fall'],
            y=['50', '70', '40', '60'],
            mode='lines',
            line=dict(width=0.5,
                      color='rgb(111, 231, 219)'),
            stackgroup='one'
        )
        trace2 = dict(
            x=['Winter', 'Spring', 'Summer', 'Fall'],
            y=['70', '80', '60', '70'],
            mode='lines',
            line=dict(width=0.5,
                      color='rgb(127, 166, 238)'),
            stackgroup='one'
        )
        trace3 = dict(
            x=['Winter', 'Spring', 'Summer', 'Fall'],
            y=['100', '100', '100', '100'],
            mode='lines',
            line=dict(width=0.5,
                      color='rgb(131, 90, 241)'),
            stackgroup='one'
        )
        data = [trace0, trace1, trace2, trace3]
        layout = go.Layout(
            showlegend=True,
            xaxis=dict(
                type='category',
            ),
            yaxis=dict(
                type='linear',
                range=[1, 100],
                dtick=20,
                ticksuffix='%'
            )
        )
        fig = dict(data=data, layout=layout)
        py.plot(fig, filename='tmp/fill_tutorial.html', auto_play=True)

    # Select Hover Points
    if __name__ == '__main__':
        trace0 = go.Scatter(
            x=[0, 0.5, 1, 1.5, 2],
            y=[0, 1, 2, 1, 0],
            fill='toself',
            fillcolor='#ab63fa',
            hoveron='points+fills',
            line=dict(
                color='#ab63fa'
            ),
            text="Points + Fills",
            hoverinfo='text'
        )

        trace1 = go.Scatter(
            x=[3, 3.5, 4, 4.5, 5],
            y=[0, 1, 2, 1, 0],
            fill='toself',
            fillcolor='#e763fa',
            hoveron='points',
            line=dict(
                color='#e763fa'
            ),
            text="Points only",
            hoverinfo='text'
        )

        data = [trace0, trace1]

        layout = go.Layout(
            title="hover on <i>points</i> or <i>fill</i>",
            xaxis=dict(
                range=[0, 5.2]
            ),
            yaxis=dict(
                range=[0, 3]
            )
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/fill_tutorial.html', auto_play=True)

# 8、Dot Plots in Python
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    # basic
    if __name__ == '__main__':
        trace1 = {"x": [72, 67, 73, 80, 76, 79, 84, 78, 86, 93, 94, 90, 92, 96, 94, 112],
                  "y": ["Brown", "NYU", "Notre Dame", "Cornell", "Tufts", "Yale",
                        "Dartmouth", "Chicago", "Columbia", "Duke", "Georgetown",
                        "Princeton", "U.Penn", "Stanford", "MIT", "Harvard"],
                  "marker": {"color": "pink", "size": 12},
                  "mode": "markers",
                  "name": "Women",
                  "type": "scatter"
                  }

        trace2 = {"x": [92, 94, 100, 107, 112, 114, 114, 118, 119, 124, 131, 137, 141, 151, 152, 165],
                  "y": ["Brown", "NYU", "Notre Dame", "Cornell", "Tufts", "Yale",
                        "Dartmouth", "Chicago", "Columbia", "Duke", "Georgetown",
                        "Princeton", "U.Penn", "Stanford", "MIT", "Harvard"],
                  "marker": {"color": "blue", "size": 12},
                  "mode": "markers",
                  "name": "Men",
                  "type": "scatter",
                  }

        data = [trace1, trace2]
        layout = {"title": "Gender Earnings Disparity",
                  "xaxis": {"title": "Annual Salary (in thousands)", },
                  "yaxis": {"title": "School"}}

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/dot_tutorial.html', auto_play=True)


    # Styled Categorical Dot Plot
    if __name__ == '__main__':
        country = ['Switzerland (2011)', 'Chile (2013)', 'Japan (2014)',
                   'United States (2012)', 'Slovenia (2014)', 'Canada (2011)',
                   'Poland (2010)', 'Estonia (2015)', 'Luxembourg (2013)', 'Portugal (2011)']
        voting_pop = [40, 45.7, 52, 53.6, 54.1, 54.2, 54.5, 54.7, 55.1, 56.6]
        reg_voters = [49.1, 42, 52.7, 84.3, 51.7, 61.1, 55.3, 64.2, 91.1, 58.9]

        trace0 = go.Scatter(
            x=voting_pop,
            y=country,
            mode='markers',
            name='Percent of estimated voting age population',
            marker=dict(
                color='rgba(156, 165, 196, 0.95)',
                line=dict(
                    color='rgba(156, 165, 196, 1.0)',
                    width=1,
                ),
                symbol='circle',
                size=16,
            )
        )
        trace1 = go.Scatter(
            x=reg_voters,
            y=country,
            mode='markers',
            name='Percent of estimated registered voters',
            marker=dict(
                color='rgba(204, 204, 204, 0.95)',
                line=dict(
                    color='rgba(217, 217, 217, 1.0)',
                    width=1,
                ),
                symbol='circle',
                size=16,
            )
        )

        data = [trace0, trace1]
        layout = go.Layout(
            title="Votes cast for ten lowest voting age population in OECD countries",
            xaxis=dict(
                showgrid=False,
                showline=True,
                linecolor='rgb(102, 102, 102)',
                titlefont=dict(
                    color='rgb(204, 204, 204)'
                ),
                tickfont=dict(
                    color='rgb(102, 102, 102)',
                ),
                showticklabels=True,
                dtick=10,
                ticks='outside',
                tickcolor='rgb(102, 102, 102)',
            ),
            margin=dict(
                l=140,
                r=40,
                b=50,
                t=80
            ),
            legend=dict(
                font=dict(
                    size=10,
                ),
                yanchor='middle',
                xanchor='right',
            ),
            width=800,
            height=600,
            paper_bgcolor='rgb(254, 247, 234)',
            plot_bgcolor='rgb(254, 247, 234)',
            hovermode='closest',
        )
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='tmp/dot_tutorial.html', auto_play=True)


# 9、Table
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    # basic，最基础的也能移动列
    if __name__ == '__main__':
        trace = go.Table(
            header=dict(values=['A Scores', 'B Scores']),
            cells=dict(values=[[100, 90, 80, 90],
                               [95, 85, 75, 95]]))

        data = [trace]
        py.plot(data, filename='tmp/table_tutorial.html', auto_play=True)


    # Styled Table，layout = dict(width=500, height=300)定义高度和宽度
    if __name__ == '__main__':
        trace = go.Table(
            header=dict(values=['A Scores', 'B Scores'],
                        line=dict(color='#7D7F80'),
                        fill=dict(color='#a1c3d1'),
                        align=['left'] * 5),
            cells=dict(values=[[100, 90, 80, 90],
                               [95, 85, 75, 95]],
                       line=dict(color='#7D7F80'),
                       fill=dict(color='#EDFAFF'),
                       align=['left'] * 5))

        layout = dict(width=500, height=300)
        data = [trace]
        fig = dict(data=data, layout=layout)
        py.plot(fig, filename='tmp/table_tutorial.html', auto_play=True)


    # Use a Panda's Dataframe
    if __name__ == '__main__':
        import pandas as pd

        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')

        trace = go.Table(
            header=dict(values=list(df.columns),
                        fill=dict(color='#C2D4FF'),
                        align=['left'] * 5),
            cells=dict(values=[df.Rank, df.State, df.Postal, df.Population],
                       fill=dict(color='#F5F8FF'),
                       align=['left'] * 5))

        data = [trace]
        py.plot(data, filename='tmp/table_tutorial.html', auto_play=True)


    # Changing Row and Column Size，这里定义宽高 columnorder=[1, 2], columnwidth=[80, 400],
    if __name__ == '__main__':
        values = [['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL<br>EXPENSES</b>'],
                  [
                       "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
                       "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
                       "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
                       "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
                       "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad"
                  ]
                 ]

        trace0 = go.Table(
            columnorder=[1, 2],
            columnwidth=[80, 400],
            header=dict(
                values=[['<b>EXPENSES</b><br>as of July 2017'],
                        ['<b>DESCRIPTION</b>']],
                line=dict(color='#506784'),
                fill=dict(color='#119DFF'),
                align=['left', 'center'],
                font=dict(color='white', size=12),
                height=40
            ),
            cells=dict(
                values=values,
                line=dict(color='#506784'),
                fill=dict(color=['#25FEFD', 'white']),
                align=['left', 'center'],
                font=dict(color='#506784', size=12),
                height=30
            ))

        data = [trace0]
        py.plot(data, filename='tmp/table_tutorial.html', auto_play=True)


    # Alternating Row Colors
    if __name__ == '__main__':
        headerColor = 'grey'
        rowEvenColor = 'lightgrey'
        rowOddColor = 'white'

        trace0 = go.Table(
            header=dict(
                values=[['<b>EXPENSES</b>'],
                        ['<b>Q1</b>'],
                        ['<b>Q2</b>'],
                        ['<b>Q3</b>'],
                        ['<b>Q4</b>']],
                line=dict(color='#506784'),
                fill=dict(color=headerColor),
                align=['left', 'center'],
                font=dict(color='white', size=12)
            ),
            cells=dict(
                values=[
                    ['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL</b>'],
                    [1200000, 20000, 80000, 2000, 12120000],
                    [1300000, 20000, 70000, 2000, 130902000],
                    [1300000, 20000, 120000, 2000, 131222000],
                    [1400000, 20000, 90000, 2000, 14102000]
                ],
                line=dict(color='#506784'),
                fill=dict(color=[rowOddColor, rowEvenColor, rowOddColor, rowEvenColor, rowOddColor]),
                align=['left', 'center'],
                font=dict(color='#506784', size=11)
            ))

        data = [trace0]

        py.plot(data, filename='tmp/table_tutorial.html', auto_play=True)

    # Row Color Based on Variable
    if __name__ == '__main__':
        import pandas as pd
        import colorlover as cl

        colors = cl.scales['5']['seq']['Blues']
        data = {'Year': [2010, 2011, 2012, 2013, 2014],
                'Color': colors}
        df = pd.DataFrame(data)

        trace0 = go.Table(
            header=dict(
                values=["Color", "<b>YEAR</b>"],
                line=dict(color='white'),
                fill=dict(color='white'),
                align=['center'],
                font=dict(color='black', size=12)
            ),
            cells=dict(
                values=[df.Color, df.Year],
                line=dict(color=[df.Color]),
                fill=dict(color=[df.Color]),
                align='center',
                font=dict(color='black', size=11)
            ))

        data = [trace0]
        py.plot(data, filename='tmp/table_tutorial.html', auto_play=True)


    # Cell Color Based on Variable
    if __name__ == '__main__':
        import numpy as np
        import colorlover as cl

        colors = cl.scales['9']['seq']['Reds']
        a = np.random.randint(low=0, high=9, size=10)
        b = np.random.randint(low=0, high=9, size=10)
        c = np.random.randint(low=0, high=9, size=10)

        trace0 = go.Table(
            header=dict(
                values=['<b>Column A</b>', '<b>Column B</b>', '<b>Column C</b>'],
                line=dict(color='white'),
                fill=dict(color='white'),
                align='center',
                font=dict(color='black', size=12)
            ),
            cells=dict(
                values=[a, b, c],
                line=dict(color=[np.array(colors)[a], np.array(colors)[b],
                                 np.array(colors)[c]]),
                fill=dict(color=[np.array(colors)[a], np.array(colors)[b],
                                 np.array(colors)[c]]),
                align='center',
                font=dict(color='white', size=11)
            ))

        data = [trace0]

        py.plot(data, filename='tmp/table_tutorial.html', auto_play=True)


# 10、Multiple Chart Types in Python
if __name__ == '__main__':
    import plotly.offline as py
    import plotly.graph_objs as go

    # Line Chart and a Bar Chart
    if __name__ == '__main__':
        trace1 = go.Scatter(
            x=[0, 1, 2, 3, 4, 5],
            y=[1.5, 1, 1.3, 0.7, 0.8, 0.9]
        )
        trace2 = go.Bar(
            x=[0, 1, 2, 3, 4, 5],
            y=[1, 0.5, 0.7, -1.2, 0.3, 0.4]
        )

        data = [trace1, trace2]
        py.plot(data, filename='tmp/multi_tutorial.html', auto_play=True)


    # A Contour and Scatter Plot of the Method of Steepest Descent
    if __name__ == '__main__':
        import json
        import six.moves.urllib

        response = six.moves.urllib.request.urlopen(
            'https://raw.githubusercontent.com/plotly/datasets/master/steepest.json')
        data = json.load(response)

        trace1 = go.Contour(
            z=data['contour_z'][0],
            y=data['contour_y'][0],
            x=data['contour_x'][0],
            ncontours=30,
            showscale=False
        )
        trace2 = go.Scatter(
            x=data['trace_x'],
            y=data['trace_y'],
            mode='markers+lines',
            name='steepest',
            line=dict(
                color='black'
            )
        )

        data = [trace1, trace2]
        py.plot(data, filename='tmp/multi_tutorial.html', auto_play=True)
