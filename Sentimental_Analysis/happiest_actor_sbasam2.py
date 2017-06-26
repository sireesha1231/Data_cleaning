import sys
import csv

def fix_string(s):
    return s.encode('ascii', errors='replace').decode('utf-8')

def main():
    sent_file = open(sys.argv[1], encoding = "utf-8")
    csv_file = open(sys.argv[2], encoding = "utf-8")
    file_reader = csv.reader(csv_file)

    # read senti file
    senti = {}
    for line in sent_file:
        parts = line.split('\t')
        senti[parts[0]] = float(parts[1])

    def text_senti(text):
        score = 0
        for word in text.split():
            if word in senti:
                score += senti[word]
        return score

    actors = {}
    for row in file_reader:
        actor = row[0]
        tweet = row[1]
        score = text_senti(tweet)
        if not actor in actors:
            actors[actor] = [0, 0]
        entry = actors[actor]
        entry[0] += score
        entry[1] += 1

    ascores = []
    for actor in actors:
        entry = actors[actor]
        avg = round(entry[0] / entry[1], 2)
        ascores.append((actor, avg))
    ascores.sort(key = lambda x : x[1], reverse = True)

    for actor, avg in ascores:
        print("{} : {}".format(avg, actor))

if __name__ == '__main__':
    main()
