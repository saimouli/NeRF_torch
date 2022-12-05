import matplotlib.pyplot as plt

'''
Returns dictionary for each file. Each element is a line from the file to then be parsed, in the form of:
Iteration #, Loss, PSNR, Time
'''
def load_data(ablation):
    file = open("ablations/" + ablation + "/fern_test/exp_log.txt")
    lines = file.readlines()

    data = {}

    line_number = 0
    for line in lines:
        line_number += 1
        raw_line = line.strip()

        #split raw line by spaces. then just access at the right spots
        split = raw_line.split()
        iter = split[2]
        loss = split[4]
        psnr = split[6]
        time = split[8]
        to_be_added = [iter, loss, psnr, time]

        data[line_number] = to_be_added

    return data

#all ablations
list_of_ablations = [
    "ablation_3_layers_no_skip",
    "ablation_5_layers",
    "ablation_5_layers_128_parameters_per_layer",
    "ablation_6_layers",
    "ablation_6_layers_128_parameters_per_layer",
    "ablation_7_layers_128_parameters_per_layer",
    "ablation_128_parameters_per_layer"
]

ablations_data = {}

for ablation in list_of_ablations:
    ablations_data[ablation] = load_data(ablation)

print(ablations_data)

#now graph with matplotlib.

#graphing of layer ablations. width per layer same as original paper
#create graph of loss v time and psnr v time

depth_ablations = [
    "ablation_3_layers_no_skip",
    "ablation_5_layers",
    "ablation_6_layers",
    "ablation_128_parameters_per_layer"
]

#iterations I want to graph

desired_iterations = [
    1, #100th iteration
    10,
    100,
    500,
    1000,
    2000
]

ablation_3_layers_no_skip = []
ablation_5_layers = []
ablation_6_layers = []
ablation_128_parameters_per_layer = []

'''
for i in ablations_data:
    for j in depth_ablations:
        if i == j:
            for k in desired_iterations:
                ablations_data[i][k]
'''

for i in desired_iterations:
    print(ablations_data["ablation_3_layers_no_skip"][i][1])
    ablation_3_layers_no_skip.append((ablations_data["ablation_3_layers_no_skip"][i][1], ablations_data["ablation_3_layers_no_skip"][i][3]))
    ablation_5_layers.append((ablations_data["ablation_5_layers"][i][1], ablations_data["ablation_5_layers"][i][3]))
    ablation_6_layers.append((ablations_data["ablation_6_layers"][i][1],ablations_data["ablation_6_layers"][i][3]))

print(ablation_3_layers_no_skip)

zip(*ablation_3_layers_no_skip)
plt.scatter(*zip(*ablation_3_layers_no_skip))
plt.show()

plt.scatter(ablation_3_layers_no_skip)
plt.show()