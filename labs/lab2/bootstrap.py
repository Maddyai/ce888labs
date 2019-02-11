import matplotlib
matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import numpy as np


def boostrap(sample, sample_size, iterations):
	per = 95
	data_mean = []
	for _ in range(iterations):
		idxs = np.random.randint(sample_size, size=sample_size)
		data = [sample[idx] for idx in idxs]
		mean = sum(data)/len(data)
		data_mean.append(mean)
	total = iterations
	remove_per = int(((100 - per)/100 * total)/2)
	data_mean = data_mean[remove_per:-remove_per]

	lower = min(data_mean)
	upper = max(data_mean)
	data_mean = sum(data_mean)/len(data_mean)
	return data_mean, lower, upper


if __name__ == "__main__":
	# df = pd.read_csv('./data/salaries.csv')

	# data = df.values.T[1]
	# boots = []
	# for i in range(100, 100000, 1000):
	# 	boot = boostrap(data, data.shape[0], i)
	# 	boots.append([i, boot[0], "mean"])
	# 	boots.append([i, boot[1], "lower"])
	# 	boots.append([i, boot[2], "upper"])

	# df_boot = pd.DataFrame(boots, columns=['Boostrap Iterations', 'Mean', "Value"])
	# sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], data=df_boot, fit_reg=False, hue="Value")

	# sns_plot.axes[0, 0].set_ylim(0,)
	# sns_plot.axes[0, 0].set_xlim(0, 100000)

	# sns_plot.savefig("./png/bootstrap_confidence.png", bbox_inches='tight')
	# sns_plot.savefig("./pdf/bootstrap_confidence.pdf", bbox_inches='tight')


	#print ("Mean: %f")%(np.mean(data))
	#print ("Var: %f")%(np.var(data))

	# Exercise 2
	df = pd.read_csv('./data/vehicles.csv')

	curr_data = df.values.T[0]
	df = df.dropna()
	new_data = df.values.T[1]

	print (len(curr_data))
	print (len(new_data))
	print (np.mean(curr_data))
	print (np.mean(new_data))

	boots = []

	for i in range(100, 100000, 1000):
		curr_boot = boostrap(curr_data, curr_data.shape[0], i)
		new_boot = boostrap(new_data, new_data.shape[0], i)

		boots.append([i, curr_boot[0], "curr-mean"])
		boots.append([i, curr_boot[1], "curr-lower"])
		boots.append([i, curr_boot[2], "curr-upper"])
		boots.append([i, new_boot[0], "new-mean"])
		boots.append([i, new_boot[1], "new-lower"])
		boots.append([i, new_boot[2], "new-upper"])

	df_boot = pd.DataFrame(boots, columns=['Boostrap Iterations', 'Mean', "Value"])
	sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], data=df_boot, fit_reg=True, hue="Value")

	sns_plot.axes[0, 0].set_ylim(0,)
	sns_plot.axes[0, 0].set_xlim(0, 100000)

	sns_plot.savefig("./png/bootstrap_vehicles.png", bbox_inches='tight')
	sns_plot.savefig("./pdf/bootstrap_vehicles.pdf", bbox_inches='tight')
		