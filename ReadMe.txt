First we will train classifier in train.py and save them for further analysis using pickles.
we will also measure their accuracy in train.py.

then in sentiment.py we load these trained classifier using pickles and use them to define sentiment function which takse piece of text as input and classifies them.

then in final.py we import sentiment.py and then will link to twitter API and stream the twitter data live and will perform data cleaning.

after that we will use sentiment function from sentiment.py and textblob from textblob module to perform sentiment analysis and generate the result.