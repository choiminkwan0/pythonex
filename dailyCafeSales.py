# 1. 가변 매개변수(*args)를 활용한 합계 계산 함수
def calculate_sum(*args):
    """주문된 모든 메뉴의 가격을 더합니다."""
    total = 0
    for price in args:
        total += price
    return total  # 계산된 총합을 반환합니다.

def main():
    # 2. 사용자 입력 활용하기 (input 사용)
    # PDF 04-2 사용자 입출력 자료를 기반으로 프롬프트를 띄워 입력을 받습니다.
    print("=== 카페 일일 매출 정산 시스템 ===")
    print("주문된 메뉴들을 공백으로 구분하여 입력해주세요.")
    print("(예: 아메리카노 카페라떼 아이스아메리카노 카푸치노)")
    
    order_data = input("주문 내역 입력: ")
    
    # 입력받은 문자열을 리스트로 변환
    order_list = order_data.split()

    # 3. 딕셔너리 활용: 메뉴판 설정
    menu_board = {
        "아메리카노": 3000,
        "카페라떼": 4000,
        "카푸치노": 4500
    }

    # 4. 리스트 조작 및 제어문: 주문된 메뉴의 가격들만 모으기
    ordered_prices = []
    valid_orders = [] # 메뉴판에 존재하는 실제 주문들
    
    for item in order_list:
        if item in menu_board:
            price = menu_board[item]
            ordered_prices.append(price)
            valid_orders.append(item)
        else:
            print(f"경고: '{item}'은(는) 메뉴판에 없는 메뉴이므로 제외됩니다.")

    # 5. 함수 호출: 가변 매개변수 함수에 리스트 내용 전달 (언패킹)
    # 리스트의 가격 데이터들을 개별 인자로 풀어서 전달합니다.
    total_sales = calculate_sum(*ordered_prices)

    # 6. 파일 입출력 및 f-문자열 포매팅: 정산 리포트 생성
    # PDF 04-3 파일 읽고 쓰기 자료의 'with' 문을 사용하여 파일을 작성합니다.
    with open("c:/pythonex/daily_report.txt", "w", encoding="utf-8") as f:
        f.write("--- 일일 매출 보고서 ---\n")
        f.write(f"총 주문 건수: {len(valid_orders)}건\n")
        f.write(f"총 매출액: {total_sales}원\n")
        f.write("----------------------\n")
        f.write("판매된 메뉴: " + ", ".join(valid_orders))

    print("\n" + "="*30)
    print("매출 정산이 완료되었습니다.")
    print(f"결과가 'daily_report.txt' 파일로 저장되었습니다.")
    print("="*30)

# 프로그램 시작점 (Entry Point)
if __name__ == "__main__":
    main()