import oracledb

db_config = {
    "user": "system",
    "password": "1234",
    "dsn": "localhost:1521/xe"
}

try:
     
    with oracledb.connect(**db_config) as conn:
        with conn.cursor() as cursor:

            print("데이터 조회 중...")
            select_sql = "SELECT id, name, TO_CHAR(join_date, 'YYYY-MM-DD') FROM members WHERE id = :1"
            target_id = 2

            cursor.execute(select_sql, [target_id])
            
            row = cursor.fetchone()
            if row:
                print(f"조회 성공! ID: {row[0]}, 이름: {row[1]}, 가입일: {row[2]}")
            else:
                print("해당 ID의 데이터가 없습니다.")

except oracledb.Error as e:
    print(f"연결 실패: {e}")