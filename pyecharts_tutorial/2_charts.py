
# 1、bar
if __name__ == '__main__':

    import pyecharts as echarts

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]

    # is_stack 实现数据堆叠
    if __name__ == '__main__':

        bar = echarts.Bar("柱状图数据堆叠示例")
        bar.add(
            "商家A",
            attr,
            v1,
            is_stack=True
        )
        bar.add(
            "商家B",
            attr,
            v2,
            is_stack=True,
            is_more_utils=True,
        )
        bar.render(path='tmp/bar.html')

    # 使用标记点和标记线
    if __name__ == '__main__':
        bar = echarts.Bar("标记线和标记点示例")
        bar.add("商家A", attr, v1,
                mark_point=["average"], # 这个是str化的函数
        )
        bar.add("商家B", attr, v2,
                mark_line=["min", "max"],
        )
        bar.render(path='tmp/bar.html')

    # is_convert 交换 XY 轴
    if __name__ == '__main__':
        bar = echarts.Bar("x 轴和 y 轴交换")
        bar.add("商家A", attr, v1)
        bar.add("商家B", attr, v2,
                is_convert=True,  # 图的全局设置
                )
        bar.render(path='tmp/bar.html')

    # dataZoom 效果，'slider' 类型
    if __name__ == '__main__':
        import random

        attr = ["{}天".format(i) for i in range(30)]
        v1 = [random.randint(1, 30) for _ in range(30)]
        bar = echarts.Bar("Bar - datazoom - slider 示例")
        bar.add("",
                attr,
                v1,
                is_label_show=True,
                is_datazoom_show=True
        )
        bar.render(path='tmp/bar.html')

    # dataZoom 效果，'inside' 类型
    if __name__ == '__main__':
        attr = ["{}天".format(i) for i in range(30)]
        v1 = [random.randint(1, 30) for _ in range(30)]
        bar = echarts.Bar("Bar - datazoom - inside 示例")
        bar.add(
            "",
            attr,
            v1,
            is_datazoom_show=True,
            datazoom_type="inside",
            datazoom_range=[10, 25],
        )
        bar.render(path='tmp/bar.html')

    # dataZoom 效果，'both' 类型
    if __name__ == '__main__':
        attr = ["{}天".format(i) for i in range(30)]
        v1 = [random.randint(1, 30) for _ in range(30)]
        bar = echarts.Bar("Bar - datazoom - inside 示例")
        bar.add(
            "",
            attr,
            v1,
            is_datazoom_show=True,
            datazoom_type="both",
            datazoom_range=[10, 25],
        )
        bar.render(path='tmp/bar.html')

    # 多 dataZoom 效果，效果同时支持 X、Y 轴
    if __name__ == '__main__':
        import random
        days = ["{}天".format(i) for i in range(30)]
        days_v1 = [random.randint(1, 30) for _ in range(30)]
        bar = echarts.Bar("Bar - datazoom - xaxis/yaxis 示例")
        bar.add(
            "",
            days,
            days_v1,
            # 默认为 X 轴，横向
            is_datazoom_show=True,
            datazoom_type="slider",
            datazoom_range=[10, 25],
            # 新增额外的 dataZoom 控制条，纵向
            is_datazoom_extra_show=True,
            datazoom_extra_type="slider",
            datazoom_extra_range=[10, 25],
            is_toolbox_show=False,
        )
        bar.render(path='tmp/bar.html')

    # 当 x 轴或者 y 轴的标签因为过于密集而导致全部显示出来会重叠的话，可采用使标签旋转的方法
    if __name__ == '__main__':
        attr = ["{}天".format(i) for i in range(20)]
        v1 = [random.randint(1, 20) for _ in range(20)]
        bar = echarts.Bar("坐标轴标签旋转示例")
        bar.add("", attr, v1,
                xaxis_interval=0,
                xaxis_rotate=30,
                yaxis_rotate=30,
                # label_color='green',
        )
        bar.render(path='tmp/bar.html')

    # 瀑布图示例
    if __name__ == '__main__':
        attr = ["{}月".format(i) for i in range(1, 8)]
        v1 = [0, 100, 200, 300, 400, 220, 250]
        v2 = [1000, 800, 600, 500, 450, 400, 300]
        bar = echarts.Bar("瀑布图示例")
        # 利用第一个 add() 图例的颜色为透明，即 'rgba(0,0,0,0)'，并且设置 is_stack 标志为 True
        bar.add("", attr, v1, label_color=['rgba(0,0,0,0)'], is_stack=True)
        bar.add("月份", attr, v2,
                is_label_show=True,
                is_stack=True,
                label_pos='inside')
        bar.render(path='tmp/bar.html')

    # 直方图示例，相同的x轴会被归并
    if __name__ == '__main__':
        attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        v1 = [5, 20, 36, 10, 75, 90]
        v2 = [10, 25, 8, 60, 20, 80]
        bar = echarts.Bar("直方图示例")
        bar.add("", attr * 2, v1 + v2, bar_category_gap=0)
        bar.render(path='tmp/bar.html')

    # 某地的降水量和蒸发量柱状图
    if __name__ == '__main__':
        attr = ["{}月".format(i) for i in range(1, 13)]
        v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
        v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
        bar = echarts.Bar("柱状图示例")
        bar.add("蒸发量", attr, v1, mark_line=["average"], mark_point=["max", "min"])
        bar.add("降水量", attr, v2, mark_line=["average"], mark_point=["max", "min"])
        bar.render(path='tmp/bar.html')

    # 额外的文本标签，@todo
    if __name__ == '__main__':
        CLOTHES = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        clothes_v1 = [5, 20, 36, 10, 75, 90]
        clothes_v2 = [10, 25, 8, 60, 20, 80]
        bar = echarts.Bar("柱状图", extra_html_text_label=["bar_extra_html_text_label", "color:red"])
        bar.add("商家A", CLOTHES, clothes_v1, is_stack=True)
        bar.add("商家B", CLOTHES, clothes_v2, is_stack=True)
        bar.render(path='tmp/bar.html')

    # 控制 X/Y 轴坐标轴线颜色以及宽度
    if __name__ == '__main__':
        CLOTHES = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        clothes_v1 = [5, 20, 36, 10, 75, 90]
        clothes_v2 = [10, 25, 8, 60, 20, 80]
        bar = echarts.Bar("柱状图")
        bar.add(
            "商家A",
            CLOTHES,
            clothes_v1,
            xaxis_line_color="green",
            xaxis_line_width=5,
            xaxis_label_textcolor="black",
        )
        bar.render(path='tmp/bar.html')

    # 进行两次或多次 add 的时候，有一次的某项数据缺失，可用 0 填充
    if __name__ == '__main__':
        CLOTHES = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        clothes_v1 = [5, 20, 36, 10, 75, 90]
        clothes_v2 = [10, 25, 8, 60, 20, 80]
        bar = echarts.Bar("折线图示例")
        bar.add("商家A", CLOTHES, clothes_v1)
        bar.add("商家B", CLOTHES, [55, 60, 16, 20, 0, 0])
        bar.render(path='tmp/bar.html')


# 2、bar 3D
if __name__ == '__main__':
    import pyecharts as echarts

    x_axis = [
        "12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
        "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"
    ]
    y_axis = [
        "Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"
    ]
    data = [
        [0, 0, 5], [0, 1, 1], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0],
        [0, 6, 0], [0, 7, 0], [0, 8, 0], [0, 9, 0], [0, 10, 0], [0, 11, 2],
        [0, 12, 4], [0, 13, 1], [0, 14, 1], [0, 15, 3], [0, 16, 4], [0, 17, 6],
        [0, 18, 4], [0, 19, 4], [0, 20, 3], [0, 21, 3], [0, 22, 2], [0, 23, 5],
        [1, 0, 7], [1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0],
        [1, 6, 0], [1, 7, 0], [1, 8, 0], [1, 9, 0], [1, 10, 5], [1, 11, 2],
        [1, 12, 2], [1, 13, 6], [1, 14, 9], [1, 15, 11], [1, 16, 6], [1, 17, 7],
        [1, 18, 8], [1, 19, 12], [1, 20, 5], [1, 21, 5], [1, 22, 7], [1, 23, 2],
        [2, 0, 1], [2, 1, 1], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0],
        [2, 6, 0], [2, 7, 0], [2, 8, 0], [2, 9, 0], [2, 10, 3], [2, 11, 2],
        [2, 12, 1], [2, 13, 9], [2, 14, 8], [2, 15, 10], [2, 16, 6], [2, 17, 5],
        [2, 18, 5], [2, 19, 5], [2, 20, 7], [2, 21, 4], [2, 22, 2], [2, 23, 4],
        [3, 0, 7], [3, 1, 3], [3, 2, 0], [3, 3, 0], [3, 4, 0], [3, 5, 0],
        [3, 6, 0], [3, 7, 0], [3, 8, 1], [3, 9, 0], [3, 10, 5], [3, 11, 4],
        [3, 12, 7], [3, 13, 14], [3, 14, 13], [3, 15, 12], [3, 16, 9], [3, 17, 5],
        [3, 18, 5], [3, 19, 10], [3, 20, 6], [3, 21, 4], [3, 22, 4], [3, 23, 1],
        [4, 0, 1], [4, 1, 3], [4, 2, 0], [4, 3, 0], [4, 4, 0], [4, 5, 1],
        [4, 6, 0], [4, 7, 0], [4, 8, 0], [4, 9, 2], [4, 10, 4], [4, 11, 4],
        [4, 12, 2], [4, 13, 4], [4, 14, 4], [4, 15, 14], [4, 16, 12], [4, 17, 1],
        [4, 18, 8], [4, 19, 5], [4, 20, 3], [4, 21, 7], [4, 22, 3], [4, 23, 0],
        [5, 0, 2], [5, 1, 1], [5, 2, 0], [5, 3, 3], [5, 4, 0], [5, 5, 0],
        [5, 6, 0], [5, 7, 0], [5, 8, 2], [5, 9, 0], [5, 10, 4], [5, 11, 1],
        [5, 12, 5], [5, 13, 10], [5, 14, 5], [5, 15, 7], [5, 16, 11], [5, 17, 6],
        [5, 18, 0], [5, 19, 5], [5, 20, 3], [5, 21, 4], [5, 22, 2], [5, 23, 0],
        [6, 0, 1], [6, 1, 0], [6, 2, 0], [6, 3, 0], [6, 4, 0], [6, 5, 0],
        [6, 6, 0], [6, 7, 0], [6, 8, 0], [6, 9, 0], [6, 10, 1], [6, 11, 0],
        [6, 12, 2], [6, 13, 1], [6, 14, 3], [6, 15, 4], [6, 16, 0], [6, 17, 0],
        [6, 18, 0], [6, 19, 0], [6, 20, 1], [6, 21, 2], [6, 22, 2], [6, 23, 6]
    ]
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
                   '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']


    # Bar3D（3D 柱状图）
    if __name__ == '__main__':
        bar3d = echarts.Bar3D("3D 柱状图示例", width=1200, height=600)

        bar3d.add(
            "",
            x_axis,
            y_axis,
            [[d[1], d[0], d[2]] for d in data],
            is_visualmap=True,
            visual_range=[0, 20],
            visual_range_color=range_color,
            grid3d_width=200,
            grid3d_depth=80,
        )
        bar3d.render(path='tmp/bar3D.html')

    # 设置 grid3d_shading 可以让柱状更真实
    if __name__ == '__main__':
        bar3d = echarts.Bar3D("3D 柱状图示例", width=1200, height=600)
        bar3d.add(
            "",
            x_axis,
            y_axis,
            [[d[1], d[0], d[2]] for d in data],
            is_visualmap=True,
            visual_range=[0, 20],
            visual_range_color=range_color,
            grid3d_width=200,
            grid3d_depth=80,
            grid3d_shading="lambert",
        )
        bar3d.render(path='tmp/bar3D.html')

    # 设置 is_grid3d_rotate 启动自动旋转功能，拖动过之后自动旋转就没用了，重新切入浏览器又起作用了
    if __name__ == '__main__':
        bar3d = echarts.Bar3D("3D 柱状图示例", width=1200, height=600)
        bar3d.add(
            "",
            x_axis,
            y_axis,
            [[d[1], d[0], d[2]] for d in data],
            is_visualmap=True,
            visual_range=[0, 20],
            visual_range_color=range_color,
            grid3d_width=200,
            grid3d_depth=80,
            is_grid3d_rotate=True,
        )
        bar3d.render(path='tmp/bar3D.html')

    # 设置 grid3d_rotate_speed 调节旋转速度
    if __name__ == '__main__':
        bar3d = echarts.Bar3D("3D 柱状图示例", width=1200, height=600)
        bar3d.add(
            "",
            x_axis,
            y_axis,
            [[d[1], d[0], d[2]] for d in data],
            is_visualmap=True,
            visual_range=[0, 20],
            visual_range_color=range_color,
            grid3d_width=200,
            grid3d_depth=80,
            is_grid3d_rotate=True,
            grid3d_rotate_speed=180,
        )
        bar3d.render(path='tmp/bar3D.html')


# 3、Boxplot（箱形图）
if __name__ == '__main__':
    # 箱形图是一种用作显示一组数据分散情况资料的统计图。它能显示出一组数据的最大值、最小值、中位数、下四分位数及上四分位数。
    import pyecharts as echarts

    x_axis = ['expr1', 'expr2', 'expr3', 'expr4', 'expr5']
    y_axis = [
        [850, 740, 900, 1070, 930, 850, 950, 980, 980, 880,
         1000, 980, 930, 650, 760, 810, 1000, 1000, 960, 960],
        [960, 940, 960, 940, 880, 800, 850, 880, 900, 840,
         830, 790, 810, 880, 880, 830, 800, 790, 760, 800],
        [880, 880, 880, 860, 720, 720, 620, 860, 970, 950,
         880, 910, 850, 870, 840, 840, 850, 840, 840, 840],
        [890, 810, 810, 820, 800, 770, 760, 740, 750, 760,
         910, 920, 890, 860, 880, 720, 840, 850, 850, 780],
        [890, 840, 780, 810, 760, 810, 790, 810, 820, 850,
         870, 870, 810, 740, 810, 940, 950, 800, 810, 870]
    ]

    # basic
    if __name__ == '__main__':
        boxplot = echarts.Boxplot("箱形图")
        _yaxis = boxplot.prepare_data(y_axis)  # 转换数据，计算每组的
        boxplot.add("boxplot", x_axis, _yaxis)
        boxplot.render(path='tmp/boxplot.html')

    # 或者直接在 add() 中转换
    if __name__ == '__main__':
        boxplot = echarts.Boxplot("箱形图")
        x_axis = ['expr1', 'expr2']
        y_axis1 = [
            [850, 740, 900, 1070, 930, 850, 950, 980, 980, 880,
             1000, 980, 930, 650, 760, 810, 1000, 1000, 960, 960],
            [960, 940, 960, 940, 880, 800, 850, 880, 900, 840,
             830, 790, 810, 880, 880, 830, 800, 790, 760, 800],
        ]
        y_axis2 = [
            [890, 810, 810, 820, 800, 770, 760, 740, 750, 760,
             910, 920, 890, 860, 880, 720, 840, 850, 850, 780],
            [890, 840, 780, 810, 760, 810, 790, 810, 820, 850,
             870, 870, 810, 740, 810, 940, 950, 800, 810, 870]
        ]
        boxplot.add("category1", x_axis, boxplot.prepare_data(y_axis1))
        boxplot.add("category2", x_axis, boxplot.prepare_data(y_axis2))
        boxplot.render(path='tmp/boxplot.html')


# 4、EffectScatter（带有涟漪特效动画的散点图）
if __name__ == '__main__':
    import pyecharts as echarts

    # basic
    if __name__ == '__main__':
        v1 = [10, 20, 30, 40, 50, 60]
        v2 = [25, 20, 15, 10, 60, 33]
        es = echarts.EffectScatter("动态散点图示例")
        es.add("effectScatter", v1, v2)
        es.render(path='tmp/es.html')

    # 动态散点图各种图形
    if __name__ == '__main__':
        es = echarts.EffectScatter("动态散点图各种图形示例")
        es.add(
            "",
            [10],
            [10],
            symbol_size=20,
            effect_scale=3.5,
            effect_period=3,
            symbol="pin",
        )
        es.add(
            "",
            [20],
            [20],
            symbol_size=12,
            effect_scale=4.5,
            effect_period=4,
            symbol="rect",
        )
        es.add(
            "",
            [30],
            [30],
            symbol_size=30,
            effect_scale=5.5,
            effect_period=5,
            symbol="roundRect",
        )
        es.add(
            "",
            [40],
            [40],
            symbol_size=10,
            effect_scale=6.5,
            effect_brushtype="fill",
            symbol="diamond",
        )
        es.add(
            "",
            [50],
            [50],
            symbol_size=16,
            effect_scale=5.5,
            effect_period=3,
            symbol="arrow",
        )
        es.add(
            "",
            [60],
            [60],
            symbol_size=6,
            effect_scale=2.5,
            effect_period=3,
            symbol="triangle",
        )
        es.render(path='tmp/es.html')


# 5 Funnel（漏斗图）
if __name__ == '__main__':
    import pyecharts as echarts

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    value = [20, 40, 60, 80, 100, 120]
    # 标签显示在内部
    if __name__ == '__main__':

        funnel = echarts.Funnel("漏斗图示例")
        funnel.add(
            "商品",
            attr,
            value,
            is_label_show=True,
            label_pos="inside",
            label_text_color="#fff",
        )
        funnel.render(path='tmp/funnel.html')

    # 标签显示在外部
    if __name__ == '__main__':
        funnel = echarts.Funnel("漏斗图示例", width=600, height=400, title_pos='center')
        funnel.add(
            "商品",
            attr,
            value,
            is_label_show=True,
            label_pos="outside",
            legend_orient="vertical",
            legend_pos="left",
        )
        funnel.render(path='tmp/funnel.html')

    # 数据按升序排序
    if __name__ == '__main__':
        funnel = echarts.Funnel("漏斗图示例", width=600, height=400, title_pos='center')
        funnel.add(
            "商品",
            attr,
            value,
            is_label_show=True,
            label_pos="inside",
            label_text_color="#fff",
            funnel_sort="ascending"
        )
        funnel.render(path='tmp/funnel.html')

    # 不排序数据
    if __name__ == '__main__':
        funnel = echarts.Funnel("漏斗图示例", width=600, height=400, title_pos='center')
        funnel.add(
            "商品",
            attr,
            value,
            is_label_show=True,
            label_pos="inside",
            label_text_color="#fff",
            funnel_sort="none"
        )
        funnel.render(path='tmp/funnel.html')

    # 指定图形间隔
    if __name__ == '__main__':
        funnel = echarts.Funnel("漏斗图示例", width=600, height=400, title_pos='center')
        funnel.add(
            "商品",
            attr,
            value,
            is_label_show=True,
            label_pos="inside",
            label_text_color="#fff",
            funnel_sort="ascending",
            funnel_gap=5,
        )
        funnel.render(path='tmp/funnel.html')


# 6 Gauge（仪表盘）
if __name__ == '__main__':
    import pyecharts as echarts

    # basic
    if __name__ == '__main__':
        gauge = echarts.Gauge("仪表盘示例")
        gauge.add("业务指标", "完成率", 66.66)
        gauge.render(path='tmp/gauge.html')

    # 大的
    if __name__ == '__main__':
        gauge = echarts.Gauge("仪表盘示例")
        gauge.add(
            "业务指标",
            "完成率",
            166.66,
            angle_range=[180, 0],
            scale_range=[0, 200],
            is_legend_show=False,
        )
        gauge.render(path='tmp/gauge.html')


# 7 Geo（地理坐标系）
if __name__ == '__main__':
    import pyecharts as echarts

    data = [
        ("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15),
        ("赤峰", 16), ("青岛", 18), ("乳山", 18), ("金昌", 19), ("泉州", 21), ("莱西", 21),
        ("日照", 21), ("胶南", 22), ("南通", 23), ("拉萨", 24), ("云浮", 24), ("梅州", 25),
        ("文登", 25), ("上海", 25), ("攀枝花", 25), ("威海", 25), ("承德", 25), ("厦门", 26),
        ("汕尾", 26), ("潮州", 26), ("丹东", 27), ("太仓", 27), ("曲靖", 27), ("烟台", 28),
        ("福州", 29), ("瓦房店", 30), ("即墨", 30), ("抚顺", 31), ("玉溪", 31), ("张家口", 31),
        ("阳泉", 31), ("莱州", 32), ("湖州", 32), ("汕头", 32), ("昆山", 33), ("宁波", 33),
        ("湛江", 33), ("揭阳", 34), ("荣成", 34), ("连云港", 35), ("葫芦岛", 35), ("常熟", 36),
        ("东莞", 36), ("河源", 36), ("淮安", 36), ("泰州", 36), ("南宁", 37), ("营口", 37),
        ("惠州", 37), ("江阴", 37), ("蓬莱", 37), ("韶关", 38), ("嘉峪关", 38), ("广州", 38),
        ("延安", 38), ("太原", 39), ("清远", 39), ("中山", 39), ("昆明", 39), ("寿光", 40),
        ("盘锦", 40), ("长治", 41), ("深圳", 41), ("珠海", 42), ("宿迁", 43), ("咸阳", 43),
        ("铜川", 44), ("平度", 44), ("佛山", 44), ("海口", 44), ("江门", 45), ("章丘", 45),
        ("肇庆", 46), ("大连", 47), ("临汾", 47), ("吴江", 47), ("石嘴山", 49), ("沈阳", 50),
        ("苏州", 50), ("茂名", 50), ("嘉兴", 51), ("长春", 51), ("胶州", 52), ("银川", 52),
        ("张家港", 52), ("三门峡", 53), ("锦州", 54), ("南昌", 54), ("柳州", 54), ("三亚", 54),
        ("自贡", 56), ("吉林", 56), ("阳江", 57), ("泸州", 57), ("西宁", 57), ("宜宾", 58),
        ("呼和浩特", 58), ("成都", 58), ("大同", 58), ("镇江", 59), ("桂林", 59), ("张家界", 59),
        ("宜兴", 59), ("北海", 60), ("西安", 61), ("金坛", 62), ("东营", 62), ("牡丹江", 63),
        ("遵义", 63), ("绍兴", 63), ("扬州", 64), ("常州", 64), ("潍坊", 65), ("重庆", 66),
        ("台州", 67), ("南京", 67), ("滨州", 70), ("贵阳", 71), ("无锡", 71), ("本溪", 71),
        ("克拉玛依", 72), ("渭南", 72), ("马鞍山", 72), ("宝鸡", 72), ("焦作", 75), ("句容", 75),
        ("北京", 79), ("徐州", 79), ("衡水", 80), ("包头", 80), ("绵阳", 80), ("乌鲁木齐", 84),
        ("枣庄", 84), ("杭州", 84), ("淄博", 85), ("鞍山", 86), ("溧阳", 86), ("库尔勒", 86),
        ("安阳", 90), ("开封", 90), ("济南", 92), ("德阳", 93), ("温州", 95), ("九江", 96),
        ("邯郸", 98), ("临安", 99), ("兰州", 99), ("沧州", 100), ("临沂", 103), ("南充", 104),
        ("天津", 105), ("富阳", 106), ("泰安", 112), ("诸暨", 112), ("郑州", 113), ("哈尔滨", 114),
        ("聊城", 116), ("芜湖", 117), ("唐山", 119), ("平顶山", 119), ("邢台", 119), ("德州", 120),
        ("济宁", 120), ("荆州", 127), ("宜昌", 130), ("义乌", 132), ("丽水", 133), ("洛阳", 134),
        ("秦皇岛", 136), ("株洲", 143), ("石家庄", 147), ("莱芜", 148), ("常德", 152), ("保定", 153),
        ("湘潭", 154), ("金华", 157), ("岳阳", 169), ("长沙", 175), ("衢州", 177), ("廊坊", 193),
        ("菏泽", 194), ("合肥", 229), ("武汉", 273), ("大庆", 279)]
    # Scatter 类型（连续型）
    if __name__ == '__main__':
        geo = echarts.Geo(
            "全国主要城市空气质量",
            "data from pm2.5",
            title_color="#fff",
            title_pos="center",
            width=1200,
            height=600,
            background_color="#404a59",
        )
        attr, value = geo.cast(data)
        geo.add(
            "",
            attr,
            value,
            visual_range=[0, 200],
            visual_text_color="#fff",
            symbol_size=15,
            is_visualmap=True,
        )
        geo.render(path='tmp/geo.html')

    # Scatter 类型（分段型）
    if __name__ == '__main__':
        geo = echarts.Geo(
            "全国主要城市空气质量",
            "data from pm2.5",
            title_color="#fff",
            title_pos="center",
            width=1200,
            height=600,
            background_color="#404a59",
        )
        attr, value = geo.cast(data)
        geo.add(
            "",
            attr,
            value,
            visual_range=[0, 200],
            visual_text_color="#fff",
            symbol_size=15,
            is_visualmap=True,
            is_piecewise=True,
            visual_split_number=6,
        )
        geo.render(path='tmp/geo.html')

    # HeatMap 类型
    if __name__ == '__main__':
        geo = echarts.Geo(
            "全国主要城市空气质量",
            "data from pm2.5",
            title_color="#fff",
            title_pos="center",
            width=1200,
            height=600,
            background_color="#404a59",
        )
        attr, value = geo.cast(data)
        geo.add(
            "",
            attr,
            value,
            type="heatmap",
            is_visualmap=True,
            visual_range=[0, 300],
            visual_text_color="#fff",
        )
        geo.render(path='tmp/geo.html')

    # EffectScatter 类型（全国）
    if __name__ == '__main__':
        data = [
            ("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15)
        ]
        geo = echarts.Geo(
            "全国主要城市空气质量",
            "data from pm2.5",
            title_color="#fff",
            title_pos="center",
            width=1200,
            height=600,
            background_color="#404a59",
        )
        attr, value = geo.cast(data)
        geo.add("", attr, value, type="effectScatter", is_random=True, effect_scale=5)
        geo.render(path='tmp/geo.html')

    # EffectScatter 类型（广东）
    if __name__ == '__main__':
        data = [("汕头市", 50), ("汕尾市", 60), ("揭阳市", 35), ("阳江市", 44), ("肇庆市", 72)]
        geo = echarts.Geo(
            "广东城市空气质量",
            "data from pm2.5",
            title_color="#fff",
            title_pos="center",
            width=1200,
            height=600,
            background_color="#404a59",
        )
        attr, value = geo.cast(data)
        geo.add(
            "",
            attr,
            value,
            maptype="广东",
            type="effectScatter",
            is_random=True,
            effect_scale=5,
            is_legend_show=False,
        )
        geo.render(path='tmp/geo.html')

    # 使用 coordinate_region 指定检索坐标的国家/地区 @todo 没有导入英国城市地图
    if __name__ == '__main__':
        geo = echarts.Geo(
            "英国主要城市空气质量",
            "data from pm2.5",
            title_color="#fff",
            title_pos="center",
            background_color="#404a59",
        )
        attr, value = geo.cast(data)
        geo.add(
            "",
            attr,
            value,
            maptype="英国",
            # 使用 coordinate_region，指定检索英国范围内的坐标，如上述的 Oxford。
            # 默认为中国
            coordinate_region="英国",
            visual_range=[0, 200],
            visual_text_color="#fff",
            symbol_size=15,
            is_visualmap=True,
        )
        geo.render(path='tmp/geo.html')


# 8 GeoLines（地理坐标系线图）
if __name__ == '__main__':
    import pyecharts as echarts

    style = echarts.Style(
        title_top="#fff",
        title_pos="center",
        width=1200,
        height=600,
        background_color="#404a59"
    )

    data_guangzhou = [
        ["广州", "上海"],
        ["广州", "北京"],
        ["广州", "南京"],
        ["广州", "重庆"],
        ["广州", "兰州"],
        ["广州", "杭州"]
    ]

    # 默认效果
    if __name__ == '__main__':
        geolines = echarts.GeoLines("GeoLines 示例", **style.init_style)
        geolines.add("从广州出发", data_guangzhou, is_legend_show=False)
        geolines.render(path='tmp/geolines.html')

    # 变成飞机
    if __name__ == '__main__':
        style_geo = style.add(
            is_label_show=True,
            line_curve=0.2,
            line_opacity=0.6,
            legend_text_color="#eee",
            legend_pos="right",
            geo_effect_symbol="plane",
            geo_effect_symbolsize=15,
            label_color=['#a6c84c', '#ffa022', '#46bee9'],
            label_pos="right",
            label_formatter="{b}",
            label_text_color="#eee",
        )
        geolines = echarts.GeoLines("GeoLines 示例", **style.init_style)
        geolines.add("从广州出发", data_guangzhou, **style_geo)
        geolines.render(path='tmp/geolines.html')

    # 指定数值
    if __name__ == '__main__':
        data_guangzhou = [
            ["广州", "上海", 10],
            ["广州", "北京", 20],
            ["广州", "南京", 30],
            ["广州", "重庆", 40],
            ["广州", "兰州", 50],
            ["广州", "杭州", 60],
        ]
        geolines = echarts.GeoLines("GeoLines 示例", **style.init_style)
        geolines.add(
            "从广州出发", data_guangzhou, tooltip_formatter="{a} : {c}", **style_geo
        )
        geolines.render(path='tmp/geolines.html')

    # 多例模式
    if __name__ == '__main__':
        data_beijing = [
            ["北京", "上海"],
            ["北京", "广州"],
            ["北京", "南京"],
            ["北京", "重庆"],
            ["北京", "兰州"],
            ["北京", "杭州"]
        ]
        geolines = echarts.GeoLines("GeoLines 示例", **style.init_style)
        geolines.add("从广州出发", data_guangzhou, **style_geo)
        geolines.add("从北京出发", data_beijing, **style_geo)
        geolines.render(path='tmp/geolines.html')

    # 单例模式，指定 legend_selectedmode="single"  @ todo
    if __name__ == '__main__':
        style_geo = style.add(
            is_label_show=True,
            line_curve=0.2,
            line_opacity=0.6,
            legend_text_color="#eee",
            legend_pos="right",
            geo_effect_symbol="plane",
            geo_effect_symbolsize=15,
            label_color=['#a6c84c', '#ffa022', '#46bee9'],
            label_pos="right",
            label_formatter="{b}",
            label_text_color="#eee",
            legend_selectedmode="single",  # 指定单例模式
        )
        geolines = echarts.GeoLines("GeoLines 示例", **style.init_style)
        geolines.add("从广州出发", data_guangzhou, **style_geo)
        geolines.add("从北京出发", data_beijing, **style_geo)
        geolines.render(path='tmp/geolines.html')


# 9、Graph（关系图）
if __name__ == '__main__':
    import pyecharts as echarts

    nodes = [{"name": "结点1", "symbolSize": 10},
             {"name": "结点2", "symbolSize": 20},
             {"name": "结点3", "symbolSize": 30},
             {"name": "结点4", "symbolSize": 40},
             {"name": "结点5", "symbolSize": 50},
             {"name": "结点6", "symbolSize": 40},
             {"name": "结点7", "symbolSize": 30},
             {"name": "结点8", "symbolSize": 20}]
    links = []  # 做成相互连接
    for i in nodes:
        for j in nodes:
            links.append({"source": i.get('name'), "target": j.get('name')})
    # basic
    if __name__ == '__main__':

        graph = echarts.Graph("关系图-力引导布局示例")
        graph.add("", nodes, links, repulsion=8000)
        graph.render(path='tmp/graph.html')

    # 关系图-环形布局示例
    if __name__ == '__main__':
        graph = echarts.Graph("关系图-环形布局示例")
        graph.add(
            "",
            nodes,
            links,
            is_label_show=True,
            graph_repulsion=8000,
            graph_layout="circular",
            label_text_color=None,
        )

        graph.render(path='tmp/graph.html')

    # 微博转发关系图
    if __name__ == '__main__':
        import json
        with open('static/json/weibo.json', "r", encoding="utf-8") as f:
            j = json.load(f)
            nodes, links, categories, cont, mid, userl = j
        graph = echarts.Graph("微博转发关系图", width=1200, height=600)
        graph.add(
            "",
            nodes,
            links,
            categories,
            label_pos="right",
            graph_repulsion=50,
            is_legend_show=False,
            line_curve=0.2,
            label_text_color=None,
        )
        graph.render(path='tmp/graph.html')


# 10、HeatMap（热力图）
if __name__ == '__main__':
    import pyecharts as echarts

    # 默认情况，不指定 is_calendar_heatmap
    if __name__ == '__main__':
        import random

        x_axis = [
            "12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
            "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"]
        y_axis = [
            "Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"]
        data = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
        heatmap = echarts.HeatMap()
        heatmap.add(
            "热力图直角坐标系",
            x_axis,
            y_axis,
            data,
            is_visualmap=True,
            visual_text_color="#000",
            visual_orient="horizontal",
        )
        heatmap.render(path='tmp/heatmap.html')

    # 使用日历热力图，指定 is_calendar_heatmap 为 True
    if __name__ == '__main__':
        import datetime
        import random

        begin = datetime.date(2017, 1, 1)
        end = datetime.date(2017, 12, 31)
        data = [
            [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
            for i in range((end - begin).days + 1)
        ]
        heatmap = echarts.HeatMap("日历热力图示例", "某人 2017 年微信步数情况", width=1100)
        heatmap.add(
            "",
            data,
            is_calendar_heatmap=True,
            visual_text_color="#000",
            visual_range_text=["", ""],
            visual_range=[1000, 25000],
            calendar_cell_size=["auto", 30],
            is_visualmap=True,
            calendar_date_range="2017",
            visual_orient="horizontal",
            visual_pos="center",
            visual_top="80%",
            is_piecewise=True,
        )
        heatmap.render(path='tmp/heatmap.html')


# Kline/Candlestick（K线图）
if __name__ == '__main__':
    import pyecharts as echarts

    v1 = [[2320.26, 2320.26, 2287.3, 2362.94], [2300, 2291.3, 2288.26, 2308.38],
          [2295.35, 2346.5, 2295.35, 2345.92], [2347.22, 2358.98, 2337.35, 2363.8],
          [2360.75, 2382.48, 2347.89, 2383.76], [2383.43, 2385.42, 2371.23, 2391.82],
          [2377.41, 2419.02, 2369.57, 2421.15], [2425.92, 2428.15, 2417.58, 2440.38],
          [2411, 2433.13, 2403.3, 2437.42], [2432.68, 2334.48, 2427.7, 2441.73],
          [2430.69, 2418.53, 2394.22, 2433.89], [2416.62, 2432.4, 2414.4, 2443.03],
          [2441.91, 2421.56, 2418.43, 2444.8], [2420.26, 2382.91, 2373.53, 2427.07],
          [2383.49, 2397.18, 2370.61, 2397.94], [2378.82, 2325.95, 2309.17, 2378.82],
          [2322.94, 2314.16, 2308.76, 2330.88], [2320.62, 2325.82, 2315.01, 2338.78],
          [2313.74, 2293.34, 2289.89, 2340.71], [2297.77, 2313.22, 2292.03, 2324.63],
          [2322.32, 2365.59, 2308.92, 2366.16], [2364.54, 2359.51, 2330.86, 2369.65],
          [2332.08, 2273.4, 2259.25, 2333.54], [2274.81, 2326.31, 2270.1, 2328.14],
          [2333.61, 2347.18, 2321.6, 2351.44], [2340.44, 2324.29, 2304.27, 2352.02],
          [2326.42, 2318.61, 2314.59, 2333.67], [2314.68, 2310.59, 2296.58, 2320.96],
          [2309.16, 2286.6, 2264.83, 2333.29], [2282.17, 2263.97, 2253.25, 2286.33],
          [2255.77, 2270.28, 2253.31, 2276.22]]

    # basic
    if __name__ == '__main__':
        kline = echarts.Kline("K 线图示例")
        kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1)
        kline.render(path='tmp/kline.html')

    # Kline + dataZoom
    if __name__ == '__main__':
        kline = echarts.Kline("K 线图示例")
        kline.add(
            "日K",
            ["2017/7/{}".format(i + 1) for i in range(31)],
            v1,
            mark_point=["max"],
            is_datazoom_show=True,
        )
        kline.render(path='tmp/kline.html')

    # dataZoom 效果加在纵坐标轴上
    if __name__ == '__main__':
        kline = echarts.Kline("K 线图示例")
        kline.add(
            "日K",
            ["2017/7/{}".format(i + 1) for i in range(31)],
            v1,
            mark_point=["max"],
            is_datazoom_show=True,
            datazoom_orient="vertical",
        )
        kline.render(path='tmp/kline.html')

    # 指定 markLine 位于开盘或者收盘上  @ todo 有问题
    if __name__ == '__main__':
        kline = echarts.Kline("K 线图示例")
        kline.add(
            "日K",
            ["2017/7/{}".format(i + 1) for i in range(31)],
            v1,
            mark_line=["max"],
            mark_point=['min'],
            is_datazoom_show=True,
        )
        kline.render(path='tmp/kline.html')

# 12、Line
if __name__ == '__main__':
    import pyecharts as echarts

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 10, 100]
    v2 = [55, 60, 16, 20, 15, 80]

    # basic
    if __name__ == '__main__':

        line = echarts.Line("折线图示例")
        line.add("商家A", attr, v1, mark_point=["average"])
        line.add("商家B", attr, v2, is_smooth=True, mark_line=["max", "average"])
        line.render()
        line.render(path='tmp/line.html')

    # 标记点其他配置
    if __name__ == '__main__':
        line = echarts.Line("折线图示例")
        line.add(
            "商家A",
            attr,
            v1,
            mark_point=["average", "max", "min"],
            mark_point_symbol="diamond",
            mark_point_textcolor="#40ff27",
        )
        line.add(
            "商家B",
            attr,
            v2,
            mark_point=["average", "max", "min"],
            mark_point_symbol="arrow",
            mark_point_symbolsize=40,
        )
        line.render(path='tmp/line.html')

    # 另外一个示例
    if __name__ == '__main__':
        line = echarts.Line("折线图示例")
        line.add(
            "商家A",
            attr,
            v1,
            mark_point=["average", {"coord": ["裤子", 10], "name": "这是我想要的第一个标记点"}],
        )
        line.add(
            "商家B",
            attr,
            v2,
            is_smooth=True,
            mark_point=[{"coord": ["袜子", 80], "name": "这是我想要的第二个标记点"}],
        )
        line.render(path='tmp/line.html')

    # 堆叠
    if __name__ == '__main__':
        line = echarts.Line("折线图-数据堆叠示例")
        line.add("商家A", attr, v1, is_stack=True, is_label_show=True)
        line.add("商家B", attr, v2, is_stack=True, is_label_show=True)
        line.render()
        line.render(path='tmp/line.html')

    # 阶梯图
    if __name__ == '__main__':
        line = echarts.Line("折线图-阶梯图示例")
        line.add("商家A", attr, v1, is_step=True, is_label_show=True)
        line.render()
        line.render(path='tmp/line.html')

    # 面积图
    if __name__ == '__main__':
        line = echarts.Line("折线图-面积图示例")
        line.add(
            "商家A",
            attr,
            v1,
            is_fill=True,
            line_opacity=0.2,
            area_opacity=0.4,
            symbol=None,
        )
        line.add(
            "商家B",
            attr,
            v2,
            is_fill=True,
            area_color="#000",
            area_opacity=0.3,
            is_smooth=True,
        )
        line.render(path='tmp/line.html')

    # 如果是对数数据，推荐使用 yaxis_type 参数来设置 y 坐标轴为对数轴
    if __name__ == '__main__':
        import math, random

        line = echarts.Line("折线图示例")
        line.add("商家A", attr, [math.log10(random.randint(1, 99999)) for _ in range(6)])
        line.add(
            "商家B",
            attr,
            [math.log10(random.randint(1, 99999999)) for _ in range(6)],
            yaxis_type="log",
        )
        line.render(path='tmp/line.html')

    # 某地最低温和最高气温折线图
    if __name__ == '__main__':
        attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        line = echarts.Line("折线图示例")
        line.add(
            "最高气温",
            attr,
            [11, 11, 15, 13, 12, 13, 10],
            mark_point=["max", "min"],
            mark_line=["average"],
        )
        line.add(
            "最低气温",
            attr,
            [1, -2, 2, 5, 3, 2, 0],
            mark_point=["max", "min"],
            mark_line=["average"],
            yaxis_formatter="°C",
        )
        line.render(path='tmp/line.html')


# Line3D（3D 折线图）
if __name__ == '__main__':
    import pyecharts as echarts

    # 画个弹簧
    if __name__ == '__main__':
        import math

        _data = []
        for t in range(0, 25000):
            _t = t / 1000
            x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
            y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
            z = _t + 2.0 * math.sin(75 * _t)
            _data.append([x, y, z])
        range_color = [
            '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
            '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
        line3d = echarts.Line3D("3D 折线图示例", width=1200, height=600)
        line3d.add(
            "",
            _data,
            is_visualmap=True,
            visual_range_color=range_color,
            visual_range=[0, 30],
            grid3d_rotate_sensitivity=5,
        )
        line3d.render(path='tmp/line3d.html')

    # 旋转弹簧
    if __name__ == '__main__':
        import math

        _data = []
        for t in range(0, 25000):
            _t = t / 1000
            x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
            y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
            z = _t + 2.0 * math.sin(75 * _t)
            _data.append([x, y, z])
        range_color = [
            '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
            '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
        line3d = echarts.Line3D("3D 折线图示例", width=1200, height=600)
        line3d.add(
            "",
            _data,
            is_visualmap=True,
            visual_range_color=range_color,
            visual_range=[0, 30],
            is_grid3d_rotate=True,
            grid3d_rotate_speed=180,
        )
        line3d.render(path='tmp/line3d.html')


# Liquid（水球图）
if __name__ == '__main__':
    import pyecharts as echarts

    # 示例
    if __name__ == '__main__':
        liquid = echarts.Liquid("水球图示例")
        liquid.add("Liquid", [0.6])
        liquid.render()
        liquid.render(path='tmp/liquid.html')

    # 多层
    if __name__ == '__main__':
        liquid = echarts.Liquid("水球图示例")
        liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_outline_show=False)
        liquid.render(path='tmp/liquid.html')

    # diamond
    if __name__ == '__main__':
        liquid = echarts.Liquid("水球图示例")
        liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3],
                   is_liquid_animation=False, shape='diamond')
        liquid.render()
        liquid.render(path='tmp/liquid.html')

    # 自定义 SVG 路径
    if __name__ == '__main__':
        shape = ("path://M367.855,428.202c-3.674-1.385-7.452-1.966-11.146-1"
                 ".794c0.659-2.922,0.844-5.85,0.58-8.719 c-0.937-10.407-7."
                 "663-19.864-18.063-23.834c-10.697-4.043-22.298-1.168-29.9"
                 "02,6.403c3.015,0.026,6.074,0.594,9.035,1.728 c13.626,5."
                 "151,20.465,20.379,15.32,34.004c-1.905,5.02-5.177,9.115-9"
                 ".22,12.05c-6.951,4.992-16.19,6.536-24.777,3.271 c-13.625"
                 "-5.137-20.471-20.371-15.32-34.004c0.673-1.768,1.523-3.423"
                 ",2.526-4.992h-0.014c0,0,0,0,0,0.014 c4.386-6.853,8.145-14"
                 ".279,11.146-22.187c23.294-61.505-7.689-130.278-69.215-153"
                 ".579c-61.532-23.293-130.279,7.69-153.579,69.202 c-6.371,"
                 "16.785-8.679,34.097-7.426,50.901c0.026,0.554,0.079,1.121,"
                 "0.132,1.688c4.973,57.107,41.767,109.148,98.945,130.793 c58."
                 "162,22.008,121.303,6.529,162.839-34.465c7.103-6.893,17.826"
                 "-9.444,27.679-5.719c11.858,4.491,18.565,16.6,16.719,28.643 "
                 "c4.438-3.126,8.033-7.564,10.117-13.045C389.751,449.992,"
                 "382.411,433.709,367.855,428.202z")
        liquid = echarts.Liquid("水球图示例", width=1000, height=600)
        liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3],
                   shape=shape, is_liquid_outline_show=False)
        liquid.render(path='tmp/liquid.html')


# Map（地图）
if __name__ == '__main__':
    import pyecharts as echarts

    # 示例
    if __name__ == '__main__':
        value = [155, 10, 66, 78]
        attr = ["福建", "山东", "北京", "上海"]
        map = echarts.Map("全国地图示例", width=1200, height=600)
        map.add("", attr, value, maptype='china')
        map.render(path='tmp/map.html')

    # 显示各区域名称
    if __name__ == '__main__':
        value = [155, 10, 66, 78]
        attr = ["福建", "山东", "北京", "上海"]
        map = echarts.Map("全国地图示例", width=1200, height=600)
        map.add("", attr, value, maptype='china', is_label_show=True)
        map.render(path='tmp/map.html')

    # 结合visualMap
    if __name__ == '__main__':
        value = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]
        attr = [
            "福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"
        ]
        map = echarts.Map("Map 结合 VisualMap 示例", width=1200, height=600)
        map.add(
            "",
            attr,
            value,
            maptype="china",
            is_visualmap=True,
            visual_text_color="#000",
        )
        map.render(path='tmp/map.html')

    # 广东地图
    if __name__ == '__main__':
        value = [20, 190, 253, 77, 65]
        attr = ['汕头市', '汕尾市', '揭阳市', '阳江市', '肇庆市']
        map = echarts.Map("广东地图示例", width=1200, height=600)
        map.add(
            "", attr, value, maptype="广东", is_visualmap=True, visual_text_color="#000"
        )
        map.render(path='tmp/map.html')

    # 世界地图示例
    if __name__ == '__main__':
        value = [95.1, 23.2, 43.3, 66.4, 88.5]
        attr = ["China", "Canada", "Brazil", "Russia", "United States"]
        map = echarts.Map("世界地图示例", width=1200, height=600)
        map.add(
            "",
            attr,
            value,
            maptype="world",
            is_visualmap=True,
            visual_text_color="#000",
        )
        map.render(path='tmp/map.html')

    # 设置 is_map_symbol_show=False 取消显示标记红点
    if __name__ == '__main__':
        value = [95.1, 23.2, 43.3, 66.4, 88.5]
        attr = ["China", "Canada", "Brazil", "Russia", "United States"]
        map = echarts.Map("世界地图示例", width=1200, height=600)
        map.add(
            "",
            attr,
            value,
            maptype="world",
            is_visualmap=True,
            visual_text_color="#000",
            is_map_symbol_show=False,
        )
        map.render(path='tmp/map.html')

    # 设置 pieces 自定义 visualMap 组件标签
    if __name__ == '__main__':
        value = [155, 10, 66, 78]
        attr = ["福建", "山东", "北京", "上海"]
        map = echarts.Map("全国地图示例", width=1200, height=600)
        map.add("", attr, value, maptype='china',
                is_visualmap=True, is_piecewise=True,
                visual_text_color="#000",
                visual_range_text=["", ""],
                pieces=[
                    {"max": 160, "min": 70, "label": "高数值"},
                    {"max": 69, "min": 0, "label": "低数值"},
                ])
        map.render(path='tmp/map.html')


# Parallel（平行坐标系）
if __name__ == '__main__':
    import pyecharts as echarts

    # 示例
    if __name__ == '__main__':
        schema = ["data", "AQI", "PM2.5", "PM10", "CO", "NO2"]
        data = [
            [1, 91, 45, 125, 0.82, 34],
            [2, 65, 27, 78, 0.86, 45, ],
            [3, 83, 60, 84, 1.09, 73],
            [4, 109, 81, 121, 1.28, 68],
            [5, 106, 77, 114, 1.07, 55],
            [6, 109, 81, 121, 1.28, 68],
            [7, 106, 77, 114, 1.07, 55],
            [8, 89, 65, 78, 0.86, 51, 26],
            [9, 53, 33, 47, 0.64, 50, 17],
            [10, 80, 55, 80, 1.01, 75, 24],
            [11, 117, 81, 124, 1.03, 45]
        ]
        parallel = echarts.Parallel("平行坐标系-默认指示器")
        parallel.config(schema)
        parallel.add("parallel", data, is_random=True)
        parallel.render(path='tmp/parallel.html')

    # 用户自定义指示器
    if __name__ == '__main__':
        c_schema = [
            {"dim": 0, "name": "data"},
            {"dim": 1, "name": "AQI"},
            {"dim": 2, "name": "PM2.5"},
            {"dim": 3, "name": "PM10"},
            {"dim": 4, "name": "CO"},
            {"dim": 5, "name": "NO2"},
            {"dim": 6, "name": "CO2"},
            {"dim": 7, "name": "等级",
             "type": "category",
             "data": ['优', '良', '轻度污染', '中度污染', '重度污染', '严重污染']}
        ]
        data = [
            [1, 91, 45, 125, 0.82, 34, 23, "良"],
            [2, 65, 27, 78, 0.86, 45, 29, "良"],
            [3, 83, 60, 84, 1.09, 73, 27, "良"],
            [4, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
            [5, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
            [6, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
            [7, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
            [8, 89, 65, 78, 0.86, 51, 26, "良"],
            [9, 53, 33, 47, 0.64, 50, 17, "良"],
            [10, 80, 55, 80, 1.01, 75, 24, "良"],
            [11, 117, 81, 124, 1.03, 45, 24, "轻度污染"],
            [12, 99, 71, 142, 1.1, 62, 42, "良"],
            [13, 95, 69, 130, 1.28, 74, 50, "良"],
            [14, 116, 87, 131, 1.47, 84, 40, "轻度污染"]
        ]
        parallel = echarts.Parallel("平行坐标系-用户自定义指示器")
        parallel.config(c_schema=c_schema)
        parallel.add("parallel", data)
        parallel.render(path='tmp/parallel.html')


# Pie（饼图）
if __name__ == '__main__':
    import pyecharts as echarts

    # 示例
    if __name__ == '__main__':
        attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        v1 = [11, 12, 13, 10, 10, 10]
        pie = echarts.Pie("饼图示例")
        pie.add("", attr, v1, is_label_show=True)
        pie.render(path='tmp/pie.html')

    # 圆环图
    if __name__ == '__main__':
        attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        v1 = [11, 12, 13, 10, 10, 10]
        pie = echarts.Pie("饼图-圆环图示例", title_pos='center')
        pie.add(
            "",
            attr,
            v1,
            radius=[40, 75],
            label_text_color=None,
            is_label_show=True,
            legend_orient="vertical",
            legend_pos="left",
        )
        pie.render(path='tmp/pie.html')

    # 玫瑰图
    if __name__ == '__main__':
        attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        v1 = [11, 12, 13, 10, 10, 10]
        v2 = [19, 21, 32, 20, 20, 33]
        pie = echarts.Pie("饼图-玫瑰图示例", title_pos='center', width=900)
        pie.add(
            "商品A",
            attr,
            v1,
            center=[25, 50],
            is_random=True,
            radius=[30, 75],
            rosetype="radius",
        )
        pie.add(
            "商品B",
            attr,
            v2,
            center=[75, 50],
            is_random=True,
            radius=[30, 75],
            rosetype="area",
            is_legend_show=False,
            is_label_show=True,
        )
        pie.render(path='tmp/pie.html')

    # 饼中饼
    if __name__ == '__main__':
        import random

        attr = ['A', 'B', 'C', 'D', 'E', 'F']
        pie = echarts.Pie("饼图示例", width=1000, height=600)
        pie.add(
            "",
            attr,
            [random.randint(0, 100) for _ in range(6)],
            radius=[50, 55],
            center=[25, 50],
            is_random=True,
        )
        pie.add(
            "",
            attr,
            [random.randint(20, 100) for _ in range(6)],
            radius=[0, 45],
            center=[25, 50],
            rosetype="area",
        )
        pie.add(
            "",
            attr,
            [random.randint(0, 100) for _ in range(6)],
            radius=[50, 55],
            center=[65, 50],
            is_random=True,
        )
        pie.add(
            "",
            attr,
            [random.randint(20, 100) for _ in range(6)],
            radius=[0, 45],
            center=[65, 50],
            rosetype="radius",
        )
        pie.render(path='tmp/pie.html')

    # 多个饼图画在一张图内
    if __name__ == '__main__':
        pie = echarts.Pie('各类电影中"好片"所占的比例', "数据来着豆瓣", title_pos='center')
        style = echarts.Style()
        pie_style = style.add(
            label_pos="center",
            is_label_show=True,
            label_text_color=None
        )

        pie.add(
            "", ["剧情", ""], [25, 75], center=[10, 30], radius=[18, 24], **pie_style
        )
        pie.add(
            "", ["奇幻", ""], [24, 76], center=[30, 30], radius=[18, 24], **pie_style
        )
        pie.add(
            "", ["爱情", ""], [14, 86], center=[50, 30], radius=[18, 24], **pie_style
        )
        pie.add(
            "", ["惊悚", ""], [11, 89], center=[70, 30], radius=[18, 24], **pie_style
        )
        pie.add(
            "", ["冒险", ""], [27, 73], center=[90, 30], radius=[18, 24], **pie_style
        )
        pie.add(
            "", ["动作", ""], [15, 85], center=[10, 70], radius=[18, 24], **pie_style
        )
        pie.add(
            "", ["喜剧", ""], [54, 46], center=[30, 70], radius=[18, 24], **pie_style
        )
        pie.add(
            "", ["科幻", ""], [26, 74], center=[50, 70], radius=[18, 24], **pie_style
        )
        pie.add(
            "", ["悬疑", ""], [25, 75], center=[70, 70], radius=[18, 24], **pie_style
        )
        pie.add(
            "",
            ["犯罪", ""],
            [28, 72],
            center=[90, 70],
            radius=[18, 24],
            legend_top="center",
            **pie_style
        )
        pie.render(path='tmp/pie.html')


# Polar（极坐标系）
if __name__ == '__main__':
    import pyecharts as echarts

    # 示例
    if __name__ == '__main__':
        import random

        data = [(i, random.randint(1, 100)) for i in range(101)]
        polar = echarts.Polar("极坐标系-散点图示例")
        polar.add(
            "",
            data,
            boundary_gap=False,
            type="scatter",
            is_splitline_show=False,
            area_color=None,
            is_axisline_show=True,
        )
        polar.render(path='tmp/polar.html')

    # Note： 可配置 lineStyle 参数
    if __name__ == '__main__':
        import random

        data_1 = [(10, random.randint(1, 100)) for i in range(300)]
        data_2 = [(11, random.randint(1, 100)) for i in range(300)]
        polar = echarts.Polar("极坐标系-散点图示例", width=1200, height=600)
        polar.add("", data_1, type='scatter')
        polar.add("", data_2, type='scatter')
        polar.render(path='tmp/polar.html')

    # 动散点
    if __name__ == '__main__':
        import random

        data = [(i, random.randint(1, 100)) for i in range(10)]
        polar = echarts.Polar("极坐标系-动态散点图示例", width=1200, height=600)
        polar.add("", data, type='effectScatter', effect_scale=10, effect_period=5)
        polar.render(path='tmp/polar.html')

    # 堆叠柱状图
    if __name__ == '__main__':
        radius = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        polar = echarts.Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
        polar.add(
            "A",
            [1, 2, 3, 4, 3, 5, 1],
            radius_data=radius,
            type="barRadius",
            is_stack=True,
        )
        polar.add(
            "B",
            [2, 4, 6, 1, 2, 3, 1],
            radius_data=radius,
            type="barRadius",
            is_stack=True,
        )
        polar.add(
            "C",
            [1, 2, 3, 4, 1, 2, 5],
            radius_data=radius,
            type="barRadius",
            is_stack=True,
        )
        polar.render(path='tmp/polar.html')

    # 另外一个堆叠柱状图
    if __name__ == '__main__':
        angle = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        polar = echarts.Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
        polar.add(
            "",
            [1, 2, 3, 4, 3, 5, 1],
            angle_data=angle,
            type="barAngle",
            is_stack=True,
        )
        polar.add(
            "",
            [2, 4, 6, 1, 2, 3, 1],
            angle_data=angle,
            type="barAngle",
            is_stack=True,
        )
        polar.add(
            "",
            [1, 2, 3, 4, 1, 2, 5],
            angle_data=angle,
            type="barAngle",
            is_stack=True,
        )
        polar.render(path='tmp/polar.html')

    # 自定义渲染逻辑示例
    if __name__ == '__main__':
        def render_item(params, api):
            values = [api.value(0), api.value(1)]
            coord = api.coord(values)
            size = api.size([1, 1], values)
            return {
                "type": "sector",
                "shape": {
                    "cx": params.coordSys.cx,
                    "cy": params.coordSys.cy,
                    "r0": coord[2] - size[0] / 2,
                    "r": coord[2] + size[0] / 2,
                    "startAngle": coord[3] - size[1] / 2,
                    "endAngle": coord[3] + size[1] / 2,
                },
                "style": api.style({"fill": api.visual("color")}),
            }


        polar = echarts.Polar("自定义渲染逻辑示例", width=1200, height=600)
        polar.add(
            "",
            [
                [
                    random.randint(0, 6),
                    random.randint(1, 24),
                    random.randint(1, 24),
                ]
                for _ in range(100)
            ],
            render_item=render_item,
            type="custom",
            angle_data=X_TIME,
            radius_data=WEEK,
            is_visualmap=True,
            visual_range=[0, 30]
        )
        polar.render(path='tmp/polar.html')


# Radar（雷达图）
if __name__ == '__main__':
    import pyecharts as echarts

    value_bj = [
        [55, 9, 56, 0.46, 18, 6, 1], [25, 11, 21, 0.65, 34, 9, 2],
        [56, 7, 63, 0.3, 14, 5, 3], [33, 7, 29, 0.33, 16, 6, 4],
        [42, 24, 44, 0.76, 40, 16, 5], [82, 58, 90, 1.77, 68, 33, 6],
        [74, 49, 77, 1.46, 48, 27, 7], [78, 55, 80, 1.29, 59, 29, 8],
        [267, 216, 280, 4.8, 108, 64, 9], [185, 127, 216, 2.52, 61, 27, 10],
        [39, 19, 38, 0.57, 31, 15, 11], [41, 11, 40, 0.43, 21, 7, 12],
        [64, 38, 74, 1.04, 46, 22, 13], [108, 79, 120, 1.7, 75, 41, 14],
        [108, 63, 116, 1.48, 44, 26, 15], [33, 6, 29, 0.34, 13, 5, 16],
        [94, 66, 110, 1.54, 62, 31, 17], [186, 142, 192, 3.88, 93, 79, 18],
        [57, 31, 54, 0.96, 32, 14, 19], [22, 8, 17, 0.48, 23, 10, 20],
        [39, 15, 36, 0.61, 29, 13, 21], [94, 69, 114, 2.08, 73, 39, 22],
        [99, 73, 110, 2.43, 76, 48, 23], [31, 12, 30, 0.5, 32, 16, 24],
        [42, 27, 43, 1, 53, 22, 25], [154, 117, 157, 3.05, 92, 58, 26],
        [234, 185, 230, 4.09, 123, 69, 27], [160, 120, 186, 2.77, 91, 50, 28],
        [134, 96, 165, 2.76, 83, 41, 29], [52, 24, 60, 1.03, 50, 21, 30],
    ]
    value_sh = [
        [91, 45, 125, 0.82, 34, 23, 1], [65, 27, 78, 0.86, 45, 29, 2],
        [83, 60, 84, 1.09, 73, 27, 3], [109, 81, 121, 1.28, 68, 51, 4],
        [106, 77, 114, 1.07, 55, 51, 5], [109, 81, 121, 1.28, 68, 51, 6],
        [106, 77, 114, 1.07, 55, 51, 7], [89, 65, 78, 0.86, 51, 26, 8],
        [53, 33, 47, 0.64, 50, 17, 9], [80, 55, 80, 1.01, 75, 24, 10],
        [117, 81, 124, 1.03, 45, 24, 11], [99, 71, 142, 1.1, 62, 42, 12],
        [95, 69, 130, 1.28, 74, 50, 13], [116, 87, 131, 1.47, 84, 40, 14],
        [108, 80, 121, 1.3, 85, 37, 15], [134, 83, 167, 1.16, 57, 43, 16],
        [79, 43, 107, 1.05, 59, 37, 17], [71, 46, 89, 0.86, 64, 25, 18],
        [97, 71, 113, 1.17, 88, 31, 19], [84, 57, 91, 0.85, 55, 31, 20],
        [87, 63, 101, 0.9, 56, 41, 21], [104, 77, 119, 1.09, 73, 48, 22],
        [87, 62, 100, 1, 72, 28, 23], [168, 128, 172, 1.49, 97, 56, 24],
        [65, 45, 51, 0.74, 39, 17, 25], [39, 24, 38, 0.61, 47, 17, 26],
        [39, 24, 39, 0.59, 50, 19, 27], [93, 68, 96, 1.05, 79, 29, 28],
        [188, 143, 197, 1.66, 99, 51, 29], [174, 131, 174, 1.55, 108, 50, 30],
    ]
    c_schema = [{"name": "AQI", "max": 300, "min": 5},
                {"name": "PM2.5", "max": 250, "min": 20},
                {"name": "PM10", "max": 300, "min": 5},
                {"name": "CO", "max": 5},
                {"name": "NO2", "max": 200},
                {"name": "SO2", "max": 100}]
    # 示例
    if __name__ == '__main__':
        schema = [
            ("销售", 6500), ("管理", 16000), ("信息技术", 30000),
            ("客服", 38000), ("研发", 52000), ("市场", 25000)
        ]
        v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
        v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
        radar = echarts.Radar()
        radar.config(schema)
        radar.add("预算分配", v1, is_splitline=True, is_axisline_show=True)
        radar.add("实际开销", v2, label_color=["#4e79a7"], is_area_show=False,
                  legend_selectedmode='single')
        radar.render(path='tmp/radar.html')

    # Note： 可配置 lineStyle 参数
    if __name__ == '__main__':


        radar = echarts.Radar()
        radar.config(c_schema=c_schema, shape='circle')
        radar.add("北京", value_bj, item_color="#f9713c", symbol=None)
        radar.add("上海", value_sh, item_color="#b3e4a1", symbol=None,
                  legend_selectedmode='single')
        radar.render(path='tmp/radar.html')

    # 图例多例模式
    if __name__ == '__main__':
        radar = echarts.Radar()
        radar.config(c_schema=c_schema, shape='circle')
        radar.add("北京", value_bj, item_color="#f9713c", symbol=None)
        radar.add("上海", value_sh, item_color="#b3e4a1", symbol=None)
        radar.render(path='tmp/radar.html')


# sankey图
if __name__ == '__main__':
    import pyecharts as echarts

    # basic
    if __name__ == '__main__':
        nodes = [
            {'name': 'category1'}, {'name': 'category2'}, {'name': 'category3'},
            {'name': 'category4'}, {'name': 'category5'}, {'name': 'category6'},
        ]

        links = [
            {'source': 'category1', 'target': 'category2', 'value': 10},
            {'source': 'category2', 'target': 'category3', 'value': 15},
            {'source': 'category3', 'target': 'category4', 'value': 20},
            {'source': 'category5', 'target': 'category6', 'value': 25}
        ]
        sankey = echarts.Sankey("桑基图示例", width=1200, height=600)
        sankey.add(
            "sankey",
            nodes,
            links,
            line_opacity=0.2,
            line_curve=0.5,
            line_color="source",
            is_label_show=True,
            label_pos="right",
        )
        sankey.render(path='tmp/sankey.html')

    # 官方提供的更加复杂的图
    if __name__ == '__main__':
        import json

        with open('static/json/energy.json', "r", encoding="utf-8") as f:
            j = json.load(f)
        sankey = echarts.Sankey("桑基图示例", width=1200, height=600)
        sankey.add(
            "sankey",
            nodes=j["nodes"],
            links=j["links"],
            line_opacity=0.2,
            line_curve=0.5,
            line_color="source",
            is_label_show=True,
            label_pos="right",
        )
        sankey.render(path='tmp/sankey.html')


# Scatter（散点图）
if __name__ == '__main__':
    import pyecharts as echarts

    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [10, 20, 30, 40, 50, 60]
    # basic
    if __name__ == '__main__':

        scatter = echarts.Scatter("散点图示例")
        scatter.add("A", v1, v2)
        scatter.add("B", v1[::-1], v2)
        scatter.render(path='tmp/scatter.html')

    # 利用 Visualmap 组件，通过颜色映射数值
    if __name__ == '__main__':
        scatter = echarts.Scatter("散点图示例")
        scatter.add("A", v1, v2)
        scatter.add("B", v1[::-1], v2, is_visualmap=True)
        scatter.render(path='tmp/scatter.html')

    # 利用 Visualmap 组件，通过图形点大小映射数值
    if __name__ == '__main__':
        scatter = echarts.Scatter("散点图示例")
        scatter.add("A", v1, v2)
        scatter.add(
            "B",
            v1[::-1],
            v2,
            is_visualmap=True,
            visual_type="size",
            visual_range_size=[20, 80],
        )
        scatter.render(path='tmp/scatter.html')

    # 利用 Visualmap 组件映射到第三维度数据
    if __name__ == '__main__':
        data = [
            [28604, 77, 17096869],
            [31163, 77.4, 27662440],
            [1516, 68, 1154605773],
            [13670, 74.7, 10582082],
            [28599, 75, 4986705],
            [29476, 77.1, 56943299],
            [31476, 75.4, 78958237],
            [28666, 78.1, 254830],
            [1777, 57.7, 870601776],
            [29550, 79.1, 122249285],
            [2076, 67.9, 20194354],
            [12087, 72, 42972254],
            [24021, 75.4, 3397534],
            [43296, 76.8, 4240375],
            [10088, 70.8, 38195258],
            [19349, 69.6, 147568552],
            [10670, 67.3, 53994605],
            [26424, 75.7, 57110117],
            [37062, 75.4, 252847810]
        ]

        x_lst = [v[0] for v in data]
        y_lst = [v[1] for v in data]
        extra_data = [v[2] for v in data]
        sc = echarts.Scatter()
        sc.add(
            "scatter",
            x_lst,
            y_lst,
            extra_data=extra_data,
            is_visualmap=True,
            visual_dimension=2,
            visual_orient="horizontal",
            visual_type="size",
            visual_range=[254830, 1154605773],
            visual_text_color="#000",
        )
        sc.render(path='tmp/sc.html')

    # 为每个坐标点指定一个名称，可用于 tooltip 展示
    if __name__ == '__main__':
        def custom_formatter(params):
            return params.value[3]


        data = [
            [28604, 77, 17096],
            [31163, 77.4, 27662],
            [1516, 68, 11546],
        ]
        x_lst = [v[0] for v in data]
        y_lst = [v[1] for v in data]
        extra_data = [v[2] for v in data]
        extra_name = ["point A", "point B", "point C"]
        sc = echarts.Scatter()
        sc.add(
            "scatter",
            x_lst,
            y_lst,
            extra_data=extra_data,
            extra_name=extra_name,
            is_visualmap=True,
            visual_dimension=2,
            visual_orient="horizontal",
            visual_type="size",
            visual_range=[17000, 28000],
            visual_text_color="#000",
            tooltip_formatter=custom_formatter,
        )
        sc.render(path='tmp/sc.html')

    # 散点图默认的坐标轴都为数值轴，如果想实现横坐标为类目轴，可通过 xaxis_type 修改
    if __name__ == '__main__':
        scatter = echarts.Scatter("散点图示例")
        scatter.add("A", ["a", "b", "c", "d", "e", "f"], v2)
        scatter.add("B", ["a", "b", "c", "d", "e", "f"], v1[::-1], xaxis_type="category")
        scatter.render(path='tmp/scatter.html')

    # Scatter 还内置了画画方法
    if __name__ == '__main__':
        scatter = echarts.Scatter("散点图示例")
        v1, v2 = scatter.draw("../images/pyecharts-0.png")
        scatter.add("pyecharts", v1, v2, is_random=True)
        scatter.render(path='tmp/scatter.html')


# Scatter3D（3D 散点图）
if __name__ == '__main__':
    import pyecharts as echarts


    import random

    data = [
        [random.randint(0, 100),
         random.randint(0, 100),
         random.randint(0, 100)] for _ in range(80)
    ]
    range_color = [
        '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
        '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    scatter3D = echarts.Scatter3D("3D 散点图示例", width=1200, height=600)
    scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
    scatter3D.render(path='tmp/scatter3D.html')


# Surface3D（3D 曲面图）
if __name__ == '__main__':
    import pyecharts as echarts

    range_color = [
        "#313695",
        "#4575b4",
        "#74add1",
        "#abd9e9",
        "#e0f3f8",
        "#ffffbf",
        "#fee090",
        "#fdae61",
        "#f46d43",
        "#d73027",
        "#a50026",
    ]
    # 示例
    if __name__ == '__main__':
        import math


        def create_surface3d_data():
            for t0 in range(-60, 60, 1):
                y = t0 / 60
                for t1 in range(-60, 60, 1):
                    x = t1 / 60
                    if math.fabs(x) < 0.1 and math.fabs(y) < 0.1:
                        z = '-'
                    else:
                        z = math.sin(x * math.pi) * math.sin(y * math.pi)
                    yield [x, y, z]

        _data = list(create_surface3d_data())
        surface3d = echarts.Surface3D("3D 曲面图示例", width=1200, height=600)
        surface3d.add(
            "",
            _data,
            is_visualmap=True,
            visual_range_color=range_color,
            visual_range=[-3, 3],
            grid3d_rotate_sensitivity=5,
        )
        surface3d.render(path='tmp/surface3d.html')

    # 曲面波图
    if __name__ == '__main__':
        import math


        def create_surface3d_data():
            for t0 in range(-30, 30, 1):
                y = t0 / 10
                for t1 in range(-30, 30, 1):
                    x = t1 / 10
                    z = math.sin(x * x + y * y) * x / 3.14
                    yield [x, y, z]


        data = list(create_surface3d_data())
        surface3D = echarts.Surface3D("3D 曲面图", width=1200, height=600)
        surface3D.add(
            "",
            data,
            is_visualmap=True,
            visual_range=[-1, 1],
            visual_range_color=range_color,
        )
        surface3D.render(path='tmp/surface3D.html')


# ThemeRiver（主题河流图）
if __name__ == '__main__':
    import pyecharts as echarts

    # 示例
    if __name__ == '__main__':
        data = [
            ['2015/11/08', 10, 'DQ'], ['2015/11/09', 15, 'DQ'], ['2015/11/10', 35, 'DQ'],
            ['2015/11/14', 7, 'DQ'], ['2015/11/15', 2, 'DQ'], ['2015/11/16', 17, 'DQ'],
            ['2015/11/17', 33, 'DQ'], ['2015/11/18', 40, 'DQ'], ['2015/11/19', 32, 'DQ'],
            ['2015/11/20', 26, 'DQ'], ['2015/11/21', 35, 'DQ'], ['2015/11/22', 40, 'DQ'],
            ['2015/11/23', 32, 'DQ'], ['2015/11/24', 26, 'DQ'], ['2015/11/25', 22, 'DQ'],
            ['2015/11/08', 35, 'TY'], ['2015/11/09', 36, 'TY'], ['2015/11/10', 37, 'TY'],
            ['2015/11/11', 22, 'TY'], ['2015/11/12', 24, 'TY'], ['2015/11/13', 26, 'TY'],
            ['2015/11/14', 34, 'TY'], ['2015/11/15', 21, 'TY'], ['2015/11/16', 18, 'TY'],
            ['2015/11/17', 45, 'TY'], ['2015/11/18', 32, 'TY'], ['2015/11/19', 35, 'TY'],
            ['2015/11/20', 30, 'TY'], ['2015/11/21', 28, 'TY'], ['2015/11/22', 27, 'TY'],
            ['2015/11/23', 26, 'TY'], ['2015/11/24', 15, 'TY'], ['2015/11/25', 30, 'TY'],
            ['2015/11/26', 35, 'TY'], ['2015/11/27', 42, 'TY'], ['2015/11/28', 42, 'TY'],
            ['2015/11/08', 21, 'SS'], ['2015/11/09', 25, 'SS'], ['2015/11/10', 27, 'SS'],
            ['2015/11/11', 23, 'SS'], ['2015/11/12', 24, 'SS'], ['2015/11/13', 21, 'SS'],
            ['2015/11/14', 35, 'SS'], ['2015/11/15', 39, 'SS'], ['2015/11/16', 40, 'SS'],
            ['2015/11/17', 36, 'SS'], ['2015/11/18', 33, 'SS'], ['2015/11/19', 43, 'SS'],
            ['2015/11/20', 40, 'SS'], ['2015/11/21', 34, 'SS'], ['2015/11/22', 28, 'SS'],
            ['2015/11/14', 7, 'QG'], ['2015/11/15', 2, 'QG'], ['2015/11/16', 17, 'QG'],
            ['2015/11/17', 33, 'QG'], ['2015/11/18', 40, 'QG'], ['2015/11/19', 32, 'QG'],
            ['2015/11/20', 26, 'QG'], ['2015/11/21', 35, 'QG'], ['2015/11/22', 40, 'QG'],
            ['2015/11/23', 32, 'QG'], ['2015/11/24', 26, 'QG'], ['2015/11/25', 22, 'QG'],
            ['2015/11/26', 16, 'QG'], ['2015/11/27', 22, 'QG'], ['2015/11/28', 10, 'QG'],
            ['2015/11/08', 10, 'SY'], ['2015/11/09', 15, 'SY'], ['2015/11/10', 35, 'SY'],
            ['2015/11/11', 38, 'SY'], ['2015/11/12', 22, 'SY'], ['2015/11/13', 16, 'SY'],
            ['2015/11/14', 7, 'SY'], ['2015/11/15', 2, 'SY'], ['2015/11/16', 17, 'SY'],
            ['2015/11/17', 33, 'SY'], ['2015/11/18', 40, 'SY'], ['2015/11/19', 32, 'SY'],
            ['2015/11/20', 26, 'SY'], ['2015/11/21', 35, 'SY'], ['2015/11/22', 4, 'SY'],
            ['2015/11/23', 32, 'SY'], ['2015/11/24', 26, 'SY'], ['2015/11/25', 22, 'SY'],
            ['2015/11/26', 16, 'SY'], ['2015/11/27', 22, 'SY'], ['2015/11/28', 10, 'SY'],
            ['2015/11/08', 10, 'DD'], ['2015/11/09', 15, 'DD'], ['2015/11/10', 35, 'DD'],
            ['2015/11/11', 38, 'DD'], ['2015/11/12', 22, 'DD'], ['2015/11/13', 16, 'DD'],
            ['2015/11/14', 7, 'DD'], ['2015/11/15', 2, 'DD'], ['2015/11/16', 17, 'DD'],
            ['2015/11/17', 33, 'DD'], ['2015/11/18', 4, 'DD'], ['2015/11/19', 32, 'DD'],
            ['2015/11/20', 26, 'DD'], ['2015/11/21', 35, 'DD'], ['2015/11/22', 40, 'DD'],
            ['2015/11/23', 32, 'DD'], ['2015/11/24', 26, 'DD'], ['2015/11/25', 22, 'DD']
        ]
        tr = echarts.ThemeRiver("主题河流图示例图")
        tr.add(['DQ', 'TY', 'SS', 'QG', 'SY', 'DD'], data, is_label_show=True)
        tr.render(path='tmp/tr.html')


# Tree（树图）
if __name__ == '__main__':
    import pyecharts as echarts

    data = [
        {
            "children": [
                {
                    "children": [],
                    "name": "B"
                },
                {
                    "children": [
                        {
                            "children": [
                                {
                                    "children": [],
                                    "name": "I"
                                }
                            ],
                            "name": "E"
                        },
                        {
                            "children": [],
                            "name": "F"
                        }
                    ],
                    "name": "C"
                },
                {
                    "children": [
                        {
                            "children": [
                                {
                                    "children": [],
                                    "name": "J"
                                },
                                {
                                    "children": [],
                                    "name": "K"
                                }
                            ],
                            "name": "G"
                        },
                        {
                            "children": [],
                            "name": "H"
                        }
                    ],
                    "name": "D"
                }
            ],
            "name": "A"
        }
    ]
    # 示例
    if __name__ == '__main__':
        tree = echarts.Tree("树图示例")
        tree.add("", data)
        tree.render(path='tmp/tree.html')

    # 使用 tree_collapse_interva 控制折叠节点间隔
    if __name__ == '__main__':
        import json

        with open('static/json/flare.json', "r", encoding="utf-8") as f:
            j = json.load(f)
        tree = echarts.Tree(width=1200, height=800)
        tree.add("", data)
        tree.render(path='tmp/tree.html')

    # 设置 tree_collapse_interval 为 2（表示间隔折叠节点），图明显就好看多了
    if __name__ == '__main__':
        import json

        with open('static/json/flare.json', "r", encoding="utf-8") as f:
            j = json.load(f)
        data = [j]

        tree = echarts.Tree(width=1200, height=800)
        tree.add("", data, tree_collapse_interval=2)
        tree.render(path='tmp/tree.html')

    # 指定方向，从右到左
    if __name__ == '__main__':
        tree = echarts.Tree(width=1200, height=800)
        tree.add("", data, tree_orient="RL", tree_collapse_interval=2)
        tree.render(path='tmp/tree.html')

    # 指定方向，从上到下
    if __name__ == '__main__':
        tree = echarts.Tree(width=1200, height=800)
        tree.add(
            "",
            data,
            tree_collapse_interval=2,
            tree_orient="TB",
            tree_label_rotate=-90,
            tree_leaves_rotate=-90
        )
        tree.render(path='tmp/tree.html')

    # 指定布局
    if __name__ == '__main__':
        tree = echarts.Tree(width=1200, height=800)
        tree.add("", data, tree_collapse_interval=2, tree_layout="radial")
        tree.render(path='tmp/tree.html')

    # 调整容器布局
    if __name__ == '__main__':
        tree = echarts.Tree(width=1200, height=800)
        tree.add("", data, tree_collapse_interval=2, tree_top="15%", tree_right="20%")
        tree.render(path='tmp/tree.html')


# TreeMap（矩形树图）
if __name__ == '__main__':
    import pyecharts as echarts

    data = [
        {
            "value": 40,
            "name": "我是A",
        },
        {
            "value": 180,
            "name": "我是B",
            "children": [
                {
                    "value": 76,
                    "name": "我是B.children",
                    "children": [
                        {
                            "value": 12,
                            "name": "我是B.children.a",
                        },
                        {
                            "value": 28,
                            "name": "我是B.children.b",
                        },
                        {
                            "value": 20,
                            "name": "我是B.children.c",
                        },
                        {
                            "value": 16,
                            "name": "我是B.children.d",
                        }]
                }]}
    ]
    # basic
    if __name__ == '__main__':

        treemap = echarts.TreeMap("矩形树图-默认示例", width=1200, height=600)
        treemap.add("演示数据", data, is_label_show=True, label_pos='inside')
        treemap.render(path='tmp/treemap.html')

    # 矩形树图-下钻示例
    if __name__ == '__main__':
        treemap = echarts.TreeMap("矩形树图-下钻示例", width=1200, height=600)
        treemap.add("演示数据", data, is_label_show=True, label_pos='inside',
                    treemap_left_depth=1)
        treemap.render(path='tmp/treemap.html')

    #
    if __name__ == '__main__':
        treemap = echarts.TreeMap("矩形树图示例", width=1200, height=600)
        import json

        with open('static/json/treemap.json', "r", encoding="utf-8") as f:
            data = json.load(f)
        treemap.add("演示数据", data, is_label_show=True, label_pos='inside')
        treemap.render(path='tmp/treemap.html')


# WordCloud（词云图）
if __name__ == '__main__':
    import pyecharts as echarts

    name = [
        'Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications',
        'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp',
        'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham',
        'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']
    value = [
        10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112,
        965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265]

    # 示例1
    if __name__ == '__main__':

        wordcloud = echarts.WordCloud(width=1300, height=620)
        wordcloud.add("", name, value, word_size_range=[20, 100])
        wordcloud.render(path='tmp/wordcloud.html')

    # 示例2
    if __name__ == '__main__':
        wordcloud = echarts.WordCloud(width=1300, height=620)
        wordcloud.add("", name, value, word_size_range=[30, 100],
                      shape='diamond')
        wordcloud.render(path='tmp/bar3D.html')
