
'''
官方教程
https://plot.ly/python/
'''

import plotly.offline as py
import plotly.graph_objs as go

# 1、一个综合的例子-bar
if __name__ == '__main__1':
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
    # 附带hoverinfo 'x'只显示x，name是显示系列名称，text是显示x轴坐标对应的名称
    if __name__ == '__main__':
        N = 500

        trace0 = go.Scatter(
            x=np.random.randn(N),
            y=np.random.randn(N) + 2,
            # visible=False,
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
            hoverinfo='name',

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

    # 全部的参数解析 https://plot.ly/python/reference/#scattergl


