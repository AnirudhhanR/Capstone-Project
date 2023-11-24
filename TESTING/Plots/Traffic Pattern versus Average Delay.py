import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Reading dataframes 
# Ani Path
butterfly5 = pd.read_csv('TESTING/testfiles/BUTTERFLY_TRAFFIC/0_to_15_bitsize_5.csv')
exp5 = pd.read_csv('TESTING/testfiles/EXPONENTIAL/0_to_15_bitsize_5.csv')
hotspotcentre5 = pd.read_csv('TESTING/testfiles/HOTSPOT_CENTER_TRAFFIC/0_to_15_bitsize_5.csv')
hotspotedge5 = pd.read_csv("TESTING/testfiles/HOTSPOT_EDGES_TRAFFIC/0_to_15_bitsize_5.csv")
normal5 = pd.read_csv("TESTING/testfiles/NORMAL_TRAFFIC/0_to_15_bitsize_5.csv")
poisson5 = pd.read_csv("TESTING/testfiles/POISSON_TRAFFIC_DISTRIBUTION/0_to_15_bitsize_5.csv")
random5 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_5.csv")
butterfly5.loc['Averages'] = butterfly5.mean(numeric_only=True)
exp5.loc['Averages'] = exp5.mean(numeric_only=True)
hotspotcentre5.loc['Averages'] = hotspotcentre5.mean(numeric_only=True)
hotspotedge5.loc['Averages'] = hotspotedge5.mean(numeric_only=True)
normal5.loc['Averages'] = normal5.mean(numeric_only=True)
poisson5.loc['Averages'] = poisson5.mean(numeric_only=True)
random5.loc['Averages'] = random5.mean(numeric_only=True)

butterfly20 = pd.read_csv('TESTING/testfiles/BUTTERFLY_TRAFFIC/0_to_15_bitsize_20.csv')
exp20 = pd.read_csv('TESTING/testfiles/EXPONENTIAL/0_to_15_bitsize_20.csv')
hotspotcentre20 = pd.read_csv('TESTING/testfiles/HOTSPOT_CENTER_TRAFFIC/0_to_15_bitsize_20.csv')
# hotspotedge20 = pd.read_csv("TESTING/testfiles/HOTSPOT_EDGES_TRAFFIC/0_to_15_bitsize_20.csv")
normal20 = pd.read_csv("TESTING/testfiles/NORMAL_TRAFFIC/0_to_15_bitsize_20.csv")
poisson20 = pd.read_csv("TESTING/testfiles/POISSON_TRAFFIC_DISTRIBUTION/0_to_15_bitsize_20.csv")
random20 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_20.csv")
butterfly20.loc['Averages'] = butterfly20.mean(numeric_only=True)
exp20.loc['Averages'] = exp20.mean(numeric_only=True)
hotspotcentre20.loc['Averages'] = hotspotcentre20.mean(numeric_only=True)
# hotspotedge20.loc['Averages'] = hotspotedge20.mean(numeric_only=True)
normal20.loc['Averages'] = normal20.mean(numeric_only=True)
poisson20.loc['Averages'] = poisson20.mean(numeric_only=True)
random20.loc['Averages'] = random20.mean(numeric_only=True)

butterfly40 = pd.read_csv('TESTING/testfiles/BUTTERFLY_TRAFFIC/0_to_15_bitsize_40.csv')
exp40 = pd.read_csv('TESTING/testfiles/EXPONENTIAL/0_to_15_bitsize_40.csv')
hotspotcentre40 = pd.read_csv('TESTING/testfiles/HOTSPOT_CENTER_TRAFFIC/0_to_15_bitsize_40.csv')
hotspotedge40 = pd.read_csv("TESTING/testfiles/HOTSPOT_EDGES_TRAFFIC/0_to_15_bitsize_40.csv")
normal40 = pd.read_csv("TESTING/testfiles/NORMAL_TRAFFIC/0_to_15_bitsize_40.csv")
poisson40 = pd.read_csv("TESTING/testfiles/POISSON_TRAFFIC_DISTRIBUTION/0_to_15_bitsize_40.csv")
random40 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_40.csv")
butterfly40.loc['Averages'] = butterfly40.mean(numeric_only=True)
exp40.loc['Averages'] = exp40.mean(numeric_only=True)
hotspotcentre40.loc['Averages'] = hotspotcentre40.mean(numeric_only=True)
hotspotedge40.loc['Averages'] = hotspotedge40.mean(numeric_only=True)
normal40.loc['Averages'] = normal40.mean(numeric_only=True)
poisson40.loc['Averages'] = poisson40.mean(numeric_only=True)
random40.loc['Averages'] = random40.mean(numeric_only=True)

butterfly64 = pd.read_csv('TESTING/testfiles/BUTTERFLY_TRAFFIC/0_to_15_bitsize_64.csv')
exp64 = pd.read_csv('TESTING/testfiles/EXPONENTIAL/0_to_15_bitsize_64.csv')
hotspotcentre64 = pd.read_csv('TESTING/testfiles/HOTSPOT_CENTER_TRAFFIC/0_to_15_bitsize_64.csv')
hotspotedge64 = pd.read_csv("TESTING/testfiles/HOTSPOT_EDGES_TRAFFIC/0_to_15_bitsize_64.csv")
normal64 = pd.read_csv("TESTING/testfiles/NORMAL_TRAFFIC/0_to_15_bitsize_64.csv")
poisson64 = pd.read_csv("TESTING/testfiles/POISSON_TRAFFIC_DISTRIBUTION/0_to_15_bitsize_64.csv")
random64 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_64.csv")
butterfly64.loc['Averages'] = butterfly64.mean(numeric_only=True)
exp64.loc['Averages'] = exp64.mean(numeric_only=True)
hotspotcentre64.loc['Averages'] = hotspotcentre64.mean(numeric_only=True)
hotspotedge64.loc['Averages'] = hotspotedge64.mean(numeric_only=True)
normal64.loc['Averages'] = normal64.mean(numeric_only=True)
poisson64.loc['Averages'] = poisson64.mean(numeric_only=True)
random64.loc['Averages'] = random64.mean(numeric_only=True)


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

average_list = [
    butterfly5.loc['Averages']['Total Delay'],
    exp5.loc['Averages']['Total Delay'],
    hotspotcentre5.loc['Averages']['Total Delay'],
    hotspotedge5.loc['Averages']['Total Delay'],
    normal5.loc['Averages']['Total Delay'],
    poisson5.loc['Averages']['Total Delay'],
    random5.loc['Averages']['Total Delay']
]

print(average_list)
x_pos = [1,3,5,7,9,11,13]
name = ('butterfly','exponential', 'hotspot: centre', 'hotspot: edge', 'normal', 'poisson', 'random')

plt.title("Traffic Pattern versus Average Delay")
plt.ylabel("Average Delay (In Cycles)")
plt.xlabel("Traffic Pattern")
plt.bar(x_pos, average_list, width = 1.25)
plt.xticks(x_pos,name)
plt.show()

# ax = average_list.plot(kind='bar', legend=False, width=3, color='blue')  # Set color to blue
# ax.set_xlabel('Dataframe')
# ax.set_ylabel('Average Total Delay')
# ax.set_title('Average Total Delay for Different Dataframes')
# plt.bar()
