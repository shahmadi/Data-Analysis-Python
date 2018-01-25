from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from textblob import TextBlob
import time
import sentiment as s
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from langdetect import detect
#import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import datetime
import matplotlib.pyplot as plt
import numpy as np
from nltk.stem import WordNetLemmatizer

lemmatizer=WordNetLemmatizer()

start=time.clock()

style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

#consumer key, consumer secret, access token, access secret.
ckey="I7wNQnhjndEYaDNMUgLz12szN"
csecret="pmy1niowN4jbiesRyK7DZOf7ZgVE81TIln06fwgpZKtInzksRo"
atoken="836016328397979648-UXvSz3TYrGGIASVOW7aFQ7fsofXtEEp"
asecret="2jNlaB570c9mTGSAxA3PWYhbAd3HZl8a1f5JexittB9QY"

#saveFile = open('twitem.txt','a')
#text_new=open("twich.txt",'a')

stop_words=set(stopwords.words("english"))
liste=[]
niste=[]
x=0
y=0
ii=0
class listener(StreamListener):
   
    def on_data(self, data):
        try:
          
           tweet1=data.split(',"text":"')[1]
           tweet2=tweet1.split(',"source":"')[0]
           tweet3=tweet2.split('https:')[0]
           tweet4=tweet3.split(':')[1]
           tweet5=tweet4.replace('RT','')
           tweet6=tweet5.replace(':','')
           tweett=tweet6.replace('@','')
           xx=detect(tweett)
           
           if(xx=='en'):
               saveFile = open('CristianoGame.txt','a')   
               saveFile.write(tweett)
               saveFile.write('\n')
               saveFile.close()
               words=word_tokenize(tweett)
               #print(words)
               #print('\n')
               fili=[]
              
               for w in words:
                   if w not in stop_words:
                       fili.append(w)

               fili2=[]

               #print(fili)

              # print("TABDIL")

               for w in fili:
                   fili2.append(lemmatizer.lemmatize(w))

               #print(fili2)
                       
                #further checking
               end=time.clock()
               zaman=end-start
               str1=" ".join(str(e) for e in fili2)
               #print(str1)
               analysis=TextBlob(str1)
               analysis2=s.sentiment(str1)
               
               adad=analysis.sentiment.polarity
               print(adad)
               #print(adad)
               #xar[0]=x
               #print(zaman)
               x=adad
               y=zaman
               liste.append(adad)
               niste.append(zaman)
               print(len(liste))
               #print("HI")
               #print(ii)
               #print("HI2")
               #alpha=open('file2.txt','a')
               #print >>alpha, adad
               #print("HI")
               #saveFile.write(tweett)
               #xar.append(x)
               #print(zaman)
               #yar.append(y)
               #ax1.clear()
               #ax1.plot(xar,yar)
               #print("HI")


           if(len(liste)==5000):
               print(liste[0])
               print(" 150 ta !!! " )
               print(np.mean(liste))
               print("AVERAGE")
               print(sum(liste))
               print("SUM")
               print(zaman)
               plt.plot(niste, liste,'-o')
               plt.title('Cristiano-1500')
               plt.xlabel('Time(sec)')
               plt.ylabel('SentimentValue')
               
               plt.show()

           if(len(liste)==30000):
               print(liste[0])
               print(" 300 ta !!! " )
               print(np.mean(liste))
               print("AVERAGE")
               print(sum(liste))
               print("SUM")
               print(zaman)
               plt.plot(niste, liste,'-o')
               plt.title('Messi-300')
               plt.xlabel('Time(sec)')
               plt.ylabel('SentimentValue')
               
               plt.show()
               
           if(len(liste)==3000):
               print(liste[0])
               print(" 500 ta !!! " )
               print(np.mean(liste))
               print("AVERAGE")
               print(sum(liste))
               print("SUM")
               print(zaman)
               plt.plot(niste, liste,'-o')
               plt.title('Cristiano-500')
               plt.xlabel('Time(sec)')
               plt.ylabel('SentimentValue')
               
               plt.show()
           
           if(len(liste)==11000):
               print(liste[0])
               print(" 1000 ta !!! " )
               print(np.mean(liste))
               print("AVERAGE")
               print(sum(liste))
               print("SUM")
               print(zaman)
               plt.plot(niste, liste,'-o')
               plt.title('Cristiano-1000')
               plt.xlabel('Time(sec)')
               plt.ylabel('SentimentValue')
               
               plt.show()

           if(len(liste)==20000):
               print(liste[0])
               print(" 2000 ta !!! " )
               print(np.mean(liste))
               print("AVERAGE")
               print(sum(liste))
               print("SUM")
               print(zaman)
               plt.plot(niste, liste,'-o')
               plt.title('Messi-2000')
               plt.xlabel('Time(sec)')
               plt.ylabel('SentimentValue')
               plt.show()

           if(len(liste)==30000):
               print(liste[0])
               print(" 3000 ta !!! " )
               print(np.mean(liste))
               print("AVERAGE")
               print(sum(liste))
               print("SUM")
               print(zaman)
               plt.plot(niste, liste,'-o')
               plt.title('Messi-3000')
               plt.xlabel('Time(sec)')
               plt.ylabel('SentimentValue')
               plt.show()
               #alaf = open('twik.txt','a')
               '''
               for p in liste:
                   alaf.write("%f\n" % p)
                   #alaf.write('\n')
               '''
               #alaf.close()
               #for itm in liste:
                #   print>>
           

           #print(len(liste))
           return True
   
        except:
            return True

    def on_error(self, status):
        print (status)
    

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Cristiano"])
'''
def animate(i):
    pullData=open('twicher.txt','r').read()
    lines=pullData.split('\n')
    xar=[]
    yar=[]
    x=0
    y=0
    for l in lines:
        x+=1
        if 		
'''

