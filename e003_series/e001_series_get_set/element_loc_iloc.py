"""
要素の抽出・置換(loc, iloc)
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

print("\n{:*<100}".format("***** 要素の抽出(loc) "))
print("{:-<50}".format("----- 単一要素の抽出 "))
elem = sr.loc["2020/4/8"]
print(elem)
print("{:-<50}".format("----- 型の確認 "))
print(type(elem))
print("{:-<50}".format("----- 複数要素の抽出（リスト） "))
sr_elems = sr.loc[["2020/4/6", "2020/4/8", "2020/4/10"]]
print(sr_elems)
print("{:-<50}".format("----- 型の確認 "))
print(type(sr_elems))
print("{:-<50}".format("----- 複数要素の抽出（スライス） "))
sr_elems = sr.loc["2020/4/7":"2020/4/9"]
print(sr_elems)
print("{:-<50}".format("----- 型の確認 "))
print(type(sr_elems))

print("\n{:*<100}".format("***** 要素の置換(loc) "))
print("{:-<50}".format("----- 単一要素の置換 "))
sr = sr_mst.copy()
sr.loc["2020/4/8"] = 0.0
print(sr)
print("{:-<50}".format("----- 要素の置換（リスト）1 "))
sr = sr_mst.copy()
sr.loc[["2020/4/6", "2020/4/8", "2020/4/10"]] = -1.0
print(sr)
print("{:-<50}".format("----- 要素の置換（リスト）2 "))
sr.loc[["2020/4/6", "2020/4/8", "2020/4/10"]] = [1.0, 2.0, 3.0]
print(sr)
# sr.loc[["2020/4/6", "2020/4/8", "2020/4/10"]] = [4.0, 5.0]
print(sr)

print("{:-<50}".format("----- 複数列の抽出(スライス) "))
sr = sr_mst.copy()
sr.loc["2020/4/7":"2020/4/9"] = -2.0
print(sr)

print("\n{:*<100}".format("***** 要素の抽出(iloc) "))
sr = sr_mst.copy()
print("{:-<50}".format("----- 単一要素の抽出 "))
elem = sr.iloc[2]
print(elem)
print("{:-<50}".format("----- 型の確認 "))
print(type(elem))

print("{:-<50}".format("----- 複数要素の抽出（リスト） "))
sr_elems = sr.iloc[[0, 2, 4]]
print(sr_elems)
print("{:-<50}".format("----- 型の確認 "))
print(type(sr_elems))

print("{:-<50}".format("----- 複数要素の抽出（スライス） "))
sr_elems = sr.iloc[1:3]
print(sr_elems)
print("{:-<50}".format("----- 型の確認 "))
print(type(sr_elems))

print("\n{:*<100}".format("***** 要素の置換(iloc) "))
print("{:-<50}".format("----- 単一要素の置換 "))
sr = sr_mst.copy()
sr.iloc[2] = 0.0
print(sr)
print("{:-<50}".format("----- 要素の置換（リスト）1 "))
sr = sr_mst.copy()
sr.iloc[[0, 2, 4]] = -1.0
print(sr)
print("{:-<50}".format("----- 要素の置換（リスト）2 "))
sr.iloc[[0, 2, 4]] = [1.0, 2.0, 3.0]
print(sr)

print("{:-<50}".format("----- 要素の置換(スライス) "))
sr = sr_mst.copy()
sr.iloc[1:3] = -2.0
print(sr)
