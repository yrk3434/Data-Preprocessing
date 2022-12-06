import pyarrow.parquet as pq
import pyarrow.dataset as ds

'''
save data with partitioon
'''
table = pa.Table.from_pandas(pandas_df)
pq.write_to_dataset(
table,
root_path
partiton_cols
)

'''
read data with partition
'''
# path: partitioning 폴더 이름
dataset = ds.dataset(path, partitioning='hive', format = 'parquet')
df = dataset.to_table().to_pandas()
