import oracledb

db_config = {
    "user": "system",
    "password": "1234",
    "dsn": "localhost:1521/xe"
}

try:
     
    with oracledb.connect(**db_config) as conn:
        with conn.cursor() as cursor:

            print("데이터 삽입 중...")
            insert_sql = "INSERT INTO members (id, name, email) VALUES (:1, :2, :3)"

            user_date = (2, "이순신", "lee@example.com")

            try:
                cursor.execute(insert_sql, user_date)
                conn.commit()
                print("삽입 성공!")
            except oracledb.IntegrityError:
                print("중복된 ID가 이미 존재하여 삽입을 건너뜁니다.")

except oracledb.Error as e:
    print(f"연결 실패: {e}")