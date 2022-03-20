from google.cloud import bigquery
import pandas as pd
import datetime


df=pd.DataFrame({'Col1':['A'],'Col2':['B']})

df['Run_Time']=datetime.datetime.now()

client=bigquery.Client(project='famous-strategy-344516')

job_conf=bigquery.LoadJobConfig(write_disposition='WRITE_APPEND')


client.load_table_from_dataframe(df,'famous-strategy-344516.sample_load_job.data_from_job',job_config=job_conf).result()
