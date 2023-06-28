# chart-plot
需要导入matplotlib.pyplot，pandas，numpy，matplotlib.ticker中的FuncFormatter以及scipy中的interpolate

通过pandas读取excel表格数据创建了一个Figure class 需要用excel路径以及选择读取的列来初始化
__init__(self, path, title=None, usecols=None): path是excel路径 usecols是选择需要读取的列数，usecols=[0, 1, 2]表示读取前三列

figure的方法有：

1.#bar_line(self, bars=1,lines=1,bar_color='r', line_color='g', marker='.', line_number=False,percent_bar=False,bar_number=False,percent_line=False)

表示同时画出折线图和柱状图，bars表示柱状图个数，以堆叠的方式话多个柱状图，line_number为真表示显示折线点的数据默认不显示，bar_number同理表示是否在柱状图上显示数据，percent_bar和percent_line分别表示柱状图和折线图的纵坐标是否以百分数的形式显示。
 
 2.#lines(self,percentage=False)

表示根据读取的数据画出多条折线图，percentage表示是否纵坐标以百分数显示。
 
 3.#bars(self,bar_color='r',width=0.8,barsnumber=1,bar_number=False)

根据读取的数据以堆叠的形式画出多条柱状图，width指示所画柱状图的宽度，barsnumber表示堆叠的柱状图个数，bar_number指示是否显示数据。
 
 4.#pie(self)

根据数据绘制出饼图。
 
 5.#bar_group(self,barsnumber=1,bar_number=False)

根据数据同时画出多组柱状图，barsnumber表示堆叠的柱状图个数，bar_number指示是否显示数据。
 
 6.#bar_curve(self, bars=1,lines=1,percent_bar=False,bar_color='r',percent_line=False)

同时画出曲线和柱状图，其他参数与bar_line类似。
 
 7.#curves(self,percentage=False,grid=False)

画出多条曲线，percentage表示是否纵坐标以百分数显示，grid表示是否需要显示网格。
