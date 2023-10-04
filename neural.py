import numpy as np

desired = np.array([0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0])

training_data = np.array([[0.3355, 0.3351, 0.336, 0.3356, 0.3358], [0.3356, 0.3352, 0.3349, 0.3339, 0.3333], [0.3342, 0.334, 0.3332, 0.3329, 0.3315], [0.331, 0.3304, 0.3303, 0.331, 0.3316], [0.331, 0.331, 0.3313, 0.3317, 0.3314], [0.3323, 0.3327, 0.3334, 0.3342, 0.335], [0.3303, 0.3266, 0.3272, 0.3276, 0.3274], [0.3286, 0.3287, 0.3302, 0.3297, 0.3288], [0.3279, 0.3283, 0.3268, 0.3244, 0.323], [0.3224, 0.3211, 0.3198, 0.3232, 0.3226], [0.3221, 0.3219, 0.3224, 0.3229, 0.3227], [0.3224, 0.3227, 0.3237, 0.3242, 0.3242], [0.3247, 0.325, 0.3254, 0.326, 0.3261], [0.3264, 0.3275, 0.3281, 0.3276, 0.3276], [0.3273, 0.3269, 0.327, 0.3269, 0.3275], [0.3272, 0.3276, 0.3274, 0.3263, 0.3265], [0.3271, 0.3269, 0.3263, 0.3267, 0.3266], [0.3272, 0.3271, 0.3273, 0.3268, 0.3268], [0.3281, 0.3287, 0.3285, 0.3292, 0.3295], [0.3298, 0.3306, 0.3315, 0.3317, 0.3311], [0.3305, 0.3306, 0.3301, 0.3302, 0.3299]])

weights = np.random.randn(5)

bias = int(np.random.randn(1))


def sig(z):
    z = 1 / (1 + np.exp(-z))
    return z


"""dc/dw = dc/da da/dz dz/ dw"""
output = []
for i in range(1000):
    for i in training_data:
        output.append(sig(np.dot(i, weights)) + bias)
    counter = 0
    for i in output:
        counter += 0
        if i - desired[counter - 1] != 0:
            weights -= 2 * (i - desired[counter - 1]) * (sig(np.dot(training_data[counter-1], weights)+bias) * (1-sig(np.dot(training_data[counter-1], weights) + bias))) * training_data[counter - 1]
            bias -= 2 * (i - desired[counter - 1]) * (sig(np.dot(training_data[counter-1], weights)+bias) * (1-sig(np.dot(training_data[counter-1], weights) + bias)))
    print(weights)
    print(output)