# 导入相关模块
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 50)
y = np.sin(x)

# 设置figure
plt.figure(figsize=(6, 4))

# 修改颜色、点、线
plt.plot(x, y, 'g.-')
plt.plot(x, y * 2, 'm--')

# 添加标题
plt.title("sin(x) & 2sin(x)")

# 设置坐标轴
plt.xlim((0, np.pi + 4))
plt.ylim((-3.0, 3.0))
plt.xlabel('X')
plt.ylabel('Y')

# 设置刻度
plt.xticks((0, np.pi * 0.5, np.pi, np.pi * 1.5, np.pi * 2))

# 设置label和legend
plt.plot(x, y, label="sin(x)")
plt.plot(x, y * 2, label="2sin(x)")
# plt.legend()
plt.legend(loc='best')

# 添加注释
x0 = np.pi
y0 = 0
plt.scatter(x0, y0, s=50) # 画出标注点
plt.annotate('sin(np.pi)=%s' % y0, xy=(np.pi, 0), xycoords='data', xytext=(+35, -15),
             textcoords='offset points', fontsize=14,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.3"))
plt.text(0.5, -0.25, "sin(np.pi) = 0", fontdict={'size': 16, 'color': 'r'})

# 画图
plt.show()
