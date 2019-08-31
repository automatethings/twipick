import tweepy
import re

# ----------------------------------setting------------------------------------
KEYFILE = 'twi_api_keys.txt'
wish_words = ["python","進捗","機械学習","統計","物理","インターン","ソース","github"]
OUTPUTFILE = 'result.text'
N_read = 100 # the number of reading tweet
#------------------------------------------------------------------------------






keys = {}
for index,key in enumerate(open(KEYFILE)):
    keys[index]=key.strip().split(":")[1] #remove \n by strip
auth = tweepy.OAuthHandler(keys[0],keys[1])
auth.set_access_token(keys[2],keys[3])
api = tweepy.API(auth)


timeline = api.home_timeline(count=N_read)
flag = 0



outputfile = open('result.txt','w')
for i in timeline:
    for word in wish_words:
        if re.search(u'{}'.format(word),i.text)!=None:
            print("-------------------------------------------------------------------------------------------------------------------------------------------")
            print("name : "+i.user.name)
            print(i.text)
            outputfile.write("-------------------------------------------------------------------------------------------------------------------------------------------\n")
            outputfile.write("name : "+i.user.name +'\n')
            outputfile.write(i.text +'\n')
            flag += 1
        else:
            pass

print("\n\n////////////////////////////////////")
print("searched {0} latest tweet\n{1} tweets contain wish_word".format(N_read,flag))
print("////////////////////////////////////")
outputfile.close()