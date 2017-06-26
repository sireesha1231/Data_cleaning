def load_file(filename):
    f_in = open(filename,'r')
    mydata = []
    lines = f_in.readlines()
    for line in lines:
        row = {}
        values = line.partition('-')
        prof_name = values[0]
        courses = values[2]
        courses = courses.split('|')
        row['Prof_Name'] = prof_name.strip()
        row['Courses'] = [c.strip() for c in courses]
        mydata.append(row)
    f_in.close()
    return mydata

def jaccard(a,b):
        a = set(a)
        b = set(b)
        union = a.union(b)
        inter = a.intersection(b)
        j = len(inter) / len(union)
        return j
    
def q1():
    courses = []
    for d in data:
        courses.extend(d['Courses'])
    courses = list(set(courses))
    print(len(courses))

def q2():
    for d in data:
        if d['Prof_Name'] == 'Theys':
            courses = d['Courses']
            courses = ",".join(courses)
            print(courses)
            break

def q3():
    data2 = []
    for d in data:
        if len(d['Courses'])>=5:
            data2.append(d)

    maxj = -1
    maxp = None
    for i in range(len(data2) - 1):
        for j in range(i + 1, len(data2) - 1):
            c1 = data2[i]['Courses']
            c2 = data2[j]['Courses']
            jc = jaccard(c1, c2)
            if jc > maxj:
                maxj = jc
                maxp = (data2[i]['Prof_Name'], data2[j]['Prof_Name'])
    if maxp != None:
        print("{}, {}".format(maxp[0], maxp[1]))

data = load_file('cleaned.txt')
q1()
q2()
q3()
