import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Reading dataframes
butterfly5 = pd.read_csv('TESTING/testfiles/BUTTERFLY_TRAFFIC/0_to_15_bitsize_5.csv')
exp5 = pd.read_csv('F:/COllege/Capstone/Capstone -Master/Capstone-Project/TESTING/testfiles/EXPONENTIAL/0_to_15_bitsize_5.csv')
hotspotcentre5 = pd.read_csv('TESTING/testfiles/HOTSPOT_CENTER_TRAFFIC/0_to_15_bitsize_5.csv')
hotspotedge5 = pd.read_csv("TESTING/testfiles/HOTSPOT_EDGES_TRAFFIC/0_to_15_bitsize_5.csv")
normal5 = pd.read_csv("TESTING/testfiles/NORMAL_TRAFFIC/0_to_15_bitsize_5.csv")
poisson5 = pd.read_csv("TESTING/testfiles/POISSON_TRAFFIC_DISTRIBUTION/0_to_15_bitsize_5.csv")
random5 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_5.csv")

# Drop columns from DataFrames
butterfly5.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
exp5.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
hotspotcentre5.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
hotspotedge5.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
normal5.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
poisson5.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)
random5.drop(['Hop Count', 'link Delay', 'Virtual Hop Count', 'VC Delay', 'Wait Delay'], axis=1, inplace=True)

# Combine dataframes
# combined_df = pd.concat([butterfly5, exp5, hotspotcentre5, hotspotedge5, normal5, poisson5, random5])
# print(combined_df.shape)

index = list(range(1,102,1))
butterfly5['iteration'] = index
plt.plot(butterfly5["iteration"], butterfly5['Total Delay'], label='Butterfly', linestyle='-', color='blue')
plt.plot(butterfly5["iteration"], exp5['Total Delay'], label='Exponential', linestyle='-', color='orange')
plt.plot(butterfly5["iteration"], hotspotcentre5['Total Delay'], label='Hotspot Center', linestyle='-', color='green')
plt.plot(butterfly5["iteration"], hotspotedge5['Total Delay'], label='Hotspot Edge', linestyle='-', color='red')
plt.plot(butterfly5["iteration"], normal5['Total Delay'], label='Normal', linestyle='-', color='purple')
plt.plot(butterfly5["iteration"], poisson5['Total Delay'], label='Poisson', linestyle='-', color='brown')
plt.plot(butterfly5["iteration"], random5['Total Delay'], label='Random', linestyle='-', color='pink')

# print(combined_df.head)


plt.xlabel('Index')
plt.ylabel('Total Delays')
plt.title('Total Delays')
plt.legend()
plt.show()

# exp5['Total Delay'],hotspotcentre5['Total Delay'],hotspotedge5['Total Delay'],normal5['Total Delay'],poisson5['Total Delay'],random5['Total Delay']],
