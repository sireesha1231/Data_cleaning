import sys
import json
from collections import Counter

def main():
    stop_file = open(sys.argv[1], "r", encoding="utf-8")
    stopwords = set(stop_file.read().split())

    tweet_file = open(sys.argv[2], "r", encoding="utf-8")
    input_text = tweet_file.read()
    data = [json.loads(line) for line in input_text.splitlines()]
    tweets = [d['text'] for d in data]
    wcount = Counter()
    for tweet in tweets:
        for word in tweet.split():
            word = word.lower()
            if word not in stopwords:
                wcount[word] += 1
    wcount = [(word, wcount[word]) for word in wcount]
    wcount.sort(key=lambda x: x[1], reverse=True)
    n = 0 
    for w in wcount:
        n += w[1]

    def fix_string(s):
        return s.encode('ascii', errors='replace').decode('utf-8')

    for w in wcount:
        print(fix_string(w[0]) + " " + str(round(w[1] / n, 4)))
    pass

if __name__ == '__main__':
    main()
