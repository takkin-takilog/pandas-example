import pandas as pd

ohlc_data = [
    ["2020/4/1", 107.607, 117.952, 96.929, 107.191],
    ["2020/4/2", 107.191, 118.104, 97.028, 107.922],
    ["2020/4/3", 107.922, 118.688, 97.811, 108.578],
    ["2020/4/4", 108.432, 119.393, 98.403, 109.252],
    ["2020/4/5", 109.252, 119.294, 98.680, 108.799],
]

print("\n{:*<100}".format("***** DataFrameの生成 "))
df = pd.DataFrame(ohlc_data, columns=["datetime", "open", "high", "low", "close"])
print(df)
print("{:-<50}".format("----- インデックスを取得 "))
print(df.index.to_list())

print("\n{:*<100}".format("***** インデックスの設定 [set_index()] "))
df_i = df.set_index("datetime")
print("{:-<50}".format("----- DataFrameの中身を確認 "))
print(df_i)
print("{:-<50}".format("----- インデックスを取得 "))
print(df_i.index.to_list())
print("{:-<50}".format("----- 元データのDataFrameの中身を確認 "))
print(df)
print("{:-<50}".format("----- インデックスの設定(inplace=True) "))
df.set_index("datetime", inplace=True)
print(df)

df_mst = df.copy()

print("\n{:*<100}".format("***** インデックスの設定 [rename()] "))
print("{:-<50}".format("----- 元データのDataFrameの中身を確認 "))
print(df)
index_mapper = {"2020/4/2": "aaaaaaaa", "2020/4/4": "bbbbbbbb"}
df_i = df.rename(index=index_mapper)
print("{:-<50}".format("----- DataFrameの中身を確認 "))
print(df_i)
print("{:-<50}".format("----- インデックスを取得 "))
print(df_i.index.to_list())

print("{:-<50}".format("----- DataFrameの中身を確認(inplace=True)  "))
print(df)
print("{:-<50}".format("----- インデックスの変更(inplace=True) "))
df.rename(index=index_mapper, inplace=True)
print("{:-<50}".format("----- 元データのDataFrameの中身を確認(inplace=True)  "))
print(df)

print("\n{:*<100}".format("***** インデックスの振り直し "))

df = df_mst.copy()

print("{:-<50}".format("----- 元データのDataFrameの中身を確認 "))
print(df)
print("{:-<50}".format("----- インデックスを取得 "))
print(df.index.to_list())

df_i = df.reset_index()
print("{:-<50}".format("----- 振り直し後のDataFrameの中身を確認 "))
print(df_i)
print("{:-<50}".format("----- インデックスを取得 "))
print(df_i.index.to_list())

print("{:-<50}".format("----- DataFrameの中身を確認(変更前)  "))
print(df)
print("{:-<50}".format("----- DataFrameの中身を確認(inplace=True)  "))
df.reset_index(inplace=True)
print(df)


print("\n{:*<100}".format("***** インデックスの削除 "))

df = df_mst.copy()

print("{:-<50}".format("----- 元データのDataFrameの中身を確認 "))
print(df)
print("{:-<50}".format("----- インデックスを取得 "))
print(df.index.to_list())

df_i = df.reset_index(drop=True)
print("{:-<50}".format("----- 削除後のDataFrameの中身を確認 "))
print(df_i)
print("{:-<50}".format("----- インデックスを取得 "))
print(df_i.index.to_list())

print("{:-<50}".format("----- DataFrameの中身を確認(変更前)  "))
print(df)
print("{:-<50}".format("----- DataFrameの中身を確認(inplace=True)  "))
df.reset_index(drop=True, inplace=True)
print(df)
