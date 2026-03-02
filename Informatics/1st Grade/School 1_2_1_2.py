import matplotlib.pyplot as plt

high=[2.3, 3.0, 2.5, 1.0, 1.9, 3.3, 4.5, 3.7, 5.6, 4.4, 0.3, -3.4, -3.1, 1.3, 1.8, 2.4, 0.1, -0.7, -2.7, 0.9, 4.6, 7.1, 6.7, 8.4, 4.5, 6.8, 4.0, 2.1, 0.9, 2.4, 4.8]
low=[-10.2, -5.2, -8.0, -5.6, -7.8, -5.9, -5.9, -5.0, -1.2, -3.4, -10.3, -11.3, -8.9, -10.1, -5.3, -7.2, -9.2, -9.9, -7.7, -9.8, -8.7, -5.0, -0.6, 1.3, 1.9, -1.9, -4.6, -5.9, -7.2, -8.0, -6.8]
plt.figure(dpi=100)
plt.style.use('ggplot')
plt.title('january high-low 10106')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(high, color='red', label='h')
plt.plot(low, color='blue', label='l')
plt.xticks([0, 1, 2], ['a', 'b', 'c'])
plt.yticks([1, 2, 3], ['d', 'e', 'f'])
plt.legend()
plt.show()

# plt.plot()
# plt.bar(), plt.barh()
# plt.hist(bins=)
# plt.boxplot()
# plt.scatter()

# plt.bar([1, 2, 3, 4, 5], [12, 19, 1, 2, 31])
# plt.xticks([0, 1, 2, 3, 4], ['a', 'b', 'c', 'd', 'e'])
plt.show()