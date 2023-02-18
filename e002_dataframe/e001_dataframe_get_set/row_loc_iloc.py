"""
行の抽出・置換(loc, iloc)
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


print("\n{:*<100}".format("***** 行の抽出(loc) "))
print("{:-<50}".format("----- 1行の抽出 "))
sr_row = df.loc["2020/4/8"]
print(sr_row)
print("{:-<50}".format("----- 型の確認 "))
print(type(sr_row))

print("{:-<50}".format("----- 複数行の抽出(リスト) "))
df_rows = df.loc[["2020/4/6", "2020/4/8", "2020/4/10"]]
print(df_rows)
print("{:-<50}".format("----- 型の確認 "))
print(type(df_rows))

print("{:-<50}".format("----- 複数行の抽出(スライス) "))
print("※※※ 通常のpythonスライスとは異なり、開始と終了の両方が含まれていることに注意 ※※※")
df_rows = df.loc["2020/4/7":"2020/4/9"]
print(df_rows)
print("{:-<50}".format("----- 型の確認 "))
print(type(df_rows))


print("\n{:*<100}".format("***** 行の置換(loc) "))
print("{:-<50}".format("----- 1行の置換 "))
df = df_mst.copy()
df.loc["2020/4/8"] = 0.0
print(df)
df.loc["2020/4/8"] = [1.0, 2.0, 3.0, 4.0]
print(df)
print("{:-<50}".format("----- 複数行の置換(リスト) "))
df = df_mst.copy()
df.loc[["2020/4/6", "2020/4/8", "2020/4/10"]] = -1.0
print(df)
print("{:-<50}".format("----- 複数行の置換(スライス) "))
print("※※※ 通常のpythonスライスとは異なり、開始と終了の両方が含まれていることに注意 ※※※")
df = df_mst.copy()
df.loc["2020/4/7":"2020/4/9"] = -2.0
print(df)


print("\n{:*<100}".format("***** 行の抽出(iloc) "))
print("{:-<50}".format("----- 1行の抽出 "))
print(df.iloc[2])
print("{:-<50}".format("----- 複数行の抽出(リスト) "))
print(df.iloc[[0, 2, 4]])
print("{:-<50}".format("----- 複数行の抽出(スライス) "))
print(df.iloc[1:3])

print("\n{:*<100}".format("***** 行の置換(iloc) "))
print("{:-<50}".format("----- 1行の置換 "))
df = df_mst.copy()
df.iloc[2] = 0.0
print(df)
df.iloc[2] = [1.0, 2.0, 3.0, 4.0]
print(df)

print("{:-<50}".format("----- 複数行の置換(リスト) "))
df = df_mst.copy()
df.iloc[[0, 2, 4]] = -1.0
print(df)
print("{:-<50}".format("----- 複数行の置換(スライス) "))
df = df_mst.copy()
df.iloc[1:3] = -2.0
print(df)
