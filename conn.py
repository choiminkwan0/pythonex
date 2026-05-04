import oracledb

with oracledb.connect(user="system", password="1234", dsn="localhost:1521/xe") as conn:
    cursor = conn.cursor()
    
    # 기존 테이블이 있다면 삭제 (연습용)
    try:
        cursor.execute("DROP TABLE members")
    except oracledb.DatabaseError:
        pass

    # 새 테이블 생성
    create_sql = """
    CREATE TABLE members (
        id NUMBER PRIMARY KEY,
        name VARCHAR2(50) NOT NULL,
        email VARCHAR2(100) UNIQUE,
        join_date DATE DEFAULT SYSDATE
    )
    """
    cursor.execute(create_sql)
    print("테이블 생성 완료")