"""
行の追加・結合
"""

import pandas as pd

ohlc_data = [
    ["2020/4/6", 108.432, 119.393, 98.403, 109.252],
    ["2020/4/7", 109.252, 119.294, 98.680, 108.799],
]

print("\n{:*<100}".format("***** DataFrameの生成 "))
df = pd.DataFrame(ohlc_data, columns=["datetime", "open", "high", "low", "close"])
df.set_index("datetime", inplace=True)
print(df)
df_mst = df.copy()

df = df_mst.copy()
print("\n{:*<100}".format("***** 行の追加（シンプル：スカラ） "))
df.loc["2020/4/8"] = 0.0
# df.loc["2020/4/8", :] = 0.0
print(df)

print("\n{:*<100}".format("***** 行の追加（シンプル：リスト） "))
df.loc["2020/4/9"] = [108.854, 119.071, 98.218, 108.545]
# df.loc["2020/4/9", :] = [108.854, 119.071, 98.218, 108.545]
print(df)

# df.loc["2020/4/9_2", :] = [108.854, 119.071]  # ValueError

print("\n{:*<100}".format("***** 行の追加（シンプル：Series） "))
data = [108.545, 118.615, 98.341, 108.515]
index = df.columns
sr_new = pd.Series(data, index, name="new_row")
print(sr_new)
df.loc["2020/4/10"] = sr_new
# df.loc["2020/4/10", :] = sr_new
print(df)

print("{:-<50}".format("----- Series2 "))
data = [108.545, 118.615]
index = ["open", "high"]
sr_new2 = pd.Series(data, index, name="new_col")
print(sr_new2)
df.loc["2020/4/10-2"] = sr_new2
print(df)

df = df_mst.copy()
print("\n{:*<100}".format("***** 行の追加（append） "))
data = [108.799, 119.109, 98.514, 108.854]
index = ["open", "high", "low", "close"]
sr = pd.Series(data, index, name="2020/4/8")
print(sr)
df_a = df.append(sr)
print(df_a)

print("\n{:*<100}".format("***** 行の追加（concat） "))

ohlc_data = [
    ["2020/4/6", 108.432, 119.393, 98.403, 109.252],
    ["2020/4/7", 109.252, 119.294, 98.680, 108.799],
]

df = pd.DataFrame(ohlc_data, columns=["datetime", "open", "high", "low", "close"])
df.set_index("datetime", inplace=True)
print(df)
df_mst = df.copy()

print("{:-<50}".format("----- Series "))
df1 = df_mst.copy()

data = [108.799, 119.109, 98.514, 108.854]
index = ["open", "high", "low", "close"]
sr1 = pd.Series(data, index, name="2020/4/8")
print(sr1)

print("{:-<50}".format("----- NGケース "))
df_c = pd.concat([df1, sr1], axis=0)
print(df_c)

print("{:-<50}".format("----- OKケース "))
df2 = pd.DataFrame(sr1)
df_c = pd.concat([df1, df2.T], axis=0)
print(df_c)

print("{:-<50}".format("----- DataFrame "))
df1 = df_mst.copy()

ohlc_data = [
    ["2020/4/8", 108.799, 119.109, 98.514, 108.854],
    ["2020/4/9", 108.854, 119.071, 98.218, 108.545],
]
df2 = pd.DataFrame(ohlc_data, columns=["datetime", "open", "high", "low", "close"])
df2.set_index("datetime", inplace=True)
print(df2)
df_c = pd.concat([df1, df2], axis=0)
print(df_c)
