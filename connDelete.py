import oracledb

db_config = {
    "user": "system",
    "password": "1234",
    "dsn": "localhost:1521/xe"
}

try:
     
    with oracledb.connect(**db_config) as conn:
        with conn.cursor() as cursor:

            print("데이터 삭제 중...")
            delete_sql = "DELETE FROM members WHERE id = :1"
            target_id = 2

            cursor.execute(delete_sql, [target_id])

            if cursor.rowcount > 0:
                conn.commit()
                print("삭제 성공")
            else:
                print("데이터가 존재하지 않습니다")
                
except oracledb.Error as e:
    print(f"연결 실패: {e}")