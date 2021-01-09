import tweepy

#先ほど取得した各種キーを代入する
CK='consumer_key'
CS='consumer_secret'
AT='access_token'
AS='access_token_secret'

#Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

api = tweepy.API(auth)

#ツイート
api.update_status('私はロボットではありません!!')