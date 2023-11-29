import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.ticker import FormatStrFormatter

# Reading dataframes 
# Ani Path
butterfly5 = pd.read_csv('TESTING/testfiles/BUTTERFLY_TRAFFIC/0_to_15_bitsize_5.csv')
exp5 = pd.read_csv('TESTING/testfiles/EXPONENTIAL/0_to_15_bitsize_5.csv')
hotspotcentre5 = pd.read_csv('TESTING/testfiles/HOTSPOT_CENTER_TRAFFIC/0_to_15_bitsize_5.csv')
hotspotedge5 = pd.read_csv("TESTING/testfiles/HOTSPOT_EDGES_TRAFFIC/0_to_15_bitsize_5.csv")
normal5 = pd.read_csv("TESTING/testfiles/NORMAL_TRAFFIC/0_to_15_bitsize_5.csv")
poisson5 = pd.read_csv("TESTING/testfiles/POISSON_TRAFFIC_DISTRIBUTION/0_to_15_bitsize_5.csv")
random5 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_5.csv")
# butterfly5.loc['Averages'] = butterfly5.mean(numeric_only=True)
# exp5.loc['Averages'] = exp5.mean(numeric_only=True)
# hotspotcentre5.loc['Averages'] = hotspotcentre5.mean(numeric_only=True)
# hotspotedge5.loc['Averages'] = hotspotedge5.mean(numeric_only=True)
# normal5.loc['Averages'] = normal5.mean(numeric_only=True)
# poisson5.loc['Averages'] = poisson5.mean(numeric_only=True)
# random5.loc['Averages'] = random5.mean(numeric_only=True)

butterfly20 = pd.read_csv('TESTING/testfiles/BUTTERFLY_TRAFFIC/0_to_15_bitsize_20.csv')
exp20 = pd.read_csv('TESTING/testfiles/EXPONENTIAL/0_to_15_bitsize_20.csv')
hotspotcentre20 = pd.read_csv('TESTING/testfiles/HOTSPOT_CENTER_TRAFFIC/0_to_15_bitsize_20.csv')
hotspotedge20 = pd.read_csv("TESTING/testfiles/HOTSPOT_EDGES_TRAFFIC/0_to_15_bitsize_20.csv")
normal20 = pd.read_csv("TESTING/testfiles/NORMAL_TRAFFIC/0_to_15_bitsize_20.csv")
poisson20 = pd.read_csv("TESTING/testfiles/POISSON_TRAFFIC_DISTRIBUTION/0_to_15_bitsize_20.csv")
random20 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_20.csv")
# butterfly20.loc['Averages'] = butterfly20.mean(numeric_only=True)
# exp20.loc['Averages'] = exp20.mean(numeric_only=True)
# hotspotcentre20.loc['Averages'] = hotspotcentre20.mean(numeric_only=True)
# hotspotedge20.loc['Averages'] = hotspotedge20.mean(numeric_only=True)
# normal20.loc['Averages'] = normal20.mean(numeric_only=True)
# poisson20.loc['Averages'] = poisson20.mean(numeric_only=True)
# random20.loc['Averages'] = random20.mean(numeric_only=True)

butterfly40 = pd.read_csv('TESTING/testfiles/BUTTERFLY_TRAFFIC/0_to_15_bitsize_40.csv')
exp40 = pd.read_csv('TESTING/testfiles/EXPONENTIAL/0_to_15_bitsize_40.csv')
hotspotcentre40 = pd.read_csv('TESTING/testfiles/HOTSPOT_CENTER_TRAFFIC/0_to_15_bitsize_40.csv')
hotspotedge40 = pd.read_csv("TESTING/testfiles/HOTSPOT_EDGES_TRAFFIC/0_to_15_bitsize_40.csv")
normal40 = pd.read_csv("TESTING/testfiles/NORMAL_TRAFFIC/0_to_15_bitsize_40.csv")
poisson40 = pd.read_csv("TESTING/testfiles/POISSON_TRAFFIC_DISTRIBUTION/0_to_15_bitsize_40.csv")
random40 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_40.csv")
# butterfly40.loc['Averages'] = butterfly40.mean(numeric_only=True)
# exp40.loc['Averages'] = exp40.mean(numeric_only=True)
# hotspotcentre40.loc['Averages'] = hotspotcentre40.mean(numeric_only=True)
# hotspotedge40.loc['Averages'] = hotspotedge40.mean(numeric_only=True)
# normal40.loc['Averages'] = normal40.mean(numeric_only=True)
# poisson40.loc['Averages'] = poisson40.mean(numeric_only=True)
# random40.loc['Averages'] = random40.mean(numeric_only=True)

butterfly64 = pd.read_csv('TESTING/testfiles/BUTTERFLY_TRAFFIC/0_to_15_bitsize_64.csv')
exp64 = pd.read_csv('TESTING/testfiles/EXPONENTIAL/0_to_15_bitsize_64.csv')
hotspotcentre64 = pd.read_csv('TESTING/testfiles/HOTSPOT_CENTER_TRAFFIC/0_to_15_bitsize_64.csv')
hotspotedge64 = pd.read_csv("TESTING/testfiles/HOTSPOT_EDGES_TRAFFIC/0_to_15_bitsize_64.csv")
normal64 = pd.read_csv("TESTING/testfiles/NORMAL_TRAFFIC/0_to_15_bitsize_64.csv")
poisson64 = pd.read_csv("TESTING/testfiles/POISSON_TRAFFIC_DISTRIBUTION/0_to_15_bitsize_64.csv")
random64 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_64.csv")
# butterfly64.loc['Averages'] = butterfly64.mean(numeric_only=True)
# exp64.loc['Averages'] = exp64.mean(numeric_only=True)
# hotspotcentre64.loc['Averages'] = hotspotcentre64.mean(numeric_only=True)
# hotspotedge64.loc['Averages'] = hotspotedge64.mean(numeric_only=True)
# normal64.loc['Averages'] = normal64.mean(numeric_only=True)
# poisson64.loc['Averages'] = poisson64.mean(numeric_only=True)
# random64.loc['Averages'] = random64.mean(numeric_only=True)


# average5 = [butterfly5.loc['Averages'], exp5.loc['Averages'], hotspotcentre5.loc['Averages'],
#             hotspotedge5.loc['Averages'], normal5.loc['Averages'], poisson5.loc['Averages'],
#             random5.loc['Averages']]
# average20 = [butterfly20.loc['Averages'], exp20.loc['Averages'], hotspotcentre20.loc['Averages'],
#             normal20.loc['Averages'], poisson20.loc['Averages'],
#             random20.loc['Averages']]
# average40 = [butterfly40.loc['Averages'], exp40.loc['Averages'], hotspotcentre40.loc['Averages'],
#             hotspotedge40.loc['Averages'], normal40.loc['Averages'], poisson40.loc['Averages'],
#             random40.loc['Averages']]
# average64 = [butterfly64.loc['Averages'], exp64.loc['Averages'], hotspotcentre64.loc['Averages'],
#             hotspotedge64.loc['Averages'], normal64.loc['Averages'], poisson64.loc['Averages'],
#             random64.loc['Averages']]

# plt.plot(butterfly5["Averages"],index)

delaylist5 = [
    butterfly5.loc[100]['Total Delay'],
    exp5.loc[100]['Total Delay'],
    hotspotcentre5.loc[100]['Total Delay'],
    hotspotedge5.loc[100]['Total Delay'],
    normal5.loc[100]['Total Delay'],
    poisson5.loc[100]['Total Delay'],
    random5.loc[100]['Total Delay']
]

delaylist20 = [
    butterfly20.loc[100]['Total Delay'],
    exp20.loc[100]['Total Delay'],
    hotspotcentre20.loc[100]['Total Delay'],
    hotspotedge20.loc[100]['Total Delay'],
    normal20.loc[100]['Total Delay'],
    poisson20.loc[100]['Total Delay'],
    random20.loc[100]['Total Delay']
]

delaylist40 = [
    butterfly40.loc[100]['Total Delay'],
    exp40.loc[100]['Total Delay'],
    hotspotcentre40.loc[100]['Total Delay'],
    hotspotedge40.loc[100]['Total Delay'],
    normal40.loc[100]['Total Delay'],
    poisson40.loc[100]['Total Delay'],
    random40.loc[100]['Total Delay']
]

delaylist64 = [
    butterfly64.loc[100]['Total Delay'],
    exp64.loc[100]['Total Delay'],
    hotspotcentre64.loc[100]['Total Delay'],
    hotspotedge64.loc[100]['Total Delay'],
    normal64.loc[100]['Total Delay'],
    poisson64.loc[100]['Total Delay'],
    random64.loc[100]['Total Delay']
]

hoplist5 = [
    butterfly5.loc[100]['Total Hopcount'],
    exp5.loc[100]['Total Hopcount'],
    hotspotcentre5.loc[100]['Total Hopcount'],
    hotspotedge5.loc[100]['Total Hopcount'],
    normal5.loc[100]['Total Hopcount'],
    poisson5.loc[100]['Total Hopcount'],
    random5.loc[100]['Total Hopcount']
]

hoplist20 = [
    butterfly20.loc[100]['Total Hopcount'],
    exp20.loc[100]['Total Hopcount'],
    hotspotcentre20.loc[100]['Total Hopcount'],
    hotspotedge20.loc[100]['Total Hopcount'],
    normal20.loc[100]['Total Hopcount'],
    poisson20.loc[100]['Total Hopcount'],
    random20.loc[100]['Total Hopcount']
]

hoplist40 = [
    butterfly40.loc[100]['Total Hopcount'],
    exp40.loc[100]['Total Hopcount'],
    hotspotcentre40.loc[100]['Total Hopcount'],
    hotspotedge40.loc[100]['Total Hopcount'],
    normal40.loc[100]['Total Hopcount'],
    poisson40.loc[100]['Total Hopcount'],
    random40.loc[100]['Total Hopcount']
]

hoplist64 = [
    butterfly64.loc[100]['Total Hopcount'],
    exp64.loc[100]['Total Hopcount'],
    hotspotcentre64.loc[100]['Total Hopcount'],
    hotspotedge64.loc[100]['Total Hopcount'],
    normal64.loc[100]['Total Hopcount'],
    poisson64.loc[100]['Total Hopcount'],
    random64.loc[100]['Total Hopcount']
]
i = 0.0
# print(average_list20)
x_pos = [1,3,5,7,9,11,13]
y_pos = []
for i in range(0,21):
    y_pos.append(i)
    i = i + 1
name = ('butterfly','exponential', 'hotspot\ncentre', 'hotspot\nedge', 'normal', 'poisson', 'random')
print(hoplist64)
print(random64)
plt.subplot(2,2,1)
plt.title("Traffic Pattern versus Average Delay : 5 Bits")
plt.ylabel("Average Delay (In Cycles)")
plt.xlabel("Traffic Pattern")
plt.bar(x_pos, delaylist5, width = 1.25)
plt.xticks(x_pos,name)
plt.yticks(y_pos)

plt.subplot(2,2,2)
plt.title("Traffic Pattern versus Average Delay : 20 Bits")
plt.ylabel("Average Delay (In Cycles)")
plt.xlabel("Traffic Pattern")
plt.bar(x_pos, delaylist20, width = 1.25)
plt.xticks(x_pos,name)
plt.yticks(y_pos)

plt.subplot(2,2,3)
plt.title("Traffic Pattern versus Average Delay : 40 Bits")
plt.ylabel("Average Delay (In Cycles)")
plt.xlabel("Traffic Pattern")
plt.bar(x_pos, delaylist40, width = 1.25)
plt.xticks(x_pos,name)
plt.yticks(y_pos)

plt.subplot(2,2,4)
plt.title("Traffic Pattern versus Average Delay : 64 Bits")
plt.ylabel("Average Delay (In Cycles)")
plt.xlabel("Traffic Pattern")
plt.bar(x_pos, delaylist64, width = 1.25)
plt.xticks(x_pos,name)
plt.yticks(y_pos)

# ax = average_list.plot(kind='bar', legend=False, width=3, color='blue')  # Set color to blue
# ax.set_xlabel('Dataframe')
# ax.set_ylabel('Average Total Delay')
# ax.set_title('Average Total Delay for Different Dataframes')
# plt.bar()

plt.tight_layout(pad = 0.1)
plt.show()

plt.subplot(2,2,1)
plt.title("Traffic Pattern versus Average hop count : 5 Bits")
plt.ylabel("Average hop count")
plt.xlabel("Traffic Pattern")
plt.bar(x_pos, hoplist5, width = 1.25)
plt.xticks(x_pos,name)
plt.yticks(y_pos)

plt.subplot(2,2,2)
plt.title("Traffic Pattern versus Average hop count : 20 Bits")
plt.ylabel("Average hop count")
plt.xlabel("Traffic Pattern")
plt.bar(x_pos, hoplist20, width = 1.25)
plt.xticks(x_pos,name)
plt.yticks(y_pos)

plt.subplot(2,2,3)
plt.title("Traffic Pattern versus Average hop count : 40 Bits")
plt.ylabel("Average hop count")
plt.xlabel("Traffic Pattern")
plt.bar(x_pos, hoplist40, width = 1.25)
plt.xticks(x_pos,name)
plt.yticks(y_pos)

plt.subplot(2,2,4)
plt.title("Traffic Pattern versus Average hop count : 64 Bits")
plt.ylabel("Average hop count")
plt.xlabel("Traffic Pattern")
plt.bar(x_pos, hoplist64, width = 1.25)
plt.xticks(x_pos,name)
plt.yticks(y_pos)

plt.tight_layout(pad = 0.1)
plt.show()
