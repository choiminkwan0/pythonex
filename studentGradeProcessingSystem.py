def calculate_sum(*args):
    """학생의 합계 점수를 구합니다."""
    total = 0
    for score in args:
        total += score
    return total

def main():
    print("=== 기말고사 성적 결과 보고서 ===")

    student = input("대상 학생: ")

    student_list = student.split()

    students_data = {
        "홍길동": [90, 80, 85, 95, 75],
        "성춘향": [95, 95, 82, 77, 100],
        "흥부": [90, 93, 94, 91, 80],
        "놀부": [60, 80, 75, 90, 92]
    }

    student_name = []

    for item in student_list:
        if item in students_data:
            score = students_data[item]
            student_name.append(item)

            total_scores = calculate_sum(*score)
            avg = total_scores / len(score)

            if avg >= 90: 
                grade = "A"
            elif avg >= 80: 
                grade = "B"
            elif avg >= 70: 
                grade = "C"
            else: 
                grade = "F"                
        else:
            print(f"\n경고: '{item}'은(는) 등록되지 않은 학생입니다.")

        with open("C:/pythonex/grade_report.txt", "w", encoding="utf-8") as f:
            f.write("\n--- 기말고사 성적 결과 보고서 ---\n")
            f.write(f"대상 학생: {item}\n")
            f.write(f"합계 점수: {total_scores}점\n")
            f.write(f"평균 점수: {avg:.1f}\n")
            f.write(f"최종 등급: {grade}\n")
            f.write("----------------------\n")
            f.write(f"입력 데이터: 국어, 영어, 수학, 사회, 과학\n")
            f.write(f"저장 위치: C:/pythonex/grade_report.txt\n")
                
        print("\n" + "="*30)
        print(f"등록이 완료 되었습니다.")
        print(f"저장 완료: C:/pythonex/grade_report.txt")
        print("="*30)

if __name__ == "__main__":
    main()


