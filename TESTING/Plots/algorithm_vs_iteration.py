import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Reading dataframes 
vc5 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_5.csv')
vc20 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_20.csv')
vc40 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_40.csv')
vc64 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_64_new_final_final.csv')

dynamic_adaptive5 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/DYNAMIC_ADAPTIVE/0_to_15_bitsize_5.csv')
dynamic_adaptive20 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/DYNAMIC_ADAPTIVE/0_to_15_bitsize_20.csv')
dynamic_adaptive40 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/DYNAMIC_ADAPTIVE/0_to_15_bitsize_40.csv')
dynamic_adaptive64 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/DYNAMIC_ADAPTIVE/0_to_15_bitsize_64.csv')

dynamic_xy5 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/DYNAMIC_XY/0_to_15_bitsize_5.csv')
dynamic_xy20 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/DYNAMIC_XY/0_to_15_bitsize_20.csv')
dynamic_xy40 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/DYNAMIC_XY/0_to_15_bitsize_40.csv')
dynamic_xy64 = pd.read_csv('C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/DYNAMIC_XY/0_to_15_bitsize_64.csv')
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
fig1, axs1 = plt.subplots(3, 1, figsize=(10, 15), sharex=True, gridspec_kw={'hspace': 0.5})

labels = ['XY routing', 'ADAPTIVE routing', 'PROPOSED routing algorithm']
colors = ['blue', 'green', 'red']

for ax, data, label, color in zip(axs1, [dynamic_xy5, dynamic_adaptive5, vc5], labels, colors):
    x_values = np.arange(len(data['Total Delay']))
    y_values = np.array(data['Total Delay'])
    
    # Plot segments with np.nan as discontinuities
    nan_positions = np.where(np.isnan(y_values))[0]

    # Plot normal line
    ax.plot(x_values, y_values, linestyle='-', color=color, label=label, linewidth = 2.5)

    # Add discontinuity markers where np.nan values occur
    if nan_positions.size > 0:
        for nan_position in nan_positions:
            ax.scatter(x_values[nan_position], y_values[nan_position], color='red', linestyle='-', s=100, zorder=5, linewidth = 2.5)

    # Set x-axis ticks to 0, 1, 2, ..., 99
    ax.set_xticks(np.arange(0, 100, 5))
    ax.set_xticklabels(np.arange(0, 100, 5), rotation=0)  # Adjust rotation if needed

# fig1.legend(labels, loc='upper right')
fig1.legend()
fig1.text(0.04, 0.5, 'Latency (in Cycles)', va='center', rotation='vertical',fontsize = 16)
fig1.suptitle('Latency vs Iteration (5 bits)', fontsize=16)
fig1.text(0.5, 0.04, 'Iteration', ha='center', fontsize=16)






#************************************************************************************************************************************

#  Traffic Vs Iteration (20 bits)
fig2, axs2 = plt.subplots(3, 1, figsize=(10, 15), sharex=True, gridspec_kw={'hspace': 0.5})

labels = ['XY routing', 'ADAPTIVE routing', 'PROPOSED routing algorithm']
colors = ['blue', 'green', 'red']

for ax, data, label, color in zip(axs2, [dynamic_xy20, dynamic_adaptive20, vc20], labels, colors):
    x_values = np.arange(len(data['Total Delay']))
    y_values = np.array(data['Total Delay'])
    
    # Plot segments with np.nan as discontinuities
    nan_positions = np.where(np.isnan(y_values))[0]

    # Plot normal line
    ax.plot(x_values, y_values, linestyle='-', color=color, label=label, linewidth = 2.5)

    # Add discontinuity markers where np.nan values occur
    if nan_positions.size > 0:
        for nan_position in nan_positions:
            ax.scatter(x_values[nan_position], y_values[nan_position], color='red', linestyle='-', s=100, zorder=5, linewidth = 2.5)

    # Set x-axis ticks to 0, 1, 2, ..., 99
    ax.set_xticks(np.arange(0, 100, 5))
    ax.set_xticklabels(np.arange(0, 100, 5), rotation=0)  # Adjust rotation if needed

# fig1.legend(labels, loc='upper right')
fig2.legend()
fig2.text(0.04, 0.5, 'Latency (in Cycles)', va='center', rotation='vertical',fontsize = 16)
fig2.suptitle('Latency vs Iteration (20 bits)', fontsize=16)
fig2.text(0.5, 0.04, 'Iteration', ha='center', fontsize=16)

# #************************************************************************************************************************************

# # Traffic Vs Iteration (40 bits)
fig3, axs3 = plt.subplots(3, 1, figsize=(10, 15), sharex=True, gridspec_kw={'hspace': 0.5})

labels = ['XY routing', 'ADAPTIVE routing', 'PROPOSED routing algorithm']
colors = ['blue', 'green', 'red']

for ax, data, label, color in zip(axs3, [dynamic_xy40, dynamic_adaptive40, vc40], labels, colors):
    x_values = np.arange(len(data['Total Delay']))
    y_values = np.array(data['Total Delay'])
    
    # Plot segments with np.nan as discontinuities
    nan_positions = np.where(np.isnan(y_values))[0]

    # Plot normal line
    ax.plot(x_values, y_values, linestyle='-', color=color, label=label, linewidth = 2.5)

    # Add discontinuity markers where np.nan values occur
    if nan_positions.size > 0:
        for nan_position in nan_positions:
            ax.scatter(x_values[nan_position], y_values[nan_position], color='red', linestyle='-', s=100, zorder=5, linewidth = 2.5)

    # Set x-axis ticks to 0, 1, 2, ..., 99
    ax.set_xticks(np.arange(0, 100, 5))
    ax.set_xticklabels(np.arange(0, 100, 5), rotation=0)  # Adjust rotation if needed

# fig1.legend(labels, loc='upper right')
fig3.legend()
fig3.text(0.04, 0.5, 'Latency (in Cycles)', va='center', rotation='vertical', fontsize =16)
fig3.suptitle('Latency vs Iteration (40 bits)', fontsize=16)
fig3.text(0.5, 0.04, 'Iteration', ha='center', fontsize=16)


# #************************************************************************************************************************************

# # Traffic Vs Iteration (64 bits)
fig4, axs4 = plt.subplots(3, 1, figsize=(10, 15), sharex=True, gridspec_kw={'hspace': 0.5})

labels = ['XY routing', 'ADAPTIVE routing', 'PROPOSED routing algorithm']
colors = ['blue', 'green', 'red']

for ax, data, label, color in zip(axs4, [dynamic_xy64, dynamic_adaptive64, vc64], labels, colors):
    x_values = np.arange(len(data['Total Delay']))
    y_values = np.array(data['Total Delay'])
    
    # Plot segments with np.nan as discontinuities
    nan_positions = np.where(np.isnan(y_values))[0]

    # Plot normal line
    ax.plot(x_values, y_values, linestyle='-', color=color, label=label, linewidth = 2.5)

    # Add discontinuity markers where np.nan values occur
    if nan_positions.size > 0:
        for nan_position in nan_positions:
            ax.scatter(x_values[nan_position], y_values[nan_position], color='red', linestyle='-', s=100, zorder=5, linewidth = 2.5)

    # Set x-axis ticks to 0, 1, 2, ..., 99
    ax.set_xticks(np.arange(0, 100, 5))
    ax.set_xticklabels(np.arange(0, 100, 5), rotation=0)  # Adjust rotation if needed

# fig1.legend(labels, loc='upper right')
fig4.legend()
fig4.text(0.04, 0.5, 'Latency (in Cycles)', va='center', rotation='vertical',fontsize =16)
fig4.suptitle('Latency vs Iteration (64 bits)', fontsize=16)
fig4.text(0.5, 0.04, 'Iteration', ha='center', fontsize=16)


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