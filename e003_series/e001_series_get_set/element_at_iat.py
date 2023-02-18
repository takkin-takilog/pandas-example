"""
要素の抽出・置換(at, iat)
"""

import pandas as pd

o_data = [
    108.432,
    109.252,
    108.799,
    108.854,
    108.545,
]

o_index = [
    "2020/4/6",
    "2020/4/7",
    "2020/4/8",
    "2020/4/9",
    "2020/4/10",
]

print("\n{:*<100}".format("***** Seriesの生成 "))
sr = pd.Series(data=o_data, index=o_index, name="open")
print(sr)
sr_mst = sr.copy()

print("\n{:*<100}".format("***** 要素の抽出(at) "))
elem = sr.at["2020/4/8"]
print(elem)

print("\n{:*<100}".format("***** 要素の置換(at) "))
sr = sr_mst.copy()
sr.at["2020/4/8"] = 0.0
print(sr)

print("\n{:*<100}".format("***** 要素の抽出(iat) "))
sr = sr_mst.copy()
elem = sr.iat[2]
print(elem)

print("\n{:*<100}".format("***** 要素の置換(iat) "))
sr = sr_mst.copy()
sr.iat[2] = 0.0
print(sr)
