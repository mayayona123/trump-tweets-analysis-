#!/usr/bin/env python
# coding: utf-8

# # Task 2 - Donald Trump's Tweets
# 
# **congratulations!** You have been hired by Donald John Trump as a personal analyst. He has a few missions for you. However, he doesn't like to share a lot of information about himself... So you'll have to answer all his questions using his Tweets on Twitter.
# 

# # Instructions
# 
# #### 1 - Loading the data
# First, load the data you've received:
# - Remove any blank rows (where all the values are missing).
# - Treat every missing numeric value as zero and every missing textual value as blank string.
# - Set the type of every column to the best fitting (float, date, boolean, etc.)
# 
# #### 2 - Which platform?
# Generate a bar chart showing in which platform Trump is twitting (Android, iPhone, etc). Eech bar should represent the total amount of tweets written from its platform. Show only the 10 platforms he uses most.
# 
# #### 3 - Best time to tweet
# Trump wants his tweets to be viral. He is asking you to check at what time of the day his tweets get on average the most retweets (shares) and the most favorite (likes).
# 
# The time spans to compare is every round hour (i.e. 00:00-01:00, 01:00-02:00, etc). Show this data in a bar chart. Each bar should represent an hour of the day, and show the average amount of likes/shares of tweets created in that hour.
# 
# Do it twice: once for the time **before** Trump got elected, and once **after** he got elected. The election date was November 8th 2016. The election date itself should be included in the `before` data (since it was known that Trump won only by the end of this day).
# 
# #### 4 - Tweets per hour
# Generate another bar chart showing when does Trump tweet, to understand if he is doing it well or not.
# 
# The chart should show the total amount of tweets created in every hour of the day.
# 
# Can you assume how many hours a day does Trump sleep? Write your assumption, and how you reached that conclusion.
# 
# Do it twice: once for the time **before** Trump got elected, and once **after** he got elected.
# 
# #### 5 - Best tweet length
# Trump also wants to know whether he should do long tweets or short ones.
# 
# Create a horizontal bar plot of the average number of retweets and favorite based on the tweets length (Do it twice: once for the time **before** Trump got elected, and once **after** he got elected):
#   * **Very short**: len < 70
#   * **Short**: 70 <= len < 110
#   * **Medium**: 110 <= len < 130
#   * **Long**: 130 <= len < 140
#   * **Very long**: 140 <= len
# 
# You may create a single plot showing both the likes and shares (in different colors), or a plot for likes and another one for the shares.
# 
# The bars should be ordered from `Very short` to `Very long`.
# 
# #### 6 - Tweet length distribution
# Generate a pie chart showing how Trump's tweets really are distributed between these categories (`Very short` to `Very long`). The pie chart should show represent the total amount of tweets in each length category.
# 
# Do it twice: once for the time **before** Trump got elected, and once **after** he got elected.
# 
# #### 7 - Android vs iPhone
# Generate a plot showing Trump's usage of Android and of iPhone over time. It should be a plot with two lines one over the other, when one shows the iPhone usage and the other shows the Android usage.
# 
# The lines can represent the total amount of tweets created from iPhone/Android per unit of time (can be day/week/month).
# 
# #### 8 - Market influence
# Trump has a theory that people tend to retweet him much more when the stock market goes up. Check if that is true and show it on a visual. 
# 
# For that you have another file with the stock market performance (the value of the S&P 500 index). The stock market goes up if the `Close` price is higher than the `Open` price.
# 
# Show the average retweets Trump got on days that the market went up, versus the average on days that the market went down. Choose a plot type that you see fit for representing this data.
# 
# ## Notes
# 1. Use a seperate cell (or more) for each section.
# 2. Use headings for the different sections - make it clear which code belongs to which section of the task.
# 3. You should design the plots to be clear and readable - you can use titles, labels, grid, styles, and any other feature that will help you produce beautiful and useful plots.
# 4. Use meaningful names of variables and functions.
# 5. Document your code.
# 6. Delete any irrelevant code before submitting - drafts, tests etc should not be submitted.
# 7. Do **not** use absolute paths, always use relative paths, so your code can be tested by the staff.
# 8. Overall, the submition should look clear, clean and tidy.
# 9. **You can use external modules if you wish**
# 10. Besides code correctness, your grade will be based on all the above
# 
# ## Good luck!
# ![alt text](https://cdn.pixabay.com/photo/2017/01/31/19/15/cartoon-2026571_1280.png "Donald Trump")
# 

# In[117]:


import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv('.\\trump_tweets.csv')
df.columns = df.columns.str.strip()
df['is_retweet'] = df['is_retweet'].astype(bool)
df['retweet_count'] = df['retweet_count'].astype(float)
df['favorite_count'] = df['favorite_count'].astype(float)
df['text'] = df['text'].astype(str)
df['created_at']=pd.to_datetime(df['created_at'])
df.dropna(how='all')
df.fillna({'source':'','text':'','is_retweet':'','retweet_count':0,'favorite_count':0})


# In[115]:


two=df.groupby('source')['source'].value_counts().sort_values(ascending=False).head(10).plot(kind='barh',figsize=(7,7),title='used platform')
two.set_xlabel("otal amount of tweets written from its platform")
two.set_ylabel("used platform")
plt.show()


# In[114]:


df['hour'] = df.created_at.dt.hour
before_elctions = df['created_at'] <= '2016-11-08'
three=df[before_elctions].groupby('hour')['retweet_count','favorite_count'].mean().plot(kind='bar',figsize=(7,7),title='Best time to tweet- before elections')
three.set_ylabel("number of retweet/favorite")
plt.show()


# In[113]:


after_elctions = df['created_at'] > '2016-11-08'
three1=df[after_elctions].groupby('hour')['retweet_count','favorite_count'].mean().plot(kind='bar',figsize=(7,7),title='Best time to tweet- after elections')
three1.set_ylabel("number of retweet/favorite")
plt.show()


# In[90]:


four=df[before_elctions].groupby('hour')['text'].count().plot(kind='bar',figsize=(7,7),title='')
four.set_ylabel("number of tweets")
plt.show()


# In[91]:


four1=df[after_elctions].groupby('hour')['text'].count().plot(kind='bar',figsize=(7,7),title='Tweets Per Hour- after elections')
four1.set_ylabel("number of tweets")
#my assumption about how many hours trump sleeps is 4 hours, i reached that conclusion by looking at the charts and the main times he dosn't tweets is beteen 5am-9am


# In[112]:


def tweet_size(tweet):
    tweet_length=len(tweet)
    if tweet_length < 70:
        return "very short"
    elif tweet_length >= 70 and tweet_length < 110:
        return "short"
    elif tweet_length >= 110 and tweet_length < 130:
        return "medium"
    elif tweet_length >= 130 and tweet_length < 140:
        return "long"
    elif tweet_length >=140:
        return "very long"
df['tweet_length']=df['text'].apply(tweet_size)
five=df[after_elctions].groupby('tweet_length')['favorite_count','retweet_count'].mean().plot(kind='barh',figsize=(7,7),title='Best Tweet Length- after elections')
five.set_xlabel('number of retweet/favorite')

plt.show()


# In[111]:


five1=df[before_elctions].groupby('tweet_length')['favorite_count','retweet_count'].mean().plot(kind='barh',figsize=(7,7),title='Best Tweet Length- before elections')
five1.set_xlabel('number of retweet/favorite')
plt.show()


# In[94]:


df[before_elctions]['tweet_length'].value_counts().head(5).plot(kind='pie',autopct='%1.1f%%',colors=['#91d7ff', '#ffcca6', '#83fce6', '#d3bdfc', '#ffff6e'],figsize=(7,7),title='Tweet Length Distribution- before elections')


# In[110]:


df[after_elctions]['tweet_length'].value_counts().head(5).plot(kind='pie',autopct='%1.1f%%',colors=['#91d7ff', '#ffcca6', '#83fce6', '#d3bdfc', '#ffff6e'],figsize=(7,7),title='Tweet Length Distribution- after elections')
plt.show()


# In[108]:


def iphone(text):
    if 'Android'in text:
        return('android')
    elif 'iPhone' in text:
        return('iphone')
    else:
        return 'na'

df['iphone_or_android']=df['source'].apply(iphone)


# In[116]:


import calendar
df['month_year'] = df['created_at'].dt.to_period('M')
df['android'] = (df['iphone_or_android']=='android')
df['iphone']=(df['iphone_or_android']=='iphone')
seven=df.groupby('month_year')['iphone','android'].sum().plot(kind='line',figsize=(7,7),title='Android vs iPhone- per month')
seven.set_ylabel('number of tweets')
plt.show()


# In[107]:


df_spy= pd.read_csv('.\\SPY.csv', parse_dates = ['Date'])
df_spy
df['just_date'] = df['created_at'].dt.date
df.just_date = pd.to_datetime(df.just_date)
df_spy['is_up']=df_spy['Close']>df_spy['Open']
merged_df=pd.merge(df,df_spy, how='inner', right_on='Date',left_on='just_date')
eight=merged_df.groupby('is_up')['retweet_count'].mean().plot(kind='bar',figsize=(7,7),color=['#91d7ff', '#ffcca6'],title="Market influance on Trump's tweets- based on the stock market")
eight.set_ylabel('number of tweets')
eight.set_xlabel('is the market up?')
plt.show()

