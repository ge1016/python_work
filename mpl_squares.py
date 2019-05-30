import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.plot(x_values,y_values,linewidth=5) #linewidth决定线条粗细
plt.title('Squares Numbers',fontsize = 24)
plt.xlabel('value',fontsize = 14)
plt.ylabel('square of value',fontsize = 14)
plt.tick_params(axis='both',labelsize = 14)
plt.axis = ([0,1100,1,1100000]) #设置x,y轴的取值范围
plt.show()