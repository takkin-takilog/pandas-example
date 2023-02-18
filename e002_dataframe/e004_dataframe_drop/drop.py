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
df.set_index("datetime", inplace=True)
print(df)

df_mst = df.copy()

print("\n{:*<100}".format("***** 行の削除(drop) "))
df = df_mst.copy()
print("{:-<50}".format("----- 単一ラベル "))
df_s = df.drop(index="2020/4/8")
print(df_s)
print("{:-<50}".format("----- 元データ確認 "))
print(df)
print("{:-<50}".format("----- 複数ラベル(リスト) "))
df_l = df.drop(index=["2020/4/7", "2020/4/9"])
print(df_l)
print("{:-<50}".format("----- inplace=True "))
df.drop(index=["2020/4/7", "2020/4/9"], inplace=True)
print(df)

print("\n{:*<100}".format("***** 列の削除(drop) "))
df = df_mst.copy()
print("{:-<50}".format("----- 単一ラベル "))
df_s = df.drop(columns="high")
print(df_s)
print("{:-<50}".format("----- 元データ確認 "))
print(df)
print("{:-<50}".format("----- 複数ラベル(リスト) "))
df_l = df.drop(columns=["open", "low"])
print(df_l)
print("{:-<50}".format("----- inplace=True "))
df.drop(columns=["open", "low"])
print(df)

print("\n{:*<100}".format("***** KeyError "))
print("{:-<50}".format("----- KeyError(raise) "))
df = df_mst.copy()
try:
    df_s = df.drop(columns="aaa")
except KeyError as err:
    print(err)

print("{:-<50}".format("----- KeyError(ignore) "))
df_s = df.drop(columns="aaa", errors="ignore")
print(df_s)
