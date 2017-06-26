import sys
import json

def fix_string(s):
    return s.encode('ascii', errors='replace').decode('utf-8')

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    # read tweet file
    tweet_jsons = tweet_file.read()
    data = [json.loads(line) for line in tweet_jsons.splitlines()]
    tweets = [d['text'] for d in data]

    # read sentiment file
    sentiment = {}
    for line in sent_file:
        x = line.split('\t')
        phrase = x[0]
        score = x[1].strip()
        sentiment[phrase] = float(score)

    def text_sentiment(text):
        score = 0
        text = text.lower()
        for word in text.split():
            if word in sentiment:
                score += sentiment[word]
        return score

    ts = [(fix_string(tweet), text_sentiment(tweet)) for tweet in tweets]
    ts.sort(key=lambda x: x[1])
    for t in ts[::-1][:10] + ts[:10]:
        print("{} : {}".format(t[1], fix_string(t[0])))
    pass

if __name__ == '__main__':
    main()
