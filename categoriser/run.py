import matplotlib.pyplot as plot

#TODO : should automate this task
arr_mean = [75.32, 74.12, 79.11, 80.33, 81.68]
arr_deviation = [0.6666, 0.666, 0.133, 1.33, 0.133]
stringis = "Plot for categorisation when fold = 5"
plot.title(stringis)
plot.errorbar(range(1, 6), arr_mean, xerr=0, yerr=arr_deviation)
plot.xlabel('kValue')
plot.ylabel('Accuracy')
plot.ylim([20, 100])
plot.xlim([0, 6])
plot.show()
