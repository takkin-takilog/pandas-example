"""
要素の抽出・置換(at, iat)
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


print("\n{:*<100}".format("***** 要素の抽出(at) "))
elem = df.at["2020/4/7", "open"]
print(elem)


print("\n{:*<100}".format("***** 要素の置換(at) "))
df = df_mst.copy()
df.at["2020/4/7", "open"] = 0.0
print(df)


print("\n{:*<100}".format("***** 要素の抽出(iat) "))
df = df_mst.copy()
elem = df.iat[1, 0]
print(elem)


print("\n{:*<100}".format("***** 要素の置換(iat) "))
df = df_mst.copy()
df.iat[1, 0] = 0.0
print(df)
