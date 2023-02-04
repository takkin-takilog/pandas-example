import pandas as pd

ohlc_mat = [
    ["2020/4/6", 108.432, 109.393, 108.403, 109.252],
    ["2020/4/7", 109.252, 109.294, 108.680, 108.799],
    ["2020/4/8", 108.799, 109.109, 108.514, 108.854],
    ["2020/4/9", 108.854, 109.071, 108.218, 108.545],
    ["2020/4/10", 108.545, 108.615, 108.341, 108.515],
]

print("\n{:*<100}".format("***** DataFrameの生成 "))
df_ohlc = pd.DataFrame(ohlc_mat, columns=["datetime", "open", "high", "low", "close"])
print(df_ohlc)

print("\n{:*<100}".format("***** インデックス（行ラベル）の設定 "))
df_ohlc.set_index("datetime", inplace=True)
print(df_ohlc)

print("\n{:*<100}".format("***** インデックス（行ラベル）の取得 "))
print(df_ohlc.index)
print("{:-<50}".format("----- 型の確認 "))
print(type(df_ohlc.index))

print("\n{:*<100}".format("***** インデックス型の変換[Index -> list] "))
index_list = df_ohlc.index.to_list()
print(index_list)
print("{:-<50}".format("----- 型の確認 "))
print(type(index_list))

print("\n{:*<100}".format("***** カラム（列ラベル）の取得 "))
print(df_ohlc.columns)
print("{:-<50}".format("----- 型の確認 "))
print(type(df_ohlc.columns))

print("\n{:*<100}".format("***** インデックス型の変換[Index -> list] "))
columns_list = df_ohlc.columns.to_list()
print(columns_list)
print("{:-<50}".format("----- 型の確認 "))
print(type(columns_list))

print("\n{:*<100}".format("***** 空データ判定 "))
print("{:-<50}".format("----- データ有り "))
print(df_ohlc.empty)

print("{:-<50}".format("----- データ無し（空） "))
df_emp = pd.DataFrame()
print(df_emp.empty)

print("\n{:*<100}".format("***** 列の抽出(DataFrame -> Series) "))
sr_col = df_ohlc["high"]
print(sr_col)
print("{:-<50}".format("----- 型の確認 "))
print(type(sr_col))
print("{:-<50}".format("----- indexの取得 "))
print(sr_col.index.to_list())
print("{:-<50}".format("----- nameの取得 "))
print(sr_col.name)

print("\n{:*<100}".format("***** 行の抽出(DataFrame -> Series) "))
sr_row = df_ohlc.loc["2020/4/8"]
print(sr_row)
print("{:-<50}".format("----- 型の確認 "))
print(type(sr_row))
print("{:-<50}".format("----- indexの取得 "))
print(sr_row.index.to_list())
print("{:-<50}".format("----- nameの取得 "))
print(sr_row.name)

print("\n{:*<100}".format("***** Seriesの生成 "))
volume_list = [90673, 96199, 84646, 94182, 12024]
name_list = ["2020/4/6", "2020/4/7", "2020/4/8", "2020/4/9", "2020/4/10"]

sr_volume = pd.Series(volume_list, index=name_list, name="volume")
print(sr_volume)
print("{:-<50}".format("----- 型の確認 "))
print(type(sr_volume))
print("{:-<50}".format("----- SeriesをDataFrame（列）へ連結 "))
df_ohlc_con = pd.concat([df_ohlc, sr_volume], axis=1)
print(df_ohlc_con)
