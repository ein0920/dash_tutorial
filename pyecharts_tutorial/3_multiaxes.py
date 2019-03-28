
# Grid：并行显示多张图
if __name__ == '__main__':
    import pyecharts as echarts

    # 上下类型，Bar + Line
    if __name__ == '__main__':
        attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        v1 = [5, 20, 36, 10, 75, 90]
        v2 = [10, 25, 8, 60, 20, 80]
        bar = echarts.Bar("柱状图示例", height=720)
        bar.add("商家A", attr, v1, is_stack=True)
        bar.add("商家B", attr, v2, is_stack=True)
        line = echarts.Line("折线图示例", title_top="50%")
        attr = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
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
            legend_top="50%",
        )

        grid = echarts.Grid()
        grid.add(bar, grid_bottom="60%")
        grid.add(line, grid_top="60%")
        grid.render(path='tmp/grid.html')

    # 左右类型，Scatter + EffectScatter
    if __name__ == '__main__':
        v1 = [5, 20, 36, 10, 75, 90]
        v2 = [10, 25, 8, 60, 20, 80]
        scatter = echarts.Scatter(width=1200)
        scatter.add("散点图示例", v1, v2, legend_pos="70%")
        es = echarts.EffectScatter()
        es.add(
            "动态散点图示例",
            [11, 11, 15, 13, 12, 13, 10],
            [1, -2, 2, 5, 3, 2, 0],
            effect_scale=6,
            legend_pos="20%",
        )

        grid = echarts.Grid()
        grid.add(scatter, grid_left="60%")
        grid.add(es, grid_right="60%")
        grid.render(path='tmp/grid.html')

    # 上下左右类型，Bar + Line + Scatter + EffectScatter
    if __name__ == '__main__':
        attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        v1 = [5, 20, 36, 10, 75, 90]
        v2 = [10, 25, 8, 60, 20, 80]
        bar = echarts.Bar("柱状图示例", title_pos="65%")
        bar.add("商家A", attr, v1, is_stack=True)
        bar.add("商家B", attr, v2, is_stack=True, legend_pos="80%")
        line = echarts.Line("折线图示例")
        attr = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
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
            legend_pos="20%",
        )
        v1 = [5, 20, 36, 10, 75, 90]
        v2 = [10, 25, 8, 60, 20, 80]
        scatter = echarts.Scatter("散点图示例", title_top="50%", title_pos="65%")
        scatter.add("scatter", v1, v2, legend_top="50%", legend_pos="80%")
        es = echarts.EffectScatter("动态散点图示例", title_top="50%")
        es.add(
            "es",
            [11, 11, 15, 13, 12, 13, 10],
            [1, -2, 2, 5, 3, 2, 0],
            effect_scale=6,
            legend_top="50%",
            legend_pos="20%",
        )

        grid = echarts.Grid(height=720, width=1200)
        grid.add(bar, grid_bottom="60%", grid_left="60%")
        grid.add(line, grid_bottom="60%", grid_right="60%")
        grid.add(scatter, grid_top="60%", grid_left="60%")
        grid.add(es, grid_top="60%", grid_right="60%")
        grid.render(path='tmp/grid.html')

    # Line + Pie
    if __name__ == '__main__':
        line = echarts.Line("折线图示例")
        attr = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
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
            legend_pos="20%",
        )
        attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        v1 = [11, 12, 13, 10, 10, 10]
        pie = echarts.Pie("饼图示例", title_pos="55%")
        pie.add(
            "",
            attr,
            v1,
            radius=[45, 65],
            center=[65, 50],
            legend_pos="80%",
            legend_orient="vertical",
        )

        grid = echarts.Grid(width=1200)
        grid.add(line, grid_right="55%")
        grid.add(pie, grid_left="60%")
        grid.render(path='tmp/grid.html')

    # Line + Kline
    if __name__ == '__main__':
        line = echarts.Line("折线图示例")
        attr = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
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
            legend_pos="20%",
        )
        v1 = [
            [2320.26, 2320.26, 2287.3, 2362.94],
            [2300, 2291.3, 2288.26, 2308.38],
            [2295.35, 2346.5, 2295.35, 2345.92],
            [2347.22, 2358.98, 2337.35, 2363.8],
            [2360.75, 2382.48, 2347.89, 2383.76],
            [2383.43, 2385.42, 2371.23, 2391.82],
            [2377.41, 2419.02, 2369.57, 2421.15],
            [2425.92, 2428.15, 2417.58, 2440.38],
            [2411, 2433.13, 2403.3, 2437.42],
            [2432.68, 2334.48, 2427.7, 2441.73],
            [2430.69, 2418.53, 2394.22, 2433.89],
            [2416.62, 2432.4, 2414.4, 2443.03],
            [2441.91, 2421.56, 2418.43, 2444.8],
            [2420.26, 2382.91, 2373.53, 2427.07],
            [2383.49, 2397.18, 2370.61, 2397.94],
            [2378.82, 2325.95, 2309.17, 2378.82],
            [2322.94, 2314.16, 2308.76, 2330.88],
            [2320.62, 2325.82, 2315.01, 2338.78],
            [2313.74, 2293.34, 2289.89, 2340.71],
            [2297.77, 2313.22, 2292.03, 2324.63],
            [2322.32, 2365.59, 2308.92, 2366.16],
            [2364.54, 2359.51, 2330.86, 2369.65],
            [2332.08, 2273.4, 2259.25, 2333.54],
            [2274.81, 2326.31, 2270.1, 2328.14],
            [2333.61, 2347.18, 2321.6, 2351.44],
            [2340.44, 2324.29, 2304.27, 2352.02],
            [2326.42, 2318.61, 2314.59, 2333.67],
            [2314.68, 2310.59, 2296.58, 2320.96],
            [2309.16, 2286.6, 2264.83, 2333.29],
            [2282.17, 2263.97, 2253.25, 2286.33],
            [2255.77, 2270.28, 2253.31, 2276.22],
        ]
        kline = echarts.Kline("K 线图示例", title_pos="60%")
        kline.add(
            "日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1, legend_pos="80%"
        )

        grid = echarts.Grid(width=1200)
        grid.add(line, grid_right="60%")
        grid.add(kline, grid_left="55%")
        grid.render(path='tmp/grid.html')

    # HeatMap + Bar
    if __name__ == '__main__':
        import random

        x_axis = [
            "12a", "1a", "2a", "3a", "4a", "5a", "6a",
            "7a", "8a", "9a", "10a", "11a", "12p", "1p",
            "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p",
            "10p", "11p",
        ]
        y_axis = [
            "Saturday",
            "Friday",
            "Thursday",
            "Wednesday",
            "Tuesday",
            "Monday",
            "Sunday",
        ]
        data = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
        heatmap = echarts.HeatMap("热力图示例")
        heatmap.add(
            "热力图直角坐标系",
            x_axis,
            y_axis,
            data,
            is_visualmap=True,
            visual_top="45%",
            visual_text_color="#000",
            visual_orient="horizontal",
        )
        attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        v1 = [5, 20, 36, 10, 75, 90]
        v2 = [10, 25, 8, 60, 20, 80]
        bar = echarts.Bar("柱状图示例", title_top="52%")
        bar.add("商家A", attr, v1, is_stack=True)
        bar.add("商家B", attr, v2, is_stack=True, legend_top="50%")

        grid = echarts.Grid(height=700)
        grid.add(heatmap, grid_bottom="60%")
        grid.add(bar, grid_top="60%")
        grid.render(path='tmp/grid.html')

    # 利用 Grid 解决 dataZoom 与 X 轴标签重叠问题
    if __name__ == '__main__':
        x = [
            "名字很长的x轴1",
            "名字很长的x轴2",
            "名字很长的x轴3",
            "名字很长的x轴4",
            "名字很长的x轴5",
            "名字很长的x轴6",
            "名字很长的x轴7",
            "名字很长的x轴8",
            "名字很长的x轴9",
        ]
        y = [10, 20, 30, 40, 50, 60, 70, 80, 90]

        grid = echarts.Grid()
        bar = echarts.Bar("利用 Grid 解决 dataZoom 与 X 轴标签重叠问题")
        bar.add("", x, y, is_datazoom_show=True, xaxis_interval=0, xaxis_rotate=30)
        # 把 bar 加入到 grid 中，并适当调整 grid_bottom 参数，使 bar 图整体上移
        grid.add(bar, grid_bottom="25%")
        grid.render(path='tmp/grid.html')

    # datazoom 组件同时控制多个图
    if __name__ == '__main__':
        line = echarts.Line("折线图示例")
        attr = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
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
            legend_top="50%",
            mark_line=["average"],
            # 设置 dataZoom 控制索引为 0,1 的 x 轴，即第一个和第二个
            is_datazoom_show=True,
            datazoom_xaxis_index=[0, 1],
        )

        v1 = [
            [2320.26, 2320.26, 2287.3, 2362.94],
            [2300, 2291.3, 2288.26, 2308.38],
            [2295.35, 2346.5, 2295.35, 2345.92],
            [2347.22, 2358.98, 2337.35, 2363.8],
            [2360.75, 2382.48, 2347.89, 2383.76],
            [2383.43, 2385.42, 2371.23, 2391.82],
            [2377.41, 2419.02, 2369.57, 2421.15],
            [2425.92, 2428.15, 2417.58, 2440.38],
            [2411, 2433.13, 2403.3, 2437.42],
            [2432.68, 2334.48, 2427.7, 2441.73],
            [2430.69, 2418.53, 2394.22, 2433.89],
            [2416.62, 2432.4, 2414.4, 2443.03],
            [2441.91, 2421.56, 2418.43, 2444.8],
            [2420.26, 2382.91, 2373.53, 2427.07],
            [2383.49, 2397.18, 2370.61, 2397.94],
            [2378.82, 2325.95, 2309.17, 2378.82],
            [2322.94, 2314.16, 2308.76, 2330.88],
            [2320.62, 2325.82, 2315.01, 2338.78],
            [2313.74, 2293.34, 2289.89, 2340.71],
            [2297.77, 2313.22, 2292.03, 2324.63],
            [2322.32, 2365.59, 2308.92, 2366.16],
            [2364.54, 2359.51, 2330.86, 2369.65],
            [2332.08, 2273.4, 2259.25, 2333.54],
            [2274.81, 2326.31, 2270.1, 2328.14],
            [2333.61, 2347.18, 2321.6, 2351.44],
            [2340.44, 2324.29, 2304.27, 2352.02],
            [2326.42, 2318.61, 2314.59, 2333.67],
            [2314.68, 2310.59, 2296.58, 2320.96],
            [2309.16, 2286.6, 2264.83, 2333.29],
            [2282.17, 2263.97, 2253.25, 2286.33],
            [2255.77, 2270.28, 2253.31, 2276.22],
        ]
        kline = echarts.Kline("K 线图示例", title_top="50%")
        kline.add(
            "日K",
            ["2017/7/{}".format(i + 1) for i in range(31)],
            v1,
            is_datazoom_show=True,
        )

        grid = echarts.Grid(width=1200, height=700)
        grid.add(line, grid_top="60%")
        grid.add(kline, grid_bottom="60%")
        grid.render(path='tmp/grid.html')

    # 倒映直角坐标系
    if __name__ == '__main__':
        import random

        attr = ["{}天".format(i) for i in range(1, 31)]
        line_top = echarts.Line("折线图示例")
        line_top.add(
            "最高气温",
            attr,
            [random.randint(20, 100) for i in range(30)],
            mark_point=["max", "min"],
            mark_line=["average"],
            legend_pos="38%",
        )
        line_bottom = echarts.Line()
        line_bottom.add(
            "最低气温",
            attr,
            [random.randint(20, 100) for i in range(30)],
            mark_point=["max", "min"],
            mark_line=["average"],
            is_yaxis_inverse=True,
            xaxis_pos="top",
        )

        grid = echarts.Grid(width=1200, height=700)
        grid.add(line_top, grid_bottom="60%")
        grid.add(line_bottom, grid_top="50%")
        grid.render(path='tmp/grid.html')

    # Grid + Overlap
    if __name__ == '__main__':
        grid = echarts.Grid()

        attr = ["{}月".format(i) for i in range(1, 13)]
        v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
        v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
        v3 = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]

        bar = echarts.Bar(title="Overlap+Grid 示例", title_pos="40%")
        bar.add("蒸发量", attr, v1)
        bar.add(
            "降水量",
            attr,
            v2,
            yaxis_formatter=" ml",
            yaxis_max=250,
            legend_pos="85%",
            legend_orient="vertical",
            legend_top="45%",
        )
        line = echarts.Line()
        line.add("平均温度", attr, v3, yaxis_formatter=" °C")
        overlap = echarts.Overlap(width=1200, height=600)
        overlap.add(bar)
        overlap.add(line, is_add_yaxis=True, yaxis_index=1)

        grid.add(overlap, grid_right="20%")
        grid.render(path='tmp/grid.html')


# Overlap：结合不同类型图表叠加画在同张图上
if __name__ == '__main__':
    import pyecharts as echarts

    # Line + Bar
    if __name__ == '__main__':
        attr = ['A', 'B', 'C', 'D', 'E', 'F']
        v1 = [10, 20, 30, 40, 50, 60]
        v2 = [38, 28, 58, 48, 78, 68]
        bar = echarts.Bar("Line - Bar 示例")
        bar.add("bar", attr, v1)
        line = echarts.Line()
        line.add("line", attr, v2)

        overlap = echarts.Overlap()
        overlap.add(bar)
        overlap.add(line)
        overlap.render(path='tmp/overlap.html')

    # Scatter + EffectScatter
    if __name__ == '__main__':
        v1 = [10, 20, 30, 40, 50, 60]
        v2 = [30, 30, 30, 30, 30, 30]
        v3 = [50, 50, 50, 50, 50, 50]
        v4 = [10, 10, 10, 10, 10, 10]
        es = echarts.EffectScatter("Scatter - EffectScatter 示例")
        es.add("es", v1, v2)
        scatter = echarts.Scatter()
        scatter.add("scatter", v1, v3)
        es_1 = echarts.EffectScatter()
        es_1.add("es_1", v1, v4, symbol='pin', effect_scale=5)

        overlap = echarts.Overlap()
        overlap.add(es)
        overlap.add(scatter)
        overlap.add(es_1)
        overlap.render(path='tmp/overlap.html')

    # Kline + Line
    if __name__ == '__main__':
        import random

        v1 = [[2320.26, 2320.26, 2287.3, 2362.94],
              [2300, 2291.3, 2288.26, 2308.38],
              [2295.35, 2346.5, 2295.35, 2345.92],
              [2347.22, 2358.98, 2337.35, 2363.8],
              [2360.75, 2382.48, 2347.89, 2383.76],
              [2383.43, 2385.42, 2371.23, 2391.82],
              [2377.41, 2419.02, 2369.57, 2421.15],
              [2425.92, 2428.15, 2417.58, 2440.38],
              [2411, 2433.13, 2403.3, 2437.42],
              [2432.68, 2334.48, 2427.7, 2441.73],
              [2430.69, 2418.53, 2394.22, 2433.89],
              [2416.62, 2432.4, 2414.4, 2443.03],
              [2441.91, 2421.56, 2418.43, 2444.8],
              [2420.26, 2382.91, 2373.53, 2427.07],
              [2383.49, 2397.18, 2370.61, 2397.94],
              [2378.82, 2325.95, 2309.17, 2378.82],
              [2322.94, 2314.16, 2308.76, 2330.88],
              [2320.62, 2325.82, 2315.01, 2338.78],
              [2313.74, 2293.34, 2289.89, 2340.71],
              [2297.77, 2313.22, 2292.03, 2324.63],
              [2322.32, 2365.59, 2308.92, 2366.16],
              [2364.54, 2359.51, 2330.86, 2369.65],
              [2332.08, 2273.4, 2259.25, 2333.54],
              [2274.81, 2326.31, 2270.1, 2328.14],
              [2333.61, 2347.18, 2321.6, 2351.44],
              [2340.44, 2324.29, 2304.27, 2352.02],
              [2326.42, 2318.61, 2314.59, 2333.67],
              [2314.68, 2310.59, 2296.58, 2320.96],
              [2309.16, 2286.6, 2264.83, 2333.29],
              [2282.17, 2263.97, 2253.25, 2286.33],
              [2255.77, 2270.28, 2253.31, 2276.22]]
        attr = ["2017/7/{}".format(i + 1) for i in range(31)]
        kline = echarts.Kline("Kline - Line 示例")
        kline.add("日K", attr, v1)
        line_1 = echarts.Line()
        line_1.add("line-1", attr, [random.randint(2400, 2500) for _ in range(31)])
        line_2 = echarts.Line()
        line_2.add("line-2", attr, [random.randint(2400, 2500) for _ in range(31)])

        overlap = echarts.Overlap()
        overlap.add(kline)
        overlap.add(line_1)
        overlap.add(line_2)
        overlap.render(path='tmp/overlap.html')

    # Line + EffectScatter
    if __name__ == '__main__':
        attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        v1 = [5, 20, 36, 10, 10, 100]
        line = echarts.Line("line - es 示例")
        line.add("", attr, v1, is_random=True)
        es = echarts.EffectScatter()
        es.add("", attr, v1, effect_scale=8)

        overlap = echarts.Overlap()
        overlap.add(line)
        overlap.add(es)
        overlap.render(path='tmp/overlap.html')

    # 如果想改变轴索引，使其有多 X 轴或者多 Y 轴的话。请看下面
    if __name__ == '__main__':
        attr = ["{}月".format(i) for i in range(1, 13)]
        v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
        v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
        v3 = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]

        bar = echarts.Bar()
        bar.add("蒸发量", attr, v1)
        bar.add("降水量", attr, v2, yaxis_formatter=" ml",
                yaxis_interval=50, yaxis_max=250)

        line = echarts.Line()
        line.add("平均温度", attr, v3, yaxis_formatter=" °C", yaxis_interval=5)

        overlap = echarts.Overlap(width=1200, height=600)
        # 默认不新增 x y 轴，并且 x y 轴的索引都为 0
        overlap.add(bar)
        # 新增一个 y 轴，此时 y 轴的数量为 2，第二个 y 轴的索引为 1（索引从 0 开始），所以设置 yaxis_index = 1
        # 由于使用的是同一个 x 轴，所以 x 轴部分不用做出改变
        overlap.add(line, yaxis_index=1, is_add_yaxis=True)
        overlap.render(path='tmp/overlap.html')


# Page：同一网页按顺序展示多图
if __name__ == '__main__':
    import pyecharts as echarts

    # 示例
    if __name__ == '__main__':
        page = echarts.Page()  # step 1

        # bar
        attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        v1 = [5, 20, 36, 10, 75, 90]
        v2 = [10, 25, 8, 60, 20, 80]
        bar = echarts.Bar("柱状图数据堆叠示例")
        bar.add("商家A", attr, v1, is_stack=True)
        bar.add("商家B", attr, v2, is_stack=True)
        page.add(bar)  # step 2

        # scatter3D
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
        page.add(scatter3D)  # step 2
        page.render(path='tmp/page.html')

    # 当然，更多图也是可以的
    if __name__ == '__main__':
        page = echarts.Page()

        # line
        attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        line = echarts.Line("折线图示例")
        line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10],
                 mark_point=["max", "min"], mark_line=["average"])
        line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0],
                 mark_point=["max", "min"], mark_line=["average"])
        page.add(line)

        # pie
        attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        v1 = [11, 12, 13, 10, 10, 10]
        pie = echarts.Pie("饼图-圆环图示例", title_pos='center')
        pie.add("", attr, v1, radius=[40, 75], label_text_color=None,
                is_label_show=True, legend_orient='vertical', legend_pos='left')
        page.add(pie)

        # kline
        v1 = [[2320.26, 2320.26, 2287.3, 2362.94],
              [2300, 2291.3, 2288.26, 2308.38],
              [2295.35, 2346.5, 2295.35, 2345.92],
              [2347.22, 2358.98, 2337.35, 2363.8],
              [2360.75, 2382.48, 2347.89, 2383.76],
              [2383.43, 2385.42, 2371.23, 2391.82],
              [2377.41, 2419.02, 2369.57, 2421.15],
              [2425.92, 2428.15, 2417.58, 2440.38],
              [2411, 2433.13, 2403.3, 2437.42],
              [2432.68, 2334.48, 2427.7, 2441.73],
              [2430.69, 2418.53, 2394.22, 2433.89],
              [2416.62, 2432.4, 2414.4, 2443.03],
              [2441.91, 2421.56, 2418.43, 2444.8],
              [2420.26, 2382.91, 2373.53, 2427.07],
              [2383.49, 2397.18, 2370.61, 2397.94],
              [2378.82, 2325.95, 2309.17, 2378.82],
              [2322.94, 2314.16, 2308.76, 2330.88],
              [2320.62, 2325.82, 2315.01, 2338.78],
              [2313.74, 2293.34, 2289.89, 2340.71],
              [2297.77, 2313.22, 2292.03, 2324.63],
              [2322.32, 2365.59, 2308.92, 2366.16],
              [2364.54, 2359.51, 2330.86, 2369.65],
              [2332.08, 2273.4, 2259.25, 2333.54],
              [2274.81, 2326.31, 2270.1, 2328.14],
              [2333.61, 2347.18, 2321.6, 2351.44],
              [2340.44, 2324.29, 2304.27, 2352.02],
              [2326.42, 2318.61, 2314.59, 2333.67],
              [2314.68, 2310.59, 2296.58, 2320.96],
              [2309.16, 2286.6, 2264.83, 2333.29],
              [2282.17, 2263.97, 2253.25, 2286.33],
              [2255.77, 2270.28, 2253.31, 2276.22]]
        kline = echarts.Kline("K 线图示例")
        kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1)
        page.add(kline)

        # radar
        schema = [
            ("销售", 6500), ("管理", 16000), ("信息技术", 30000),
            ("客服", 38000), ("研发", 52000), ("市场", 25000)
        ]
        v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
        v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
        radar = echarts.Radar("雷达图示例")
        radar.config(schema)
        radar.add("预算分配", v1, is_splitline=True, is_axisline_show=True)
        radar.add("实际开销", v2, label_color=["#4e79a7"], is_area_show=False,
                  legend_selectedmode='single')
        page.add(radar)
        page.render(path='tmp/page.html')

    # Page 类的额外的文本标签，由各图形本身携带
    if __name__ == '__main__':
        page = echarts.Page()
        line = echarts.Line("折线图示例", extra_html_text_label=["LINE TEXT LABEL", "color:red"])
        line.add(
            "最高气温",
            WEEK,
            [11, 11, 15, 13, 12, 13, 10],
            mark_point=["max", "min"],
            mark_line=["average"],
        )
        page.add(line)

        v1 = [11, 12, 13, 10, 10, 10]
        pie = echarts.Pie("饼图-圆环图示例", title_pos="center", extra_html_text_label=["PIE TEXT LABEL"])
        pie.add(
            "",
            CLOTHES,
            v1,
            radius=[40, 75],
            label_text_color=None,
            is_label_show=True,
            legend_orient="vertical",
            legend_pos="left",
        )
        page.add(pie)

        v2 = [10, 25, 8, 60, 20, 80]
        bar = echarts.Bar("柱状图", extra_html_text_label=["BAR TEXT LABEL"])
        bar.add("商家B", CLOTHES, v2)
        page.add(bar)
        page.render(path='tmp/page.html')


# Timeline：提供时间线轮播多张图
if __name__ == '__main__':
    import pyecharts as echarts
    from random import *
    # basic
    if __name__ == '__main__':
        from random import *
        attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        bar_1 = echarts.Bar("2012 年销量", "数据纯属虚构")
        bar_1.add("春季", attr, [randint(10, 100) for _ in range(6)])
        bar_1.add("夏季", attr, [randint(10, 100) for _ in range(6)])
        bar_1.add("秋季", attr, [randint(10, 100) for _ in range(6)])
        bar_1.add("冬季", attr, [randint(10, 100) for _ in range(6)])

        bar_2 = echarts.Bar("2013 年销量", "数据纯属虚构")
        bar_2.add("春季", attr, [randint(10, 100) for _ in range(6)])
        bar_2.add("夏季", attr, [randint(10, 100) for _ in range(6)])
        bar_2.add("秋季", attr, [randint(10, 100) for _ in range(6)])
        bar_2.add("冬季", attr, [randint(10, 100) for _ in range(6)])

        bar_3 = echarts.Bar("2014 年销量", "数据纯属虚构")
        bar_3.add("春季", attr, [randint(10, 100) for _ in range(6)])
        bar_3.add("夏季", attr, [randint(10, 100) for _ in range(6)])
        bar_3.add("秋季", attr, [randint(10, 100) for _ in range(6)])
        bar_3.add("冬季", attr, [randint(10, 100) for _ in range(6)])

        bar_4 = echarts.Bar("2015 年销量", "数据纯属虚构")
        bar_4.add("春季", attr, [randint(10, 100) for _ in range(6)])
        bar_4.add("夏季", attr, [randint(10, 100) for _ in range(6)])
        bar_4.add("秋季", attr, [randint(10, 100) for _ in range(6)])
        bar_4.add("冬季", attr, [randint(10, 100) for _ in range(6)])

        bar_5 = echarts.Bar("2016 年销量", "数据纯属虚构")
        bar_5.add("春季", attr, [randint(10, 100) for _ in range(6)])
        bar_5.add("夏季", attr, [randint(10, 100) for _ in range(6)])
        bar_5.add("秋季", attr, [randint(10, 100) for _ in range(6)])
        bar_5.add("冬季", attr, [randint(10, 100) for _ in range(6)], is_legend_show=True)

        timeline = echarts.Timeline(is_auto_play=True, timeline_bottom=0)
        timeline.add(bar_1, '2012 年')
        timeline.add(bar_2, '2013 年')
        timeline.add(bar_3, '2014 年')
        timeline.add(bar_4, '2015 年')
        timeline.add(bar_5, '2016 年')
        timeline.render(path='tmp/timeline.html')

    #
    if __name__ == '__main__':
        attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        pie_1 = echarts.Pie("2012 年销量比例", "数据纯属虚构")
        pie_1.add(
            "秋季",
            attr,
            [randint(10, 100) for _ in range(6)],
            is_label_show=True,
            radius=[30, 55],
            rosetype="radius",
        )

        pie_2 = echarts.Pie("2013 年销量比例", "数据纯属虚构")
        pie_2.add(
            "秋季",
            attr,
            [randint(10, 100) for _ in range(6)],
            is_label_show=True,
            radius=[30, 55],
            rosetype="radius",
        )

        pie_3 = echarts.Pie("2014 年销量比例", "数据纯属虚构")
        pie_3.add(
            "秋季",
            attr,
            [randint(10, 100) for _ in range(6)],
            is_label_show=True,
            radius=[30, 55],
            rosetype="radius",
        )

        pie_4 = echarts.Pie("2015 年销量比例", "数据纯属虚构")
        pie_4.add(
            "秋季",
            attr,
            [randint(10, 100) for _ in range(6)],
            is_label_show=True,
            radius=[30, 55],
            rosetype="radius",
        )

        pie_5 = echarts.Pie("2016 年销量比例", "数据纯属虚构")
        pie_5.add(
            "秋季",
            attr,
            [randint(10, 100) for _ in range(6)],
            is_label_show=True,
            radius=[30, 55],
            rosetype="radius",
        )

        timeline = echarts.Timeline(is_auto_play=True, timeline_bottom=0)
        timeline.add(pie_1, '2012 年')
        timeline.add(pie_2, '2013 年')
        timeline.add(pie_3, '2014 年')
        timeline.add(pie_4, '2015 年')
        timeline.add(pie_5, '2016 年')
        timeline.render(path='tmp/timeline.html')

    #
    if __name__ == '__main__':
        attr = ["{}月".format(i) for i in range(1, 7)]
        bar = echarts.Bar("1 月份数据", "数据纯属虚构")
        bar.add("bar", attr, [randint(10, 50) for _ in range(6)])
        line = echarts.Line()
        line.add("line", attr, [randint(50, 80) for _ in range(6)])
        overlap = echarts.Overlap()
        overlap.add(bar)
        overlap.add(line)

        bar_1 = echarts.Bar("2 月份数据", "数据纯属虚构")
        bar_1.add("bar", attr, [randint(10, 50) for _ in range(6)])
        line_1 = echarts.Line()
        line_1.add("line", attr, [randint(50, 80) for _ in range(6)])
        overlap_1 = echarts.Overlap()
        overlap_1.add(bar_1)
        overlap_1.add(line_1)

        bar_2 = echarts.Bar("3 月份数据", "数据纯属虚构")
        bar_2.add("bar", attr, [randint(10, 50) for _ in range(6)])
        line_2 = echarts.Line()
        line_2.add("line", attr, [randint(50, 80) for _ in range(6)])
        overlap_2 = echarts.Overlap()
        overlap_2.add(bar_2)
        overlap_2.add(line_2)

        bar_3 = echarts.Bar("4 月份数据", "数据纯属虚构")
        bar_3.add("bar", attr, [randint(10, 50) for _ in range(6)])
        line_3 = echarts.Line()
        line_3.add("line", attr, [randint(50, 80) for _ in range(6)])
        overlap_3 = echarts.Overlap()
        overlap_3.add(bar_3)
        overlap_3.add(line_3)

        bar_4 = echarts.Bar("5 月份数据", "数据纯属虚构")
        bar_4.add("bar", attr, [randint(10, 50) for _ in range(6)])
        line_4 = echarts.Line()
        line_4.add("line", attr, [randint(50, 80) for _ in range(6)])
        overlap_4 = echarts.Overlap()
        overlap_4.add(bar_4)
        overlap_4.add(line_4)

        timeline = echarts.Timeline(timeline_bottom=0)
        timeline.add(overlap.chart, '1 月')
        timeline.add(overlap_1.chart, '2 月')
        timeline.add(overlap_2.chart, '3 月')
        timeline.add(overlap_3.chart, '4 月')
        timeline.add(overlap_4.chart, '5 月')
        timeline.render(path='tmp/timeline.html')
