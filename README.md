# tweet_analyzer

This program will read a file containing tweets, and produce two files as output.
ft1.txt contains a list of unique words found in the tweets, and a count of how many times each word occurs.
ft2.txt contains a running median of the number of words found in the tweets.  It is updated as each tweet is read.

The code is run by executing run.sh.  It requires only Python 2.7, and is designed to be simple and straightforward.
Both features are implemented using the same script, so the input file needs to be read only once.
