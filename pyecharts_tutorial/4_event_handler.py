
import pyecharts as echarts

# label_formatter
if __name__ == '__main__':
    def label_formatter(params):
        return params.value + ' [Good!]'


    attr = ["Jan", "Feb"]
    v1 = [2.0, 4.9]
    bar = echarts.Bar("Bar chart", "precipitation and evaporation one year")
    bar.add("precipitation", attr, v1, is_label_show=True, label_formatter=label_formatter)
    bar.render(path='tmp/formatter.html')


# Tooltip tooltip_formatter
if __name__ == '__main__':
    def geo_formatter(params):
        return params.name + ' : ' + params.value[2]


    data = [('澄海区', 30), ('南澳县', 40), ('龙湖区', 50), ('金平区', 60)]
    geo = echarts.Geo("汕头市地图示例", )
    attr, value = geo.cast(data)
    geo.add(
        "",
        attr,
        value,
        maptype="汕头",
        is_visualmap=True,
        is_legend_show=False,
        tooltip_formatter=geo_formatter,  # 重点在这里，将函数直接传递为参数。
        label_emphasis_textsize=15,
        label_emphasis_pos='right',
    )
    geo.render(path='tmp/formatter.html')

# Label 示例
if __name__ == '__main__':
    from pyecharts_javascripthon.dom import window


    def custom_formatter(params):
        return window.parseFloat(params.value).toFixed(2)


    attr = ["aa", "bb", "Diabetes Mellitus Requiring Medication", "d", "e", "fff"]
    v1 = [5.12, 20.85, 36.69, 10.10, 75.20, 90.36]
    v2 = [10.00, 25.45, 8.23, 60.00, 20.50, 80.00]
    bar = echarts.Bar("x 轴和 y 轴交换")
    bar.add(
        "商家A",
        attr,
        v1,
        is_label_show=True,
        label_pos="right",
        # label_formatter=custom_formatter,
    )
    bar.add(
        "商家B",
        attr,
        v2,
        is_convert=True,
        is_label_show=True,
        label_pos="right",
        # label_formatter=custom_formatter,
    )
    grid = echarts.Grid()
    grid.add(bar, grid_left="40%")
    grid.render('tmp/formatter.html')


# handlers事件名
if __name__ == '__main__':
    '''
    # Mouse Events
    MOUSE_CLICK = "click"
    MOUSE_DBCLICK = "dbclick"
    MOUSE_DOWN = "mousedown"
    MOUSE_OVER = "mouseover"
    MOUSE_GLOBALOUT = "globalout"
    
    # Other Events
    LEGEND_SELECT_CHANGED = "legendselectchanged"
    LEGEND_SELECTED = "legendselected"
    LEGEND_UNSELECTAED = "legendunselected"
    LEGEND_SCROLL = "legendscroll"
    DATA_ZOOM = "datazoom"
    DATA_RANGE_SELECTED = "datarangeselected"
    TIMELINE_CHANGED = "timelinechanged"
    TIMELINE_PLAY_CHANGED = "timelineplaychanged"
    RESTORE = "restore"
    DATA_VIEW_CHANGED = "dataviewchanged"
    MAGIC_TYPE_CHANGED = "magictypechanged"
    GEO_SELECT_CHANGED = "geoselectchanged"
    GEO_SELECTED = "geoselected"
    GEO_UNSELECTED = "geounselected"
    PIE_SELECT_CHANGED = "pieselectchanged"
    PIE_SELECTED = "pieselected"
    PIE_UNSELECTED = "pieunselected"
    MAP_SELECT_CHANGED = "mapselectchanged"
    MAP_SELECTED = "mapselected"
    MAP_UNSELECTED = "mapunselected"
    AXIS_AREA_SELECTED = "axisareaselected"
    FOCUS_NODE_ADJACENCY = "focusnodeadjacency"
    UNFOCUS_NODE_ADJACENCY = "unfocusnodeadjacency"
    BRUSH = "brush"
    BRUSH_SELECTED = "brushselected"
    '''

if __name__ == '__main__':
    import pyecharts.echarts.events as events
    from pyecharts_javascripthon.dom import alert


    def on_click():
        alert("点击事件触发")


    def test_mouse_click():
        bar = echarts.Bar("我的第一个图表", "这里是副标题")
        bar.add(
            "服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90]
        )
        bar.on(events.MOUSE_CLICK, on_click)
        bar.render()