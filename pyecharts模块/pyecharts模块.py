# 导包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 创建一个拆线图对象
line = Line()

# 给拆线图添加x轴的数据
line.add_xaxis(["中国", "美国", "英国"])

# 给拆线图添加y轴的数据
line.add_yaxis("GDP", [30, 20, 10])

# 进行全局的配置
line.set_global_opts(
    title_opts=TitleOpts(title="我是标题", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

# 生成网页
line.render()
















