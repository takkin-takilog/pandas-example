import pandas as pd

o_data1 = [108.432, 109.252, 108.799]
o_index1 = ["2020/4/6", "2020/4/7", "2020/4/8"]

# Seriesの生成
sr = pd.Series(data=o_data1, index=o_index1, name="open")
print(sr)

sr_mst = sr.copy()

sr = sr_mst.copy()

print("\n{:*<100}".format("***** 値の追加（シンプル：スカラ①） "))
sr.loc["2020/4/9"] = 108.854
print(sr)

print("\n{:*<100}".format("***** 値の追加（シンプル：スカラ②） "))
sr["2020/4/10"] = 108.545
print(sr)

print("\n{:*<100}".format("***** 値の結合 "))
sr1 = sr_mst.copy()

print("{:-<50}".format("----- sr1 "))
print(sr1)

print("{:-<50}".format("----- sr2 "))

o_data2 = [108.854, 108.545, 108.453]
o_index2 = ["2020/4/9", "2020/4/10", "2020/4/11"]

# Seriesの生成
sr2 = pd.Series(data=o_data2, index=o_index2, name="open")
print(sr2)

print("{:-<50}".format("----- 結合後 "))
sr_c = pd.concat([sr1, sr2])
print(sr_c)

print("{:-<50}".format("----- sr1 "))
print(sr1)

print("{:-<50}".format("----- sr2 "))
print(sr2)

print("\n{:*<100}".format("***** 値の削除 "))
o_data = [108.432, 109.252, 108.799, 108.854, 108.545]
o_index = ["2020/4/6", "2020/4/7", "2020/4/8", "2020/4/9", "2020/4/10"]

# Seriesの生成
sr = pd.Series(data=o_data, index=o_index, name="open")
print(sr)
sr_mst = sr.copy()

print("{:-<50}".format("----- 削除（単一） "))
sr = sr_mst.copy()
sr_d = sr.drop("2020/4/7")
print(sr_d)

print("{:-<50}".format("----- 元データ確認 "))
print(sr)

print("{:-<50}".format("----- 削除（リスト） "))
sr_d = sr.drop(["2020/4/7", "2020/4/9"])
print(sr_d)

print("{:-<50}".format("----- inplace=True "))
sr = sr_mst.copy()
print(sr)
sr.drop(["2020/4/7", "2020/4/9"], inplace=True)
print(sr)

print("\n{:*<100}".format("***** ラベルが存在しない場合 "))
sr = sr_mst.copy()
print(sr)

# sr_d = sr.drop("2020/12/31")

print("{:-<50}".format("----- errors=\"raise\" "))
try:
    # 存在しないカラム"aaa"を指定する
    sr_d = sr.drop("aaa")
except KeyError as err:
    print(err)

print("{:-<50}".format("----- errors=\"ignore\" "))
# errors="ignore"を指定するとKeyErrorが発生しなくなる
sr_d = sr.drop("aaa", errors="ignore")
print(sr_d)
