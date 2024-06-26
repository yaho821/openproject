def inpu(number, name, eng, c, py):
    number.append(input("학번:"))
    name.append(input("이름:"))
    eng.append(int(input("영어:")))
    c.append(int(input("C-언어:")))
    py.append(int(input("파이썬:")))
    return number, name, eng, c, py

def tot_ave(total, aveage, eng, c, py, i, check):
    total.append(eng[i] + c[i] + py[i])
    average.append(int(total[i]/3))
    check.append(average[i])
    return total, average, check

def abc(average, grade, i):
    if average[i] >= 95:
        grade.append('A+')
    elif average[i] >= 90 and average[i] < 95:
        grade.append('A0')
    elif average[i] >= 85 and average[i] < 90:
        grade.append('B+')
    elif average[i] >= 80 and average[i] < 85:
        grade.append('B0')
    elif average[i] >= 75 and average[i] < 80:
        grade.append('C+')
    elif average[i] >= 70 and average[i] < 75:
        grade.append('C0')
    else:
        grade.append('F')
    return grade

def ranking(average, rank, check):
    for i in range(0, 5, 1):
        minimum = check[i]
        min_index = i
        for k in range(i, 5, 1):
            if check[k] < minimum :
                minimum = check[k]
                min_index = k
        temp = check[i]
        check[i] = minimum
        check[min_index] = temp
    for i in range(0, 5, 1):
        for k in range(0, 5, 1):
            if average[i] == check[k] :
                rank.append(i+1)
                break
    return rank

def outpu(number, name, eng, c, py, total, average, grade, rank):
    print("\t성적관리 프로그램\0")
    print("===============================================================================\0")
    print("\t학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수\0")
    print("===============================================================================\0")
    for i in range(0, 5, 1):
        print(f"{number[i]:<10}\t{name[i]}\t{eng[i]}\t{c[i]}\t{py[i]}\t{total[i]}\t{average[i]}\t{grade[i]}\t{rank[i]}\0")
    return

number = []
name = []
eng = []
c = []
py = []
total = []
average = []
grade = []
rank = []
check = []
for i in range(0, 5, 1):
    number, name, eng, c, py = inpu(number, name, eng, c, py) 
    total, average, check = tot_ave(total, average, eng, c, py, i, check)
    grade = abc(average, grade, i)
rank = ranking(average, rank, check)
outpu(number, name, eng, c, py, total, average, grade, rank)
