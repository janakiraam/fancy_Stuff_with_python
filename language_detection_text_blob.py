"""
Created on Tue Jan 12 21:04:22 2021
"""

#வணக்கம்

from textblob import TextBlob
word = TextBlob(u'வணக்கம்')
wordl = word.detect_language()
print(wordl)

#धन्यवाद

from textblob import TextBlob
word = TextBlob(u'धन्यवाद')
wordl = word.detect_language()
print(wordl)