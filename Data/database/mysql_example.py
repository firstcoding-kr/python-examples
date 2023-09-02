import pymysql

# DB서버의 IP주소와 ID PW등 정보로 접속 정보를 설정하고 connect한다.
conn = pymysql.connect(host='127.0.0.1', user='root', password='', db='test', charset='utf8', autocommit=True)

# 커서를 가져온다.
# 커서(cursor)는 데이터베이스에 SQL 문을 실행하거나 실행된 결과를 돌려받는 통로같은 것
cur = conn.cursor(pymysql.cursors.DictCursor)

# 쿼리 실행
cur.execute('SELECT * FROM example_post;')

# 쿼리 실행 결과를 가져온다.
result = cur.fetchall()
print(result)

# DB서버 접속 종료
conn.close()
