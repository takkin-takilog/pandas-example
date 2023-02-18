"""
列の追加・結合
"""

import pandas as pd

ohlc_data = [
    ["2020/4/6", 108.432],
    ["2020/4/7", 109.252],
    ["2020/4/8", 108.799],
    ["2020/4/9", 108.854],
    ["2020/4/10", 108.545],
]

print("\n{:*<100}".format("***** DataFrameの生成 "))
df = pd.DataFrame(ohlc_data, columns=["datetime", "open"])
df.set_index("datetime", inplace=True)
print(df)
df_mst = df.copy()

df = df_mst.copy()
print("\n{:*<100}".format("***** 列の追加（シンプル：スカラ） "))
df.loc[:, "high"] = 0.0
# df["high"] = 0.0
print(df)

print("\n{:*<100}".format("***** 列の追加（シンプル：リスト） "))
df.loc[:, "low"] = [98.403, 98.680, 98.514, 98.218, 98.341]
# df["low"] = [98.403, 98.680, 98.514, 98.218, 98.341]
print(df)

# df.loc[:, "low2"] = [98.403, 98.680]  # ValueError

print("\n{:*<100}".format("***** 列の追加（シンプル：Series） "))
data = [109.252, 108.799, 108.854, 108.545, 108.515]
index = df.index
sr_new = pd.Series(data, index, name="new_col")
print(sr_new)
df.loc[:, "close"] = sr_new
# df["close"] = sr_new
print(df)


print("{:-<50}".format("----- Series2 "))
data = [109.252, 108.799]
index = ["2020/4/6", "2020/4/7"]
sr_new2 = pd.Series(data, index, name="new_col")
print(sr_new2)
df["close2"] = sr_new2
print(df)


print("\n{:*<100}".format("***** 列の連結（concat） "))


ohlc_data = [
    ["2020/4/6", 108.432, 119.393],
    ["2020/4/7", 109.252, 119.294],
    ["2020/4/8", 108.799, 119.109],
    ["2020/4/9", 108.854, 119.071],
    ["2020/4/10", 108.545, 118.615],
]
df = pd.DataFrame(ohlc_data, columns=["datetime", "open", "high"])
df.set_index("datetime", inplace=True)
print(df)
df_mst = df.copy()

print("{:-<50}".format("----- Series "))
df1 = df_mst.copy()
data = [98.403, 98.680, 98.514, 98.218, 98.341]
index = df1.index
sr2 = pd.Series(data, index, name="low")
print(sr2)
df_c = pd.concat([df1, sr2], axis=1)
print(df_c)

print("{:-<50}".format("----- DataFrame "))
df1 = df_mst.copy()
ohlc_data = [
    ["2020/4/6", 98.403, 109.252],
    ["2020/4/7", 98.680, 108.799],
    ["2020/4/8", 98.514, 108.854],
    ["2020/4/9", 98.218, 108.545],
    ["2020/4/10", 98.341, 108.515],
]
df2 = pd.DataFrame(ohlc_data, columns=["datetime", "low", "close"])
df2.set_index("datetime", inplace=True)
print(df2)
df_c = pd.concat([df1, df2], axis=1)
print(df_c)
