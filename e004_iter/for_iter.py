import pandas as pd

ohlc_data = [
    ["2020/4/6", 108.432, 119.393, 98.403, 109.252],
    ["2020/4/7", 109.252, 119.294, 98.680, 108.799],
    ["2020/4/8", 108.799, 119.109, 98.514, 108.854],
]

print("\n{:*<100}".format("***** DataFrameの生成 "))
df = pd.DataFrame(ohlc_data, columns=["datetime", "open", "high", "low", "close"])
df.set_index("datetime", inplace=True)
print(df)
df_mst = df.copy()

print("\n{:*<100}".format("***** [DataFrame]forループで１行ずつ処理(iterrows) "))
counter = 0
for index, sr_row in df.iterrows():
    print("\n*** Loop:[{}] ********************".format(counter))
    print("--- index -----")
    print(index)
    print("--- content -----")
    print(sr_row)
    print("--- 型を確認 -----")
    print(type(sr_row))
    counter += 1

print("\n{:*<100}".format("***** [DataFrame]forループで１行ずつ処理(itertuples)<named tuple> "))
counter = 0
for n_tuple in df.itertuples():
    print("\n*** Loop:[{}] ********************".format(counter))
    print("--- 型を確認 -----")
    print(type(n_tuple))
    print("--- 名前で取得 -----")
    print("index: {}".format(n_tuple.Index))
    print("open : {}".format(n_tuple.open))
    print("high : {}".format(n_tuple.high))
    print("low  : {}".format(n_tuple.low))
    print("close: {}".format(n_tuple.close))
    print("--- インデックスで取得 -----")
    print("index: {}".format(n_tuple[0]))
    print("open : {}".format(n_tuple[1]))
    print("high : {}".format(n_tuple[2]))
    print("low  : {}".format(n_tuple[3]))
    print("close: {}".format(n_tuple[4]))
    counter += 1

print("\n{:*<100}".format("***** [DataFrame]forループで１行ずつ処理(itertuples)<regular tuple> "))
counter = 0
for r_tuple in df.itertuples(name=None):
    print("\n*** Loop:[{}] ********************".format(counter))
    print("--- 型を確認 -----")
    print(type(r_tuple))
    print("--- インデックスで取得 -----")
    print("index: {}".format(r_tuple[0]))
    print("open : {}".format(r_tuple[1]))
    print("high : {}".format(r_tuple[2]))
    print("low  : {}".format(r_tuple[3]))
    print("close: {}".format(r_tuple[4]))
    counter += 1

print("\n{:*<100}".format("***** [DataFrame]forループで１列ずつ処理(items) "))
counter = 0
for label, sr_col in df.items():
    print("\n*** Loop:[{}] ********************".format(counter))
    print("--- label -----")
    print(label)
    print("--- content -----")
    print(sr_col)
    print("--- 型を確認 -----")
    print(type(sr_col))
    counter += 1

print("\n{:*<100}".format("***** Seriesの生成 "))
# Seriesの生成
o_data = [108.432, 109.252, 108.799]
o_index = ["2020/4/6", "2020/4/7", "2020/4/8"]
sr = pd.Series(data=o_data, index=o_index, name="open")
print(sr)
print("\n{:*<100}".format("***** [Series]forループで１つずつ処理(iterrows) "))
for index, value in sr.items():
    print("index: {}, value: {}".format(index, value))
