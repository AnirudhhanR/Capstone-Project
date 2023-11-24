import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Reading dataframes Ani Path
# butterfly5 = pd.read_csv('TESTING/testfiles\BUTTERFLY_TRAFFIC\0_to_15_bitsize_5.csv')
# exp5 = pd.read_csv('TESTING/testfiles/EXPONENTIAL/0_to_15_bitsize_5.csv')
# hotspotcentre5 = pd.read_csv('TESTING/testfiles/HOTSPOT_CENTER_TRAFFIC/0_to_15_bitsize_5.csv')
# hotspotedge5 = pd.read_csv("TESTING/testfiles/HOTSPOT_EDGES_TRAFFIC/0_to_15_bitsize_5.csv")
# normal5 = pd.read_csv("TESTING/testfiles/NORMAL_TRAFFIC/0_to_15_bitsize_5.csv")
# poisson5 = pd.read_csv("TESTING/testfiles/POISSON_TRAFFIC_DISTRIBUTION/0_to_15_bitsize_5.csv")
# random5 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_5.csv")


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
# hotspotedge20 = pd.read_csv("C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/HOTSPOT_EDGES_TRAFFIC/0_to_15_bitsize_20.csv")
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
butterfly5.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
exp5.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
hotspotcentre5.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
hotspotedge5.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
normal5.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
poisson5.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
random5.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)

butterfly20.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
exp20.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
hotspotcentre20.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
# hotspotedge20.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
normal20.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
poisson20.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
random20.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)

butterfly40.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
exp40.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
hotspotcentre40.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
hotspotedge40.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
normal40.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
poisson40.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
random40.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)

butterfly64.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
exp64.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
hotspotcentre64.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
hotspotedge64.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
normal64.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
poisson64.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
random64.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)

# Combine dataframes
# combined_df = pd.concat([butterfly5, exp5, hotspotcentre5, hotspotedge5, normal5, poisson5, random5])
# print(combined_df.shape)

index1 = list(range(1,102,1))
index = list(range(1,101,1))
# butterfly5['iteration'] = np.array(index)

# print(type(butterfly5['Total Delay']))
plt.subplot(2,2,1)
plt.plot(index1, np.array(butterfly5['Total Delay']), label='Butterfly', linestyle='-', color='blue')
plt.plot(index1, np.array(exp5['Total Delay']), label='Exponential', linestyle='-', color='orange')
plt.plot(index1, np.array(hotspotcentre5['Total Delay']), label='Hotspot Center', linestyle='-', color='green')
plt.plot(index1, np.array(hotspotedge5['Total Delay']), label='Hotspot Edge', linestyle='-', color='red')
plt.plot(index1, np.array(normal5['Total Delay']), label='Normal', linestyle='-', color='purple')
plt.plot(index1, np.array(poisson5['Total Delay']), label='Poisson', linestyle='-', color='brown')
plt.plot(index1, np.array(random5['Total Delay']), label='Random', linestyle='-', color='pink')
plt.legend()

plt.subplot(2,2,2)
plt.plot(index1, np.array(butterfly20['Total Delay']), label='Butterfly', linestyle='-', color='blue')
plt.plot(index1, np.array(exp20['Total Delay']), label='Exponential', linestyle='-', color='orange')
plt.plot(index1, np.array(hotspotcentre20['Total Delay']), label='Hotspot Center', linestyle='-', color='green')
# plt.plot(index, np.array(hotspotedge20['Total Delay']), label='Hotspot Edge', linestyle='-', color='red')
plt.plot(index1, np.array(normal20['Total Delay']), label='Normal', linestyle='-', color='purple')
plt.plot(index1, np.array(poisson20['Total Delay']), label='Poisson', linestyle='-', color='brown')
plt.plot(index1, np.array(random20['Total Delay']), label='Random', linestyle='-', color='pink')
plt.legend()

plt.subplot(2,2,3)
plt.plot(index1, np.array(butterfly40['Total Delay']), label='Butterfly', linestyle='-', color='blue')
plt.plot(index1, np.array(exp40['Total Delay']), label='Exponential', linestyle='-', color='orange')
plt.plot(index1, np.array(hotspotcentre40['Total Delay']), label='Hotspot Center', linestyle='-', color='green')
plt.plot(index1, np.array(hotspotedge40['Total Delay']), label='Hotspot Edge', linestyle='-', color='red')
plt.plot(index1, np.array(normal40['Total Delay']), label='Normal', linestyle='-', color='purple')
plt.plot(index1, np.array(poisson40['Total Delay']), label='Poisson', linestyle='-', color='brown')
plt.plot(index1, np.array(random40['Total Delay']), label='Random', linestyle='-', color='pink')
plt.legend()

plt.subplot(2,2,4)
plt.plot(index1, np.array(butterfly64['Total Delay']), label='Butterfly', linestyle='-', color='blue')
plt.plot(index, np.array(exp64['Total Delay']), label='Exponential', linestyle='-', color='orange')
plt.plot(index1, np.array(hotspotcentre64['Total Delay']), label='Hotspot Center', linestyle='-', color='green')
plt.plot(index1, np.array(hotspotedge64['Total Delay']), label='Hotspot Edge', linestyle='-', color='red')
plt.plot(index1, np.array(normal64['Total Delay']), label='Normal', linestyle='-', color='purple')
plt.plot(index1, np.array(poisson64['Total Delay']), label='Poisson', linestyle='-', color='brown')
plt.plot(index1, np.array(random64['Total Delay']), label='Random', linestyle='-', color='pink')
plt.legend()



# print(combined_df.head)


plt.xlabel('Index')
plt.ylabel('Total Delays')
plt.title('Total Delays')
plt.legend()
plt.yticks(range(0, 21))
plt.ylim(bottom = 5)
plt.show()

# exp5['Total Delay'],hotspotcentre5['Total Delay'],hotspotedge5['Total Delay'],normal5['Total Delay'],poisson5['Total Delay'],random5['Total Delay']],
