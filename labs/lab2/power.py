import numpy as np

def power(sample1, sample2, reps, size, alpha):
    count = 0
    for _ in range(reps):
		idxs = np.random.randint(len(sample1), size=len(sample1))
		data1 = [sample1[idx] for idx in idxs]

		idxs = np.random.randint(len(sample2), size=len(sample2))
		data2 = [sample1[idx] for idx in idxs]
        data1_mean = sum(data1)/len(data1)
        data2_mean = sum(data2)/len(data2)

        val = data1_mean - data2_mean

        if va <= 0:
            count += 1

    pval = count/reps
    if (pval < 1-alpha):
        return ?    


fun1;


fun2;
