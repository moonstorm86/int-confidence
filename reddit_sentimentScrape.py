import praw
import datetime as dt
import pandas as pd
from pandas import DataFrame

reddit = praw.Reddit(client_id='mZMu1hzVkJclGg',
                     client_secret='AnQMjtuOAKOBSSJafkDCOUK-kRE',
                     password='xasdr5k7',
                     user_agent='hot_taco',
                     username='Moonstorm0725')

submission = reddit.submission(id='7v8ob2')

comments = submission.comments

df_rows = [[comment.parent, comment.id, comment.score, comment.created, comment.body,comment.ups,comment.downs] for comment in comments]

df = pd.DataFrame(df_rows, columns=['Parent ID', 'Comment ID', 'Score', 'Created', 'Body','Ups','Downs'])

df.to_csv('google_home.csv',encoding='utf-8')