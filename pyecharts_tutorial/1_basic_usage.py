
# 第一个chart
if __name__ == '__main__':
    from pyecharts import Bar

    bar = Bar("我的第一个图表",
              "这里是副标题")
    bar.use_theme('dark')  # 0.5.2+才有
    bar.add("服装",
            ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
            [5, 20, 36, 10, 75, 90],
            # is_more_utils=True,  # 如果想要提供更多实用工具按钮
            )
    bar.render(path='tmp/echart.html',)  # 生成本地 HTML 文件


# 多次显示chart
if __name__ == '__main__':
    from pyecharts import Bar, Line
    from pyecharts.engine import create_default_environment

    bar = Bar("我的第一个图表", "这里是副标题")
    bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])

    line = Line("我的第一个图表", "这里是副标题")
    line.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])

    env = create_default_environment("html")
    # 为渲染创建一个默认配置环境
    # create_default_environment(filet_ype)
    # file_type: 'html', 'svg', 'png', 'jpeg', 'gif' or 'pdf'

    env.render_chart_to_file(bar, path='tmp/bar.html')
    env.render_chart_to_file(line, path='tmp/line.html')
    # 相比第一个例子，该代码只是使用同一个引擎对象，减少了部分重复操作，速度有所提高。