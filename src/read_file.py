from collections import Counter
import bisect
import sys

tweet_input = sys.argv[1]
wc_output = sys.argv[2]
median_output = sys.argv[3]

wordCounts = {}
medianList = []

def getMedian(medians):
    L = len(medians)
    if L%2==0: # even
        return (medians[(L//2)-1]+medians[L//2])/2.
    else: # odd
        return medians[L//2]

with open(tweet_input, 'r', -1) as f0: # open in read mode with default buffer
    with open(median_output, 'w+') as f2: # open in write mode
        for line in f0: 
            tweet = line.split() # list of words in tweets
            cnt = Counter(tweet)
            x = len(cnt)            # number of unique words in tweet
            bisect.insort(medianList, x) # add median to list such that list remains sorted
    #         print medianList
            f2.write(str(getMedian(medianList))+'\n') 
                    
            for word in cnt: # add each word to word count list
                if word in wordCounts:
                    wordCounts[word]+=cnt[word]
                else: 
                    wordCounts[word] = cnt[word]
                 
# sort output so that it prints counts in ASCII order
with open(wc_output, 'w+') as f1:
    for key in sorted(wordCounts): 
        # pad spacing so the longest word has 6 spaces after it
        f1.write(key+'\t\t\t\t'+str(wordCounts[key])+'\n')
