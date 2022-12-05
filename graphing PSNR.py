import matplotlib.pyplot as plt
import datetime
import numpy as np

def datetime_to_int(datetime):
    #datetime here is just a string composed from a datetime obj.
    #ex: 10:30:56.xxxx

    #first, remove trailing decimal
    dec_split = datetime.split(".")
    dec_split = dec_split[0]

    colon_split = dec_split.split(":")
    hours = int(colon_split[0])
    minutes = int(colon_split[1])
    seconds = int(colon_split[2])

    minutes = minutes * (100/60)
    seconds = seconds * (100/60)
    time = hours + (minutes / 100) + (seconds/100**2)
    return time

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

#iterations I want to graph

desired_iterations = [
    1, #100th iteration
    10,
    100,
    500,
    1000,
    2000 #200,00th iteration
]

#depth ablations
ablation_2_layers_no_skip = []
ablation_3_layers_no_skip = []
ablation_4_layers_no_skip = []
ablation_5_layers = []
ablation_6_layers = []
ablation_7_layers = []

#width & depth ablations
ablation_5_layers_128_parameters_per_layer = []
ablation_6_layers_128_parameters_per_layer = []
ablation_7_layers_128_parameters_per_layer = []
ablation_128_parameters_per_layer = []

for i in desired_iterations:
    #ablation_2_layers_no_skip.append((ablations_data["ablation_2_layers_no_skip"][i][2], ablations_data["ablation_2_layers_no_skip"][i][3]))
    ablation_3_layers_no_skip.append((ablations_data["ablation_3_layers_no_skip"][i][2], ablations_data["ablation_3_layers_no_skip"][i][3]))
    #ablation_4_layers_no_skip.append((ablations_data["ablation_4_layers_no_skip"][i][2], ablations_data["ablation_4_layers_no_skip"][i][3]))
    ablation_5_layers.append((ablations_data["ablation_5_layers"][i][2], ablations_data["ablation_5_layers"][i][3]))
    #ablation_5_layers_128_parameters_per_layer.append((ablations_data["ablation_5_layers_128_parameters_per_layer"][i][2], ablations_data["ablation_5_layers_128_parameters_per_layer"][i][3]))
    ablation_6_layers.append((ablations_data["ablation_6_layers"][i][2],ablations_data["ablation_6_layers"][i][3]))
    #ablation_6_layers_128_parameters_per_layer.append((ablations_data["ablation_6_layers_128_parameters_per_layer"][i][2], ablations_data["ablation_6_layers_128_parameters_per_layer"][i][3]))
    #ablation_7_layers.append((ablations_data["ablation_7_layers"][i][2],ablations_data["ablation_7_layers"][i][3]))
    #ablation_7_layers_128_parameters_per_layer.append((ablations_data["ablation_7_layers_128_parameters_per_layer"][i][2], ablations_data["ablation_7_layers_128_parameters_per_layer"][i][3]))
    #ablation_128_parameters_per_layer.append((ablations_data["ablation_128_parameters_per_layer"][i][2],ablations_data["ablation_128_parameters_per_layer"][i][3]))


"""

TO DO

ADD AXIS LABELS
RE-SCALE Y AXIS

"""
fig, ax = plt.subplots()
plt.xticks(range(1, 12)) #this sets it to increment up to 11.
plt.yticks(np.arange(0,0.055, 0.005))

'''
y_val = [float(x[0]) for x in ablation_2_layers_no_skip]
x_val = [y[1] for y in ablation_2_layers_no_skip]
for x in range(len(x_val)):
    x_val[x] = datetime_to_int(x_val[x])
ax.scatter(x_val, y_val, label="2 layers", marker="1")
'''

y_val = [float(x[0]) for x in ablation_3_layers_no_skip]
x_val = [y[1] for y in ablation_3_layers_no_skip]
for x in range(len(x_val)):
    x_val[x] = datetime_to_int(x_val[x])
ax.scatter(x_val, y_val, label="3 layers", marker=".")

'''
y_val = [float(x[0]) for x in ablation_4_layers_no_skip]
x_val = [y[1] for y in ablation_4_layers_no_skip]
for x in range(len(x_val)):
    x_val[x] = datetime_to_int(x_val[x])
ax.scatter(x_val, y_val, label="4 layers", marker="2")
'''

y_val = [float(x[0]) for x in ablation_5_layers]
x_val = [y[1] for y in ablation_5_layers]
for x in range(len(x_val)):
    x_val[x] = datetime_to_int(x_val[x])
ax.scatter(x_val, y_val, label="5 layers", marker="o")

"""
y_val = [float(x[0]) for x in ablation_5_layers_128_parameters_per_layer]
x_val = [y[1] for y in ablation_5_layers_128_parameters_per_layer]
for x in range(len(x_val)):
    x_val[x] = datetime_to_int(x_val[x])
ax.scatter(x_val, y_val, label="5 layers, half width", marker="*")
"""

y_val = [float(x[0]) for x in ablation_6_layers]
x_val = [y[1] for y in ablation_6_layers]
for x in range(len(x_val)):
    x_val[x] = datetime_to_int(x_val[x])
ax.scatter(x_val, y_val, label="6 layers", marker="s")

"""
y_val = [float(x[0]) for x in ablation_6_layers_128_parameters_per_layer]
x_val = [y[1] for y in ablation_6_layers_128_parameters_per_layer]
for x in range(len(x_val)):
    x_val[x] = datetime_to_int(x_val[x])
ax.scatter(x_val, y_val, label="6 layers, half width", marker="x")
"""

"""
y_val = [float(x[0]) for x in ablation_7_layers]
x_val = [y[1] for y in ablation_7_layers]
for x in range(len(x_val)):
    x_val[x] = datetime_to_int(x_val[x])
ax.scatter(x_val, y_val, label="7 layers", marker="8")
"""

"""
y_val = [float(x[0]) for x in ablation_7_layers_128_parameters_per_layer]
x_val = [y[1] for y in ablation_7_layers_128_parameters_per_layer]
for x in range(len(x_val)):
    x_val[x] = datetime_to_int(x_val[x])
ax.scatter(x_val, y_val, label="7 layers, half width", marker="d")
"""

"""
y_val = [float(x[0]) for x in ablation_128_parameters_per_layer]
x_val = [y[1] for y in ablation_128_parameters_per_layer]
for x in range(len(x_val)):
    x_val[x] = datetime_to_int(x_val[x])
ax.scatter(x_val, y_val, label="8 layers, half width", marker="h")
"""

plt.legend()
plt.show()