def input_info(number, name, eng, c, py):    ##정보 입력 함수
    number.append(input("학번: "))
    name.append(input("이름: "))
    eng.append(int(input("영어: ")))
    c.append(int(input("C-언어: ")))
    py.append(int(input("파이썬: ")))
    return number, name, eng, c, py

def tot_ave(total, average, eng, c, py, student_num, check, count):  ##총점, 평균 계산용
    total.append(eng[student_num] + c[student_num] + py[student_num])
    average.append(int(total[student_num]/3))
    check.append(average[student_num])
    if average[student_num] >= 80:
        count += 1
    return total, average, check, count

def abc(average, grade, student_num):   ##학점 판정 함수
    if average[student_num] >= 95:
        grade.append('A+')
    elif average[student_num] >= 90:
        grade.append('A0')
    elif average[student_num] >= 85:
        grade.append('B+')
    elif average[student_num] >= 80:
        grade.append('B0')
    elif average[student_num] >= 75:
        grade.append('C+')
    elif average[student_num] >= 70:
        grade.append('C0')
    else:
        grade.append('F')
    return grade

def ranking(average, rank, check, student_num):     ##등수 판정 함수(출력하기 직전에 사용)
    for i in range(0, student_num, 1):
        minimum = check[i]
        min_index = i
        for k in range(i, student_num, 1):
            if check[k] < minimum:
                minimum = check[k]
                min_index = k
        temp = check[i]
        check[i] = minimum
        check[min_index] = temp
    for i in range(0, student_num, 1):
            for k in range(0, student_num, 1):
                if average[i] == check[k]:
                    rank.append(i+1)
                    break
    return rank

def delete_info(number, name, eng, c, py, total, average, grade, check, count, index):     ##정보 삭제 함수
    if average[index] >= 80:    ##삭제하는 학생의 평균이 80점 이상이면 count 감소
        count -= 1
    del name[index]     ##정보 삭제
    del number[index]
    del eng[index]
    del c[index]
    del py[index]
    del total[index]
    del average[index]
    del grade[index]
    del check[index]
    return number, name, eng, c, py, total, average, grade, check, count

def output_info(number, name, eng, c, py, total, average, grade, rank, student_num, count):  ##정보 출력 함수
    print("\t\t성적관리 프로그램\0")
    print("===============================================================================\0")
    print("\t학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수\0")
    print("===============================================================================\0")
    for i in range(0, student_num, 1):
        print(f"{number[i]:<10}\t{name[i]}\t{eng[i]}\t{c[i]}\t{py[i]}\t{total[i]}\t{average[i]}\t{grade[i]}\t{rank[i]}\0")
    print("평균 80점 이상 학생 수: ", count, "명")
    return

number = []     ##학번 배열
name = []       ##이름 배열
eng = []        ##영어 성적 배열
c = []          ##c언어 성적 배열
py = []         ##파이썬 성적 배열
total = []      ##총점 배열
average = []    ##평균 배열
grade = []      ##학점 배열
rank = []       ##등수 배열
check = []      ##등수 만드는 용도
student_num = 0     ##입력받은 학생 수
count = 0       ##80점 이상 학생 수

while True:     ##성적관리 프로그램 시작
    print("=============menu==================")
    print("1.입력")
    print("2.삭제")
    print("3.출력")
    print("===================================")
    menu = int(input("번호를 입력하세요 1~3 : "))   ##메뉴 항목 입력
    
    if menu == 1:   ##입력
        number, name, eng, c, py = input_info(number, name, eng, c, py)     ##정보 입력받고
        total, average, check, count = tot_ave(total, average, eng, c, py, student_num, check, count)   ##총점, 평균, 80점 이상 여부 계산 및 입력
        grade = abc(average, grade, student_num)        ##학점 계산 및 입력
        student_num += 1        ##학생 수 증가
        
    elif menu == 2: ##삭제
        if student_num < 1:     ##입력받은 정보가 없을 때
            print("삭제할 정보가 없습니다.")
        else:       ##입력받은 정보가 있을 때
            what = int(input("삭제할 성적의 정보(번호)를 고르세요.(1.이름, 2. 학번): "))
            if what == 1:       ##1(이름)을 입력받았을 때
                w_name = input("이름을 입력하세요: ")   ##삭제할 성적의 이름 입력
                index = name.index(w_name)      ##삭제할 이름이 있는 배열의 주소 찾기
                number, name, eng, c, py, total, average, grade, check, count = delete_info(number, name, eng, c, py, total, average, grade, check, count, index)     ##찾은 주소의 정보들 삭제
                student_num -= 1    ##학생 수 감소
            elif what == 2:     ##2(학번)를 입력받았을때
                w_num = input("학번을 입력하세요: ")    ##학번 입력
                index = number.index(w_num)     ##삭제할 학번이 있는 배열의 주소 찾기
                number, name, eng, c, py, total, average, grade, check, count = delete_info(number, name, eng, c, py, total, average, grade, check, count, index)     ##찾은 주소의 정보들 삭제
                student_num -= 1    ##학생 수 감소
            else:       ##1, 2가 아닌 수를 입력했을 때
                print("잘못된 입력입니다.")
        
    elif menu == 3: ##출력
        if student_num < 1: ##입력받은 정보가 없을 때
            print("출력할 정보가 없습니다.")
        else:       ##입력받은 정보가 있을 때
            rank = ranking(average, rank, check, student_num)   ##이때까지 받은 정보들로 등수 매긴 후
            output_info(number, name, eng, c, py, total, average, grade, rank, student_num, count)  ##저장해 둔 정보 출력
            break       ##프로그램 종료
    else:           ##1~3의 수가 아닌 수를 입력했을 때
        print("잘못된 입력입니다.")
