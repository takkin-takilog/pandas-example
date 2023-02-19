import pandas as pd
import datetime as dt
import numpy as np
import time

indexes = pd.date_range(
    start=dt.datetime(2000, 1, 1, 0, 0), end=dt.datetime(2023, 12, 31, 23, 0), freq="1H"
)

mat = np.arange(indexes.size * 4).reshape((indexes.size, 4)) / 100
df = pd.DataFrame(mat, columns=["open", "high", "low", "close"], index=indexes)
print(df)

print("\n{:*<100}".format("***** forループで１行ずつ処理(iterrows) "))
start = time.perf_counter()
for index, series in df.iterrows():
    last_op = series.iat[0]
    last_cl = series.iat[3]
    # print(series.iat[0])
duration = time.perf_counter() - start
print("処理時間:{:.3f} last_op:{} last_cl:{}".format(duration, last_op, last_cl))

print("\n{:*<100}".format("***** forループで１行ずつ処理(itertuples)<named tuple> "))
start = time.perf_counter()
for n_tuple in df.itertuples():
    last_op = n_tuple[1]
    last_cl = n_tuple[4]
    # print(n_tuple[1])
duration = time.perf_counter() - start
print("処理時間:{:.3f} last_op:{} last_cl:{}".format(duration, last_op, last_cl))

print("\n{:*<100}".format("***** forループで１行ずつ処理(itertuples)<regular tuple> "))
start = time.perf_counter()
for r_tuple in df.itertuples(name=None):
    last_op = r_tuple[1]
    last_cl = r_tuple[4]
    # print(r_tuple[1])
duration = time.perf_counter() - start
print("処理時間:{:.3f} last_op:{} last_cl:{}".format(duration, last_op, last_cl))

print("\n{:*<100}".format("***** forループで１行ずつ処理(itertuples)<改良1> "))
open_list = df["open"].to_list()
close_list = df["close"].to_list()
start = time.perf_counter()
for op, cl in zip(open_list, close_list):
    last_op = op
    last_cl = cl
    # print(open_list[index])
duration = time.perf_counter() - start
print("処理時間:{:.3f} last_op:{} last_cl:{}".format(duration, last_op, last_cl))

print("\n{:*<100}".format("***** forループで１行ずつ処理(itertuples)<改良2> "))
open_list = df["open"].to_list()
close_list = df["close"].to_list()
start = time.perf_counter()
for index in range(df.shape[0]):
    last_op = open_list[index]
    last_cl = close_list[index]
    # print(open_list[index])
duration = time.perf_counter() - start
print("処理時間:{:.3f} last_op:{} last_cl:{}".format(duration, last_op, last_cl))
