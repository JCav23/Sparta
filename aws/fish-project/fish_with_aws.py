import boto3
import pprint as pp
import json
import pandas as pd
import io

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

bucket_name = 'data-eng-resources'

fish_market_1 = s3_client.get_object(Bucket=bucket_name, Key='python/fish-market.csv')
fish_market_2 = s3_client.get_object(Bucket=bucket_name, Key='python/fish-market-mon.csv')
fish_market_3 = s3_client.get_object(Bucket=bucket_name, Key='python/fish-market-tues.csv')
# pp.pprint(fish_market_1)
df1 = pd.read_csv(fish_market_1['Body'])
df2 = pd.read_csv(fish_market_2['Body'])
df3 = pd.read_csv(fish_market_3['Body'])

frame_list = [df1, df2, df3]
fish_market_data = pd.concat(frame_list)

fish_averages = fish_market_data.groupby('Species').mean()
print(fish_averages)

# str_buffer = io.StringIO()
# fish_averages.to_csv(str_buffer)
# s3_client.put_object(Body=str_buffer.getvalue(),
#                      Bucket=bucket_name,
#                      Key='Data249/fish/jack.csv')
