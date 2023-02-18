"""
列の抽出・置換(loc, iloc)
"""

import pandas as pd

ohlc_data = [
    ["2020/4/6", 108.432, 119.393, 98.403, 109.252],
    ["2020/4/7", 109.252, 119.294, 98.680, 108.799],
    ["2020/4/8", 108.799, 119.109, 98.514, 108.854],
    ["2020/4/9", 108.854, 119.071, 98.218, 108.545],
    ["2020/4/10", 108.545, 118.615, 98.341, 108.515],
]

print("\n{:*<100}".format("***** DataFrameの生成 "))
df = pd.DataFrame(ohlc_data, columns=["datetime", "open", "high", "low", "close"])
print(df)
print("{:-<50}".format("----- インデックス（行ラベル）の設定 "))
df.set_index("datetime", inplace=True)
print(df)
df_mst = df.copy()


print("\n{:*<100}".format("***** 列の抽出(loc) "))
print("{:-<50}".format("----- 1列の抽出 "))
sr_col = df.loc[:, "open"]
print(sr_col)
print("{:-<50}".format("----- 型の確認 "))
print(type(sr_col))

print("{:-<50}".format("----- 複数列の抽出(リスト) "))
sr_cols = df.loc[:, ["high", "close"]]
print(sr_cols)
print("{:-<50}".format("----- 型の確認 "))
print(type(sr_cols))

print("{:-<50}".format("----- 複数列の抽出(スライス) "))
print("※※※ 通常のpythonスライスとは異なり、開始と終了の両方が含まれていることに注意 ※※※")
sr_cols = df.loc[:, "high":"close"]
print(sr_cols)
print("{:-<50}".format("----- 型の確認 "))
print(type(sr_cols))

print("\n{:*<100}".format("***** 列の抽出([]) "))
print("{:-<50}".format("----- 1列の抽出 "))
print(df["open"])
print("{:-<50}".format("----- 複数列の抽出(リスト) "))
print(df[["high", "close"]])
print("{:-<50}".format("----- 複数列の抽出(スライス) "))
# print(df["high":"close"])
print("※[]参照だとスライスは抽出NG")


print("\n{:*<100}".format("***** 列の置換(loc) "))
print("{:-<50}".format("----- 1列の置換 "))
df = df_mst.copy()
df.loc[:, "open"] = 0.0
print(df)
df.loc[:, "open"] = [1.0, 2.0, 3.0, 4.0, 5.0]
print(df)
print("{:-<50}".format("----- 複数列の置換(リスト) "))
df = df_mst.copy()
df.loc[:, ["high", "close"]] = -1.0
print(df)
print("{:-<50}".format("----- 複数列の抽出(スライス) "))
print("※※※ 通常のpythonスライスとは異なり、開始と終了の両方が含まれていることに注意 ※※※")
df = df_mst.copy()
df.loc[:, "high":"close"] = -2.0
print(df)

print("\n{:*<100}".format("***** 列の置換([]) "))
print("{:-<50}".format("----- 1列の置換 "))
df = df_mst.copy()
df["open"] = 0.0
print(df)
df["low"] = [10.0, 20.0, 30.0, 40.0, 50.0]
print(df)

print("{:-<50}".format("----- 複数列の置換(リスト) "))
df = df_mst.copy()
df[["high", "close"]] = -10.0
print(df)

print("{:-<50}".format("----- 複数列の置換(スライス) "))
df = df_mst.copy()
# df["high":"close"] = -1.0
# print(df)
print("※[]参照だとスライスは抽出NG")


print("\n{:*<100}".format("***** 列の抽出(iloc) "))
print("{:-<50}".format("----- 1列の抽出 "))
print(df.iloc[:, 0])
print("{:-<50}".format("----- 複数列の抽出(リスト) "))
print(df.iloc[:, [1, 3]])
print("{:-<50}".format("----- 複数列の抽出(スライス) "))
print(df.iloc[:, 1:3])


print("\n{:*<100}".format("***** 列の抽出([]) "))
print("{:-<50}".format("----- 1列の抽出 "))
# print(df[0])
print("※[]参照だとスライスは抽出NG")
print("{:-<50}".format("----- 複数列の抽出(リスト) "))
# print(df[[1, 3]])
print("※[]参照だとスライスは抽出NG")
print("{:-<50}".format("----- 複数列の抽出(スライス) "))
print(df[1:3])
print("※[]参照だと行が抽出される")


print("\n{:*<100}".format("***** 列の置換(iloc) "))
print("{:-<50}".format("----- 1列の置換 "))
df = df_mst.copy()
df.iloc[:, 0] = 0.0
print(df)
df.iloc[:, 0] = [1.0, 2.0, 3.0, 4.0, 5.0]
print(df)
print("{:-<50}".format("----- 複数列の置換(リスト) "))
df = df_mst.copy()
df.iloc[:, [1, 3]] = -1.0
print(df)
print("{:-<50}".format("----- 複数列の抽出(スライス) "))
df = df_mst.copy()
df.iloc[:, 1:3] = -2.0
print(df)


print("\n{:*<100}".format("***** 列の置換([]) "))
print("{:-<50}".format("----- 1列の置換（NG） "))
df = df_mst.copy()
df[0] = 0.0
print(df)
df[0] = [1.0, 2.0, 3.0, 4.0, 5.0]
print(df)
print("{:-<50}".format("----- 複数列の置換（NG） "))
df = df_mst.copy()
df[[1, 3]] = -1.0
print(df)

print("{:-<50}".format("----- 複数列の置換(スライス) "))
df = df_mst.copy()
df[1:3] = -1.0
print(df)
print("※[]参照だと行が置換される")
