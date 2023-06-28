# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.ticker import FuncFormatter
from scipy import interpolate #拟合曲线


class Figure:
    def __init__(self, path, title=None, usecols=None):
        self.data = pd.read_excel(path, usecols=usecols)
        self.columns = len(self.data.columns)
        self.title = title
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        print(self.data)


    #画柱状图和折线图 bars表示柱状图的数量，lines表示折线的数量，
    def bar_line(self, bars=1,lines=1,bar_color='r', line_color='g', marker='.', line_number=False,percent_bar=False,
                 bar_number=False,percent_line=False):
        fig = plt.figure()
        a = fig.add_subplot(111)
        labels = self.data.iloc[:, 0]
        a.bar(range(len(self.data.index)), self.data.iloc[:, 1], color=bar_color, alpha=0.6, label=self.data.columns[1],
              width = 0.3,tick_label=labels)
        if percent_bar:
            a.yaxis.set_major_formatter(FuncFormatter(lambda x, _: '{}%'.format(x * 100)))
        if bar_number:
            for i, j in zip(range(len(self.data.index)), self.data.iloc[:, 1]):
                plt.text(i-0.1, j, str(j))

        bottom=self.data.iloc[:, 1]
        for i in range(bars-1):
            a.bar(range(len(self.data.index)), self.data.iloc[:, i+2], bottom=bottom,  alpha=0.6, label=self.data.columns[i+2],
                  tick_label=labels)
            bottom += self.data.iloc[:, i + 1]

        a.legend(bbox_to_anchor=(0.15, -0.1-0.05*bars),loc=3, borderaxespad=0)
        plt.tight_layout()

        b = a.twinx()
        for i in range(lines):
            b.plot(range(len(self.data.index)), self.data.iloc[:, bars+i+1], color=line_color, marker=marker,label=self.data.columns[i+bars+1])
            plt.xlabel(self.data.columns[0])
            if line_number and lines == 1:
                for i, j in zip(range(len(self.data.index)), self.data.iloc[:, bars+i+1]):
                    plt.text(i, j, str(j))
        b.legend(bbox_to_anchor=(0.6, -0.1-0.05*bars),loc=3, borderaxespad=0)
        plt.tight_layout()
        b.set_xticklabels(self.data.iloc[:, 0])
        if percent_line:
            b.yaxis.set_major_formatter(FuncFormatter(lambda x, _: '{}%'.format(x * 100)))

        plt.title(self.title)
        plt.tight_layout()
        plt.show()
    #画折线图
    def lines(self,percentage=False):
        markers=['.', 'x', 'o', 'v', '^', '<',
         '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X']
        fig = plt.figure()
        a = fig.add_subplot(111)
        for i in range(self.columns-1):
            a.plot(range(len(self.data.index)), self.data.iloc[:, i+1], label=self.data.columns[i+1], marker=markers[i])
            plt.xticks(range(len(self.data.index)), self.data.iloc[:, 0])
        a.legend(bbox_to_anchor=(0.15, -0.1-0.05*(self.columns/3)),loc=3, borderaxespad=0,ncol=3)
        plt.tight_layout()
        #plt.xlabel(self.data.columns[0])
        a.grid(True, color="gray", axis="both", ls="--", lw=0.5)
        if percentage:
           a.yaxis.set_major_formatter(FuncFormatter(lambda x, _: '{}%'.format(x * 100)))
        plt.title(self.title)
        plt.tight_layout()
        plt.show()

    #画柱状图
    def bars(self,bar_color='r',width=0.8,barsnumber=1,bar_number=False):
        fig = plt.figure()
        a = fig.add_subplot(111)
        labels = self.data.iloc[:, 0]
        a.bar(range(len(self.data.index)), self.data.iloc[:, 1], color=bar_color, alpha=0.6, label=self.data.columns[1],width=width,
              tick_label=labels)
        a.legend(bbox_to_anchor=(1.05, 1), loc=3, borderaxespad=0)
        plt.tight_layout()
        if bar_number:
            for i, j in zip(range(len(self.data.index)), self.data.iloc[:, 1]):
                plt.text(i-0.1, j/2, str(j))
        if barsnumber > 1:
            bottom=self.data.iloc[:, 1]
            for i in range(barsnumber-1):
                a.bar(range(len(self.data.index)), self.data.iloc[:, i+2], bottom=bottom,  alpha=0.6, label=self.data.columns[i+2],width=width,
                      tick_label=labels)
                if bar_number:
                    for j, k in zip(range(len(self.data.index)), self.data.iloc[:, i+2]):
                        plt.text(j - 0.1, k/2+bottom[j], str(k))
                bottom += self.data.iloc[:, i + 2]

            a.legend(bbox_to_anchor=(0.15, -0.1-0.05*(self.columns/3)),loc=3, borderaxespad=0,ncol=3)
            plt.tight_layout()
        plt.title(self.title)
        plt.tight_layout()
        plt.show()
    #画饼图
    def pie(self):
        my_dpi = 96
        plt.figure(figsize=(480 / my_dpi, 480 / my_dpi), dpi=my_dpi)
        values = self.data.iloc[:, 1]
        print(len(self.data))
        explode = [0]*(len(self.data))
        for i in range(len(self.data)):
            if self.data.iloc[:,1][i]<0.5:
                explode[i]=0.1
        plt.pie(values,
        autopct='%.2f%%',shadow=True,explode=explode,
                )  # 绘制饼图
        plt.legend( self.data.iloc[:, 0],
                   loc="center left",
                   fontsize=15,
                   bbox_to_anchor=(1, 0, 0.5, 1))
        plt.tight_layout()
        plt.title(self.title)
        plt.show()

    def bar_group(self,barsnumber=1,bar_number=False):
        width=0.8/barsnumber
        fig = plt.figure()
        a = fig.add_subplot(111)
        labels = self.data.iloc[:, 0]
        a.bar(range(len(self.data.index)), self.data.iloc[:, 1], alpha=0.6, label=self.data.columns[1],
              width=width)

        a.legend(bbox_to_anchor=(1.05, 1), loc=3, borderaxespad=0)
        plt.tight_layout()
        if bar_number:
            for i, j in zip(range(len(self.data.index)), self.data.iloc[:, 1]):
                plt.text(i-0.1, j, str(j))
        if barsnumber > 1:
            multiplier = 1
            for i in range(barsnumber-1):
                offset = multiplier * width
                if i > barsnumber/2-1:
                    a.bar(np.arange(len(self.data.index))+offset, self.data.iloc[:, i+2],  alpha=0.6, label=self.data.columns[i+2],width=width)
                else:
                    a.bar(np.arange(len(self.data.index)) + offset, self.data.iloc[:, i + 2], alpha=0.6,
                          label=self.data.columns[i + 2], width=width,tick_label=labels)
                multiplier += 1
                if bar_number:
                    for j, k in zip(range(len(self.data.index)), self.data.iloc[:, i+2]):
                        plt.text(j - 0.1+offset, k, str(k))

            a.legend(bbox_to_anchor=(0.15, -0.1 - 0.05 * (self.columns / 3)), loc=3, borderaxespad=0, ncol=3)
            plt.tight_layout()

        plt.title(self.title)
        plt.tight_layout()
        plt.show()
    def bar_curve(self, bars=1,lines=1,percent_bar=False,bar_color='r',
                 percent_line=False):
        fig = plt.figure()
        a = fig.add_subplot(111)
        labels = self.data.iloc[:, 0]
        a.bar(range(len(self.data.index)), self.data.iloc[:, 1], alpha=0.6, label=self.data.columns[1],color=bar_color,
              width=0.3, tick_label=labels)
        if percent_bar:
            a.yaxis.set_major_formatter(FuncFormatter(lambda x, _: '{}%'.format(x * 100)))

        bottom = self.data.iloc[:, 1]
        for i in range(bars - 1):
            a.bar(range(len(self.data.index)), self.data.iloc[:, i + 2], bottom=bottom, alpha=0.6,
                  label=self.data.columns[i + 2],width=0.3,
                  tick_label=labels)
            bottom += self.data.iloc[:, i + 1]

        a.legend(bbox_to_anchor=(0.15, -0.1-0.05*bars), loc=3, borderaxespad=0)
        plt.tight_layout()

        b = a.twinx()
        for i in range(lines):
            x = np.arange(len(self.data.index))
            y = self.data.iloc[:, bars+i+1]
            xnew = np.linspace(min(x), max(x), 100)
            f = interpolate.interp1d(x, y, kind="cubic")
            ynew = f(xnew)
            b.plot(xnew, ynew,label=self.data.columns[i + bars + 1])
            plt.xlabel(self.data.columns[0])
        b.legend(bbox_to_anchor=(0.6, -0.1-0.05*lines), loc=3, borderaxespad=0)
        plt.tight_layout()
        b.set_xticklabels(self.data.iloc[:, 0])
        if percent_line:
            b.yaxis.set_major_formatter(FuncFormatter(lambda x, _: '{}%'.format(x * 100)))

        plt.title(self.title)
        plt.tight_layout()
        plt.show()
    def curves(self,percentage=False,grid=False):
        fig = plt.figure()
        a = fig.add_subplot(111)
        for i in range(self.columns - 1):
            x = np.arange(len(self.data.index))
            y = self.data.iloc[:, i + 1]
            xnew = np.linspace(min(x), max(x), 100)
            f = interpolate.interp1d(x, y, kind="cubic")
            ynew = f(xnew)
            a.plot(xnew, ynew, label=self.data.columns[i + 1])
        plt.xticks(range(len(self.data.index)), self.data.iloc[:, 0])
        a.legend(bbox_to_anchor=(1.05, 1), loc=3, borderaxespad=0)
        plt.tight_layout()
        if grid:
            a.grid(True, color="gray", axis="both", ls="--", lw=0.5)
        if percentage:
            a.yaxis.set_major_formatter(FuncFormatter(lambda x, _: '{}%'.format(x * 100)))
        a.legend(bbox_to_anchor=(0.15, -0.1 - 0.05 * (self.columns / 3)), loc=3, borderaxespad=0, ncol=3)
        plt.tight_layout()
        plt.title(self.title)
        plt.tight_layout()
        plt.show()




figure1 = Figure('图4数据.xlsx', title='图4：公司营收规模逐渐提升', usecols=[0, 1, 2])
figure1.bar_line(bars=1,lines=1,bar_color='r',line_number=True,percent_line=True)
figure1 = Figure('图5数据.xlsx', title='图5：公司三费增速陆续进入健康所见通道', usecols=[0, 1, 2,3,4])
figure1.lines(percentage=True)
figure1.curves(percentage=True,grid=True)
figure1 = Figure('图6数据.xlsx', title='图6：公司研发投入逐年提升，营收占比持续维持高位', usecols=[0, 1, 2])
figure1.bar_line(bars=1,lines=1,bar_color='r',bar_number=True,percent_line=True)
figure1 = Figure('图7数据.xlsx', title='图7：公司研发人员硕士及以上学历占比超77%', usecols=[0, 1])
figure1.pie()
figure1 = Figure('图5数据.xlsx', title='图5：公司三费增速陆续进入健康所见通道', usecols=[0, 1,3,4])
figure1.bars(width=0.3,barsnumber=3,bar_number=True)
figure1 = Figure('图5数据.xlsx', title='图5：公司三费增速陆续进入健康所见通道', usecols=[0, 1,3,4])
figure1.bar_group(barsnumber=3,bar_number=True)
figure1 = Figure('图4数据.xlsx', title='图4:公司营收规模逐渐提升', usecols=[0, 1,2])
figure1.bar_curve(bars=1,lines=1,bar_color='r',percent_line=True)

#figure1.bars()
#figure1.lines()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# import plotly.graph_objects as go
#
# # 数据
# labels = ['A', 'B', 'C', 'D']
# values = [15, 30, 45, 10]
#
# # 创建立体饼图
# fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
#
# # 设置立体效果
# fig.update_traces(hole=.4, hoverinfo="label+percent+name")

# 显示图形
# fig.show()




