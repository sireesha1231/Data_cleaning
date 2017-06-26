"""
  1. Read lines from input file. //done
  2. Clean professor name by:
     i. Swapping first/last when comma.  //done
     ii. Remove period.     //done
     iii. Keep only last name   //done
  3. Clean course names:
     i. Fix spelling mistakes //done
     ii. Expand abbreviations //done
     iii. Fix capitilizations. //done
  4. Combine duplicate professors. //done
  5. Write file. //done
"""

import re
from autocorrect import spell

def name_clean(name):
    if name.find(',')!=-1:
        part = name.partition(',')
        name = part[2].title()+' '+part[0].title()
        name = name.strip()
    name = name.replace('.',' ')
    name = name.split()[-1].title()
    return name

def course_clean(course):
    def fix_spelling(s):
        return re.sub(r"[a-zA-Z-]+", \
                      lambda m: spell(m.group(0)), s)
    course = re.sub(r"(?i)\bintro\.", "Introduction", course)
    course = re.sub(r"(?i)\bintro\b", "Introduction", course)
    course = course.replace('&','and')
    course = fix_spelling(course)
    course = course.title()
    course = course.strip()
    return course

def read_data(filename):
    f_in = open(filename,'r')
    mydata = []
    lines = f_in.readlines()
    for line in lines:
        row = {}
        values = line.partition('-')
        prof_name = values[0]
        courses = values[2]
        courses = courses.split('|')
        row['Prof_Name'] = name_clean(prof_name)
        row['Courses'] = [course_clean(c) for c in courses]
        mydata.append(row)
    f_in.close()

    # merge duplicate professors
    pset = dict()
    for d in mydata:
        name = d['Prof_Name']
        courses = d['Courses']
        if name in pset:
            pset[name].extend(courses)
        else:
            pset[name ] = courses
    
    return [{'Prof_Name': x, 'Courses': pset[x]} for x in pset]

def write_data(filename, data):
    f_out = open(filename,'w')
    for d in data:
        f_out.write(d['Prof_Name']+' - ' + '|'.join(d['Courses']) + '\n')
    f_out.close()

mydata = read_data('class.txt')
write_data('cleaned.txt', mydata)

def printl(l):
    for d in l:
        print(d)
