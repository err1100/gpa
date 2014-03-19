letters = {
    'A':  4.0,
    'A-': 3.7,
    'B+': 3.4,
    'B':  3.1,
    'B-': 2.8,
    'C+': 2.5,
    'C':  2.2,
    'C-': 1.9,
    'D':  1.6,
    'F':  1.3
}

def gpaForGrade(grade):
    return letters[grade]

def qpsForGradeHrs(grade,hrs):
    return hrs*gpaForGrade(grade)

def gpa(hrs,qps):
    return (qps/(hrs*4))*4

def newGpa(oldhrs,oldqps,newhrs,newqps):
    qps = oldqps+newqps
    hrs = oldhrs+newhrs
    return gpa(hrs,qps)

def nextSemesterOneGrade(oldhrs,oldqps,newhrs,grade):
    newqps = qpsForGradeHrs(grade,newhrs)
    return newGpa(oldhrs,oldqps,newhrs,newqps)

def nextSemesterGradeTuplets(oldhrs,oldqps,tuplets):
    newhrs = 0
    newqps = 0
    for tuplet in tuplets:
        newhrs += tuplet[0]
        newqps += qpsForGradeHrs(tuplet[1],tuplet[0])
    return newGpa(oldhrs,oldqps,newhrs,newqps)

def main():
    print("Welcome! Calculate some GPA eventualities here.")
    hrsStr = input("First, enter your current number of earned GPA hours: ")
    oldhrs = float(hrsStr)

    oldqps = 0
    gpaStr = input("Now, enter your current GPA (enter 'q' to use quality points): ")
    if (gpaStr == 'q'):
        qpaStr = input("Enter your current quality points: ")
        oldqps = float(qpaStr)
    else: oldqps = float(gpaStr)*oldhrs

    print("\nGreat! Now, start entering anticipated grades for this coming semester.")
    print("Use the format `credits,grade` (e.g. `6,A-`).")
    print("When finished, enter a period to calculate your anticipated GPA!\n")
    
    sentinel = ""
    while (True):
        if (sentinel == "."): break
        
        grades = []
        cur = input("Enter credits,grade: ")
        while (cur != "."):
            cur = cur.split(',')
            curCreds = int(cur[0])
            curGrade = cur[1]
            grades.append((curCreds,curGrade))
            cur = input("Enter credits,grade: ")
        gpa = nextSemesterGradeTuplets(oldhrs,oldqps,grades)
        print("Your anticipated GPA for the end of the semester is: %.3f" % gpa)
        sentinel = input("\nTo go again, press Enter (or enter a period to quit): ")

    print("\nThanks for playing! Goodbye!")
main()
