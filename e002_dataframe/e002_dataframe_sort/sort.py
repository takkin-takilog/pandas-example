"""
ソート(sort_index, sort_values)
"""

import pandas as pd

id_data = [
    [104, "ccc", 179.2, 61.6],
    [105, "aaa", 198.6, 54.8],
    [102, "eee", 158.1, 58.0],
    [101, "bbb", 179.3, 60.4],
    [103, "ddd", 167.9, 73.9],
]

print("\n{:*<100}".format("***** DataFrameの生成 "))
df = pd.DataFrame(id_data, columns=["id", "name", "height", "weight"])
df.set_index("id", inplace=True)
print(df)
df_mst = df.copy()

print("\n{:*<100}".format("***** インデックス・ソート（昇順） "))
df_asc = df.sort_index(ascending=True)
print("{:-<50}".format("----- ソート後 "))
print(df_asc)
print("{:-<50}".format("----- ソート前 "))
print(df)

print("\n{:*<100}".format("***** インデックス・ソート（降順） "))
df_des = df.sort_index(ascending=False)
print("{:-<50}".format("----- ソート後 "))
print(df_des)
print("{:-<50}".format("----- ソート前 "))
print(df)

print("{:-<50}".format("----- ソート後(inplace=True) "))
df.sort_index(ascending=True, inplace=True)
print(df)

df = df_mst.copy()
print("\n{:*<100}".format("***** バリュー・ソート（昇順） "))

print("{:-<50}".format("----- nameを昇順ソート "))
df_name = df.sort_values("name", ascending=True)
print(df_name)

print("{:-<50}".format("----- 体重を降順ソート "))
df_weight = df.sort_values("weight", ascending=False)
print(df_weight)

print("{:-<50}".format("----- nameを昇順ソート "))
df_name = df.sort_values(["name", "weight"], ascending=True)
print(df_name)
