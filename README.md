This was a simple project to help gain confidence in the feedback I was given during interviews. I was doing an analysis of user behavior and their feelings about using their voice interfaces, Alexa and Google Home. The interviews gave some interesting data, but since interviews are case studies I wanted to explore ways to confirm the findings in a more robust way. 

This led to the experiment I have here. I used the praw library to make a super basic web scraper for the subreddit AmazonEcho. There was a stick page that had user requests. So, I pulled down the most requested features and pushed them over to a .csv file that I then used to further analyze and confirm the data I recieved from the interviews while also doing a deeper sentiment analysis since I was able to harvest far more data than I had initially intended. 