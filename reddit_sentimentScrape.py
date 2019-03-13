import praw
import datetime as dt
import pandas as pd
from pandas import DataFrame

reddit = praw.Reddit(client_id='=======',
                     client_secret='=======',
                     password='=======',
                     user_agent='=======',
                     username='=======')

submission = reddit.submission(id='7v8ob2')

comments = submission.comments

df_rows = [[comment.parent, comment.id, comment.score, comment.created, comment.body,comment.ups,comment.downs] for comment in comments]

df = pd.DataFrame(df_rows, columns=['Parent ID', 'Comment ID', 'Score', 'Created', 'Body','Ups','Downs'])

df.to_csv('data_scrape.csv',encoding='utf-8')
