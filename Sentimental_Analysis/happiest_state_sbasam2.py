import sys
import json
import csv

def fix_string(s):
    return s.encode('ascii', errors='replace').decode('utf-8')

def main():
    try:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
    except IndexError:
        arg1 = "./data/AFINN-111.txt"
        arg2 = "./data/streaming_output_full_sbasam2.txt"
        
    sent_file = open(arg1, encoding = "utf-8")
    tweet_file = open(arg2, encoding = "utf-8")
 
    abb = {
        "AL":"Alabama",
        "AK":"Alaska",
        "AZ":"Arizona",
        "AR":"Arkansas",
        "CA":"California",
        "CO":"Colorado",
        "CT":"Connecticut",
        "DE":"Delaware",
        "DC":"District of Columbia",
        "FL":"Florida",
        "GA":"Georgia",
        "HI":"Hawaii",
        "ID":"Idaho",
        "IL":"Illinois",
        "IN":"Indiana",
        "IA":"Iowa",
        "KS":"Kansas",
        "KY":"Kentucky",
        "LA":"Louisiana",
        "ME":"Maine",
        "MT":"Montana",
        "NE":"Nebraska",
        "NV":"Nevada",
        "NH":"New Hampshire",
        "NJ":"New Jersey",
        "NM":"New Mexico",
        "NY":"New York",
        "NC":"North Carolina",
        "ND":"North Dakota",
        "OH":"Ohio",
        "OK":"Oklahoma",
        "OR":"Oregon",
        "MD":"Maryland",
        "MA":"Massachusetts",
        "MI":"Michigan",
        "MN":"Minnesota",
        "MS":"Mississippi",
        "MO":"Missouri",
        "PA":"Pennsylvania",
        "RI":"Rhode Island",
        "SC":"South Carolina",
        "SD":"South Dakota",
        "TN":"Tennessee",
        "TX":"Texas",
        "UT":"Utah",
        "VT":"Vermont",
        "VA":"Virginia",
        "WA":"Washington",
        "WV":"West Virginia",
        "WI":"Wisconsin",
        "WY":"Wyoming"
        }

    def state_from_text(text):
        for a in abb:
            if a in text:
                return a
            if abb[a] in text:
                return a
        return None
    
    def place_state(place):
        if not place:
            return None
        if place["country_code"] != "US":
            return None
        return state_from_text(str(place["full_name"]))
  
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

    states = {}
    for json_line in tweet_file:
        tweet = json.loads(json_line)
        uloc = tweet['user']['location']
        ucord = tweet['coordinates']
        uplace = tweet['place']
        state = place_state(uplace)
        if state is None:
            if uloc is not None:
                state = state_from_text(uloc)
        if state is None:
            continue
        text = tweet["text"]
        score = text_senti(text)
        if state not in states:
            states[state] = [0, 0]
        entry = states[state]
        entry[0] += score
        entry[1] += 1

    sscores = []
    for s in states:
        entry = states[s]
        avg = round(entry[0] / entry[1], 2)
        sscores.append((s, avg))
    sscores.sort(key=lambda x: x[1], reverse = True)
    for state, score in sscores:
        print("{} : {}".format(state, score))

if __name__ == '__main__':
    main()
