import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Reading dataframes 
# Ani Path
# butterfly5 = pd.read_csv('TESTING/testfiles/BUTTERFLY_TRAFFIC/0_to_15_bitsize_5.csv')
# exp5 = pd.read_csv('TESTING/testfiles/EXPONENTIAL/0_to_15_bitsize_5.csv')
# hotspotcentre5 = pd.read_csv('TESTING/testfiles/HOTSPOT_CENTER_TRAFFIC/0_to_15_bitsize_5.csv')
# hotspotedge5 = pd.read_csv("TESTING/testfiles/HOTSPOT_EDGES_TRAFFIC/0_to_15_bitsize_5.csv")
# normal5 = pd.read_csv("TESTING/testfiles/NORMAL_TRAFFIC/0_to_15_bitsize_5.csv")
# poisson5 = pd.read_csv("TESTING/testfiles/POISSON_TRAFFIC_DISTRIBUTION/0_to_15_bitsize_5.csv")
# random5 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_5.csv")

# butterfly20 = pd.read_csv('TESTING/testfiles/BUTTERFLY_TRAFFIC/0_to_15_bitsize_20.csv')
# exp20 = pd.read_csv('TESTING/testfiles/EXPONENTIAL/0_to_15_bitsize_20.csv')
# hotspotcentre20 = pd.read_csv('TESTING/testfiles/HOTSPOT_CENTER_TRAFFIC/0_to_15_bitsize_20.csv')
# # hotspotedge20 = pd.read_csv("TESTING/testfiles/HOTSPOT_EDGES_TRAFFIC/0_to_15_bitsize_20.csv")
# normal20 = pd.read_csv("TESTING/testfiles/NORMAL_TRAFFIC/0_to_15_bitsize_20.csv")
# poisson20 = pd.read_csv("TESTING/testfiles/POISSON_TRAFFIC_DISTRIBUTION/0_to_15_bitsize_20.csv")
# random20 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_20.csv")

# butterfly40 = pd.read_csv('TESTING/testfiles/BUTTERFLY_TRAFFIC/0_to_15_bitsize_40.csv')
# exp40 = pd.read_csv('TESTING/testfiles/EXPONENTIAL/0_to_15_bitsize_40.csv')
# hotspotcentre40 = pd.read_csv('TESTING/testfiles/HOTSPOT_CENTER_TRAFFIC/0_to_15_bitsize_40.csv')
# hotspotedge40 = pd.read_csv("TESTING/testfiles/HOTSPOT_EDGES_TRAFFIC/0_to_15_bitsize_40.csv")
# normal40 = pd.read_csv("TESTING/testfiles/NORMAL_TRAFFIC/0_to_15_bitsize_40.csv")
# poisson40 = pd.read_csv("TESTING/testfiles/POISSON_TRAFFIC_DISTRIBUTION/0_to_15_bitsize_40.csv")
# random40 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_40.csv")

# butterfly64 = pd.read_csv('TESTING/testfiles/BUTTERFLY_TRAFFIC/0_to_15_bitsize_64.csv')
# exp64 = pd.read_csv('TESTING/testfiles/EXPONENTIAL/0_to_15_bitsize_64.csv')
# hotspotcentre64 = pd.read_csv('TESTING/testfiles/HOTSPOT_CENTER_TRAFFIC/0_to_15_bitsize_64.csv')
# hotspotedge64 = pd.read_csv("TESTING/testfiles/HOTSPOT_EDGES_TRAFFIC/0_to_15_bitsize_64.csv")
# normal64 = pd.read_csv("TESTING/testfiles/NORMAL_TRAFFIC/0_to_15_bitsize_64.csv")
# poisson64 = pd.read_csv("TESTING/testfiles/POISSON_TRAFFIC_DISTRIBUTION/0_to_15_bitsize_64.csv")
# random64 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_64.csv")


# deepath
butterfly5 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/BUTTERFLY_TRAFFIC/0_to_15_bitsize_5.csv')
exp5 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/EXPONENTIAL/0_to_15_bitsize_5.csv')
hotspotcentre5 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/HOTSPOT_CENTER_TRAFFIC/0_to_15_bitsize_5.csv')
hotspotedge5 = pd.read_csv("C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/HOTSPOT_EDGES_TRAFFIC/0_to_15_bitsize_5.csv")
normal5 = pd.read_csv("C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/NORMAL_TRAFFIC/0_to_15_bitsize_5.csv")
poisson5 = pd.read_csv("C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/POISSON_TRAFFIC_DISTRIBUTION/0_to_15_bitsize_5.csv")
random5 = pd.read_csv("C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_5.csv")

butterfly20 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/BUTTERFLY_TRAFFIC/0_to_15_bitsize_20.csv')
exp20 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/EXPONENTIAL/0_to_15_bitsize_20.csv')
hotspotcentre20 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/HOTSPOT_CENTER_TRAFFIC/0_to_15_bitsize_20.csv')
hotspotedge20 = pd.read_csv("C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/HOTSPOT_EDGES_TRAFFIC/0_to_15_bitsize_20.csv")
normal20 = pd.read_csv("C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/NORMAL_TRAFFIC/0_to_15_bitsize_20.csv")
poisson20 = pd.read_csv("C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/POISSON_TRAFFIC_DISTRIBUTION/0_to_15_bitsize_20.csv")
random20 = pd.read_csv("C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_20.csv")

butterfly40 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/BUTTERFLY_TRAFFIC/0_to_15_bitsize_40.csv')
exp40 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/EXPONENTIAL/0_to_15_bitsize_40.csv')
hotspotcentre40 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/HOTSPOT_CENTER_TRAFFIC/0_to_15_bitsize_40.csv')
hotspotedge40 = pd.read_csv("C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/HOTSPOT_EDGES_TRAFFIC/0_to_15_bitsize_40.csv")
normal40 = pd.read_csv("C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/NORMAL_TRAFFIC/0_to_15_bitsize_40.csv")
poisson40 = pd.read_csv("C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/POISSON_TRAFFIC_DISTRIBUTION/0_to_15_bitsize_40.csv")
random40 = pd.read_csv("C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_40.csv")

butterfly64 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/BUTTERFLY_TRAFFIC/0_to_15_bitsize_64.csv')
exp64 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/EXPONENTIAL/0_to_15_bitsize_64.csv')
hotspotcentre64 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/HOTSPOT_CENTER_TRAFFIC/0_to_15_bitsize_64.csv')
hotspotedge64 = pd.read_csv("C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/HOTSPOT_EDGES_TRAFFIC/0_to_15_bitsize_64.csv")
normal64 = pd.read_csv("C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/NORMAL_TRAFFIC/0_to_15_bitsize_64.csv")
poisson64 = pd.read_csv("C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/POISSON_TRAFFIC_DISTRIBUTION/0_to_15_bitsize_64.csv")
random64 = pd.read_csv("C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_64.csv")


# Drop columns from DataFrames
# butterfly5.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# exp5.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# hotspotcentre5.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# hotspotedge5.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# normal5.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# poisson5.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# random5.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)

# butterfly20.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# exp20.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# hotspotcentre20.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# # hotspotedge20.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# normal20.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# poisson20.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# random20.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)

# butterfly40.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# exp40.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# hotspotcentre40.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# hotspotedge40.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# normal40.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# poisson40.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# random40.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)

# butterfly64.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# exp64.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# hotspotcentre64.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# hotspotedge64.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# normal64.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# poisson64.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# random64.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)

# Combine dataframes
# combined_df = pd.concat([butterfly5, exp5, hotspotcentre5, hotspotedge5, normal5, poisson5, random5])
# print(combined_df.shape)

index1 = list(range(1,102,1))
index = list(range(1,101,1))




# Traffic Vs Iteration(5 bits)
fig1, axs1 = plt.subplots(7, 1, figsize=(10, 15), sharex=True, gridspec_kw={'hspace': 0.5})

labels = ['Butterfly', 'Exponential', 'Hotspot Center', 'Hotspot Edge', 'Normal', 'Poisson', 'Random']
colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan', 'magenta']

for ax, data, label, color in zip(axs1, [butterfly5, exp5, hotspotcentre5, hotspotedge5, normal5, poisson5, random5], labels, colors):
    ax.plot(index1, np.array(data['Total Delay']), linestyle='-', color=color)

fig1.text(0.04, 0.5, 'Total Delays', va='center', rotation='vertical')
fig1.legend(labels, loc='upper right')
fig1.suptitle('Traffic vs Iteration(5 bits)', fontsize=16)

#************************************************************************************************************************************

# Traffic Vs Iteration (20 bits)
fig2, axs2 = plt.subplots(7, 1, figsize=(10, 15), sharex=True, gridspec_kw={'hspace': 0.5})

labels = ['Butterfly', 'Exponential', 'Hotspot Center', 'Hotspot Edge', 'Normal', 'Poisson', 'Random']
colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan', 'magenta']

for ax, data, label, color in zip(axs2, [butterfly20, exp20, hotspotcentre20, hotspotedge20, normal20, poisson20, random20], labels, colors):
    ax.plot(index1, np.array(data['Total Delay']), linestyle='-', color=color, label=label)
 

fig2.text(0.04, 0.5, 'Total Delays', va='center', rotation='vertical')
fig2.legend(labels, loc='upper right')
fig2.suptitle('Traffic vs Iteration(20 bits)', fontsize=16)


#************************************************************************************************************************************

# Traffic Vs Iteration (40 bits)
fig3, axs3 = plt.subplots(7, 1, figsize=(10, 15), sharex=True, gridspec_kw={'hspace': 0.5})

labels = ['Butterfly', 'Exponential', 'Hotspot Center', 'Hotspot Edge', 'Normal', 'Poisson', 'Random']
colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan', 'magenta']

for ax, data, label, color in zip(axs3, [butterfly40, exp40, hotspotcentre40, hotspotedge40, normal40, poisson40, random40], labels, colors):
    ax.plot(index1, np.array(data['Total Delay']), linestyle='-', color=color)

fig3.text(0.04, 0.5, 'Total Delays', va='center', rotation='vertical')
fig3.legend(labels, loc='upper right')
fig3.suptitle('Traffic vs Iteration(40 bits)', fontsize=16)

#************************************************************************************************************************************

# Traffic Vs Iteration (64 bits)
fig4, axs4 = plt.subplots(7, 1, figsize=(10, 15), sharex=True, gridspec_kw={'hspace': 0.5})

labels = ['Butterfly', 'Exponential', 'Hotspot Center', 'Hotspot Edge', 'Normal', 'Poisson', 'Random']
colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan', 'magenta']

for ax, data, label, color in zip(axs4, [butterfly64, exp64, hotspotcentre64, hotspotedge64, normal64, poisson64, random64], labels, colors):
    
    if label == 'Exponential':
        ax.plot(index, np.array(data['Total Delay']), linestyle='-', color=color, label=label)
    else:
        ax.plot(index1, np.array(data['Total Delay']), linestyle='-', color=color, label=label)

fig4.text(0.04, 0.5, 'Total Delays', va='center', rotation='vertical')
fig4.legend(labels, loc='upper right')
fig4.suptitle('Traffic vs Iteration(64 bits)', fontsize=16)


plt.show()












# plt.subplot(3,3,1)
# plt.plot(index1, np.array(butterfly5['Total Delay']), linestyle='-', color='blue', label = "5 Bit Traffic")
# plt.plot(index1, np.array(butterfly20['Total Delay']), linestyle='-', color='orange', label = "20 Bit Traffic")
# plt.plot(index1, np.array(butterfly40['Total Delay']), linestyle='-', color='green', label = "40 Bit Traffic")
# plt.plot(index1, np.array(butterfly64['Total Delay']), linestyle='-', color='red', label = "64 Bit Traffic")
# # plt.xlabel('Index')
# plt.ylabel('Total Delays')
# plt.title('Total Delays')
# plt.legend(loc='upper right')
# # plt.yticks(range(0, 21))
# # plt.ylim(bottom = 5)

# plt.subplot(3,3,2)
# plt.title("Exponential Traffic")
# plt.plot(index1, np.array(exp5['Total Delay']), linestyle='-', color='blue', label = "5 Bit Traffic")
# plt.plot(index1, np.array(exp20['Total Delay']), linestyle='-', color='orange', label = "20 Bit Traffic")
# plt.plot(index1, np.array(exp40['Total Delay']), linestyle='-', color='green', label = "40 Bit Traffic")
# plt.plot(index, np.array(exp64['Total Delay']), linestyle='-', color='red', label = "64 Bit Traffic")
# # plt.xlabel('Index')
# plt.ylabel('Total Delays')
# plt.legend(loc='upper right')
# # plt.yticks(range(0, 21))
# # plt.ylim(bottom = 5)

# plt.subplot(3,3,3)
# plt.title("Center Hotspot Traffic")
# plt.plot(index1, np.array(hotspotcentre5['Total Delay']), linestyle='-', color='blue', label = "5 Bit Traffic")
# plt.plot(index1, np.array(hotspotcentre20['Total Delay']), linestyle='-', color='orange', label = "20 Bit Traffic")
# plt.plot(index1, np.array(hotspotcentre40['Total Delay']), linestyle='-', color='green', label = "40 Bit Traffic")
# plt.plot(index1, np.array(hotspotcentre64['Total Delay']), linestyle='-', color='red', label = "64 Bit Traffic")
# # plt.xlabel('Index')
# plt.ylabel('Total Delays')
# plt.legend(loc='upper right')
# # plt.yticks(range(0, 21))
# # plt.ylim(bottom = 5)

# plt.subplot(3,3,4)
# plt.title("Edge Hotspot Traffic")
# plt.plot(index1, np.array(hotspotedge5['Total Delay']), linestyle='-', color='blue', label = "5 Bit Traffic")
# # plt.plot(index, np.array(hotspotedge20['Total Delay']), linestyle='-', color='orange', label = "20 Bit Traffic")
# plt.plot(index1, np.array(hotspotedge40['Total Delay']), linestyle='-', color='green', label = "40 Bit Traffic")
# plt.plot(index1, np.array(hotspotedge64['Total Delay']), linestyle='-', color='red', label = "64 Bit Traffic")
# # plt.xlabel('Index')
# plt.ylabel('Total Delays')
# plt.legend(loc='upper right')
# # plt.yticks(range(0, 21))
# # plt.ylim(bottom = 5)

# plt.subplot(3,3,5)
# plt.title("Normal Traffic")
# plt.plot(index1, np.array(normal5['Total Delay']), linestyle='-', color='blue', label = "5 Bit Traffic")
# plt.plot(index1, np.array(normal20['Total Delay']), linestyle='-', color='orange', label = "20 Bit Traffic")
# plt.plot(index1, np.array(normal40['Total Delay']), linestyle='-', color='green', label = "40 Bit Traffic")
# plt.plot(index1, np.array(normal64['Total Delay']), linestyle='-', color='red', label = "64 Bit Traffic")
# # plt.xlabel('Index')
# plt.ylabel('Total Delays')
# plt.legend(loc='upper right')
# # plt.yticks(range(0, 21))
# # plt.ylim(bottom = 5)

# plt.subplot(3,3,6)
# plt.title("Poisson Traffic")
# plt.plot(index1, np.array(poisson5['Total Delay']), linestyle='-', color='blue', label = "5 Bit Traffic")
# plt.plot(index1, np.array(poisson20['Total Delay']), linestyle='-', color='orange', label = "20 Bit Traffic")
# plt.plot(index1, np.array(poisson40['Total Delay']), linestyle='-', color='green', label = "40 Bit Traffic")
# plt.plot(index1, np.array(poisson64['Total Delay']), linestyle='-', color='red', label = "64 Bit Traffic")
# # plt.xlabel('Index')
# plt.ylabel('Total Delays')
# plt.legend(loc='upper right')
# # plt.yticks(range(0, 21))
# # plt.ylim(bottom = 5)

# plt.subplot(3,3,8)
# plt.title("Random Traffic")
# plt.plot(index1, np.array(random5['Total Delay']), linestyle='-', color='blue', label = "5 Bit Traffic")
# plt.plot(index1, np.array(random20['Total Delay']), linestyle='-', color='orange', label = "20 Bit Traffic")
# plt.plot(index1, np.array(random40['Total Delay']), linestyle='-', color='green', label = "40 Bit Traffic")
# plt.plot(index1, np.array(random64['Total Delay']), linestyle='-', color='red', label = "60 Bit Traffic")
# # plt.xlabel('Index')
# plt.ylabel('Total Delays')
# plt.legend(loc='upper right')
# # plt.yticks(range(0, 21))
# # plt.ylim(bottom = 5)

# plt.show()

# exp5['Total Delay'],hotspotcentre5['Total Delay'],hotspotedge5['Total Delay'],normal5['Total Delay'],poisson5['Total Delay'],random5['Total Delay']],