import boto3
import pprint as pp
import json
import pandas as pd
import io

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

bucket_list = s3_client.list_buckets()
bucket_name = 'data-eng-resources'
# bucket_contents = s3_client.list_objects_v2(Bucket=bucket_name, Prefix='python')

# bucket = s3_resource.Bucket(bucket_name)
# print(bucket)
# object = bucket.objects.all()
# for obj in object:
#     print(obj.key)

# Reading JSON Files

# s3_object = s3_client.get_object(Bucket=bucket_name, Key='python/chatbot-intent.json')

# strbody = s3_object['Body'].read()
# print(strbody)
# body = json.loads(strbody)
# print(body)

# Reading CSV Files

# s3_object = s3_client.get_object(Bucket=bucket_name, Key='python/happiness-2019.csv')
# pp.pprint(print(s3_object))
#
# # print(s3_object['Body'].read())
#
# df = pd.read_csv(s3_object['Body'])
# print(df)

# Writing objects

# dict_to_upload = {'name': 'data', 'status':1}
#
# s3_client.put_object(Body=json.dumps(dict_to_upload),
#                      Bucket=bucket_name,
#                      Key='Test249/jack.json')
#
# s3_client.upload_file(Filename='new_json.json',
#                       Bucket=bucket_name,
#                       Key='Test249/jack2.json')

# Writing DataFrames

df = pd.DataFrame([[1, 2, 3, 4, 5], [6, 7, 8, 9, 1]])
str_buffer = io.StringIO()
df.to_csv(str_buffer)
s3_client.put_object(Body=str_buffer.getvalue(),
                     Bucket=bucket_name,
                     Key='Test249/jack.csv')
