import matplotlib.pyplot as plt
import pandas as pd
import math

dynamicVC5 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_5.csv")
dynamicVC20 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_20.csv")
dynamicVC40 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_40.csv")
dynamicVC64 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/0_to_15_bitsize_64.csv")
dynamicVC5.loc['Averages'] = dynamicVC5.mean(numeric_only=True)
dynamicVC20.loc['Averages'] = dynamicVC20.mean(numeric_only=True)
dynamicVC40.loc['Averages'] = dynamicVC40.mean(numeric_only=True)
dynamicVC64.loc['Averages'] = dynamicVC64.mean(numeric_only=True)

dynamic5 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/DYNAMIC_ADAPTIVE/0_to_15_bitsize_5.csv").fillna(0)
dynamic20 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/DYNAMIC_ADAPTIVE/0_to_15_bitsize_20.csv").fillna(0)
dynamic40 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/DYNAMIC_ADAPTIVE/0_to_15_bitsize_40.csv").fillna(0)
dynamic64 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/DYNAMIC_ADAPTIVE/0_to_15_bitsize_64.csv").fillna(0)
dynamic5.loc['Averages'] = dynamic5.mean(numeric_only=True)
dynamic20.loc['Averages'] = dynamic20.mean(numeric_only=True)
dynamic40.loc['Averages'] = dynamic40.mean(numeric_only=True)
dynamic64.loc['Averages'] = dynamic64.mean(numeric_only=True)

xy5 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/DYNAMIC_XY/0_to_15_bitsize_5.csv").fillna(0)
xy20 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/DYNAMIC_XY/0_to_15_bitsize_20.csv").fillna(0)
xy40 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/DYNAMIC_XY/0_to_15_bitsize_40.csv").fillna(0)
xy64 = pd.read_csv("TESTING/testfiles/RANDOM_TRAFFIC/DYNAMIC_XY/0_to_15_bitsize_64.csv").fillna(0)
xy5.loc['Averages'] = xy5.mean(numeric_only=True)
xy20.loc['Averages'] = xy20.mean(numeric_only=True)
xy40.loc['Averages'] = xy40.mean(numeric_only=True)
xy64.loc['Averages'] = xy64.mean(numeric_only=True)

dynamicVClist = [
    dynamicVC5.loc["Averages"]['Total Delay'],
    dynamicVC20.loc["Averages"]['Total Delay'],
    dynamicVC40.loc["Averages"]['Total Delay'],
    dynamicVC64.loc["Averages"]['Total Delay'],
]
dynamiclist = [
    dynamic5.loc["Averages"]['Total Delay'],
    dynamic20.loc["Averages"]['Total Delay'],
    dynamic40.loc["Averages"]['Total Delay'],
    dynamic64.loc["Averages"]['Total Delay'],
]

dynamicXYlist = [
    xy5.loc["Averages"]['Total Delay'],
    xy20.loc["Averages"]['Total Delay'],
    xy40.loc["Averages"]['Total Delay'],
    xy64.loc["Averages"]['Total Delay'],
]

list5 = [
    dynamicVC5.loc["Averages"]['Total Delay'],
    dynamic5.loc["Averages"]['Total Delay'],
    xy5.loc["Averages"]['Total Delay'],
]

list20 = [
    dynamicVC20.loc["Averages"]['Total Delay'],
    dynamic20.loc["Averages"]['Total Delay'],
    xy20.loc["Averages"]['Total Delay'],
]

list40 = [
    dynamicVC40.loc["Averages"]['Total Delay'],
    dynamic40.loc["Averages"]['Total Delay'],
    xy40.loc["Averages"]['Total Delay'],
]

list64 = [
    dynamicVC64.loc["Averages"]['Total Delay'],
    dynamic64.loc["Averages"]['Total Delay'],
    xy64.loc["Averages"]['Total Delay'],
]

list5 = [1e10 if math.isnan(x) else x for x in list5]
list20 = [1e10 if math.isnan(x) else x for x in list20]
list40 = [1e10 if math.isnan(x) else x for x in list40]
list64 = [1e10 if math.isnan(x) else x for x in list64]

print(list5)
print(list20)
print(list40)
print(list64)
i = 0.0
x_pos = [1,3,5]
y_pos = []
for i in range(0,21):
    y_pos.append(i)
    i = i + 1
name = ('VC',"XY Adaptive", "XY")

plt.subplot(2,2,1)
plt.bar(x_pos, list5, width = 1.25)
plt.xticks(x_pos,name)
plt.title("Average Delay Versus Algorithm: 5 Bits")
plt.xlabel("Algorithm")
plt.ylabel("Average Delay (in cycles)")
# plt.yticks(y_pos)
plt.ylim((0,30))

plt.subplot(2,2,2)
plt.bar(x_pos, list20, width = 1.25)
plt.xticks(x_pos,name)
# plt.yticks(y_pos)
plt.title("Average Delay Versus Algorithm: 20 Bits")
plt.xlabel("Algorithm")
plt.ylabel("Average Delay (in cycles)")
plt.ylim((0,30))

plt.subplot(2,2,3)
plt.bar(x_pos, list40, width = 1.25)
plt.xticks(x_pos,name)
plt.title("Average Delay Versus Algorithm: 40 Bits")
plt.xlabel("Algorithm")
plt.ylabel("Average Delay (in cycles)")
# plt.yticks(y_pos)
plt.ylim((0,30))

plt.subplot(2,2,4)
plt.bar(x_pos, list64, width = 1.25)
plt.xticks(x_pos,name)
# plt.yticks(y_pos)
plt.title("Average Delay Versus Algorithm: 64 Bits")
plt.xlabel("Algorithm")
plt.ylabel("Average Delay (in cycles)")
plt.ylim((0,30))
plt.show()

